# object
# 2021/7/14
class AddProdPageObject(object):
    productCategoryLabel = "form > div:nth-child(1) .el-cascader__label"
    categoryListSelector = "ul.el-cascader-menu > li:nth-child(%s)"
    categoryOptionSelector = "ul + ul.el-cascader-menu > li:nth-child(%s)"
    productNameLabel = "label[for=\"name\"] + div input"
    productSubTitleLabel = "label[for=\"subTitle\"] + div input"
    productBrandIdLabel = "label[for=\"brandId\"] + div input"
    productBrandIdDropDownList = "body > div:nth-child(8) ul > li:nth-child(%s)"
    heraldProductFlag = "//*[text()=\"预告商品：\"]/..//span"
    nextStepForDiscount = "//*[text()=\"下一步，填写商品促销\"]"
    nextStepForProductAttribute = "//*[text()=\"下一步，填写商品属性\"]"
    nextStepForRelatedProduct = "//*[text()=\"下一步，选择商品关联\"]"
    nextStepForSubmitProduct = "//*[text()=\"完成，提交商品\"]"
    confirmSubmitButton = "[class=\"el-button el-button--default el-button--small el-button--primary \"]"