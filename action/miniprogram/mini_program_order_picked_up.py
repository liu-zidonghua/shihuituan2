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



    '''进入待提货订单页面'''

    def mini_op_mine_group_buy_order_picked_up(self):
        # 点击我的
        self.wait_presence_element(MINI_BUTTON_MINE).click()
        # 点击待提货订单
        self.wait_presence_element(MINI_BUTTON_MINE_ORDER_TO_BE_PICKED_UP).click()

    '''已提走列表'''

    def order_picked_end(self):
        # 点击待提货订单
        self.wait_presence_element(MINI_BUTTON_MINE_ORDER_TO_BE_PICKED_UP).click()
        # 点击已提走
        self.wait_presence_element(MINI_BUTTON_MINE_ORDER_PICK_TAKEN_AWAY).click()

    '''手机号搜索待提货订单'''

    def order_phone_search(self,mp_driver):
        # 点击搜索输入框
        self.wait_presence_element(MINI_INPUT_MINE_ORDER_PICK_EDIT_TEXT).click()
        # 输入手机号
        self.wait_presence_element(MINI_INPUT_MINE_ORDER_PICK_EDIT_TEXT).send_keys("17330291054")
        # 点击搜索按钮
        TouchAction(mp_driver).tap(x=949, y=292).perform()

    '''手机号搜索待提货列表无订单订单'''

    def mini_op_mine_order_picked_up_phone_not_list(self,mp_driver):

        # 切换手机号搜索
        self.wait_presence_element(MINI_BUTTON_MINE_ORDER_PICK_PHONE_NUMBER).click()
        # 点击搜索输入框
        self.wait_presence_element(MINI_INPUT_MINE_ORDER_PICK_EDIT_TEXT).click()
        # 输入手机号
        self.wait_presence_element(MINI_INPUT_MINE_ORDER_PICK_EDIT_TEXT).send_keys("18501355438")

    '''姓名搜索待提货订单'''

    def mini_op_mine_order_picked_up_name_search(self,mp_driver):
        time.sleep(3)
        # 点击切换符号
        TouchAction(mp_driver).tap(x=174, y=292).perform()
        # 选择姓名搜索
        self.wait_presence_element(MINI_BUTTON_MINE_ORDER_PICK_NAME).click()
        # 点击搜索输入框
        self.wait_presence_element(MINI_INPUT_MINE_ORDER_PICK_EDIT_TEXT).click()
        # 输入姓名
        self.wait_presence_element(MINI_INPUT_MINE_ORDER_PICK_EDIT_TEXT).send_keys("测试2")
        #　点击搜索
        TouchAction(mp_driver).tap(x=934, y=292).perform()


    '''微信昵称搜索待提货订单'''

    def mini_op_mine_order_picked_up_wei_xin_search(self,mp_driver):
        time.sleep(5)
        # 切换 符号
        TouchAction(mp_driver).tap(x=154, y=317).perform()
        # 选择微信昵称搜索
        self.wait_presence_element(MINI_BUTTON_MINE_ORDER_PICK_WEI_XIN_NAME).click()
        # 点击搜索输入框
        self.wait_presence_element(MINI_INPUT_MINE_ORDER_PICK_EDIT_TEXT).click()
        # 输入微信昵称
        self.wait_presence_element(MINI_INPUT_MINE_ORDER_PICK_EDIT_TEXT).send_keys("jisiyu1008")
        # 点击搜索
        TouchAction(mp_driver).tap(x=944, y=292).perform()


    '''送货上门'''

    def mini_op_mine_order_picked_up_home_delivery_service(self):
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
