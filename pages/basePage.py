# basePage
# 2021/7/12
# basePage主要封装一些常用的函数，为页面对象类进行服务
# 例如元素定位，输入，点击，访问url，等待，关闭


from selenium.webdriver.support import expected_conditions as ec  # 显示等待
from selenium.webdriver.support.wait import WebDriverWait  # 提供显示等待类
from utils.myDriver import Driver
import time

# from utils.mySettings import time_out, poll_frequency
class BasePage:
    def __init__(self,driver):
        self.driver = driver

    def to_page(self, url):
        time.sleep(3)
        self.driver.get(url)

    def get_locator(self, locator):
        """
                        走显示等待的逻辑，寻找元素
                        :param locator: 元素定位的方法和表达式，以元组形式传入，示例(By.ID, "abc")
                        :return:
                        """
        WebDriverWait(
            # 传入浏览器对象
            driver=self.driver,
            # 传入超时时间
            timeout=5,
            # 设置轮询时间
            poll_frequency=0.5).until(
            # 检查元素被加载并可见
            ec.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def input_text(self, loc, txt):
        self.get_locator(loc).send_keys(txt)

    def click_element(self, loc):
        self.get_locator(loc).click()

    # def wait(self, time):
    #     time.sleep(time)

    def quit(self):
        self.driver.quit()
