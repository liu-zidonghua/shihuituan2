# coding=utf-8
import time

from appium.webdriver.common.touch_action import TouchAction

from elements.mini_program_elements import *

from action.base_page import BasePage

"""我的团购"""


class MiniMyGroupBuy(BasePage):
    """历史开团"""

    def mini_op_mine_group_buy_historical_opening(self):
        # 点击历史开团
        self.wait_presence_element(MINI_BUTTON_MINE_HISTORICAL_OPENING).click()

    """配送跟踪"""

    def mini_op_mine_group_buy_distribution_tracking(self):
        # 点击配送跟踪
        self.wait_presence_element(MINI_BUTTON_MINE_DISTRIBUTION_TRACKING).click()

    """签收码"""

    def mini_op_mine_group_buy_sign_code(self):
        # 点击签收码
        self.wait_presence_element(MINI_BUTTON_MINE_SIGN_CODE).click()

    """到货提醒"""

    def mini_op_mine_group_buy_arrival_reminder(self):
        # 点击到货提醒
        self.wait_presence_element(MINI_BUTTON_MINE_ARRIVAL_REMINDER).click()



    '''送货上门'''

    def mini_op_mine_order_picked_up_home_delivery_service(self):
        #　点击我的
        self.wait_presence_element(MINI_BUTTON_MINE).click()
        # 点击送货上门
        self.wait_presence_element(MINI_BUTTON_MINE_HOME_DELIVERY_SERVICE).click()

    '''输入运费'''

    def mini_op_mine_order_picked_up_freight_input(self):
        # 点击请输入运费框
        self.wait_presence_element(MINI_INPUT_MINE_SERVICE_EDIT_TEXT).click()
        # 输入运费价格
        self.wait_presence_element(MINI_INPUT_MINE_SERVICE_EDIT_TEXT).send_keys("1")

    '''保存运费价格'''

    def mini_op_mine_order_picked_up_freight_save(self):
        # 点击保存
        self.wait_presence_element(MINI_BUTTON_MINE_SERVICE_SAVE).click()

    '''送货预告'''

    def mini_op_mine_group_buy_delivery_notice(self):
        # 点击送货预告
        self.wait_presence_element(MINI_BUTTON_MINE_DELIVERY_NOTICE).click()

    '''佣金记录'''

    def mini_op_mine_group_buy_commission_record(self):
        # 点击佣金记录
        self.wait_presence_element(MINI_BUTTON_MINE_COMMISSION_RECORD).click()
