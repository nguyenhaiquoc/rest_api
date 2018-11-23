#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 00:05:06 2018

@author: hai
"""
from .users import Users
import jwt

def get_token(username, password):
    """
        validate username, password then return json token
        rType: token string jwt
    """
    if Users.check_autheninfo(username, password):
        return jwt.encode({'name': username}, 'secret', algorithm='HS256')
    return ""

def validate_token(token):
    """
        validate token
        retrun True if success, else
        @raise: jwt.exceptions.DecodeError
    """
    try:
        jwt.decode(token, 'secret', algorithm='HS256')
        return True
    except jwt.exceptions.DecodeError:
        return False
    return False