"""Helper para APIs de generación con patrón 'submit job -> poll -> download'.

Tanto APImart como Kie funcionan así: se envía una tarea, se sondea su estado y
al terminar se descarga el resultado. Centralizamos esa mecánica aquí.
"""
from __future__ import annotations

import time
from typing import Any, Callable, Optional

import requests


class RestJobClient:
    def __init__(self, base_url: str, api_key: str, timeout: int = 60):
        self.base_url = base_url.rstrip("/")
        self.api_key = api_key
        self.timeout = timeout
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        })

    def post(self, path: str, payload: dict) -> dict:
        r = self.session.post(f"{self.base_url}{path}", json=payload, timeout=self.timeout)
        r.raise_for_status()
        return r.json()

    def get(self, path: str) -> dict:
        r = self.session.get(f"{self.base_url}{path}", timeout=self.timeout)
        r.raise_for_status()
        return r.json()

    def poll(
        self,
        check: Callable[[], dict],
        is_done: Callable[[dict], bool],
        is_failed: Callable[[dict], bool],
        get_result_url: Callable[[dict], Optional[str]],
        interval: float = 5.0,
        max_wait: float = 600.0,
    ) -> str:
        """Sondea hasta que el job termina; devuelve la URL del resultado."""
        waited = 0.0
        while waited < max_wait:
            data = check()
            if is_failed(data):
                raise RuntimeError(f"job falló: {data}")
            if is_done(data):
                url = get_result_url(data)
                if not url:
                    raise RuntimeError(f"job terminado sin URL de resultado: {data}")
                return url
            time.sleep(interval)
            waited += interval
        raise TimeoutError(f"job no terminó en {max_wait}s")

    @staticmethod
    def download(url: str, out_path: str) -> str:
        with requests.get(url, stream=True, timeout=120) as r:
            r.raise_for_status()
            with open(out_path, "wb") as f:
                for chunk in r.iter_content(chunk_size=1 << 16):
                    f.write(chunk)
        return out_path
