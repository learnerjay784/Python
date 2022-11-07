# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 23:15:13 2022

@author: hp
"""
#401
from emp1 import *
from pickle import *
with open('emp1.ser','wb') as f:
    while True:
        eno=int(input('Enter Eno:'))
        ename=input('Enter Ename:')
        esal=float(input('Enter Esal:'))
        eaddr=input('Enter Eaddr:')
        e=Employee(eno,ename,esal,eaddr)
        dump(e,f)
        option=input('Do you want to serialize another object:[Yes/No]')
        if option.lower()=='no':
            break
print('Multiple Employee Objects Serialized...')