# coding=utf-8

import time

from elements.mini_program_elements import *
from action.base_page import BasePage
# 小程序 购物车
class ShoppingCart(BasePage):

    """增加商品数量"""
    def cart_add_goods_number(self):
        # 点击加号
        self.wait_presence_element(MINI_BUTTON_SHOPPING_CART_ADD_GOODS_NUMBER).click()

    """减少商品数量"""
    def cart_subtract_goods(self):
        # 点击减号
        self.wait_presence_element(MINI_BUTTON_SHOPPING_CART_REDUCE_GOODS_NUMBER).click()

    """购物车商品删除按钮"""
    def cart_delete_button(self):
        # 左滑
        #  TouchAction(mp_driver).press(x=500, y=416).move_to(x=482, y=416).release().perform()
        #点击删除
        self.wait_presence_element(MINI_BUTTON_SHOPPING_CART_DELETE).click()

    """购物车的确认按钮"""
    def cart_delete_sure(self):
        # 点击确定
        self.wait_presence_element(MINI_BUTTON_MINE_ORDER_DETAILS_ORDER_SURE).click()

    """购物车的再想想按钮"""
    def cart_think(self):
        # 点击再想想
        self.wait_presence_element(MINI_BUTTON_MINE_ORDER_DETAILS_THINK).click()

    """购物车的实惠精选"""
    def cart_delicate(self):
        # 实惠精选
        self.wait_presence_element(MINI_BUTTON_SHOPPING_CART_DELI).click()

    """购物车的全选"""
    def cart_select_all(self):
        # 全选
        self.wait_presence_element(MINI_BUTTON_SHOPPING_CART_SELECTED).click()

    """购物车的去支付"""
    def cart_pay(self):
        # 去支付
        self.wait_presence_element(MINI_BUTTON_SHOPPING_CART_PAY).click()


    """购物车删除商品"""
    def mini_op_cart_del_goods(self):
        #
        self.wait_presence_element(MINI_BUTTON_SHOPPING_CART_PAY).click()




    """多规格商品加购物车"""
    def add_more_specs(self):
        # 点击1702840
        self.wait_presence_element(MINI_BUTTON_HOME_PRODUCT_MORE_SPECS).click()
        # 点击加入购物车
        self.wait_presence_element(MINI_BUTTON_GOODS_DETAILS_ADD_CART).click()
        # 点击确定
        self.wait_presence_element(MINI_BUTTON_MINE_ORDER_DETAILS_ORDER_SURE_SPACE).click()
        time.sleep(2)

    """低于1元商品加购物车"""
    def add_small_one(self):
        # 单价低于1元
        self.wait_presence_element(MINI_BUTTON_HOME_PRODUCT_SMALL_ONE).click()
        # 点击加入购物车
        self.wait_presence_element(MINI_BUTTON_GOODS_DETAILS_ADD_CART).click()

    """高于1元商品加购物车"""
    def add_big_one(self):
        #高于1元商品
        self.wait_presence_element(MINI_BUTTON_HOME_PRODUCT_BIG_ONE).click()
        # 点击加入购物车
        self.wait_presence_element(MINI_BUTTON_GOODS_DETAILS_ADD_CART).click()
        time.sleep(2)

    """零钱不足商品加购物车"""
    def add_not_money(self):
        # 零钱不足
        self.wait_presence_element(MINI_BUTTON_HOME_PRODUCT_NOT_MONEY).click()
        # 点击加入购物车
        self.wait_presence_element(MINI_BUTTON_GOODS_DETAILS_ADD_CART).click()
        time.sleep(2)

    """单价低于一元的商品进入确认订单页"""
    def small_one_confirm_order(self):
        # 单价低于一元的商品
        self.wait_presence_element(MINI_BUTTON_HOME_PRODUCT_SMALL_ONE).click()
        # 立即购买
        self.wait_presence_element(MINI_BUTTON_GOODS_DETAILS_BUYING).click()
        #确定
        self.wait_presence_element(MINI_BUTTON_MINE_ORDER_DETAILS_ORDER_SURE_SPACE).click()
        time.sleep(2)

    """单价高于一元的商品进入确认订单页"""
    def big_one_confirm_order(self):
        # 单价高于一元的商品
        self.wait_presence_element(MINI_BUTTON_HOME_PRODUCT_BIG_ONE).click()
        # 立即购买
        self.wait_presence_element(MINI_BUTTON_GOODS_DETAILS_BUYING).click()
        # 确定
        self.wait_presence_element(MINI_BUTTON_MINE_ORDER_DETAILS_ORDER_SURE_SPACE).click()
        time.sleep(2)

    '''小于1商品下单'''
    def goods_less(self):
        #点击价格小于1
        self.wait_presence_element(MINI_BUTTON_HOME_PRODUCT_SMALL_ONE).click()
        # 立即购买
        self.wait_presence_element(MINI_BUTTON_GOODS_DETAILS_BUYING).click()
        # 确定
        self.wait_presence_element(MINI_BUTTON_MINE_ORDER_DETAILS_ORDER_SURE_SPACE).click()
        # 确认支付
        self.wait_presence_element(MINI_BUTTON_MINE_CONFIRM_ORDER_PAYMENT).click()

    '''库存不足商品下单'''
    def not_stock(self):
        #点击库存不足
        self.wait_presence_element(MINI_BUTTON_HOME_PRODUCT_NOT_STOCK).click()
        # 立即购买
        self.wait_presence_element(MINI_BUTTON_GOODS_DETAILS_BUYING).click()
        # 确定
        self.wait_presence_element(MINI_BUTTON_MINE_ORDER_DETAILS_ORDER_SURE_SPACE).click()
        # 确认支付
        self.wait_presence_element(MINI_BUTTON_MINE_CONFIRM_ORDER_PAYMENT).click()

