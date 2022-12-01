import pytest
from functions_v2 import displayItem


def test_displayItem_correct(capsys):
    displayItem([0,1,2,3], 2)

    captured_stdout,captured_stderr = capsys.readouterr()
    assert captured_stdout.strip() == 'Your item at 2 index is 2'

def test_displayItem_badIndex(capsys):
    assert displayItem([0,1,2,3], 'a') == TypeError

    # captured_stdout,captured_stderr = capsys.readouterr()
    # assert captured_stdout.strip() == TypeError

def test_displayItem_badNumbers(capsys):
    assert displayItem(4, 0) == TypeError

    # captured_stdout,captured_stderr = capsys.readouterr()
    # assert captured_stdout.strip() == TypeError

def test_displayItem_badSearch(capsys):
    assert displayItem([0],1) == IndexError

    # captured_stdout,captured_stderr = capsys.readouterr()
    # assert captured_stdout.strip() == IndexError