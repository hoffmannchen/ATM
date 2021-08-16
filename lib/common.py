"""
存放公共方法
"""
import hashlib
import logging.config
from conf import settings


def get_wd_md5(password):
    md5_obj = hashlib.md5()
    md5_obj.update(password.encode('utf-8'))
    salt = '一二三四五，Egon上山打老鼠！'
    md5_obj.update(salt.encode('utf-8'))
    return md5_obj.hexdigest()


def logging_auth(func):
    from core import src

    def inner(*args, **kwargs):
        if src.login_user:
            res = func(*args, **kwargs)
            return res
        else:
            print('未出示证明，无法享受美好的功能服务!')
            src.login()

    return inner


def get_logger(log_type):
    """

    :param log_type:user日志、bank日志、shop日志
    :return:
    """
    logging.config.dictConfig(settings.LOGGING_DIC)
    logger = logging.getLogger(log_type)

    return logger
