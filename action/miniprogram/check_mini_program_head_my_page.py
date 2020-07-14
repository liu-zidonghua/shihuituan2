# coding=utf-8


import time

from elements.mini_program_elements import *
from action.base_page import BasePage

class MiniMyPage(BasePage):

    """业绩中心"""
#class MyPerformance(BasePage):


    """进入我的业绩页面"""
    def see_all_performance(self):

        # 进入我的业绩页面
        time.sleep(4)
        self.wait_presence_element(MINI_BUTTON_MINE_PERFORMANCE_SEE_ALL).click()

    """月账单"""
    def monthly_performance(self):
        # 点击月账单
        self.wait_presence_element(MINI_ELEMENT_MINE_PERFORMANCE_MONTHLY_BILL).click()

    """团账单"""
    def group_performance(self):
        # 点击团账单
        self.wait_presence_element(MINI_ELEMENT_MINE_PERFORMANCE_REGIMENT_BILL).click()



#"""营销工具"""
#class MyMarketingTools(BasePage):

    """开团海报"""
    def mini_op_mine_marketing_tool_opening_poster(self):
        # 点击开团海报
        self.wait_presence_element(MINI_BUTTON_MINE_MARKETING_TOOL_OPENING_POSTER).click()

    """保存海报"""
    def mini_op_mine_marketing_tool_save_poster(self):
        time.sleep(8)
        # 保存开团海报
        self.wait_presence_element(MINI_BUTTON_MINE_MARKETING_TOOL_OPENING_POSTER_SAVE).click()

    """副团长不存在的功能"""
    def mini_op_mine_deputy_head_not_function(self,mp_driver):
        time.sleep(3)
        try:
            for i in range(3):
                if mp_driver.find_element_by_android_uiautomator(
                        'new UiSelector().text("业绩中心")'):
                    print("业绩中心")
                    continue
                if mp_driver.find_element_by_android_uiautomator(
                        'new UiSelector().text("累计收益")'):
                    print("累计收益")
                    continue
                if mp_driver.find_element_by_android_uiautomator(
                        'new UiSelector().text("账户余额")'):
                    print("账户余额")
                    continue
                if mp_driver.find_element_by_android_uiautomator(
                        'new UiSelector().text("历史开团")'):
                    print("历史开团")
                    continue

                break
        except:
            print("无上述功能功能")