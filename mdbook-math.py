#!/usr/bin/env python3
"""mdBook preprocessor.

GitHub renders `$...$`, $`...`$ and ```math blocks itself. mdBook does not, and its
Markdown parser changes the TeX. This script escapes the TeX so that it reaches
MathJax unchanged.
"""
import json
import re
import string
import sys

PUNCTUATION = set(string.punctuation)
BLOCK = re.compile(r"^```math\n(.*?)\n```$", re.S | re.M)
INLINE = re.compile(r"\$`([^`\n]+)`\$|\$([^$\n]+)\$")


def escape(text):
    return "".join("\\" + c if c in PUNCTUATION else c for c in text)


def convert(text):
    parts = BLOCK.split(text)
    for i, part in enumerate(parts):
        if i % 2:
            parts[i] = escape("\\[" + part + "\\]")
        else:
            parts[i] = INLINE.sub(lambda m: escape("\\(" + (m.group(1) or m.group(2)) + "\\)"), part)
    return "".join(parts)


def walk(node):
    if isinstance(node, dict):
        if isinstance(node.get("content"), str):
            node["content"] = convert(node["content"])
        for value in node.values():
            walk(value)
    elif isinstance(node, list):
        for value in node:
            walk(value)


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "supports":
        sys.exit(0)
    _context, book = json.load(sys.stdin)
    walk(book)
    json.dump(book, sys.stdout)
