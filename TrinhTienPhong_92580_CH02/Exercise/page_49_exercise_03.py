"""
Author: Trinh Tien Phong
Date: 25/09/2021
Program: page_49_exercise_03.py
Problem:
      3.  Write the values of the following floating-point numbers in Python’s scientific notation:
        a.  355.76
        b.  0.007832
        c.  4.3212
Solution:
    Result:
        a.  3.5576e+02
        b.  7.8320e-03
        c.  4.3212e+00
"""
a = 355.76
b = 0.007832
c = 4.3212
print(format(a, "1.4e"))
print(format(b, "1.4e"))
print(format(c, "1.4e"))


