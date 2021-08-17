"""
银行相关业务接口
"""
import db as db

from db import db_handler
from lib import common

bank_logger = common.get_logger('bank')


def withdraw_interface(username, money):
    user_dict = db_handler.select(username)
    balance = user_dict.get('balance')
    money2 = money * 1.05
    print(f'用户{username}账户余额为{balance}')
    if money2 > balance:
        return False, '余额不足'
    balance -= money2
    user_dict['balance'] = balance
    flow = f'用户{username}提现金额{money}成功，手续费为{money * 0.05},现余额为{balance}'
    user_dict['flow'].append(flow)
    db_handler.save(user_dict)
    bank_logger.info(flow)
    return True, flow


def repay_interface(username, money):
    user_dict = db_handler.select(username)
    user_dict['balance'] += money
    flow = f'用户{username}还款金额{money}成功,为现余额为{user_dict["balance"]}'
    user_dict['flow'].append(flow)
    db_handler.save(user_dict)
    bank_logger.info(flow)
    return True, flow


def transfer_interface(login_user, to_user, money):
    login_user_dict = db_handler.select(login_user)
    to_user_dict = db_handler.select(to_user)
    if not to_user_dict:
        return False, f'用户{to_user}不存在！'
    if login_user_dict['balance'] < money:
        return False, '当前账户余额不足,请重新输入!'
    to_user_dict['balance'] += money
    login_user_dict['balance'] -= money

    login_user_flow = f'用户[{login_user}]转账{money}元给用户[{to_user}]成功！'
    login_user_dict['flow'].append(login_user_flow)
    to_user_flow = f'用户[{to_user}]接收到用户[{login_user}]转账{money}元！'
    to_user_dict['flow'].append(to_user_flow)

    db_handler.save(login_user_dict)
    bank_logger.info(login_user_flow)
    db_handler.save(to_user_dict)
    bank_logger.info(to_user_flow)
    return True, login_user_flow


def check_flow_interface(login_user):
    user_dict = db_handler.select(login_user)
    bank_logger.info(f'查看用户[{login_user}]流水')
    return True, user_dict.get('flow')


def pay_interface(login_user, cost):
    user_dict = db_handler.select(login_user)
    if cost > user_dict['balance']:
        return False
    user_dict['balance'] -= cost
    flow = f'用户消费金额: [{cost}]元'
    user_dict['flow'].append(flow)
    db_handler.save(user_dict)
    bank_logger.info(flow)
    return True
