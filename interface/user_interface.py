"""
逻辑接口层
    用户接口
"""
import json
import os
from db import db_handler


def register_interface(username, password, balance=15000):
    user_dict = db_handler.select(username)
    if user_dict:
        return False, '用户名已存在!'
    else:
        user_dict = {'username': username,
                     'password': password,
                     'balance': balance,
                     'flow': [],
                     'shop_cart': {},
                     'locked': False
                     }

        db_handler.save(user_dict)
        return True, f'{username}注册成功！'
