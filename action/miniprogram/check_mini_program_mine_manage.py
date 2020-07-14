#  coding=utf-8
import time

from appium.webdriver.common.touch_action import TouchAction

from action.miniprogram.mini_program_login import Login
from elements.mini_program_elements import *

from action.base_page import BasePage

"""我的页面-管理"""
class MiniMineManage(BasePage):

    """副团长管理"""
    def mini_op_mine_manage_deputy_head_management(self,mp_driver):
        # 点击我的
        self.wait_presence_element(MINI_BUTTON_MINE).click()
        time.sleep(2)
        # 上滑页面
        Login().swipe_up(mp_driver)
        time.sleep(2)
        # 点击副团长管理
        self.wait_presence_element(MINI_ELEMENT_MINE_MANAGE_DEPUTY_HEAD_MANAGEMENT).click()

    """团员管理"""
    def mini_op_mine_manage_league_member_management(self):
        # 点击团员管理
        self.wait_presence_element(MINI_ELEMENT_MINE_MANAGE_LEAGUE_MEMBER_MANAGEMENT).click()

    """删除副团长"""
    def mini_op_mine_deputy_head_management_del(self,mp_driver):
        # 点击删除按钮
        TouchAction(mp_driver).tap(x=1039, y=763).perform()
        # 点击确认
        self.wait_presence_element(MINI_BUTTON_MINE_ORDER_DETAILS_ORDER_TRUE).click()

    """点击添加副团长按钮"""
    def mini_op_mine_deputy_head_add(self):
        # 点击添加副团长按钮
        self.wait_presence_element(MINI_BUTTON_MINE_MANAGE_DEPUTY_HEAD_USER_ADD).click()

    """点击添加按钮"""
    def mini_op_mine_deputy_head_user_add(self):
        # 点击添加按钮
        self.wait_presence_element(MINI_INPUT_MINE_MANAGE_DEPUTY_HEAD_ADD).click()

    """添加团员冀思雨"""
    def mini_op_mine_deputy_head_user_add_ji_si_yu(self):
        #请输入用户id输入框
        self.wait_presence_element(MINI_INPUT_MINE_MANAGE_DEPUTY_HEAD_USER_ID).click()
        # 输入冀思雨团员id
        self.wait_presence_element(MINI_INPUT_MINE_MANAGE_DEPUTY_HEAD_USER_ID).send_keys("84182263")
        # 点击添加
        self.wait_presence_element(MINI_INPUT_MINE_MANAGE_DEPUTY_HEAD_ADD).click()
        # 点击确认
        self.wait_presence_element(MINI_BUTTON_MINE_ORDER_DETAILS_ORDER_TRUE).click()

    """添加团员刘亭亭"""
    def mini_op_mine_deputy_head_user_add_liu_ting_ting(self):
        # 点击冀思雨ｉｄ
        self.wait_presence_element(MINI_INPUT_MINE_MANAGE_DEPUTY_HEAD_ADD_LEAGUE_MEMBER_ID).click()
        #　清除输入框内容冀思雨id
        self.wait_presence_element(MINI_INPUT_MINE_MANAGE_DEPUTY_HEAD_ADD_LEAGUE_MEMBER_ID).clear()
        # 输入刘亭亭团员id
        self.wait_presence_element(MINI_INPUT_MINE_MANAGE_DEPUTY_HEAD_USER_ID).send_keys("83669359")
        # 点击添加按钮
        self.wait_presence_element(MINI_INPUT_MINE_MANAGE_DEPUTY_HEAD_ADD).click()
        # 点击确认按钮
        self.wait_presence_element(MINI_BUTTON_MINE_ORDER_DETAILS_ORDER_TRUE).click()

    """删除添加的副团长"""
    def mini_op_mine_del_deputy_head(self,mp_driver):
        try:
            for i in range(4):
                if mp_driver.find_element_by_android_uiautomator(
                        'new UiSelector().text("冀思雨")'):
                    TouchAction(mp_driver).tap(x=1039, y=763).perform()
                    self.wait_presence_element(MINI_BUTTON_MINE_ORDER_DETAILS_ORDER_TRUE).click()
                    continue
                elif mp_driver.find_element_by_android_uiautomator(
                        'new UiSelector().text("还未添加副团长")'):
                    continue
                break
        except:
            print("异常")