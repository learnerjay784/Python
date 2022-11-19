# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 18:34:44 2022

@author: hp
"""
#401
import pickle
class Employee:
    def __init__(self,eno,ename,esal,eaddr):
        self.eno=eno
        self.ename=ename
        self.esal=esal
        self.eaddr=eaddr
        
    def display(self):
        print('ENO:{},ENAME:{},ESAL:{},EADDR:{}'
              .format(self.eno,self.ename,self.esal,self.eaddr))
        
#403
import json
employee={'name':'Durga','age':35,'salary':1000.0,'ismarried':True,'isHavingGirlfriend':None}
#Serialization Python dict object to json string
json_string=json.dumps(employee,indent=4,sort_keys=True)
print(json_string)
#Serialization Python dict object to json file
with open('emp.json','w') as f:
    json.dump(employee,f,indent=4)
print('Open emp.json to see json data')

#404 A   Deserialization by json_string
import json
json_string='''{
    "name": "Durga",
    "age": 35,
    "salary": 1000.0,
    "ismarried": true,
    "isHavingGirlfriend": null
    }'''
employee=json.loads(json_string)
#print(type(employee)) #dict
print(employee)
for k,v in employee.items():
    print(k,':',v)
#404 B Deserialization by json file
import json
with open('emp.json','r') as f:
    employee=json.load(f)
#print(type(employee)) #dict
print(employee)
for k,v in employee.items():
    print(k,':',v)




