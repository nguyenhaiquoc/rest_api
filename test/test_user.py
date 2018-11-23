# -*- coding: utf-8 -*-

from api.users import Users

def test_user():
    username = 'test'
    password = 'test'
    assert Users.check_autheninfo(username, password) == False
    
    username = 'hainq'
    password = '123456'
    assert Users.check_autheninfo(username, password) == True
    
    
    username = 'hainq'
    password = '1'
    assert Users.check_autheninfo(username, password) == False
    
    username = None
    password = '1'
    assert Users.check_autheninfo(username, password) == False
