import math
import pytest

## opens a file in read mode
## filename received as a parameter
def openFile(filename):
    infile = open(filename, "r")

    print("File opened.")

## takes two numbers and returns
## the result of a division
def numbers(num1, num2):
    return num1 / num2

## takes in two points
## finds the distance between the points
def dist(x1, y1, x2, y2):
    dist = (x2 - x1) ** 2 + (y2 - y1) ** 2
    dist = math.sqrt(dist)

    return dist

## takes in a string -- reverses it
## then compares the two
def isPalindrome(temp):
    test = temp[::-1]

    if(test == temp):
        return True

    else:
        return False
    

#####################

## has input to receive two numbers
## divides the two, then outputs the result
def divide():
    try:
        num1 = int(input("Enter a number: "))
        num2 = int(input("Enter another number: "))

        div = num1 / num2

        print("Your numbers divided is:", div)
    except ZeroDivisionError:
        return ZeroDivisionError
    except TypeError:
        return TypeError
    except ValueError:
        return ValueError
    except:
        print("Unknown Error")


## returns the squareroot of a particular number

def sq(num):
    try:
        if(num<0):
            return TypeError
        else:
            return math.sqrt(num)
            
    except TypeError:
        return TypeError
    except:
        print("Unknown Error")


## grabs user's name
## greets them by their entire name
## names should be strings

def greetUser(first, middle, last):
    if(isinstance(first,str) != True or isinstance(middle,str)!=True or isinstance(last,str)!=True):
        print("Input Error!")
    else:
        print("Hello!")
        print("Welcome to the program ", first, middle, last)
        print("Glad to have you!")


## takes in a Python list
## attempts to display the item at the index provided

def displayItem(numbers, index):
    try:
        print("Your item at", index, "index is", numbers[index])
    except TypeError:
        return TypeError
    except IndexError:
        return IndexError
    except:
        print("Unknown Error")