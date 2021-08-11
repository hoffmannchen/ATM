"""
数据处理层
    - 专门用于处理数据
"""
import json
import os
from conf import settings


# 查看数据
def select(username):
    # 接收接口层传递的用户名，拼接用户json文件路径
    user_path = os.path.join(settings.USER_DATA_PATH, f'{username}.json')
    # 查看用户是否存在
    if os.path.exists(user_path):
        # 读取用户数据，返回给接口层
        with open(user_path, 'r', encoding='utf8') as f:
            user_dict = json.load(f)
            return user_dict
    return None
