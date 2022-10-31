# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 17:01:55 2022

@author: hp
"""

import logging
logging.basicConfig(filename='log2.txt',filemode='a')
print('logging Demo')
logging.critical('This is critical message')
logging.error('This is error message')
logging.warning('This is warning message')
logging.info('This is info message')
logging.debug('This is debug message')
