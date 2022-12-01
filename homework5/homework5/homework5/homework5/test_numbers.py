import pytest
from functions_v2 import numbers


def test_numdiv():
    assert numbers(10,5) == 2

def test_numdiv1():
    assert numbers('a','b') == TypeError


def test_numdiv2():
    assert numbers(5,0) == ZeroDivisionError

