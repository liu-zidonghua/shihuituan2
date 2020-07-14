# coding=utf-8

import time

from appium.webdriver.common.touch_action import TouchAction

from elements.mini_program_elements import *

from action.base_page import BasePage

"""我的订单"""


class MiniMineOrder(BasePage):
    """我的订单"""

    def mini_op_my_order(self):
        # 点击我的订单
        time.sleep(1)
        self.wait_presence_element(MINI_BUTTON_MINE_ORDER).click()

    """待支付"""

    def mini_op_my_order_pay(self):
        # 点击待支付
        time.sleep(1)
        self.wait_presence_element(MINI_ELEMENT_MINE_ORDER_PAID).click()

    """待收货"""

    def mini_op_my_order_received(self):
        # 点击待收货
        time.sleep(1)
        self.wait_presence_element(MINI_ELEMENT_MINE_ORDER_RECEIVED).click()

    """已完成"""

    def mini_op_my_order_finish(self):
        # 点击已完成
        time.sleep(1)
        self.wait_presence_element(MINI_ELEMENT_MINE_ORDER_FINISH).click()

    """已取消"""

    def mini_op_my_order_cancel(self):
        # 点击已取消
        time.sleep(1)
        self.wait_presence_element(MINI_ELEMENT_MINE_ORDER_CELL).click()

    """全部"""

    def mini_op_my_order_all(self):
        # 点击全部
        self.wait_presence_element(MINI_ELEMENT_MINE_ORDER_ALL).click()

    """我的二维码"""

    def mini_op_my_order_two_code(self):
        # 点击我的二维码
        self.wait_presence_element(MINI_ELEMENT_MINE_ORDER_QR_CODE).click()

    """进入我的二维码页面"""

    def mini_op_my_order_jump_two_code(self):
        # 点击我的订单
        self.wait_presence_element(MINI_BUTTON_MINE_ORDER).click()
        # 点击我的二维码
        self.wait_presence_element(MINI_ELEMENT_MINE_ORDER_QR_CODE).click()


    """订单状态跳转"""

    def mini_op_my_order_state_jump(self):
        # 点击待支付
        self.wait_presence_element(MINI_ELEMENT_MINE_ORDER_PAID).click()
        # 返回上一页
        self.wait_presence_element(MINI_ELEMENT_MINE_PERFORMANCE_GO_BACK).click()
        # 点击待收货
        self.wait_presence_element(MINI_ELEMENT_MINE_ORDER_RECEIVED).click()
        # 返回上一页
        self.wait_presence_element(MINI_ELEMENT_MINE_PERFORMANCE_GO_BACK).click()
        # 点击已完成
        self.wait_presence_element(MINI_ELEMENT_MINE_ORDER_FINISH).click()
        # 返回上一页
        self.wait_presence_element(MINI_ELEMENT_MINE_PERFORMANCE_GO_BACK).click()
        # 点击已取消
        self.wait_presence_element(MINI_ELEMENT_MINE_ORDER_CELL).click()
        # 返回上一页
        self.wait_presence_element(MINI_ELEMENT_MINE_PERFORMANCE_GO_BACK).click()

    """订单详情页"""

    def mini_op_my_order_details(self):
        # 进入订单详情页
        self.wait_presence_element(MINI_BUTTON_MINE_ORDER_SELF_MENTIONS).click()

    """取消订单"""

    def mini_op_my_order_order_cancel(self):
        # 点击取消订单
        self.wait_presence_element(MINI_BUTTON_MINE_ORDER_DETAILS_ORDER_CANCEL).click()

    """取消"""

    def mini_op_my_order_cancelled(self):
        # 取消
        self.wait_presence_element(MINI_BUTTON_MINE_ORDER_DETAILS_ORDERS_CANCEL).click()

    """确定"""

    def mini_op_my_order_sure(self):
        # 确定
        self.wait_presence_element(MINI_BUTTON_MINE_ORDER_DETAILS_ORDER_SURE_SPACE).click()

    """购物车下单后从我的订单跳转我的页面"""

    def mini_op_my_order_order_jump_mine(self):
        # 返回
        self.wait_presence_element(MINI_ELEMENT_MINE_PERFORMANCE_GO_BACK).click()
        time.sleep(2)
        # 点击我的按钮
        self.wait_presence_element(MINI_BUTTON_MINE).click()

    """取消订单后再次跳转我的页面"""

    def mini_op_my_order_cancel_order_jump_mine(self):
        # 取消订单
        self.wait_presence_element(MINI_BUTTON_MINE_ORDER_DETAILS_ORDER_CANCEL).click()
        time.sleep(2)
        # 确定
        self.wait_presence_element(MINI_BUTTON_MINE_ORDER_DETAILS_ORDER_SURE_SPACE).click()
        # 返回
        self.wait_presence_element(MINI_ELEMENT_MINE_PERFORMANCE_GO_BACK).click()
        # 返回
        time.sleep(2)
        self.wait_presence_element(MINI_ELEMENT_MINE_PERFORMANCE_GO_BACK).click()

    """首页跳转订单详情取消订单"""

    def mini_op_my_order_home_jump_order_cancel(self):
        # 点击我的
        self.wait_presence_element(MINI_BUTTON_MINE).click()
        time.sleep(2)
        # 点击待收货
        self.wait_presence_element(MINI_ELEMENT_MINE_ORDER_RECEIVED).click()
        time.sleep(4)
        # 进入订单详情
        self.wait_presence_element(MINI_BUTTON_MINE_ORDER_SELF_MENTIONS).click()
        time.sleep(2)
        # 点击取消订单
        self.wait_presence_element(MINI_BUTTON_MINE_ORDER_DETAILS_ORDER_CANCEL).click()
        # 确定
        self.wait_presence_element(MINI_BUTTON_MINE_ORDER_DETAILS_ORDER_SURE_SPACE).click()

    """我的跳转订单详情"""

    def mini_op_my_order_mine_jump_order(self):
        # 点击我的
        self.wait_presence_element(MINI_BUTTON_MINE).click()
        time.sleep(2)
        # 点击待收货
        self.wait_presence_element(MINI_ELEMENT_MINE_ORDER_RECEIVED).click()
        # 进入订单详情
        self.wait_presence_element(MINI_BUTTON_MINE_ORDER_SELF_MENTIONS).click()

    '''支付后进入订单详情'''

    def mini_op_my_order_pay_go_order_details(self):
        # 点击完成
        self.wait_presence_element(MINI_BUTTON_MINE_ARRIVAL_ACCOMPLISH).click()
        time.sleep(2)
        # 查看订单
        self.wait_presence_element(MINI_BUTTON_MINE_VIEW_ORDERS).click()
        # 点击自提
        self.wait_presence_element(MINI_ELEMENT_MINE_SERVICE_SELF_MENTION).click()


    """副团长我的订单各个状态互相跳转"""
    def mini_op_mine_order_deputy_head_state_jump(self,mp_driver):
        #　点击待支付
        self.wait_presence_element(MINI_ELEMENT_MINE_ORDER_PAID).click()
        # 　返回
        TouchAction(mp_driver).tap(x=76, y=141).perform()
        # 　点击待收货
        self.wait_presence_element(MINI_ELEMENT_MINE_ORDER_RECEIVED).click()
        # 　返回
        TouchAction(mp_driver).tap(x=76, y=141).perform()
        # 　点击已完成
        self.wait_presence_element(MINI_ELEMENT_MINE_ORDER_FINISH).click()
        # 　返回
        TouchAction(mp_driver).tap(x=76, y=141).perform()
        # 　点已取消
        self.wait_presence_element(MINI_ELEMENT_MINE_ORDER_CELL).click()
        # 　返回
        TouchAction(mp_driver).tap(x=76, y=141).perform()