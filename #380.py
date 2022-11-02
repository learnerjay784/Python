# -*- coding: utf-8 -*-
"""
Created on Sat Jan 15 16:08:17 2022

@author: hp
"""

f=open('abd.txt','r')

print('File name:',f.name)
print('File mode:',f.mode)
print('Is file closed:',f.closed)
print('Is file readable:',f.readable())
print('Is file writable:',f.writable())

f.close()
print('Is file closed:',f.closed)