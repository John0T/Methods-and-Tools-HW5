import pytest
from functions_v2 import dist

def test_dist():
    assert dist(0,4,0,8) == 4

def test_dist2():
    assert dist('a',1,2,3) == TypeError

def test_dist3():
    assert dist('a','b','c','d') == TypeError

