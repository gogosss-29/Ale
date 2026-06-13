"""Convierte el `desc` de las lecciones de Skool (Prosemirror JSON) a Markdown.

El campo viene como la cadena `"[v2]" + json.dumps(<lista de nodos>)`. Los tipos
observados: paragraph, heading, text (marks: bold, italic, code, link), bullet/
ordered list, listItem, blockquote, codeBlock, horizontalRule, hardBreak, image.
"""
from __future__ import annotations

import json
from typing import Any


def desc_to_markdown(desc: str | None) -> str:
    if not desc:
        return ""
    raw = desc
    if raw.startswith("[v2]"):
        raw = raw[4:]
    try:
        nodes = json.loads(raw)
    except json.JSONDecodeError:
        return raw.strip()
    if isinstance(nodes, dict):
        nodes = nodes.get("content", [])
    return "\n\n".join(_block(n) for n in nodes if _block(n).strip()).strip()


def _block(node: dict[str, Any]) -> str:
    t = node.get("type")
    if t == "paragraph":
        return _inline(node.get("content", []))
    if t == "heading":
        lvl = node.get("attrs", {}).get("level", 2)
        return "#" * max(1, min(6, lvl)) + " " + _inline(node.get("content", []))
    if t in ("bulletList", "unorderedList"):
        return "\n".join("- " + _list_item(li) for li in node.get("content", []))
    if t == "orderedList":
        return "\n".join(
            f"{i}. " + _list_item(li)
            for i, li in enumerate(node.get("content", []), 1)
        )
    if t == "listItem":
        return "- " + _list_item(node)
    if t == "blockquote":
        inner = "\n\n".join(_block(c) for c in node.get("content", []))
        return "\n".join("> " + ln for ln in inner.splitlines())
    if t in ("codeBlock", "code_block"):
        lang = node.get("attrs", {}).get("language", "") or ""
        code = _inline(node.get("content", []))
        return f"```{lang}\n{code}\n```"
    if t in ("horizontalRule", "horizontal_rule"):
        return "---"
    if t == "image":
        src = node.get("attrs", {}).get("src", "")
        alt = node.get("attrs", {}).get("alt", "") or "imagen"
        return f"![{alt}]({src})"
    # contenedores genéricos
    if node.get("content"):
        return "\n\n".join(_block(c) for c in node["content"])
    return ""


def _list_item(li: dict[str, Any]) -> str:
    parts = [_block(c) for c in li.get("content", [])]
    return " ".join(p for p in parts if p).replace("\n\n", " ").strip()


def _inline(content: list[dict[str, Any]]) -> str:
    out: list[str] = []
    for n in content or []:
        t = n.get("type")
        if t == "text":
            out.append(_marks(n))
        elif t in ("hardBreak", "hard_break"):
            out.append("  \n")
        elif t == "image":
            src = n.get("attrs", {}).get("src", "")
            out.append(f"![]({src})")
        elif n.get("content"):
            out.append(_inline(n["content"]))
    return "".join(out)


def _marks(node: dict[str, Any]) -> str:
    text = node.get("text", "")
    href = None
    for m in node.get("marks", []) or []:
        mt = m.get("type")
        if mt == "bold":
            text = f"**{text}**"
        elif mt == "italic":
            text = f"*{text}*"
        elif mt == "code":
            text = f"`{text}`"
        elif mt == "strike":
            text = f"~~{text}~~"
        elif mt == "link":
            href = m.get("attrs", {}).get("href")
    if href:
        text = f"[{text}]({href})"
    return text
