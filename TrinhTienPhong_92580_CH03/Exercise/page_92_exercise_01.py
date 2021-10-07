"""
Author: Trịnh Tiến Phong
Date: 05/10/2021
Program: page_92_exercise_01.py
Problem:
    1.  Translate the following for loops to equivalent while loops:
        a.  for count in range(100):
                print(count)
        b.  for count in range(1, 101):
                print(count)
        c.  for count in range(100, 0, -1):
                print(count)
Solution:

"""
# a
countA = 0
while 0 <= countA < 100:
    print(countA)
    countA += 1

# b
countB = 1
while 0 < countB < 101:
    print(countB)
    countB += 1

# c
countC = 100
while 0 < countC <= 100:
    print(countC)
    countC -= 1
