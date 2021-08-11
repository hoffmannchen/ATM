"""
逻辑接口层
    用户接口
"""
import json
import os


# 注册接口
def register_interface(username, password, balance=15000):
    # 接收到注册后的结果

    user_dict = {'username': username,
                 'password': password,
                 'balance': balance,
                 'flow': [],
                 'shop_cart': {},
                 'locked': False
                 }

    with open(user_path, 'w', encoding='utf-8') as f:
        json.dump(user_dict, f, ensure_ascii=False)
