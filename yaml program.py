# -*- coding: utf-8 -*-
"""
Created on Sat Jan 22 23:57:47 2022

@author: hp
"""

import yaml
emp_dict={'name':'Durga','age':35,'salary':10000,'ismarried':True}

#Serialization to yaml string
yaml_string=yaml.dump(emp_dict)
print(yaml_string)
#Serialization to yaml file
with open('emp.yaml','w') as f:
    yaml.dump(emp_dict,f)
    
#Deserialization from yaml string
new_dict=yaml.safe_load(yaml_string)
print(type(new_dict))
print(new_dict)

#Deserialization from yaml file
with open('emp.yaml','r') as f:
    new_dict2=yaml.safe_load(f)
print(new_dict2)