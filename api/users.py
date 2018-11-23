# -*- coding: utf-8 -*-

user_map = {
    'hainq': '123456'        
}
class Users(object):
    """
        represent User table in database
    """
    #@classmethod
    @staticmethod
    def check_autheninfo(username, password):
        """
            return True if the infor match
        """
        if username in user_map:
            return user_map[username] == password
        return False
