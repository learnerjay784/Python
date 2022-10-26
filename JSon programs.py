# -*- coding: utf-8 -*-
"""
Created on Sat Jan 22 19:38:52 2022

@author: hp
"""

import json
class Employee:
    def __init__(self,eno,ename,eage,esal):
        self.eno=eno
        self.ename=ename
        self.eage=eage
        self.esal=esal
    def display(self):
        print('ENO:{},ENAME:{},EAGE:{},ESAL:{}'.format(self.eno,self.ename,self.eage,self.esal))
e=Employee(100,'Durga',45,10000.0)
#e_dict={'eno':e.eno,'ename':e.ename,'eage':e.eage,'esal':e.esal}
e_dict=e.__dict__    #convertion into dict
#print(e_dict)
#serializing to json string
json_string=json.dumps(e_dict,indent=4)
print(json_string)
#serializing to json file
with open('emp.json','w') as f:
    json.dump(e_dict,f,indent=4)
    
#deserialization from a file
with open('emp.json','r') as f:
    edict=json.load(f)
print(type(edict))
print(edict)
e=Employee(edict['eno'],edict['ename'],edict['eage'],edict['esal'])
e.display()