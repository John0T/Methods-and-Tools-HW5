import pytest
from functions_v2 import isPalindrome


def test_palindrome():
    assert isPalindrome("racecar") == True

def test_palindrome1():
    assert isPalindrome("programming") == False

def test_palindrome2():
    assert isPalindrome(1) == TypeError



