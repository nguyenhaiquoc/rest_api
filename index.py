#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 00:48:28 2018

@author: hai
"""

import api
import jwt

if __name__ == '__main__':
    token = api.get_token('hainq','123456')
    print (token)
    decode = jwt.decode(token, 'secret', algorithms='HS256')
    print  (decode)
    
    decode = jwt.decode("hsdhsgd", 'secret', algorithms='HS256')
    print  (decode)