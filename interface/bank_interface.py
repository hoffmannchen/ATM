"""
银行相关业务接口
"""
from db import db_handler


def withdraw_interface(username, money):
    user_dict = db_handler.select(username)
    balance = user_dict.get('balance')
    money2 = money * 1.05
    print(f'用户{username}账户余额为{balance}')
    if money2 > balance:
        return False, '余额不足'
    balance -= money2
    user_dict['balance'] = balance
    db_handler.save(user_dict)
    return True, f'用户{username}提现金额{money}成功，手续费为{money * 0.05},现余额为{balance}'


def repay_interface(username, money):
    user_dict = db_handler.select(username)
    user_dict['balance'] += money
    db_handler.save(user_dict)
    return True, f'用户{username}还款金额{money}成功,为现余额为{user_dict["balance"]}'


def transfer_interface(login_user, to_user, money):
    login_user_dict = db_handler.select(login_user)
    to_user_dict = db_handler.select(to_user)
    if not to_user_dict:
        return False, f'用户{to_user}不存在！'
    if login_user_dict['balance'] < money:
        return False, '当前账户余额不足,请重新输入!'
    to_user_dict['balance'] += money
    login_user_dict['balance'] -= money
    db_handler.save(login_user_dict)
    db_handler.save(to_user_dict)
    return True, f'用户{login_user}转账{money}元给用户{to_user}成功！'
