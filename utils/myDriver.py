# myDriver
# 2021/6/29
# -*- coding:utf-8 -*-

# from utils.mySettings import url, username, password, implicitly_time_out
from selenium import webdriver
from utils.mySettings import load_yaml_data_by_key


yaml_data = load_yaml_data_by_key('../utils/mySettings.yaml', 'init_driver')


class Driver:
    # 初始化为空
    _driver = None

    @classmethod
    def get_driver(cls, browser_name="chrome"):
        """
        获取浏览器对象
        :param browser_name: 浏览器类型
        :return:
        """
        if cls._driver is None:
            if browser_name == "chrome":
                cls._driver = webdriver.Chrome()
            elif browser_name == "firefox":
                cls._driver = webdriver.Firefox()
            # ....
            else:
                raise ("没找到浏览器类型 %s, 请检查传参" % browser_name)

            cls._driver.implicitly_wait(yaml_data[0]['implicitly_time_out'])
            cls._driver.maximize_window()
            cls._driver.get(yaml_data[0]['url'])
            cls.__login()

        return cls._driver

    @classmethod  # 因为登陆只在初始化driver时使用，所以设置为私有方法
    def __login(cls):

        cls._driver.find_element_by_id("username").send_keys(yaml_data[0]['username'])
        cls._driver.find_element_by_id("password").send_keys(yaml_data[0]['password'])
        cls._driver.find_element_by_id("btnLogin").click()

#
# if __name__ == '__main__':
#     Driver.get_driver()
