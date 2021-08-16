"""
逻辑接口层
    用户接口
"""

from db import db_handler
from lib import common


def register_interface(username, password, balance=15000):
    user_dict = db_handler.select(username)
    if user_dict:
        return False, '用户名已存在!'
    else:
        password = common.get_wd_md5(password)
        user_dict = {'username': username,
                     'password': password,
                     'balance': balance,
                     'flow': [],
                     'shop_car': {},
                     'locked': False
                     }

        db_handler.save(user_dict)
        return True, f'{username}注册成功！'


def login_interface(username, password):
    password = common.get_wd_md5(password)
    user_dict = db_handler.select(username)
    if user_dict['locked']:
        return False, '该账户已被冻结！'
    if user_dict:
        if user_dict.get('password') == password:
            return True, f"用户: [{username}]登录成功！"
        else:
            return False, '密码错误！'
    else:
        return False, f"用户不存在，请重新输入！"


def check_bal_interface(username):
    user_dict = db_handler.select(username)
    return user_dict.get('balance')
