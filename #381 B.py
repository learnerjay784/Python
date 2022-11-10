# -*- coding: utf-8 -*-
"""
Created on Sat Jan 15 16:45:08 2022

@author: hp
"""

#381
fname=input('Enter File Name:')
f=open(fname,'w')
while True:
    data=input('Enter data to write:')
    f.write(data+sports.txt'\n')
    option=input('Do you want to add some more data? [Yes/No]')
    if option.lower()=='no':
        break
print('Your provided data written to the file successfully')
f.close()