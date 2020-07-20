#! /usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=line-too-long
"""Remove blank and empty lines."""
import os
import sys

from zap_blank_lines.zap_blank_lines import zap_blank_lines


# pylint: disable=expression-not-assigned
def main(argv=None):
    """Test driver for the removal of blank and empty lines from argv or stdin and writing to stdout."""
    texts = sys.stdin.readlines() if argv is None else argv
    for text in texts:
        sys.stdout.write(zap_blank_lines(text))
