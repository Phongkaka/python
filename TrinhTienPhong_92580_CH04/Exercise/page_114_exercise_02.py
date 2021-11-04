"""
Author: Trịnh Tiến Phong
Date: 20/10/2021
Program: page_114_exercise_02.py
Problem:
    2.  Translate each of the following numbers to binary numbers:
        a.  47(10)
        b.  127(10)
        c.  64(10)
* * * * * ============================================================================================= * * * * *
Solution:
    Result:
        a.  101111
        b.  1111111
        c.  1000000
"""


def swap(numberDecimal):
    index = numberDecimal
    if numberDecimal == 0:
        print(0)
    else:
        bitString = ''
        while numberDecimal > 0:
            remainder = numberDecimal % 2
            numberDecimal = numberDecimal // 2
            bitString = str(remainder) + bitString

    print("The binary representation of", str(index), "is", bitString)


element = [9]
for decimal in element:
    swap(decimal)
