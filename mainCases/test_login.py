# test_login
# 2021/7/12
import pytest
import time
from utils.myDriver import Driver
from pageObject.pages.productListPage import ProductListPageAction
from pageObject.pages.addProductPage import AddProductPageAction
from publicLib.public import ran_str


class TestLogin:
    def setup_class(cls):
        cls.driver = Driver.get_driver()
        cls.prod_list_page_obj = ProductListPageAction(cls.driver)
        cls.add_prod_page_obj = AddProductPageAction(cls.driver)

    def teardown_class(cls):
        if cls.driver is not None:
            cls.driver.quit()

    # def test_view_prod_list_info(self):
    #     first_product_name = self.prod_list_page_obj.get_product_name_info()
    #
    #     assert first_product_name == 'test'
    #     print("*********************", first_product_name)

    def test_add_prod(self):
        product_name = "自动化%s" % ran_str(5)
        self.add_prod_page_obj.add_product_action("1", "1", product_name, "副标题%s" % ran_str(5), "1")
        first_product_name = self.prod_list_page_obj.get_product_name_info()
        assert first_product_name == product_name


if __name__ == '__main__':
    pytest.main(['-s'])
