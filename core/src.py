"""
存放用户视图层
"""
from interface import user_interface
from lib import common
from interface import bank_interface

login_user = None


# 1、注册功能
def register():
    while True:
        username = input('请输入用户名: ').strip()
        password = input("请输入密码: ").strip()
        re_password = input("请确认密码: ").strip()
        if password == re_password:
            flag, msg = user_interface.register_interface(username, password)
            print(msg)
            if flag:
                break


# 2、登录功能
def login():
    while True:
        username = input('请输入用户名: ').strip()
        password = input('请输入密码: ').strip()
        flag, msg = user_interface.login_interface(username, password)
        if flag:
            print(msg)
            global login_user
            login_user = username
            break
        else:
            print(msg)


# 3、查看余额
@common.logging_auth
def check_balance():
    balance = user_interface.check_bal_interface(login_user)
    print(f'用户{login_user}账户余额为: {balance}')


# 4、提现功能
@common.logging_auth
def withdraw():
    while True:
        input_money = input('请输入提现金额: ').strip()
        if input_money.isdigit():
            input_money = int(input_money)
        else:
            print('请重新输入数字!')
            continue
        flag, msg = bank_interface.withdraw_interface(login_user, input_money)
        print(msg)
        if flag:
            break


# 5、还款功能
@common.logging_auth
def repay():
    """
    还款金额任意大小
    :return:
    """
    while True:
        input_money = input("请输入还款金额: ").strip()
        if not input_money.isdigit():
            print("请重新输入数字!")
            continue

        input_money = int(input_money)
        if input_money > 0:
            flag, msg = bank_interface.repay_interface(login_user, input_money)
            if flag:
                print(msg)
            break
        else:
            print('还款金额必须大于0!')
            continue


# 6、转账功能
@common.logging_auth
def transfer():
    while True:
        to_user = input('请输入目标账户: '.strip())
        money = input("请输入转账金额: ").strip()
        if not money.isdigit():
            print("请输入正确的金额!")
            continue
        flag, msg = bank_interface.transfer_interface(login_user, to_user, int(money))
        print(msg)
        if flag:
            break
        else:
            continue


# 7、查看流水
@common.logging_auth
def check_flow():
    flag, flow_list = bank_interface.check_flow_interface(login_user)
    if flag:
        if flow_list:
            for i in flow_list:
                print(i)
        else:
            print('当前用户没有流水！')


# 8、购物功能
@common.logging_auth
def shopping():
    pass


# 9、查看购物车
@common.logging_auth
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
        ====     end     ====
            """)
        choice = input("请输入功能编号: ").strip()
        if choice in func_dict:
            func_dict.get(choice)()
        else:
            print('请输入正确的功能编号！')
            continue
