# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 19:26:30 2022

@author: hp
"""
import requests
response=requests.get('http://api.coindesk.com/v1/bpi/currentprice.json')
binfo=response.json()  #Provides python's dict object
#print(type(binfo))
#print(binfo)
print('Bitcoin price as on',binfo['time']['updated'])
print('1 Bicoin=$',binfo['bpi']['USD']['rate'])