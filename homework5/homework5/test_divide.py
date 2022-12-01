from functions_v2 import divide
import pytest

def geninputs():
    inputs = ["6","3"]
    
    for item in inputs:
        yield item
        
GEN=geninputs()

def test_divide_correct(capsys, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: next(GEN))
    divide()
    captured_stdout,captured_stderr = capsys.readouterr()
    assert captured_stdout.strip() == "Your numbers divided is: 2.0"

    ######
    
def inputs_badType():
    inputs = [5.5, "soup"]
    
    for item in inputs:
        yield item
        
GEN1=inputs_badType()

def test_divide_badType(monkeypatch):

    monkeypatch.setattr('builtins.input', lambda _: next(GEN1))
    
    assert divide() == ValueError
    
    ####

def inputs_byZero():
    inputs = [0,0]
    
    for item in inputs:
        yield item
        
GEN2=inputs_byZero()

def test_divide_byZero(monkeypatch):

    monkeypatch.setattr('builtins.input', lambda _: next(GEN2))
    
    assert divide() == ZeroDivisionError
