# -*- coding: utf-8 -*-
"""
Created on Sat Jan 15 23:29:18 2022

@author: hp
"""
#384
f1=open('abc.txt','r')
f2=open('sports.txt','a')
data=f1.read()
f2.write(data)
f1.close()
f2.close()
print('The data copied successfully')