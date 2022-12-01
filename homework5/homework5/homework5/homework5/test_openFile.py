import pytest
from functions_v2 import openFile

def test_openFile():
    assert openFile("testing.txt") == None

def test_openFile1(capsys):
    openFile("testing.txt")
    captured_stdout, captured_stderr = capsys.readouterr()
    assert captured_stdout.strip() == "File opened."

def test_openFile2(capsys):
    openFile("testin")
    captured_stdout, captured_stderr = capsys.readouterr()
    assert captured_stdout.strip() == "file not found"

def test_openFile3():
    openFile(1234) == TypeError


