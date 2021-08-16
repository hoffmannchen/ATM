"""
购物商城接口
"""
from db import db_handler


def shopping_interface(login_user, shopping_car):
    cost = 0
    for price, number in shopping_car.values:
        cost += price * number
    # 逻辑校验成功后，再调用银行支付接口
    from interface import bank_interface
    flag = bank_interface.pay_interface(login_user, cost)
    if flag:
        return True, '支付成功, 准备发货！'
    return False, '支付失败,金额不足！'


def add_shop_car_interface(login_user, shopping_car):
    user_dict = db_handler.select(login_user)
    for shop_name, price_number in shopping_car.items():
        price, number = price_number
        if shop_name in user_dict['shop_car']:
            user_dict['shop_car'][shop_name][1] += number
        else:
            user_dict['shop_car'][shop_name] = [price, number]
    db_handler.save(user_dict)
    return True, '添加购物车成功！'
