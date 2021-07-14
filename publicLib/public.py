# public
# 2021/6/29
# -*- coding:utf-8 -*-

import random
import string


def ran_str(num):
    """
    随机生成 num 个字符串
    :param num:
    :return:
    """
    str1 = string.ascii_letters  # 返回26个英文大小写字母的字符串
    str2 = string.digits  # 返回阿拉伯数字的字符串
    salt = "".join(random.sample("%s%s" % (str1, str2), num))  #随机去除num个字符串

    # salt = "".join(random.sample(string.ascii_letters + string.digits, num))

    return salt


if __name__ == '__main__':
    print(ran_str(5))
