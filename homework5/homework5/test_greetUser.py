import pytest
from functions_v2 import greetUser

def test_greetUser_correct(capsys):
    greetUser("First", "Second", "Third") 

    captured_stdout,captured_stderr = capsys.readouterr()
    assert captured_stdout.strip() == "Hello!\nWelcome to the program  First Second Third\nGlad to have you!"


def test_greetUser_firstBlank(capsys):
    greetUser(None, "Second", "Third") 
    captured_stdout,captured_stderr = capsys.readouterr()
    assert captured_stdout.strip() == "Input Error!"

def test_greetUser_secondBlank(capsys):
    greetUser("First", None, "Third")

    captured_stdout,captured_stderr = capsys.readouterr()
    assert captured_stdout.strip() == "Input Error!"


def test_greetUser_thirdBlank(capsys):
    greetUser("First", "Second", None)

    captured_stdout,captured_stderr = capsys.readouterr()
    assert captured_stdout.strip() == "Input Error!"


def test_greetUser_firstNumbers(capsys):
    greetUser(1, "Second", "Third") 
    captured_stdout,captured_stderr = capsys.readouterr()
    assert captured_stdout.strip() == "Input Error!"


def test_greetUser_secondNumbers(capsys):
    greetUser("First", 2, "Third") 

    captured_stdout,captured_stderr = capsys.readouterr()
    assert captured_stdout.strip() == "Input Error!"


def test_greetUser_thirdNumbers(capsys):
    greetUser("First", "Second", 3)
    
    captured_stdout,captured_stderr = capsys.readouterr()
    assert captured_stdout.strip() == "Input Error!"