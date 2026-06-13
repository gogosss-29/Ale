"""Cliente de la API interna de Skool (vía endpoints Next.js _next/data).

Descubierto en vivo sobre la comunidad `imperio`:
- La lista de cursos y el árbol completo (cursos→módulos→lecciones) viaja en el
  __NEXT_DATA__ de cada página.
- `_next/data/<buildId>/imperio/classroom/<courseId>.json` responde con un
  redirect a `/imperio/classroom/<short>?md=<primeraLeccion>`.
- `_next/data/<buildId>/imperio/classroom/<short>.json?md=<lessonId>` devuelve el
  árbol del curso con el `desc` (notas Prosemirror) poblado SOLO para esa lección.

Cada nodo lección lleva en metadata: title, desc (Prosemirror [v2]), videoLink
(Loom/YouTube/Vimeo/Wistia), videoLenMs, videoThumbnail, resources, hasAccess.
"""
from __future__ import annotations

import re
from typing import Any, Iterator

from .session import SkoolSession

BASE = "https://www.skool.com"


class SkoolClient:
    def __init__(self, community: str, session: SkoolSession | None = None) -> None:
        self.community = community
        self.s = session or SkoolSession()
        self._build: str | None = None

    # ---- infraestructura ----
    def _next_data(self, path: str) -> dict:
        """GET a /_next/data/<build>/<path>.json devolviendo pageProps."""
        url = f"{BASE}/_next/data/{self.build}/{path}.json"
        d = self.s.get_json(url)
        return d.get("pageProps", d)

    @property
    def build(self) -> str:
        if self._build is None:
            r = self.s.get(f"{BASE}/{self.community}")
            m = re.search(r'"buildId":"([^"]+)"', r.text)
            if not m:
                raise RuntimeError("No pude leer buildId de Skool")
            self._build = m.group(1)
        return self._build

    def _page_next_data(self, url: str) -> dict:
        r = self.s.get(url)
        m = re.search(
            r'<script id="__NEXT_DATA__"[^>]*>(.*?)</script>', r.text, re.S
        )
        if not m:
            raise RuntimeError(f"Sin __NEXT_DATA__ en {url}")
        import json

        return json.loads(m.group(1))["props"]["pageProps"]

    # ---- classroom ----
    def list_courses(self) -> list[dict]:
        """Los 30 cursos (nodos raíz) con id, name, metadata.title, etc."""
        p = self._page_next_data(f"{BASE}/{self.community}/classroom")
        return p["allCourses"]

    def resolve_course(self, course_id: str) -> tuple[str, str]:
        """Devuelve (short_id, primera_leccion_id) siguiendo el redirect."""
        d = self.s.get_json(
            f"{BASE}/_next/data/{self.build}/{self.community}/classroom/{course_id}.json"
        )
        pp = d.get("pageProps", {})
        redirect = pp.get("__N_REDIRECT", "")
        m = re.search(r"/classroom/([^?]+)\?md=([0-9a-f]+)", redirect)
        if not m:
            raise RuntimeError(f"No pude resolver short id de {course_id}: {redirect!r}")
        return m.group(1), m.group(2)

    def course_view(self, short_id: str, md: str) -> dict:
        """pageProps de la vista de un curso con la lección `md` seleccionada."""
        url = (
            f"{BASE}/_next/data/{self.build}/{self.community}"
            f"/classroom/{short_id}.json?md={md}"
        )
        d = self.s.get_json(url)
        return d.get("pageProps", d)

    def lesson_meta(self, short_id: str, lesson_id: str) -> dict:
        """metadata de una lección concreta (con `desc` y `resources` poblados)."""
        p = self.course_view(short_id, lesson_id)
        return _find_node_meta(p, lesson_id)


def iter_tree(course_view: dict) -> Iterator[tuple[int, dict]]:
    """Recorre el árbol de un curso. Yields (profundidad, nodo_metadata+id+tipo)."""
    co = course_view.get("course") or {}

    def walk(wrapper: dict, depth: int) -> Iterator[tuple[int, dict]]:
        node = wrapper.get("course", {})
        if node:
            yield depth, node
        for ch in wrapper.get("children", []) or []:
            yield from walk(ch, depth + 1)

    # raíz: co = {"course": <courseNode>, "children": [...]}
    for ch in co.get("children", []) or []:
        yield from walk(ch, 0)


def _find_node_meta(obj: Any, target: str) -> dict:
    if isinstance(obj, dict):
        if obj.get("id") == target:
            return obj.get("metadata", {})
        for v in obj.values():
            r = _find_node_meta(v, target)
            if r:
                return r
    elif isinstance(obj, list):
        for v in obj:
            r = _find_node_meta(v, target)
            if r:
                return r
    return {}
