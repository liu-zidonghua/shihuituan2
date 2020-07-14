# coding=utf-8
import time

from appium.webdriver.common.touch_action import TouchAction

from elements.mini_program_elements import *

from action.base_page import BasePage

"""我的团购"""


class CheckMiniHomeDeliveryService(BasePage):

    """检查存在送货上门设置"""

    def mini_check_mine_provide_home_delivery_service(self):
        time.sleep(2)
        # 检查送货上门设置
        provide_home_delivery_service = self.wait_presence_element(
            MINI_ELEMENT_MINE_SERVICE_SELF_MENTION_SETTINGS).get_attribute('name')
        return provide_home_delivery_service


    """检查存在运费"""

    def mini_check_mine_provide_home_delivery_service_freight(self):
        time.sleep(2)
        # 检查运费
        provide_home_delivery_service_freight = self.wait_presence_element(
            MINE_ELEMENT_MINE_SERVICE_FREIGHT).get_attribute('name')
        return provide_home_delivery_service_freight
    """检查存在运费"""

    def mini_check_mine_provide_home_delivery_service_freight_money(self):
        time.sleep(2)
        # 检查运费金额
        provide_home_delivery_service_freight_money = self.wait_presence_element(
            MINE_ELEMENT_MINE_SERVICE_FREIGHT).get_attribute('name')
        return provide_home_delivery_service_freight_money