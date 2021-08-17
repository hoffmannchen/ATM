"""
逻辑接口层
    用户接口
"""

from db import db_handler
from lib import common

user_logger = common.get_logger('user')


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
        msg = f'{username}注册成功！'
        user_logger.info(msg)
        return True, msg


def login_interface(username, password):
    password = common.get_wd_md5(password)
    user_dict = db_handler.select(username)

    if user_dict:
        if user_dict['locked']:
            msg = '该账户已被冻结！'
            user_logger.warning(msg)
            return False, msg
        if user_dict.get('password') == password:
            msg = f"用户: [{username}]登录成功！"
            user_logger.info(msg)
            return True, msg
        else:

            msg = '密码错误！'
            user_logger.warning(msg)
            return False, msg
    else:
        msg = f"用户不存在，请重新输入！"
        user_logger.warning(msg)
        return False, msg


def check_bal_interface(username):
    user_dict = db_handler.select(username)
    return user_dict.get('balance')
