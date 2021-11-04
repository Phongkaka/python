"""
Author: Trịnh Tiến Phong
Date: 31/10/2021
Program: page_145_exercise_06.py
Problem:
    6.  Write a loop that replaces each number in a list named data with its absolute value
* * * * * ============================================================================================= * * * * *
Solution:
    Display result:
        [21, 12, 20, 5, 26, 11]
"""

data = [21, -12, 20, 0, -5, 26, -11]

for item in range(0, len(data)):
    data[item] = abs(data[item])

print(data)

