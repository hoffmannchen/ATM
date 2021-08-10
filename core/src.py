"""
存放用户视图层
"""


# 1、注册功能
def register():
    while True:
        # 第一层 让用户输入用户名和密码并校验
        username = input('请输入用户名: ').strip()
        password = input("请输入密码: ").strip()
        re_password = input("请确认密码: ")
        # 小逻辑处理: 比如两次密码是否一致
        if password == re_password:
            # 接收到注册后的结果
            user_dict = {'username': username,
                         'password': password,
                         'balance': 15000,
                         'flow': [],
                         'shop_cart': {},
                         'locked': False
                         }
            import json
            import os
            from conf import settings
            user_path = os.path.join(settings.BASE_PATH, f'{username}.json')
            with open(user_path, 'w', encoding='utf-8') as f:
                json.dump(user_dict, f)


# 2、登录功能
def login():
    pass


# 3、查看余额
def check_balance():
    pass


# 4、提现功能
def withdraw():
    pass


# 5、还款功能
def repay():
    pass


# 6、转账功能
def transfer():
    pass


# 7、查看流水
def check_flow():
    pass


# 8、购物功能
def shopping():
    pass


# 9、查看购物车
def check_shop_cart():
    pass


# 10、管理员功能
def admin():
    pass


# 创建函数功能字典
func_dict = {
    '1': register,
    '2': login,
    '3': check_balance,
    '4': withdraw,
    '5': repay,
    '6': transfer,
    '7': check_flow,
    '8': shopping,
    '9': check_shop_cart,
    '10': admin
}


# 视图层主程序
def run():
    while True:

        print(
            """
        ==== ATM + 购物车 ====
        1、注册功能
        2、登录功能
        3、查看余额
        4、提现功能
        5、还款功能
        6、转账功能
        7、查看流水
        8、购物功能
        9、查看购物车
        10、管理员功能
        ==== end ====
            """)
        choice = input("请输入功能编号: ").strip()
        if choice in func_dict:
            func_dict.get(choice)()  # func_dict.get('1') --> register()
        else:
            print('请输入正确的功能编号！')
            continue
