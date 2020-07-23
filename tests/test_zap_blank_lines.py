# -*- coding: utf-8 -*-
# pylint: disable=missing-docstring,unused-import,reimported
import pytest  # type: ignore

import zap_blank_lines.zap_blank_lines as do


def test_main_ok_string():
    assert do.zap_blank_lines("imension is implicit") == "imension is implicit\n"


def test_main_ok_same_chars_in_string():
    assert do.zap_blank_lines("a a a a") == 'a a a a\n'


def test_main_ok_empty_string():
    assert do.zap_blank_lines('') == ''


def test_main_ok_empty_line():
    assert do.zap_blank_lines('\n') == '\n'


def test_main_nok_ints():
    message = r"'list' object has no attribute 'splitlines'"
    with pytest.raises(AttributeError, match=message):
        do.zap_blank_lines([1, 2, 3])


def test_main_nok_int():
    message = r"'int' object has no attribute 'splitlines'"
    with pytest.raises(AttributeError, match=message):
        do.zap_blank_lines(42)
