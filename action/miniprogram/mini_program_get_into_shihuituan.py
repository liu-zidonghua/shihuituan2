# coding=utf-8



import time

from elements.mini_program_elements import *
from action.base_page import BasePage

"""不同身份进入"""
class MiniDifferentName(BasePage):

    """通过张珊珊链接进入小程序首页"""
    def mini_op_name_link_z(self):
        # 点击张珊珊
        self.wait_presence_element(MINI_ELEMENT_WEI_XIN_MINE_NAME_Z).click()
        time.sleep(2)
        # 点击小程序链接
        self.wait_presence_element(MINI_ELEMENT_WEI_XIN_MINE_CHAT_PAGE_SHI_HUI_GROUP).click()
        time.sleep(7)

    """通过冀思雨链接进入小程序首页"""
    def mini_op_name_link_ji_si_yu(self):
        # 点击冀思雨
        self.wait_presence_element(MINI_ELEMENT_WEI_XIN_MINE_NAME_JI_SI_YU).click()
        time.sleep(2)
        # 点击链接进入
        self.wait_presence_element(MINI_ELEMENT_WEI_XIN_MINE_CHAT_PAGE_SHI_HUI_GROUP).click()
        time.sleep(2)

    """张珊珊切换微信账户为冀思雨"""
    def mini_op_switch_wei_xin(self):
        # 点击微信我的
        self.wait_presence_element(MINI_BUTTON_WEI_XIN_MINE).click()
        time.sleep(1)
        # 点击设置
        self.wait_presence_element(MINI_BUTTON_WEI_XIN_MINE_SET).click()
        time.sleep(2)
        # 点击切换账号
        self.wait_presence_element(MINI_BUTTON_WEI_XIN_MINE_SET_SWITCH).click()
        # 团员微信
     #   TouchAction(mp_driver).tap(x=720, y=934).perform()
       # 团长微信
       # TouchAction(mp_driver).tap(x=363, y=934).perform()
        # 进入小程序
    """直接点击聊天页面的链接"""
    def mini_op_wei_xin_go_link(self):
        # 点击十荟团
        time.sleep(2)
        self.wait_presence_element(MINI_ELEMENT_WEI_XIN_MINE_CHAT_PAGE_SHI_HUI_GROUP).click()
        time.sleep(2)

    """点击sht@2"""
    def mini_op_mine_name_sht2(self):
        # sht@2进入小程序
        self.wait_presence_element(MINI_ELEMENT_WEI_XIN_MINE_NAME_SHT).click()
        time.sleep(2)

    """点击张珊珊"""
    def mini_op_mine_name_z(self):
        # 张珊珊进入小程序
        self.wait_presence_element(MINI_ELEMENT_WEI_XIN_MINE_NAME_Z).click()
        time.sleep(2)

    """点击星星"""
    def mini_op_mine_name_star(self):
        # 副团长星星进入小程序
        self.wait_presence_element(MINI_ELEMENT_WEI_XIN_MINE_NAME_STAR).click()

        time.sleep(2)

    """通过刘亭亭链接进入小程序首页"""
    def mini_op_mine_name_liu_ting_ting(self):
        # 点击刘亭亭
        self.wait_presence_element(MINI_ELEMENT_WEI_XIN_MINE_NAME_LIU_TING_TING).click()
        time.sleep(2)

