# coding=utf-8

import time

from action.miniprogram.mini_program_login import Login
from elements.mini_program_elements import *

from action.base_page import BasePage

"""团员我的页面"""


class MiniLeagueMemberMine(BasePage):
    "我的"

    def mini_op_mine(self):
        # 点击我的
        time.sleep(1)
        self.wait_presence_element(MINI_BUTTON_MINE).click()

    "优惠券"

    def mini_op_mine_coupon(self):
        # 点击优惠券
        time.sleep(1)
        self.wait_presence_element(MINI_BUTTON_MINE_COUPON).click()

    """通用券"""

    def mini_op_mine_coupon_number(self):
        # 通用券
        time.sleep(1)
        self.wait_presence_element(MINI_BUTTON_MINE_COUPON_NUMBER).click()

        """历史优惠券"""

    def mini_op_mine_coupon_historical(self):
        # 点击历史优惠券
        time.sleep(1)
        self.wait_presence_element(MINI_BUTTON_MINE_COUPON_HISTORICAL).click()

    """关于十荟团"""

    def mini_op_mine_mine_about_sht(self):
        # 点击关于十荟团
        time.sleep(1)
        self.wait_presence_element(MINI_BUTTON_MINE_ABOUT_SHT).click()

    """资质信息"""

    def mini_op_mine_qualification(self,mp_driver):
        #　上滑
        Login().swipe_up(mp_driver)
        # 点击关于十荟团
        time.sleep(1)
        self.wait_presence_element(MINI_BUTTON_MINE_ABOUT_SHT).click()
        # 资质信息
        time.sleep(1)
        self.wait_presence_element(MINI_BUTTON_MINE_ABOUT_SHT_QUALIFICATION).click()

    """隐私权政策"""

    def mini_op_mine_privacy(self):
        # 隐私权政策
        time.sleep(1)
        self.wait_presence_element(MINI_BUTTON_MINE_ABOUT_SHT_PRIVACY).click()

    # """切换默认团长"""
    # class MiniLeagueMemberMine(BasePage):

    """切换默认团长为 sht@2"""

    def mini_op_switching_head_sht(self):
        # 点击我的
        self.wait_presence_element(MINI_BUTTON_MINE).click()
        # 点击默认团长
        self.wait_presence_element(MINI_BUTTON_MINE_SET_DEFAULT_LEADER).click()
        # 点击sht@2
        self.wait_presence_element(MINI_ELEMENT_WEI_XIN_MINE_NAME_SHT).click()

    """切换默认团长为 张珊珊"""

    def mini_op_switching_head_z(self):
        # 点击我的
        self.wait_presence_element(MINI_BUTTON_MINE).click()
        # 点击默认团长
        self.wait_presence_element(MINI_BUTTON_MINE_SET_DEFAULT_LEADER).click()
        # 点击张珊珊
        self.wait_presence_element(MINI_ELEMENT_WEI_XIN_MINE_NAME_Z).click()



