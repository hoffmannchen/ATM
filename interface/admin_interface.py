from db import db_handler
from lib import common

admin_logger = common.get_logger('admin')


def change_balance_interface(username, money):
    user_dict = db_handler.select(username)
    if user_dict:
        user_dict['balance'] = int(money)
        db_handler.save(user_dict)
        msg = f'管理员修改用户:[{username}]额度修改成功！'
        admin_logger.info(msg)
        return True, msg
    msg = '修改额度的用户不存在！'
    return False, msg


def lock_user_interface(username):
    user_dict = db_handler.select(username)
    if user_dict:
        user_dict['locked'] = True
        db_handler.save(user_dict)
        msg = f'冻结用户[{username}]成功！'
        admin_logger.info(msg)
        return True, msg
    msg = '冻结用户不存在！'
    admin_logger.warning(msg)
    return False, msg
