# -*- coding: utf-8 -*-
"""
Created on Sat Jan 22 23:21:41 2022

@author: hp
"""
import jsonpickle
class Employee:
    def __init__(self,eno,ename,eage,esal,ismarried):
        self.eno=eno
        self.ename=ename
        self.eage=eage
        self.esal=esal
        self.married=ismarried
    def display(self):
        print('ENO:{},ENAME:{},EAGE:{},ESAL:{}'.format(self.eno,self.ename,self.eage,self.esal,self.married))

e=Employee(100,'Durga',45,10000.0,True)
#Serialization to json string
json_string=jsonpickle.encode(e)
print(json_string)
#Serialization to json file
with open('emp.json','w') as f:
    f.write(json_string)
    
#Deserialization from json string
e2=jsonpickle.decode(json_string)
#print(type(e2))
e2.display()
#Deserialization from json file
with open('emp.json','r') as f:
    json_string=f.readline()
e3=jsonpickle.decode(json_string)
e3.display()