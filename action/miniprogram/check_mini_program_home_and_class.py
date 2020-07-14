# coding=utf-8

import time

from appium.webdriver.common.touch_action import TouchAction

from action.miniprogram.mini_program_login import Login
from elements.mini_program_elements import *
from action.base_page import BasePage


# 今日团购类
class MiniGroupBuy(BasePage):
    """跳转首页"""
    def mini_op_home(self):
        time.sleep(1)
        # 点击首页
        self.wait_presence_element(MINI_BUTTON_HOME).click()


    """新鲜蔬菜"""
    def mini_op_group_buy_fresh_vegetables(self):
        time.sleep(1)
        # 点击新鲜蔬菜
        self.wait_presence_element(MINI_BUTTON_CLASSIFY_VEGETABLES).click()

    """时令水果"""
    def mini_op_group_buy_season_fruits(self):
        # 点击时令水果
        self.wait_presence_element(MINI_BUTTON_CLASSIFY_FRUITS).click()

    """水产冻品"""
    def mini_op_group_buy_aquatic_products(self):
        # 水产冻品
        self.wait_presence_element(MINI_BUTTON_CLASSIFY_FROZEN_AQUATIC_PRODUCTS).click()

    """肉禽蛋品"""
    def mini_op_group_buy_meat_eggs(self):
        # 肉禽蛋品
        self.wait_presence_element(MINI_BUTTON_CLASSIFY_MEAT_EGGS).click()

    """粮油调味"""
    def mini_op_group_buy_grain_oil(self):
        # 粮油调味
        self.wait_presence_element(MINI_BUTTON_CLASSIFY_SEASONING_OF_GRAIN_AND_OIL).click()

    """酒水乳品"""
    def mini_op_group_buy_drinks_dairy_products(self):
        # 酒水乳品
        self.wait_presence_element(MINI_BUTTON_CLASSIFY_ALCOHOLIC_MILK).click()

    """休闲食品"""
    def mini_op_group_buy_snacks_food(self):
        # 休闲食品
        self.wait_presence_element(MINI_BUTTON_CLASSIFY_SNACKS).click()

    """生活美妆"""
    def mini_op_group_buy_life_beauty(self):
        # 生活美妆
        self.wait_presence_element(MINI_BUTTON_CLASSIFY_LIFE_BEAUTY).click()

    """生活服务"""
    def mini_op_group_buy_life_service(self):
        # 生活服务
        self.wait_presence_element(MINI_BUTTON_CLASSIFY_LIFE_SERVICE).click()

    """居家百货"""
    def mini_op_group_buy_home_department_store(self):
        # 居家百货
        self.wait_presence_element(MINI_BUTTON_CLASSIFY_HOME_DEPARTMENT_STORE).click()

    """热卖"""
    def mini_op_group_buy_hot_sell(self):
        # 热卖
        self.wait_presence_element(MINI_BUTTON_HOME_BEST_SELLERS).click()

    """新人专享"""
    def mini_op_group_buy_new_man_vip(self):
        # 新人专享
        self.wait_presence_element(MINI_BUTTON_CLASSIFY_NEW_VIP).click()

    """妈妈食材"""
    def mini_op_group_buy_mother_food(self):
        # 妈妈食材
        self.wait_presence_element(MINI_BUTTON_CLASSIFY_MOTHER_FOODS).click()

    """精选特惠"""
    def mini_op_group_buy_wow_deals(self):
        # 精选特惠
        self.wait_presence_element(MINI_BUTTON_CLASSIFY_PREFERENTIAL_TREATMENT).click()

    """爆款生鲜"""
    def mini_op_group_buy_explosive_money(self):
        # 爆款生鲜
        self.wait_presence_element(MINI_BUTTON_CLASSIFY_FRESH_GOODS).click()

    """团长专享"""
    def mini_op_group_buy_regimental_vip(self):
        # 团长专享
        self.wait_presence_element(MINI_BUTTON_HOME_VIP_REGIMENTAL).click()

    """猜您喜欢"""
    def mini_op_group_buy_guess_you_likes(self):
        # 猜您喜欢
        self.wait_presence_element(MINI_BUTTON_CLASSIFY_YOUR_LIKE).click()

    """采购中"""
    def mini_op_group_buy_procure_go_on(self):
        # 采购中
        self.wait_presence_element(MINI_BUTTON_CLASSIFY_PROCURE).click()

    # 金刚页面返回
    # TouchAction(mp_driver).tap(x=67, y=156).perform()

    """复制拼团"""
    def mini_op_group_buy_home_copy_group(self):
        # 点击复制拼图
        self.wait_presence_element(MINI_BUTTON_HOME_COPY_GROUP).click()



    """点击搜索商品"""

    def mini_op_search_goods(self):
        # 点击搜索商品
        self.wait_presence_element(MINI_BUTTON_HOME_SEARCH_GOODS).click()

    """输入不存在的商品并搜索"""

    def mini_op_search_no_goods(self):
        # 输入不存在的商品
        self.wait_presence_element(MINI_INPUT_HOME_SEARCH_TEXT).send_keys("15511111111")
        time.sleep(2)
        # 点击搜索
        self.wait_presence_element(MINI_BUTTON_HOME_SEARCH).click()

    """输入存在的商品并搜索"""

    def mini_op_search_have_goods(self):
        # 输入存在的商品
        self.wait_presence_element(MINI_INPUT_HOME_SEARCH_TEXT).send_keys("零钱金额不足零钱金额不足")
        time.sleep(2)
        # 点击搜索
        self.wait_presence_element(MINI_BUTTON_HOME_SEARCH).click()

    """搜索框内容"""

    def mini_op_search_click_search(self):
        # 点击搜索框内容
        self.wait_presence_element(MINI_INPUT_HOME_SEARCH_TEXT).click()


    """立即买"""
    def mini_op_goods_buy(self):
        # 立即买
        self.wait_presence_element(MINI_INPUT_HOME_BUYING).click()


    """单规格大于1"""
    def mini_op_home_goods_big_one(self):
        # 点击单规格大于1的商品
        self.wait_presence_element(MINI_BUTTON_HOME_PRODUCT_BIG_ONE).click()

    """单规格小于1"""
    def mini_op_home_goods_small_one(self):
        # 点击单规格小于1的商品
        self.wait_presence_element(MINI_BUTTON_HOME_PRODUCT_SMALL_ONE).click()

    """库存不足"""
    def mini_op_home_goods_not_stock(self):
        # 点击库存不足
        self.wait_presence_element(MINI_BUTTON_HOME_PRODUCT_NOT_STOCK).click()

    """零钱不足"""
    def mini_op_home_goods_not_money(self):
        # 零钱不足
        self.wait_presence_element(MINI_BUTTON_HOME_PRODUCT_NOT_MONEY).click()

    """多规格"""
    def mini_op_home_goods_more_specs(self):
        # 多规格商品1702840
        self.wait_presence_element(MINI_BUTTON_HOME_PRODUCT_MORE_SPECS).click()

    """抢光了"""
    def mini_op_home_sell_out(self):
        # 抢光了
        self.wait_presence_element(MINI_INPUT_HOME_SEARCH_GOODS).click()

    """存在轮播图商品名称"""
    def mini_op_goods_video(self):
        # 点击轮播图商品名称
        self.wait_presence_element(MINI_BUTTON_HOME_PRODUCT_VIDEO).click()

    """选规格"""
    def mini_op_goods_selection_specification(self,mp_driver):
        # 上滑3次
        for i in range(2):
            Login().swipe_up(mp_driver)
        # 点击选规格
        self.wait_presence_element(MINI_INPUT_HOME_SPECIFICATIONS).click()
        time.sleep(3)

        # 点击确定
        self.wait_presence_element(MINI_BUTTON_MINE_ORDER_DETAILS_ORDER_SURE).click()

    """首页单规格商品点击购物车按钮"""
    def mini_op_goods_single_specification_add_cart(self,mp_driver):
        #点击去首页看看
        self.wait_presence_element(MINI_BUTTON_SHOPPING_CART_JUMP_HOME).click()
        time.sleep(3)
        Login().swipe_up(mp_driver)
        # TouchAction(mp_driver).press(x=400, y=1560).move_to(x=400, y=344).release().perform()
        time.sleep(3)
        TouchAction(mp_driver).tap(x=980, y=983).perform()
        time.sleep(1)

    """累计销量0"""
    def mini_check_home_cumulative_sales_no(self):
        # 检查购物车商品数量加2
        cumulative_sales_no = self.wait_presence_element(MINI_BUTTON_HOME_KING_CUMULATIVE_SALES_NO).get_attribute('name')
        return cumulative_sales_no

