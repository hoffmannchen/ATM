"""
银行相关业务接口
"""
from db import db_handler


def withdraw_interface(username, money):
    user_dict = db_handler.select(username)
    balance = int(user_dict.get('balance'))
    money2 = money * 1.05
    print(f'用户{username}账户余额为{balance}')
    if money2 > balance:
        return False, '余额不足'
    balance -= money2
    user_dict['balance'] = balance
    db_handler.save(user_dict)
    return True, f'用户{username}提现金额{money}成功，手续费为{money * 0.05},现余额为{balance}'
