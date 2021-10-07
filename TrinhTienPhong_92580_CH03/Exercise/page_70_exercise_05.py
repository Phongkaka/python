"""
Author: Trịnh Tiến Phong
Date: 03/10/2021
Program: page_70_exercise_05.py
Problem:
    5.  Assume that the variable teststring refers to a string. Write a loop that prints
        each character in this string, followed by its ASCII value.
Solution:
    Display:
        p = 112; h = 104; o = 111; n = 110; g = 103
"""

name = "phong"

for i in name:
    print(i, "=", ord(i), end="; ")
