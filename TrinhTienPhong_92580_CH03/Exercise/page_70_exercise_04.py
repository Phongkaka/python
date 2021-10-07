"""
Author: Trịnh Tiến Phong
Date: 03/10/2021
Program: page_70_exercise_04.py
Problem:
    4.  Write a loop that prints the first 128 ASCII values followed by the corresponding
        characters (see the section on characters in Chapter 2). Be aware that most of the
        ASCII values in the range “0..31” belong to special control characters with no
        standard print representation, so you might see strange symbols in the output for
        these values.
Solution:
    Show the results when running the program below
"""

for i in range(128):
    print(chr(i), end=" ")
