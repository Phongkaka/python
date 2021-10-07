"""
Author: Trịnh Tiến Phong
Date: 04/10/2021
Program: page_85_exercise_03.py
Problem:
    3.  Write a loop that counts the number of space characters in a string. Recall that the
        space character is represented as ' '.
Solution:
    Display result:
        There are 2 space characters in the string Trịnh Tiến Phong
"""

name = "Trịnh Tiến Phong"
count = 0

for i in name:
    if i == ' ':
        count += 1

print("There are", count, "space characters in the string", name)
