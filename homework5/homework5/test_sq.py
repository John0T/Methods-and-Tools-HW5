import pytest
from functions_v2 import sq

def test_sq_correct():
    assert sq(9) ==3
    
def test_sq_badInput():
    assert sq('a') == TypeError
    
def test_sq_impossible():
    assert sq(-9) == TypeError