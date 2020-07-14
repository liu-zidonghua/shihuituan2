# coding=utf-8
import time

from elements.mini_program_elements import *

from action.base_page import BasePage

"""我的团购"""


class MiniCheckMyGroupBuy(BasePage):




    """检查存在用户-张珊珊"""

    def mini_check_user_z(self):
        time.sleep(2)
        # 检查存在用户-张姗姗
        user_z = self.wait_presence_element(MINI_ELEMENT_WEI_XIN_MINE_NAME_Z).get_attribute('name')
        return user_z



    """未取货提示"""

    def mini_check_not_pick_up_order_prompt(self):
        time.sleep(2)
        # 未取货提示
        not_pick_up_order_prompt = self.wait_presence_element(MINI_ELEMENT_WEI_XIN_MINE_NAME_Z).get_attribute('name')
        return not_pick_up_order_prompt