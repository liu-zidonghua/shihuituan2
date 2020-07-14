# coding=utf-8


import time

from elements.mini_program_elements import *
from action.base_page import BasePage

# 商品详情类
class GoodsDetails(BasePage):

    """商品详情页分享"""
    def goods_share(self):
        # 分享
        self.wait_presence_element(MINI_BUTTON_GOODS_DETAILS_SHARE).click()

    """商品详情页微信好友"""
    def wechat_friend(self):
        # 微信好友
        self.wait_presence_element(MINI_BUTTON_HOME_SHARE_FRIEND).click()

    """商品详情页生成海报"""
    def create_bill(self):
        # 生成海报
        self.wait_presence_element(MINI_BUTTON_HOME_SHARE_CREATE_BILL).click()

    """商品详情页取消分享"""
    def cancel_share(self):
        # 取消分享
        self.wait_presence_element(MINI_BUTTON_MINE_WEI_XIN_CANCEL).click()

    """商品详情页取消分享"""
    def download_picture(self):
        # 下载图片
        self.wait_presence_element(MINI_BUTTON_HOME_SHARE_DOWNLOAD_BILL).click()

    """给微信好友发送海报"""
    def send_poster_friend(self):
        # 点击微信好友
        self.wait_presence_element(MINI_BUTTON_HOME_SHARE_FRIEND).click()
        #给中国联通发送海报
        self.wait_presence_element(MINI_BUTTON_HOME_SHARE_FRIEND_LIAN_TONG).click()
        # 点击发送
        self.wait_presence_element(MINI_BUTTON_HOME_SHARE_FRIEND_SEND).click()

    """生成海报"""
    def create_poster(self):
        # 下载海报
        self.wait_presence_element(MINI_BUTTON_HOME_SHARE_CREATE_BILL).click()
        time.sleep(5)
        #下载图片
        self.wait_presence_element(MINI_BUTTON_HOME_SHARE_DOWNLOAD_BILL).click()

    """加入购物车"""
    def adding_cart(self):
        # 加入购物车
        self.wait_presence_element(MINI_BUTTON_GOODS_DETAILS_ADD_CART).click()



    """立即购买+确定"""
    def buy_now(self):
        # 立即购买
        self.wait_presence_element(MINI_BUTTON_GOODS_DETAILS_BUYING).click()
        # 确定
        self.wait_presence_element(MINI_BUTTON_MINE_ORDER_DETAILS_ORDER_SURE).click()

    """立即购买"""
    def buy_now_button(self):
        # 立即购买
        self.wait_presence_element(MINI_BUTTON_GOODS_DETAILS_BUYING).click()

    """立即购买页添加数量"""
    def add_number_buy(self):
        # 立即购买页添加数量
        self.wait_presence_element(MINI_INPUT_HOME_ADD_CART).click()