"""Sesión autenticada contra Skool.

Usa TU cookie de sesión (env var SKOOL_COOKIE) para hablar con las APIs internas
de Skool como si fueras tú navegando. No elude ningún paywall: reusa tu acceso
legítimo de miembro, igual que el método del curso de Whop.

La cookie NUNCA se escribe en el repo. Se lee de la variable de entorno
SKOOL_COOKIE (o de un fichero local ignorado por git).
"""
from __future__ import annotations

import os
import time
from typing import Any

import requests

UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
)


def _load_cookie() -> str:
    cookie = os.environ.get("SKOOL_COOKIE", "").strip()
    if not cookie:
        path = os.environ.get("SKOOL_COOKIE_FILE", "").strip()
        if path and os.path.exists(path):
            with open(path, encoding="utf-8") as fh:
                cookie = fh.read().strip()
    if not cookie:
        raise RuntimeError(
            "Falta SKOOL_COOKIE. Exporta tu cookie de sesión de Skool:\n"
            "  export SKOOL_COOKIE='auth_token=...; ...'\n"
            "o apunta SKOOL_COOKIE_FILE a un fichero local (gitignored)."
        )
    return cookie


class SkoolSession:
    """Cliente HTTP autenticado y educado (reintentos + pausa)."""

    def __init__(self, cookie: str | None = None, pause: float = 0.4) -> None:
        self.cookie = cookie or _load_cookie()
        self.pause = pause
        self.s = requests.Session()
        self.s.headers.update(
            {
                "User-Agent": UA,
                "Cookie": self.cookie,
                "Accept": "application/json, text/plain, */*",
                "Referer": "https://www.skool.com/",
            }
        )

    def get(self, url: str, *, tries: int = 4, **kw: Any) -> requests.Response:
        last: Exception | None = None
        for i in range(tries):
            try:
                r = self.s.get(url, timeout=30, **kw)
                if r.status_code in (429, 502, 503):
                    time.sleep(2 ** i)
                    continue
                time.sleep(self.pause)
                return r
            except requests.RequestException as e:  # noqa: PERF203
                last = e
                time.sleep(2 ** i)
        raise RuntimeError(f"GET falló tras {tries} intentos: {url}") from last

    def get_json(self, url: str, **kw: Any) -> Any:
        r = self.get(url, **kw)
        r.raise_for_status()
        return r.json()

    def whoami(self) -> dict | None:
        """Comprueba que la cookie autentica. Devuelve datos del usuario o None."""
        for url in (
            "https://api.skool.com/users/me",
            "https://www.skool.com/api/users/me",
        ):
            try:
                r = self.get(url)
                if r.status_code == 200 and r.headers.get(
                    "content-type", ""
                ).startswith("application/json"):
                    return r.json()
            except Exception:  # noqa: BLE001
                continue
        return None


if __name__ == "__main__":
    sess = SkoolSession()
    me = sess.whoami()
    print("Autenticado:", bool(me))
    if me:
        print(me)
