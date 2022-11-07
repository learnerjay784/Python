# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 23:59:45 2022

@author: hp
"""

import logging
logging.basicConfig(filename='mylog14.log',level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s',
                    datefmt='%d/%m/%Y %I:%M:%S %p')

logging.info('A new request came')
try:
  x=int(input('Enter first number:')
  y=int(input('Enter second number:'))
  print('The Result:',x/y)
except ZeroDivisionError as msg:
  print('Cannot divide with zero')
  logging.exception(msg)
except ValueError as msg:
  print('Provide int value only')
  logging.exception(msg)

logging.info('Request processing complete')
