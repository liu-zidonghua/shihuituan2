# coding=utf-8
from elements.mini_program_elements import *

from action.base_page import BasePage

"""我的团购-扫码提货"""


class MiniCheckScanPickGoods(BasePage):
    """检查进入取货单页面"""

    def mini_check_scan_pick_up_goods_order(self):
        # 检查进入取货单页面
        pick_up_goods_order = self.wait_presence_element(MINI_BUTTON_MINE_PICK_UP_GOODS_ORDER).get_attribute(
            'name')
        return pick_up_goods_order

    """检查进入取货单页面"""

    def mini_check_scan_pick_up_goods_order_prompt(self):
        # 检查取货单页面提示
        pick_up_goods_order_prompt = self.wait_presence_element(
            MINI_BUTTON_MINE_PICK_UP_GOODS_ORDER_PROMPT).get_attribute(
            'name')
        return pick_up_goods_order_prompt

    """检查存在扫码提货"""

    def mini_check_scan_pick_up_goods(self):
        # 检查扫码提货
        scan_pick_up_goods = self.wait_presence_element(MINI_BUTTON_MINE_PICK_UP_BY_SCANNING_CODE).get_attribute(
            'name')
        return scan_pick_up_goods

    """检查存在扫一扫"""

    def mini_check_scan_text(self):
        # 检查存在扫一扫
        scan_text = self.wait_presence_element(MINI_BUTTON_MINE_SCANNING_SCAN).get_attribute('name')
        return scan_text

    """检查存在手机微信昵称查询"""

    def mini_check_search_phone(self):
        # 检查存在手机微信昵称查询
        search_phone = self.wait_presence_element(MINI_BUTTON_MINE_SCANNING_PHONE_WEI_XIN_SEARCH).get_attribute('name')
        return search_phone


    """检查存在未搜索到用户"""

    def mini_check_search_not_user(self):
        # 检查存在手机微信昵称查询
        search_not_user = self.wait_presence_element(MINI_INPUT_MINE_SCANNING_SEARCH_NOT_USER).get_attribute('name')
        return search_not_user


    """检查存在请输入手机微信昵称查询"""

    def mini_check_input_phone_search(self):
        # 检查存在手机微信昵称查询
        input_phone_search = self.wait_presence_element(MINI_INPUT_MINE_SCANNING_SEARCH_EDIT_TEXT).get_attribute('name')
        return input_phone_search


    """检查存在用户-张珊珊"""

    def mini_check_user_z(self):
        # 检查存在用户-张姗姗
        user_z = self.wait_presence_element(MINI_ELEMENT_WEI_XIN_MINE_NAME_Z).get_attribute('name')
        return user_z