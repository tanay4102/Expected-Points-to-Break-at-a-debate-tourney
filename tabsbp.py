# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 18:37:42 2020

@author: tanay
"""
import random
import numpy as np
n=input("Enter Number of Teams: ")
n=int(n)
y=input("Enter Number of Rounds: ")
y=int(y)
b=input("Enter Number of Breaks: ")
b=int(b)
expected=0;
xk=list([0,1,2,3])
scores=list()
for i in range(0,n):
    scores.append(0)
for e in range(0,10000) :
    scores=list()
    for i in range(0,n):
        scores.append(0)
    for i in range (0,y):
        for z in range(0,n,4) :
            random.shuffle(xk)
            for k in range(0,4):
                scores[z+k]=scores[z+k]+xk[k]
        scores.sort(reverse=True)
    expected=expected+scores[b-1]
expected=float(expected)/float(10000)
print("Expected points to break after 10000 simulations is :")
print(expected)
    
        
        
