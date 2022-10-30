# -*- coding: utf-8 -*-
"""
Created on Sat Nov 27 14:47:50 2021

@author: hp
"""

def square():
    print('You choosed to print SQUARE Pattern...')
    n=int(input('Enter the no. of rows:'))
    for i in range(n):
        print('* '*n)
        
def right_angled_triangle():
    print('You choosed to print right angled triangle pattern...')
    n=int(input('Enter the no. of rows:'))
    for i in range(n):
        for j in range(i+1):
            print('* ',end='')
        print()

def daimond():
    print('You choosed to print Daimond pattern...')
    n=int(input('Enter number of rows:'))
    for i in range(n):
        print(' '*(n-1-i)+'* '*(i+1))
    for i in range(n-1):
        print(' '*(i+1)+'* '*(n-i-1))
    
def pyramid():
    print('You choosed to print pyramid pattern')
    n=int(input('Enter no. of rows:'))
    for i in range(n):
        print(' '*(n-i-1)+('* ')*(i+1))
            
    