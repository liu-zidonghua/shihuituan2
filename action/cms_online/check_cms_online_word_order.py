# coding=utf-8
import time

from elements.cms_online_elements import *

from action.base_page import BasePage


class CmsOnlineOrderService(BasePage):
    """搜索并受理工单"""

    def cms_online_query_word_order_search(self):
        # 点击客服工单
        self.wait_presence_element(CMS_BUTTON_CUSTOMER_SERVICE_WORK).click()
        # 点击工单列表
        self.wait_presence_element(CMS_BUTTON_CUSTOMER_SERVICE_WORK_LIST).click()
        # 点击主站
        self.wait_presence_element(CMS_BUTTON_CUSTOMER_SERVICE_WORK_MASTER).click()
        # 取消默认显示
        self.wait_presence_element(CMS_BUTTON_CUSTOMER_SERVICE_WORK_REMOVE).click()

        # 选择的主站
        self.wait_presence_element(CMS_BUTTON_CUSTOMER_SERVICE_WORK_MASTER_THREE).click()
        #　点击搜索
        self.wait_presence_element(CMS_BUTTON_CUSTOMER_SERVICE_WORK_ACTION ).click()
        # 勾选工单
        self.wait_presence_element(CMS_BUTTON_CUSTOMER_SERVICE_WORK_CHECK).click()
        # 　点击受理工单
        self.wait_presence_element(CMS_BUTTON_CUSTOMER_SERVICE_WORK_BATCH_MANAGE).click()
        # 点击确定
        self.wait_presence_element(CMS_BUTTON_CUSTOMER_SERVICE_WORK_MANAGE_SURE).click()
        time.sleep(6)

    """搜索未处理工单"""

    def cms_online_query_word_order_untreated_search(self):
        # 点击客服工单
        self.wait_presence_element(CMS_BUTTON_CUSTOMER_SERVICE_WORK).click()
        # 点击工单列表
        self.wait_presence_element(CMS_BUTTON_CUSTOMER_SERVICE_WORK_LIST).click()
        # 点击主站
        self.wait_presence_element(CMS_BUTTON_CUSTOMER_SERVICE_WORK_MASTER).click()
        # 取消默认显示
        self.wait_presence_element(CMS_BUTTON_CUSTOMER_SERVICE_WORK_REMOVE).click()

        # 选择的主站
        self.wait_presence_element(CMS_BUTTON_CUSTOMER_SERVICE_WORK_MASTER_THREE).click()
        # 　点击搜索
        self.wait_presence_element(CMS_BUTTON_CUSTOMER_SERVICE_WORK_ACTION).click()
        # 勾选工单
        self.wait_presence_element(CMS_BUTTON_CUSTOMER_SERVICE_WORK_CHECK).click()
        # 　点击受理工单
        self.wait_presence_element(CMS_BUTTON_CUSTOMER_SERVICE_WORK_BATCH_MANAGE).click()
        # 点击确定
        self.wait_presence_element(CMS_BUTTON_CUSTOMER_SERVICE_WORK_MANAGE_SURE).click()
        time.sleep(6)

    """工单赔付"""
    def cms_online_op_word_order_paid(self):
        # 点击处理中
        self.wait_presence_element(CMS_BUTTON_CUSTOMER_SERVICE_WORK_HANDLE).click()
        # 点击处理
        self.wait_presence_element(CMS_BUTTON_CUSTOMER_SERVICE_WORK_HANDLES).click()
        # 打印所有句柄
        handles = list(self.driver.window_handles)
        print(handles)
        # 切换新页面句柄
        handle2 = handles[2]
        self.driver.switch_to.window(handle2)
        time.sleep(2)
        print( handle2)
        # 点击赔付
        self.wait_presence_element(CMS_BUTTON_CUSTOMER_SERVICE_WORK_PAID).click()
        time.sleep(4)

        # 打印所有句柄
        handles = list(self.driver.window_handles)
        print(handles)

        # 切换新页面句柄
        handle3 = handles[3]
        self.driver.switch_to.window(handle3)
        time.sleep(2)
        print( handle3)
        # 点击一级原因
        self.wait_presence_element(CMS_BUTTON_CUSTOMER_SERVICE_WORK_PAID_ONE_CAUSE).click()
        # 输入一级原因
        self.wait_presence_element(CMS_INPUT_CUSTOMER_SERVICE_WORK_PAID_ONE).send_keys("客户原因")
        #　点击客户原因
        self.wait_presence_element(CMS_BUTTON_CUSTOMER_SERVICE_WORK_PAID_ONE_USER).click()
        # 点击二级原因
        self.wait_presence_element(CMS_BUTTON_CUSTOMER_SERVICE_WORK_PAID_TWO_CAUSE).click()
        # 输入二级原因
        self.wait_presence_element(CMS_INPUT_CUSTOMER_SERVICE_WORK_PAID_TWO).send_keys("不想要")
        #　点击不想要
        self.wait_presence_element(CMS_BUTTON_CUSTOMER_SERVICE_WORK_PAID_TWO_USER).click()
        #　点击责任归属
        self.wait_presence_element(CMS_BUTTON_CUSTOMER_SERVICE_WORK_RESPONSIBILITY_ATTRIBUTION).click()
        # 点击金额输入框
        self.wait_presence_element(CMS_INPUT_CUSTOMER_SERVICE_WORK_MONEY_PAID).click()
        # 输入金额
        self.wait_presence_element(CMS_INPUT_CUSTOMER_SERVICE_WORK_MONEY_PAID).send_keys("0.01")
        # 点击原因输入框
        self.wait_presence_element(CMS_INPUT_CUSTOMER_SERVICE_WORK_PAID_CAUSE).click()
        # 输入原因
        self.wait_presence_element(CMS_INPUT_CUSTOMER_SERVICE_WORK_PAID_CAUSE).send_keys("其他")
        # 点击确定
        self.wait_presence_element(CMS_BUTTON_CUSTOMER_SERVICE_WORK_PAID_SURE).click()
        # 　点击二次确定
        self.wait_presence_element(CMS_BUTTON_CUSTOMER_SERVICE_WORK_PAID_SURE_TWO).click()
        # 三次确定
        self.wait_presence_element(CMS_BUTTON_OUT_STOCK_DELIVERY_STOCK_THREE).click()

    """关闭订单"""
    def cms_online_op_word_order_close(self):
        # 点击客服工单
        self.wait_presence_element(CMS_BUTTON_CUSTOMER_SERVICE_WORK).click()
        # 点击工单列表
        self.wait_presence_element(CMS_BUTTON_CUSTOMER_SERVICE_WORK_LIST).click()
        # 点击主站
        self.wait_presence_element(CMS_BUTTON_CUSTOMER_SERVICE_WORK_MASTER).click()
        # 取消默认显示
        self.wait_presence_element(CMS_BUTTON_CUSTOMER_SERVICE_WORK_REMOVE).click()

        # 选择的主站
        self.wait_presence_element(CMS_BUTTON_CUSTOMER_SERVICE_WORK_MASTER_THREE).click()
        #　点击搜索
        self.wait_presence_element(CMS_BUTTON_CUSTOMER_SERVICE_WORK_ACTION ).click()
        # 点击已完成
        self.wait_presence_element(CMS_BUTTON_CUSTOMER_SERVICE_WORK_OFF).click()
        # 第一个已解决工单
        self.wait_presence_element(CMS_BUTTON_CUSTOMER_SERVICE_WORK_OFF_ONE).click()
        # 打印所有句柄
        handles = list(self.driver.window_handles)
        print(handles)
        # 切换新页面句柄
        handle2 = handles[2]
        self.driver.switch_to.window(handle2)
        time.sleep(2)
        print( handle2)
        # 　点击关闭工单
        self.wait_presence_element(CMS_BUTTON_CUSTOMER_SERVICE_WORK_CLOSE).click()
