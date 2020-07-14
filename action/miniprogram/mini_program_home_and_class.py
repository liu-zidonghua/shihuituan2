# coding=utf-8

import time

from elements.mini_program_elements import *
from action.base_page import BasePage


# 今日团购类
class GroupBuy(BasePage):

    """新鲜蔬菜"""
    def fresh_vegetables(self):
        time.sleep(1)
        # 点击新鲜蔬菜
        self.wait_presence_element(MINI_BUTTON_CLASSIFY_VEGETABLES).click()

    """时令水果"""
    def season_fruits(self):
        # 点击时令水果
        self.wait_presence_element(MINI_BUTTON_CLASSIFY_FRUITS).click()

    """水产冻品"""
    def aquatic_products(self):
        # 水产冻品
        self.wait_presence_element(MINI_BUTTON_CLASSIFY_FROZEN_AQUATIC_PRODUCTS).click()

    """肉禽蛋品"""
    def meat_eggs(self):
        # 肉禽蛋品
        self.wait_presence_element(MINI_BUTTON_CLASSIFY_MEAT_EGGS).click()

    """粮油调味"""
    def grain_oil(self):
        # 粮油调味
        self.wait_presence_element(MINI_BUTTON_CLASSIFY_SEASONING_OF_GRAIN_AND_OIL).click()

    """酒水乳品"""
    def drinks_dairy_products(self):
        # 酒水乳品
        self.wait_presence_element(MINI_BUTTON_CLASSIFY_ALCOHOLIC_MILK).click()

    """休闲食品"""
    def snacks_food(self):
        # 休闲食品
        self.wait_presence_element(MINI_BUTTON_CLASSIFY_SNACKS).click()

    """生活美妆"""
    def life_beauty(self):
        # 生活美妆
        self.wait_presence_element(MINI_BUTTON_CLASSIFY_LIFE_BEAUTY).click()

    """生活服务"""
    def life_service(self):
        # 生活服务
        self.wait_presence_element(MINI_BUTTON_CLASSIFY_LIFE_SERVICE).click()

    """居家百货"""
    def home_department_store(self):
        # 居家百货
        self.wait_presence_element(MINI_BUTTON_CLASSIFY_HOME_DEPARTMENT_STORE).click()

    """热卖"""
    def hot_sell(self):
        # 热卖
        self.wait_presence_element(MINI_BUTTON_HOME_BEST_SELLERS).click()

    """新人专享"""
    def new_man_vip(self):
        # 新人专享
        self.wait_presence_element(MINI_BUTTON_CLASSIFY_NEW_VIP).click()

    """妈妈食材"""
    def mother_food(self):
        # 妈妈食材
        self.wait_presence_element(MINI_BUTTON_CLASSIFY_MOTHER_FOODS).click()

    """精选特惠"""
    def wow_deals(self):
        # 精选特惠
        self.wait_presence_element(MINI_BUTTON_CLASSIFY_PREFERENTIAL_TREATMENT).click()

    """爆款生鲜"""
    def explosive_money(self):
        # 爆款生鲜
        self.wait_presence_element(MINI_BUTTON_CLASSIFY_FRESH_GOODS).click()

    """团长专享"""
    def regimental_vip(self):
        # 团长专享
        self.wait_presence_element(MINI_BUTTON_HOME_VIP_REGIMENTAL).click()

    """猜您喜欢"""
    def guess_you_likes(self):
        # 猜您喜欢
        self.wait_presence_element(MINI_BUTTON_CLASSIFY_YOUR_LIKE).click()

    """采购中"""
    def procure_go_on(self):
        # 采购中
        self.wait_presence_element(MINI_BUTTON_CLASSIFY_PROCURE).click()

    # 金刚页面返回
    # TouchAction(mp_driver).tap(x=67, y=156).perform()

    """复制拼团"""
    def home_copy_group(self):
        # 点击复制拼图
        self.wait_presence_element(MINI_BUTTON_HOME_COPY_GROUP).click()



    """点击搜索商品"""

    def search_goods(self):
        # 点击搜索商品
        self.wait_presence_element(MINI_BUTTON_HOME_SEARCH_GOODS).click()

    """输入不存在的商品并搜索"""

    def no_goods(self):
        # 输入不存在的商品
        self.wait_presence_element(MINI_INPUT_HOME_SEARCH_TEXT).send_keys("15511111111")
        time.sleep(2)
        # 点击搜索
        self.wait_presence_element(MINI_BUTTON_HOME_SEARCH).click()

    """输入存在的商品并搜索"""

    def have_goods(self):
        # 输入存在的商品
        self.wait_presence_element(MINI_INPUT_HOME_SEARCH_TEXT).send_keys("零钱金额不足零钱金额不足")
        time.sleep(2)
        # 点击搜索
        self.wait_presence_element(MINI_BUTTON_HOME_SEARCH).click()

    """搜索框内容"""

    def click_seach(self):
        # 点击搜索框内容
        self.wait_presence_element(MINI_INPUT_HOME_SEARCH_TEXT).click()



# 购买类
class GoodsBuy(BasePage):

    """立即买"""
    def goods_buy(self):
        # 立即买
        self.wait_presence_element(MINI_INPUT_HOME_BUYING).click()


    """单规格大于1"""
    def goods_big_one(self):
        # 点击单规格大于1的商品
        self.wait_presence_element(MINI_BUTTON_HOME_PRODUCT_BIG_ONE).click()

    """单规格小于1"""
    def goods_small_one(self):
        # 点击单规格小于1的商品
        self.wait_presence_element(MINI_BUTTON_HOME_PRODUCT_SMALL_ONE).click()

    """库存不足"""
    def goods_not_stock(self):
        # 点击库存不足
        self.wait_presence_element(MINI_BUTTON_HOME_PRODUCT_NOT_STOCK).click()

    """零钱不足"""
    def goods_not_money(self):
        # 零钱不足
        self.wait_presence_element(MINI_BUTTON_HOME_PRODUCT_NOT_MONEY).click()

    """多规格"""
    def goods__more_specs(self):
        # 多规格商品1702840
        self.wait_presence_element(MINI_BUTTON_HOME_PRODUCT_MORE_SPECS).click()

    """抢光了"""
    def home_sell_out(self):
        # 抢光了
        self.wait_presence_element(MINI_INPUT_HOME_SEARCH_GOODS).click()



    """存在轮播图商品名称"""
    def goods_video(self):
        # 点击轮播图商品名称
        self.wait_presence_element(MINI_BUTTON_HOME_PRODUCT_VIDEO).click()

    """选规格"""
    def selection_specification(self):
        # 点击选规格
        self.wait_presence_element(MINI_INPUT_HOME_SPECIFICATIONS).click()
        # 点击确定
        self.wait_presence_element(MINI_BUTTON_MINE_ORDER_DETAILS_ORDER_SURE_SPACE).click()





