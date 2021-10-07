"""
Author: Trịnh Tiến Phong
Date: 03/10/2021
Program: page_72_exercise_04.py
Problem:
    4.  Write a loop that outputs the numbers in a list named salaries. The outputs should be formatted
        in a column that is right-justified, with a field width of 12 and a precision of 2.
Solution:
    Display result:
              999.57
              804.46
              758.12
              548.32
"""

salaries = [999.565, 804.457, 758.123, 548.321]

for i in salaries:
    print(f"{i:12.2f}")
