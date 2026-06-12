"""Cliente LLM agnóstico de proveedor para el 'cerebro' del pipeline.

Soporta Anthropic y OpenAI vía variables de entorno. Devuelve texto/JSON.
    Anthropic: ANTHROPIC_API_KEY (+ opcional ANTHROPIC_BASE_URL, ANTHROPIC_MODEL)
    OpenAI:    OPENAI_API_KEY    (+ opcional OPENAI_BASE_URL, OPENAI_MODEL)

Por defecto usa Anthropic con el modelo más capaz disponible.
"""
from __future__ import annotations

import json
import os
from typing import Optional

import requests

DEFAULT_ANTHROPIC_MODEL = "claude-opus-4-8"
DEFAULT_OPENAI_MODEL = "gpt-4o"


class LLMError(RuntimeError):
    pass


def _proveedor() -> str:
    pref = os.environ.get("AVATARHYPE_LLM", "").lower()
    if pref in ("anthropic", "openai"):
        return pref
    if os.environ.get("ANTHROPIC_API_KEY"):
        return "anthropic"
    if os.environ.get("OPENAI_API_KEY"):
        return "openai"
    raise LLMError(
        "No hay LLM configurado. Define ANTHROPIC_API_KEY u OPENAI_API_KEY."
    )


def completar(system: str, user: str, max_tokens: int = 2000,
              temperature: float = 0.8) -> str:
    """Una llamada de chat. Devuelve el texto de la respuesta."""
    prov = _proveedor()
    if prov == "anthropic":
        base = os.environ.get("ANTHROPIC_BASE_URL", "https://api.anthropic.com")
        model = os.environ.get("ANTHROPIC_MODEL", DEFAULT_ANTHROPIC_MODEL)
        r = requests.post(
            f"{base.rstrip('/')}/v1/messages",
            headers={
                "x-api-key": os.environ["ANTHROPIC_API_KEY"],
                "anthropic-version": "2023-06-01",
                "content-type": "application/json",
            },
            json={
                "model": model,
                "max_tokens": max_tokens,
                "temperature": temperature,
                "system": system,
                "messages": [{"role": "user", "content": user}],
            },
            timeout=120,
        )
        r.raise_for_status()
        data = r.json()
        return "".join(b.get("text", "") for b in data.get("content", []))
    else:
        base = os.environ.get("OPENAI_BASE_URL", "https://api.openai.com")
        model = os.environ.get("OPENAI_MODEL", DEFAULT_OPENAI_MODEL)
        r = requests.post(
            f"{base.rstrip('/')}/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {os.environ['OPENAI_API_KEY']}",
                "Content-Type": "application/json",
            },
            json={
                "model": model,
                "max_tokens": max_tokens,
                "temperature": temperature,
                "messages": [
                    {"role": "system", "content": system},
                    {"role": "user", "content": user},
                ],
            },
            timeout=120,
        )
        r.raise_for_status()
        return r.json()["choices"][0]["message"]["content"]


def completar_json(system: str, user: str, **kw) -> dict:
    """Como `completar` pero parsea JSON (tolera bloques ```json)."""
    txt = completar(system, user, **kw)
    txt = txt.strip()
    if txt.startswith("```"):
        txt = txt.split("```", 2)[1]
        if txt.startswith("json"):
            txt = txt[4:]
    try:
        return json.loads(txt.strip())
    except json.JSONDecodeError as e:
        raise LLMError(f"El LLM no devolvió JSON válido: {e}\n{txt[:500]}")
