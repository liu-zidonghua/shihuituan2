# coding=utf-8


import time

from elements.mini_program_elements import *
from action.base_page import BasePage

"""售后订单类"""


class MiniAftersSalesOrder(BasePage):
    '''售后反馈'''

    def mini_op_mine_order_picked_up_after_sales_feedback(self):
        # 点击售后反馈
        self.wait_presence_element(MINI_ELEMENT_MINE_AFTER_SALES_FEEDBACK).click()

    """订单详情跳转售后工单"""

    def mini_op_afters_sales_order(self):
        # 申请售后
        self.wait_presence_element(MINI_BUTTON_MINE_CUSTOMER_SERVICE_AFTER_APPLICATION).click()

    '''售后工单添加视频'''

    def mini_op_afters_sales_order_add_video(self):
        # 点击添加视频
        self.wait_presence_element(MINI_BUTTON_MINE_CUSTOMER_SERVICE_ADD_VIDEO).click()
        # 从相册选择
        self.wait_presence_element(MINI_BUTTON_MINE_CUSTOMER_SERVICE_CHOICE_PHOTO).click()
        # 选择视频
        self.wait_presence_element(MINI_BUTTON_MINE_CUSTOMER_SERVICE_ADD_ONE_VIDEO).click()
        # 点击完成
        self.wait_presence_element(MINI_BUTTON_MINE_CUSTOMER_SERVICE_VIDEO_FINISH).click()
        time.sleep(30)

    '''售后工单添加照片'''

    def mini_op_afters_sales_order_add_photo(self):
        # 点击添加照片
        self.wait_presence_element(MINI_BUTTON_MINE_CUSTOMER_SERVICE_ADD_PHOTO).click()
        # 从相册选择
        self.wait_presence_element(MINI_BUTTON_MINE_CUSTOMER_SERVICE_CHOICE_PHOTO).click()
        # 选择照片
        self.wait_presence_element(MINI_BUTTON_MINE_CUSTOMER_SERVICE_ADD_PHOTO_ONE).click()
        # 点击完成
        self.wait_presence_element(MINI_BUTTON_MINE_CUSTOMER_SERVICE_PHOTO_FINISH).click()
        time.sleep(5)

    '''提交售后工单'''

    def mini_op_order_submission_work_order(self):
        # 　点击问题描述输入框
        self.wait_presence_element(MINI_INPUT_MINE_CUSTOMER_SERVICE_PROBLEM_DESCRIPTION).click()
        # 　完善问题描述
        self.wait_presence_element(MINI_INPUT_MINE_CUSTOMER_SERVICE_PROBLEM_DESCRIPTION).send_keys("11")
        # 提交售后工单
        self.wait_presence_element(MINI_BUTTON_MINE_CUSTOMER_SERVICE_SUBMIT_TO).click()
        # 返回列表
        self.wait_presence_element(MINI_BUTTON_MINE_CUSTOMER_SERVICE_RETURN_LIST).click()
        # 点击未处理
        self.wait_presence_element(MINI_INPUT_MINE_CUSTOMER_SERVICE_UNTREATED_ORDER).click()

    '''撤销售后工单'''

    def mini_op_order_cancel_work_order(self):
        # 点击撤销申请
        time.sleep(30)
        self.wait_presence_element(MINI_BUTTON_MINE_CUSTOMER_SERVICE_APPLICATION_ORDER).click()
        # 确定
        self.wait_presence_element(MINI_BUTTON_MINE_CUSTOMER_SERVICE_ORDER_SURE).click()

    '''申请售后工单流程'''

    def mini_op_order_apply_for_work_order(self):
        # 申请售后
        self.wait_presence_element(MINI_BUTTON_MINE_CUSTOMER_SERVICE_AFTER_APPLICATION).click()
        # 点击添加照片
        self.wait_presence_element(MINI_BUTTON_MINE_CUSTOMER_SERVICE_ADD_VIDEO).click()
        time.sleep(2)
        # 从相册选择
        self.wait_presence_element(MINI_BUTTON_MINE_CUSTOMER_SERVICE_CHOICE_PHOTO).click()
        # 选择照片
        self.wait_presence_element(MINI_BUTTON_MINE_CUSTOMER_SERVICE_ADD_ONE_VIDEO).click()
        # 点击完成
        self.wait_presence_element(MINI_BUTTON_MINE_CUSTOMER_SERVICE_PHOTO_FINISH).click()
        time.sleep(20)
        # 　点击问题描述输入框
        self.wait_presence_element(MINI_INPUT_MINE_CUSTOMER_SERVICE_PROBLEM_DESCRIPTION).click()
        # 　完善问题描述
        self.wait_presence_element(MINI_INPUT_MINE_CUSTOMER_SERVICE_PROBLEM_DESCRIPTION).send_keys("11")
        # 点击完成
        self.wait_presence_element(MINI_BUTTON_MINE_CUSTOMER_SERVICE_PROBLEM_FINISH).click()

        # 提交售后工单
        self.wait_presence_element(MINI_BUTTON_MINE_CUSTOMER_SERVICE_SUBMIT_TO).click()
        time.sleep(15)
        # 返回列表
        self.wait_presence_element(MINI_BUTTON_MINE_CUSTOMER_SERVICE_RETURN_LIST).click()
        # 点击未处理
        self.wait_presence_element(MINI_INPUT_MINE_CUSTOMER_SERVICE_UNTREATED_ORDER).click()
