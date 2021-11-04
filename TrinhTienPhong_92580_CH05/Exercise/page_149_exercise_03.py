"""
Author: Trịnh Tiến Phong
Date: 31/10/2021
Program: page_149_exercise_03.py
Problem:
    3.  Use the function even to simplify the definition of the function odd presented in this section.
* * * * * ============================================================================================= * * * * *
Solution:
    Display result:
        False
"""


def even(num):
    if num % 2 == 0:
        return True
    else:
        return False


def odd(num):
    return not even(num)


# main
print(odd(11))
