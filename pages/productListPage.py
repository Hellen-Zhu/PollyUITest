# productListPage
# 2021/7/13
from pages.basePage import BasePage
from selenium.webdriver.common.by import By


class ProductListPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.url = "http://120.55.190.222:38090/#/pms/product"

    product_name = (By.CSS_SELECTOR, 'tbody > tr:nth-child(1) > td:nth-child(4) p:nth-child(1)')
    brand_name = (By.CSS_SELECTOR, 'tbody > tr:nth-child(1) > td:nth-child(4) p:nth-child(2)')

    # 一般来说，如果页面，有数据列表
    # 要匹配列表的第一行，列表第一行的每一个字段
    # 列表中，每一个字段，都匹配一个元素列表
    def first_product_name_box(self):
        return self.get_locator(self.product_name)

    def first_brand_name_box(self):
        return self.get_locator(self.brand_name)


class ProductListPageAction(ProductListPage):

    def get_product_name_info(self):
        self.to_page(self.url)
        return self.first_product_name_box().text



# ProductListPageActionObj = ProductListPageAction()
# if __name__ == '__main__':
#     ProductListPageActionObj.get_first_product_name('test','品牌：gucci')
