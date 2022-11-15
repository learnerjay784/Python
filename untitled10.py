# -*- coding: utf-8 -*-
"""
Created on Sun Jan 16 23:23:28 2022

@author: hp
"""
#391
import csv
with open('emp.csv','w',newline='') as f:
    w=csv.writer(f)
    #print(type(w))
    w.writerow(['ENO','ENAME','ESAL','EADDR'])
    while True:
        eno=int(input('Enter Employee Number:'))
        ename=input('Enter Employee Name:')
        esal=float(input('Enter Employee Salary:'))
        eddr=input('Enter Employee Address:')
        w.writerow([eno,ename,esal,eddr])
        option=input('Do you want to insert one more record:[Yes/No]')
        if option.lower()=='no':
            break
print('Total employee data written to csv file successfully...')

#392
import csv
with open('emp.csv','r') as f:
    r=csv.reader(f)
    #print(type(r))
    data=list(r)
    #print(data)
    for row in data:
        for column in row:
            print(column,'\t',end='')
        print()

#392
from zipfile import *
f=ZipFile('file10101010.zip','w',ZIP_DEFLATED)
f.write('file1.txt')
f.write('file2.txt')
f.write('file3.txt')
print('file10101010.zip file created successfully')
f=ZipFile('file1010.zip','r',ZIP_STORED)
names=f.namelist()
print(names)
for name in names:
    f1=open(name,'r')
    text=f1.read()
    print('File name:',name)
    print('Content of this file:')
    print(text)
    f1.close()
    print()

#398
n=int(input())
for i in range(n):
  Xa,Xb,Xc=[int(x) for x in input().split()]
  if Xa>50:
    print('A')
  elif Xb>50:
    print('B')
  elif Xc>50:
    print('C')
  else:
    print('NOT A')        