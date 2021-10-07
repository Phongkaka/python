"""
Author: Trịnh Tiến Phong
Date: 04/10/2021
Program: page_85_exercise_01.py
Problem:
    1.  Assume that x is 3 and y is 5. Write the values of the following expressions:
        a.  x == y
        b.  x > y – 3
        c.  x <= y – 2
        d.  x == y or x > 2
        e.  x != 6 and y > 10
        f.  x > 0 and x < 100
Solution:
    Display result:
        a.  False
        b.  True
        c.  True
        d.  True
        e.  False
        f.  True
"""
x = 3
y = 5

print(x == y)
print(x > y - 3)
print(x <= y - 2)
print(x == y or x > 2)
print(x != 6 and y > 10)
print(0 < x < 100)
