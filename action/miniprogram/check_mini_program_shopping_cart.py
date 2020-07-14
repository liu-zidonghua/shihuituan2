# coding=utf-8

import time

from action.miniprogram.mini_program_login import Login
from elements.mini_program_elements import *
from action.base_page import BasePage


# 小程序 购物车
class MiniShoppingCart(BasePage):
    """点击购物车页面"""

    def mini_op_shopping_cart(self):
        # 点击购物车
        self.wait_presence_element(MINI_BUTTON_SHOPPING_CART).click()

    """增加商品数量"""

    def mini_op_cart_add_goods_number(self):
        # 点击加号
        self.wait_presence_element(MINI_BUTTON_SHOPPING_CART_ADD_GOODS_NUMBER).click()

    """减少商品数量"""

    def mini_op_subtract_goods(self):
        # 点击减号
        self.wait_presence_element(MINI_BUTTON_SHOPPING_CART_REDUCE_GOODS_NUMBER).click()

    """购物车商品删除按钮"""

    def mini_op_delete_button(self):
        # 左滑
        #  TouchAction(mp_driver).press(x=500, y=416).move_to(x=482, y=416).release().perform()
        # 点击删除
        self.wait_presence_element(MINI_BUTTON_SHOPPING_CART_DELETE).click()

    """购物车的确认按钮"""

    def mini_op_cart_delete_sure(self):
        # 点击确定
        self.wait_presence_element(MINI_BUTTON_MINE_ORDER_DETAILS_ORDER_SURE).click()

    """购物车商品删除流程"""

    def mini_op_delete_goods(self):

        # 左滑
        #  TouchAction(mp_driver).press(x=500, y=416).move_to(x=482, y=416).release().perform()
        # 点击删除
        self.wait_presence_element(MINI_BUTTON_SHOPPING_CART_DELETE).click()
        time.sleep(3)
        # 点击确定
        self.wait_presence_element(MINI_BUTTON_MINE_ORDER_DETAILS_ORDER_SURE).click()

    """购物车的再想想按钮"""

    def mini_op_cart_think(self):
        # 点击再想想
        self.wait_presence_element(MINI_BUTTON_MINE_ORDER_DETAILS_THINK).click()

    """购物车的实惠精选"""

    def mini_op_cart_delicate(self):
        # 实惠精选
        self.wait_presence_element(MINI_BUTTON_SHOPPING_CART_DELI).click()

    """购物车的全选"""

    def mini_op_cart_select_all(self):
        # 全选
        self.wait_presence_element(MINI_BUTTON_SHOPPING_CART_SELECTED).click()

    """购物车的去支付"""

    def mini_op_cart_pay(self):
        # 去支付
        self.wait_presence_element(MINI_BUTTON_SHOPPING_CART_PAY).click()

    def mini_op_element_cart_pay(self):

        # 去支付
        time.sleep(3)
        self.wait_presence_element(MINI_BUTTON_SHOPPING_CART_PAY).get_attribute(
            'name')

    """购物车删除商品"""

    def mini_op_cart_del_goods(self, mp_driver):
        # 跳转购物车页面
        self.wait_presence_element(MINI_BUTTON_SHOPPING_CART).click()

        time.sleep(5)
        try:
            i = 1
            for i in range(8):

                a = self.wait_presence_element(MINI_BUTTON_SHOPPING_CART_PAY).get_attribute('name')
                b = []
                if a != b:
                    Login().swipe_left(mp_driver)
                    # 点击删除
                    self.wait_presence_element(MINI_BUTTON_SHOPPING_CART_DELETE).click()
                    time.sleep(3)
                    # 点击确定
                    self.wait_presence_element(MINI_BUTTON_MINE_ORDER_DETAILS_ORDER_SURE).click()

                    continue
                break

        except:
            print("购物车内无商品")

    """多规格商品加购物车"""

    def mini_op_cart_add_more_specs(self):
        # 点击1702840
        self.wait_presence_element(MINI_BUTTON_HOME_PRODUCT_MORE_SPECS).click()
        # 点击加入购物车
        self.wait_presence_element(MINI_BUTTON_GOODS_DETAILS_ADD_CART).click()
        # 点击确定
        self.wait_presence_element(MINI_BUTTON_MINE_ORDER_DETAILS_ORDER_SURE_SPACE).click()
        time.sleep(2)

    """低于1元商品加购物车"""

    def mini_op_cart_add_small_one(self):
        # 单价低于1元
        self.wait_presence_element(MINI_BUTTON_HOME_PRODUCT_SMALL_ONE).click()
        # 点击加入购物车
        self.wait_presence_element(MINI_BUTTON_GOODS_DETAILS_ADD_CART).click()

    """高于1元商品加购物车"""

    def mini_op_cart_add_big_one(self):
        # 高于1元商品
        self.wait_presence_element(MINI_BUTTON_HOME_PRODUCT_BIG_ONE).click()
        # 点击加入购物车
        self.wait_presence_element(MINI_BUTTON_GOODS_DETAILS_ADD_CART).click()
        time.sleep(2)

    """零钱不足商品加购物车"""

    def mini_op_cart_add_not_money(self):
        # 零钱不足
        self.wait_presence_element(MINI_BUTTON_HOME_PRODUCT_NOT_MONEY).click()
        # 点击加入购物车
        self.wait_presence_element(MINI_BUTTON_GOODS_DETAILS_ADD_CART).click()
        time.sleep(2)

    """购物车商品数量加1"""

    def mini_check_cart_add_one(self):
        # 检查购物车商品数量加1
        goods_number_one = self.wait_presence_element(MINI_BUTTON_SHOPPING_CART_ADD_GOODS_NUMBER_ONE).get_attribute(
            'name')
        return goods_number_one

    """购物车商品数量加2"""

    def mini_check_cart_add_two(self):
        # 检查购物车商品数量加2
        goods_number_two = self.wait_presence_element(MINI_BUTTON_SHOPPING_CART_ADD_GOODS_NUMBER_TWO).get_attribute(
            'name')
        return goods_number_two
