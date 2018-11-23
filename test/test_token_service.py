# coding = utf-8
import api

def test_get_token():
    username = 'username'
    password = 'password'
    result = api.get_token(username, password)
    assert len(result) == 0
    
    username = 'hainq'
    password = '123456'
    result = api.get_token(username, password)
    assert len(result) > 0 
    
    username = None
    password = '123456'
    result = api.get_token(username, password)
    assert len(result) == 0

def test_validate_token():
    token = 'dump'
    assert api.validate_token(token) == False

    username = 'hainq'
    password = 'hainq'   
    token =  api.get_token(username, password)
    assert api.validate_token(token) == False
    
    username = 'hainq'
    password = '123456'   
    token =  api.get_token(username, password)
    assert api.validate_token(token) == True