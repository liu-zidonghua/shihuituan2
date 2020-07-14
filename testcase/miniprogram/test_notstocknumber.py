# coding=utf-8

import sys
import time

import pytest

from action.miniprogram.check_mini_program_home_and_class import MiniCheckGroupBuy
from action.miniprogram.mini_program_confirm_order import MiniConfirmOrder

from action.miniprogram.mini_program_get_into_shihuituan import MiniDifferentName
from action.miniprogram.mini_program_login import Login
from action.miniprogram.mini_program_my_order import MiniMineOrder

sys.path.append('F:\\shihuituan\\miniProgram')
import allure



class TestMiniNoStockNumber():
    @pytest.mark.MiniLeaguenember
    @allure.step("库存为1的下单后验证")
    def test_mini_not_stock_number(self):
        with allure.step('1：小程序初始化'):
            mp_driver = Login().go_in()
        with allure.step('2：冀思雨小程序链接进入首页'):
            MiniDifferentName(mp_driver).mini_op_name_link_ji_si_yu()
        with allure.step('3：库存不足商品下单'):
            MiniConfirmOrder(mp_driver).mini_op_not_stock_confirm_order(mp_driver)
        with allure.step('4：输入支付密码'):
            MiniConfirmOrder(mp_driver).mini_op_payment_password(mp_driver)
        with allure.step('5：进入确认订单页'):
            MiniMineOrder(mp_driver).mini_op_my_order_pay_go_order_details()
        with allure.step('6：退出小程序再进入'):
            time.sleep(180)
            MiniDifferentName(mp_driver).mini_op_wei_xin_go_link(mp_driver)
        with allure.step('7：断言'):
            specification_big_one = MiniCheckGroupBuy(mp_driver).mini_check_specification_big_one()
            print(specification_big_one)
            assert "单规格大于1" in specification_big_one
        with allure.step('8：取消订单'):
            MiniMineOrder(mp_driver).mini_op_my_order_home_jump_order_cancel()


if __name__ == '__main__':
    pytest.main(['test_notstocknumber.py'])
    pytest.main(['-m=LeagueMember', '--html=report.html'])
