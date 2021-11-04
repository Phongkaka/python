"""
Author: Trịnh Tiến Phong
Date: 31/10/2021
Program: page_149_exercise_02.py
Problem:
    2.  Define a function named even. This function expects a number as an argument and returns True if the number
        is divisible by 2, or it returns False otherwise. (Hint: A number is evenly divisible by 2 if the remainder
        is 0.)
* * * * * ============================================================================================= * * * * *
Solution:
    Display result:
        True
"""


def even(num):
    if num % 2 == 0:
        return True
    else:
        return False


# main
print(even(10))
