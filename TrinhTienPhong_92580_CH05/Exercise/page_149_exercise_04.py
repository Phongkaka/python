"""
Author: Trịnh Tiến Phong
Date: 31/10/2021
Program: page_149_exercise_04.py
Problem:
    4.  Define a function named summation. This function expects two numbers, named low and high, as arguments.
        The function computes and returns the sum of the numbers between low and high, inclusive.
* * * * * ============================================================================================= * * * * *
Solution:
    Display result:
        10
"""


def summation(small, big):
    total = 0
    for index in range(small, big + 1):
        total += index
    return total


# main
low = 1
high = 5
print(summation(low, high))
