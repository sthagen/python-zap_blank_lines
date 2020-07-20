# -*- coding: utf-8 -*-
# pylint: disable=missing-docstring,unused-import,reimported
import pytest  # type: ignore

import zap_blank_lines.zap_blank_lines as do


def test_main_ok_string():
    assert do.zap_blank_lines("imension is implicit") == "imension is implicit\n"
