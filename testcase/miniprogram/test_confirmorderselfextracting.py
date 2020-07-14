# coding=utf-8

import sys

import pytest

from action.miniprogram.check_mini_program_confirm_order import CheckMiniConfirmOrder
from action.miniprogram.mini_program_confirm_order import MiniConfirmOrder
from action.miniprogram.mini_program_get_into_shihuituan import MiniDifferentName
from action.miniprogram.mini_program_login import Login
from action.miniprogram.mini_program_my_order import MiniMineOrder

sys.path.append('F:\\shihuituan\\miniProgram')

import allure

from action.base_page import *

import time


class TestMiniConfirmOrderSelfExtracting():
    @pytest.mark.Minileader
    @allure.step("送货上门确认订单页验证")
    def test_confirm_order_self_extracting(self):
        with allure.step('1：小程序初始化'):
            mp_driver = Login().go_in()
        with allure.step('2：进入团长首页'):
            MiniDifferentName(mp_driver).mini_op_name_link_z()
        with allure.step('3：进入确认订单页'):
            MiniConfirmOrder(mp_driver).mini_op_big_one_confirm_order(mp_driver)
        with allure.step('4：断言进入确认订单页，且存在送货上门'):
            home_delivery_service = CheckMiniConfirmOrder(mp_driver).mini_check_home_delivery_service()
            print(home_delivery_service)
            assert "送货上门" in home_delivery_service
        with allure.step('5：点击送货上门'):
            MiniConfirmOrder(mp_driver).mini_op_home_delivery_service()
        with allure.step('6：断言切换成功'):
            home_delivery_scope = CheckMiniConfirmOrder(mp_driver).mini_check_home_delivery_scope()
            print(home_delivery_scope)
            assert "送货范围：珠穆朗玛峰" in home_delivery_scope
        with allure.step('7：点击自提'):
            MiniConfirmOrder(mp_driver).mini_op_self_extracting()
        with allure.step('8：断言切换成功'):
            package_deliver = CheckMiniConfirmOrder(mp_driver).mini_check_package_deliver()
            print(package_deliver)
            assert "自提点：珠穆朗玛峰" in package_deliver
        with allure.step('9：清除购买人信息'):
            MiniConfirmOrder(mp_driver).mini_op_confirm_buy_name_del()
        with allure.step('10：断言'):
            input_name = CheckMiniConfirmOrder(mp_driver).mini_check_input_name()
            print(input_name)
            assert "请填写姓名" in input_name
        with allure.step('11：清除手机号信息'):
            MiniConfirmOrder(mp_driver).mini_op_confirm_buy_phone_del(mp_driver)
        with allure.step('12：断言'):
            input_phone = CheckMiniConfirmOrder(mp_driver).mini_check_input_phone()
            print(input_phone)
            assert "请输入您的手机号" in input_phone
        with allure.step('13：输入购买人信息'):
            MiniConfirmOrder(mp_driver).mini_op_confirm_buy_name_send()
        with allure.step('14：断言'):
            buying_name = CheckMiniConfirmOrder(mp_driver).mini_check_buying_name()
            print(buying_name)
            assert "测试2" in buying_name
        with allure.step('15：使用微信手机号'):
            MiniConfirmOrder(mp_driver).mini_op_confirm_phone_frame()
        with allure.step('16：断言'):
            wei_xin_phone = CheckMiniConfirmOrder(mp_driver).mini_check_wei_xin_phone()
            print(wei_xin_phone)
            assert "13264298003" in wei_xin_phone
        with allure.step('17：查看多个自提地址'):
            MiniConfirmOrder(mp_driver).mini_op_self_extracting_location()
        with allure.step('18：断言'):
            select_location = CheckMiniConfirmOrder(mp_driver).mini_check_select_location()
            print(select_location)
            assert "选择地址" in select_location
        with allure.step('19：点击取消'):
            MiniMineOrder(mp_driver).mini_op_my_order_cancelled()
        with allure.step('20：查看使用优惠券的总计价格'):
            total_money = CheckMiniConfirmOrder(mp_driver).mini_check_confirm_order_coupon()
            print(total_money)
        with allure.step('21：查看不使用优惠券显示'):
            MiniConfirmOrder(mp_driver).mini_op_confirm_not_coupon()
        with allure.step('22：断言'):
            coupon_number = CheckMiniConfirmOrder(mp_driver).mini_check_coupon_number()
            print(coupon_number)
            assert "张可用" in coupon_number
        with allure.step('23：查看备注信息'):
            confirm_order_notes = CheckMiniConfirmOrder(mp_driver).mini_check_confirm_order_notes()
            print(confirm_order_notes)
            assert "备注特殊要求或给团长留言" in confirm_order_notes
        with allure.step('24：填写备注信息'):
            MiniConfirmOrder(mp_driver).mini_op_confirm_place_remark_input()
        with allure.step('25：断言'):
            input_remarks = CheckMiniConfirmOrder(mp_driver).mini_check_confirm_order_input_remarks()
            print(input_remarks)
            assert "货到电联" in input_remarks
        with allure.step('26：点击确认支付'):
            MiniConfirmOrder(mp_driver).mini_op_confirm_place_payment()
        with allure.step('27：断言'):
            input_password = CheckMiniConfirmOrder(mp_driver).mini_check_confirm_order_input_password()
            print(input_password)
            assert "请输入支付密码" in input_password


if __name__ == '__main__':
    pytest.main(['test_confirmorderselfextracting.py'])
  #  pytest.main(['-m=Minileader', '--html=report.html'])