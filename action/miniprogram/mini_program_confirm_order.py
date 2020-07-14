# coding=utf-8


import time

from appium.webdriver.common.touch_action import TouchAction

from elements.mini_program_elements import *
from action.base_page import BasePage


class CheckMiniConfirmOrder(BasePage):
    """确认订单类"""

    """验证存在送货上门"""

    def mini_check_home_delivery_service(self):
        time.sleep(3)
        # 验证存在送货上门
        home_delivery_service = self.wait_presence_element(MINI_ELEMENT_MINE_SERVICE_HOME_DELIVERY_SERVICE).get_attribute(
            'name')
        return home_delivery_service
