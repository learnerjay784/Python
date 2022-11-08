# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 23:37:29 2022

@author: hp
"""
#401
#Receiver is responsiple to deserialize Employee objects
import pickle
f=open('emp1.ser','rb')
print('Deserialization Employee object and printing data...')
while True:
    try:
        e=pickle.load(f)
        e.display()
    except:
        print('Deserialization of all Employee objects completed...')
        break