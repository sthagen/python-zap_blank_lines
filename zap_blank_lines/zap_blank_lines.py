#! /usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=line-too-long
"""Expand lines in text and return only lines that contain non-sapce characters."""


def zap_blank_lines(text):
    """Return blank line compressed string."""
    if not text:  # Early out return empty text
        return ""
    non_blanks = (line for line in text.splitlines() if not line.isspace())
    return f"{'\n'.join(non_blanks)}\n"
