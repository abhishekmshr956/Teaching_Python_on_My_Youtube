# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

print('Please think of anumber between 0 and 100!')
low = 0
high = 100

while True :
    ans = (low + high) / 2
    print "Is your secret number",ans,"?"
    q = input("Enter 'h' , 'l', or 'c' ")
    if q == 'h' :
        low = ans
    elif q == 'l':
        high = ans
    elif q == 'c':
        print("the answer is", ans)
        break