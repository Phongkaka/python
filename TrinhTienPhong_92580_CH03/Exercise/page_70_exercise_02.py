"""
Author: Trịnh Tiến Phong
Date: 03/10/2021
Program: page_70_exercise_02.py
Problem:
    2.  Write a loop that prints your name 100 times. Each output should begin on a new line.
Solution:
    Display result:
        Trịnh Tiến Phong 1
        Trịnh Tiến Phong 2
        Trịnh Tiến Phong 3
        ...
        Trịnh Tiến Phong 100
"""

name = "Trịnh Tiến Phong"

for i in range(100):
    print(name, str(i+1))
