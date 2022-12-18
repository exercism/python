"""Parse an SGF tree."""
from __future__ import annotations

import collections
import dataclasses
import string


@dataclasses.dataclass
class SgfTree:
    """SGF Node."""

    properties: dict[str, str] = dataclasses.field(default_factory=dict)
    children: list[SgfTree] = dataclasses.field(default_factory=list)


def parse_property_vals(sgf: str, idx: int) -> tuple[int, list[str]]:
    """Parse property values, returning the next index and values."""
    values = []
    while idx < len(sgf):
        if sgf[idx] != "[":
            break

        # Start of the value.
        idx += 1
        prop_val = ""
        while sgf[idx] != "]":
            # \ has special SGF handling.
            if sgf[idx] == "\\":
                if sgf[idx:idx + 2] == "\\\n":
                    # Newlines are removed if they come immediately after a \,
                    # otherwise they remain as newlines.
                    pass
                else:
                    # \ is the escape character. Any non-whitespace character
                    # after \ is inserted as-is
                    prop_val += sgf[idx + 1]
                idx += 2
            else:
                prop_val += sgf[idx]
                idx += 1

        # All whitespace characters other than newline are converted to spaces.
        for char in string.whitespace:
            if char == "\n":
                continue
            prop_val = prop_val.replace(char, " ")

        values.append(prop_val)
        idx += 1

    return idx, values


def parse_node(sgf: str) -> SgfTree:
    """Parse and return a Node."""
    if not sgf.startswith(";"):
        raise ValueError("node must start with ';'")

    idx = 1
    prop_key_start = idx

    properties = collections.defaultdict(list)
    children = []

    while idx < len(sgf):
        if sgf[idx] == "[":
            # Parse property values.
            if idx == prop_key_start:
                raise ValueError("propery key is empty")
            prop_key = sgf[prop_key_start:idx]
            if not prop_key.isupper():
                raise ValueError('property must be in uppercase')

            idx, prop_vals = parse_property_vals(sgf, idx)
            properties[prop_key].extend(prop_vals)

            # New property.
            prop_key_start = idx
        elif sgf[idx] == ";":
            # Single child.
            child = parse_node(sgf[idx:])
            children.append(child)
            break
        elif sgf[idx] == "(":
            # Multiple children.
            children = []
            while idx < len(sgf):
                if sgf[idx] != "(":
                    break
                # Child start.
                idx += 1
                child_start = idx
                while sgf[idx] != ")":
                    idx += 1
                # Child end.
                child = parse_node(sgf[child_start:idx])
                children.append(child)
                idx += 1
        else:
            idx += 1

    if idx > prop_key_start and not properties:
        raise ValueError('properties without delimiter')
    return SgfTree(children=children, properties=dict(properties))


def parse(sgf: str) -> SgfTree:
    """Parse an SGF tree."""
    if not sgf.startswith("(") and not sgf.endswith(")"):
        raise ValueError('tree missing')
    if not sgf.startswith("(;"):
        raise ValueError('tree with no nodes')
    inside = sgf[1:-1]
    return parse_node(inside)
