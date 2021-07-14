# -*- coding:utf-8 -*-

"""添加商品页面"""

from pages.basePage import BasePage
# from publicLib.public import ran_str
from selenium.webdriver.common.by import By
import time


class AddProductPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)  # 执行父类的构造方法
        self.url = "http://120.55.190.222:38090/#/pms/addProduct"

    productCategoryLabel = (By.CSS_SELECTOR, "form > div:nth-child(1) .el-cascader__label")
    categoryListSelector = (By.CSS_SELECTOR, "ul.el-cascader-menu > li:nth-child(%s)")
    categoryOptionSelector = (By.CSS_SELECTOR, "ul + ul.el-cascader-menu > li:nth-child(%s)")
    productNameLabel = (By.CSS_SELECTOR, "label[for=\"name\"] + div input")
    productSubTitleLabel = (By.CSS_SELECTOR, "label[for=\"subTitle\"] + div input")
    productBrandIdLabel = (By.CSS_SELECTOR, "label[for=\"brandId\"] + div input")
    productBrandIdDropDownList = (By.CSS_SELECTOR, "body > div:nth-child(8) ul > li:nth-child(%s)")
    heraldProductFlag = (By.XPATH, "//*[text()=\"预告商品：\"]/..//span")
    nextStepForDiscount = (By.XPATH, "//*[text()=\"下一步，填写商品促销\"]")
    nextStepForProductAttribute = (By.XPATH, "//*[text()=\"下一步，填写商品属性\"]")
    nextStepForRelatedProduct = (By.XPATH, "//*[text()=\"下一步，选择商品关联\"]")
    nextStepForSubmitProduct = (By.XPATH, "//*[text()=\"完成，提交商品\"]")
    confirmSubmitButton = (
        By.CSS_SELECTOR, "[class=\"el-button el-button--default el-button--small el-button--primary \"]")

    def product_classification_select_box(self):
        """商品分类下拉框, 外框"""
        return self.get_locator(self.productCategoryLabel)

    def product_classification_select_box_idx1(self, idx1):
        """商品分类下拉框, 一级分类"""
        category_list_selector = (self.categoryListSelector[0], self.categoryListSelector[1] % idx1)
        return self.get_locator(category_list_selector)

    def product_classification_select_box_idx2(self, idx2):
        """商品分类下拉框, 二级分类"""
        category_option_selector = (self.categoryOptionSelector[0], self.categoryOptionSelector[1] % idx2)
        return self.get_locator(category_option_selector)

    def product_name_input_box(self):
        """商品名称输入框"""
        return self.get_locator(self.productNameLabel)

    def product_subtitle_input_box(self):
        """副标题输入框"""
        return self.get_locator(self.productSubTitleLabel)

    def product_brand_select_box(self):
        """商品品牌下拉框外框"""
        return self.get_locator(self.productBrandIdLabel)

    def product_brand_select_box_option(self, idx):
        """商品品牌下拉框, 一级分类"""
        product_brand_id_drop_down_list = (self.productBrandIdDropDownList[0], self.productBrandIdDropDownList[1] % idx)
        return self.get_locator(product_brand_id_drop_down_list)

    def next_step_commodity_promotion_button_box(self):
        """下一步, 填写商品促销按钮"""
        return self.get_locator(self.nextStepForDiscount)

    def is_herald_box(self):
        """预告商品开关"""
        return self.get_locator(self.heraldProductFlag)

    def next_step_product_attribute_button_box(self):
        """下一步, 填写商品属性按钮"""
        return self.get_locator(self.nextStepForProductAttribute)

    def next_step_choose_product_related_button_box(self):
        """下一步, 选择商品关联按钮"""
        return self.get_locator(self.nextStepForRelatedProduct)

    def submit_product_button_box(self):
        """完成, 提交商品按钮"""
        return self.get_locator(self.nextStepForSubmitProduct)

    def confirm_submission_box(self):
        """确认提交按钮"""
        return self.get_locator(self.confirmSubmitButton)


class AddProductPageAction(AddProductPage):

    def add_product_action(self, idx1, idx2, product_name, subtitle, brand_select_idx):
        """
        添加一个商品
        :param idx1: 商品分类一级分类下标
        :param idx2: 商品分类二级分类下标
        :param product_name: 商品名称
        :param subtitle: 商品副标题
        :param brand_select_idx: 商品品牌一级分类下标
        :return:
        """
        self.to_page(self.url)
        # 点击商品分类下拉外框
        self.product_classification_select_box().click()
        time.sleep(5)
        # 选择商品分类, 一级分类
        self.product_classification_select_box_idx1(idx1).click()
        # 选择二级分类
        self.product_classification_select_box_idx2(idx2).click()
        # 输入商品名称
        self.product_name_input_box().send_keys(product_name)
        # 输入副标题
        self.product_subtitle_input_box().send_keys(subtitle)
        # 点击商品品牌下拉框外框
        self.product_brand_select_box().click()
        # 选择商品品牌一级分类
        self.product_brand_select_box_option(brand_select_idx).click()
        # 点击[下一步,填写商品促销]按钮
        self.next_step_commodity_promotion_button_box().click()
        # 点击是否预告商品开关
        self.is_herald_box().click()
        # 点击[下一步, 填写商品属性]按钮
        self.next_step_product_attribute_button_box().click()
        # 点击下一步, 选择商品关联按钮
        self.next_step_choose_product_related_button_box().click()
        time.sleep(0.3)
        # 点击完成,提交商品按钮
        self.submit_product_button_box().click()
        # 确认提交
        self.confirm_submission_box().click()

