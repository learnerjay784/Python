# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 16:16:28 2022

@author: hp
"""

import logging
logging.basicConfig(filename='log.txt',level=40)
print('logging Demo')
logging.critical('This is critical message')
logging.error('This is error message')
logging.warning('This is warning message')
logging.info('This is info message')
logging.debug('This is debug message')
