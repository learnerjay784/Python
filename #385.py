# -*- coding: utf-8 -*-
"""
Created on Sat Jan 15 23:23:04 2022

@author: hp
"""

#385
with open('abc.txt','w') as f:
    f.write('Durga\n')
    f.write('Software\n')
    f.write('Solutions\n')
    print('Is File closed:',f.closed)
print('Is File closed:',f.closed)

#387
f=open('abc.txt','w')
f.write('ALL STUDENTS ARE STUPIDS')
with open('abc.txt','r+') as f:
    text=f.read()
    print('Data before modification:')
    print(text)   #ALL STUDENTS ARE STUPIDS
    f.seek(17)    #CURSOR MOVED TO STUPIDS WORD
    f.write('GEMS!!!')     #STUPIDS REPLACED WITH GEMS
    f.seek(0)        #CURSOR MOVED TO BEGINNING OF THE FILE
    print('Data after modification:')
    print(f.read())   #ALL STUDENTS ARE GEMS!!!
    
#388 QUES. 1
import os
fname=input('Enter file name:')
if os.path.isfile(fname):
    print('File Exists:',fname)
    print('The content of the file is:')
    f=open(fname,'r')
    text=f.read()
    print('*'*40)
    print(text)
    print('*'*40)
    f.close()
else:
    print('File does not exist:',fname)

#389
import os
fname=input('Enter File name:')
if os.path.isfile(fname):
    print('File Exists:',fname)
    f=open(fname,'r')
    lcount=wcount=ccount=0
    for line in f:
        lcount=lcount+1
        no_of_words_in_current_line=len(line.split())
        wcount=wcount+no_of_words_in_current_line
        no_of_characters_in_current_line=len(line)
        ccount=ccount+no_of_characters_in_current_line
        
    print('The Number of lines:',lcount)
    print('The number of Words:',wcount)
    print('The number of Charcters:',ccount)
else:
    print('File does not exists:',fname)

#390
f1=open('jay421.jpg','rb')
data=f1.read()
print(type(data))    
f2=open('jaypic23.jpg','wb')
f2.write(data)        
print('jaypic23 image is ready')
f1.close()
f2.close()    
