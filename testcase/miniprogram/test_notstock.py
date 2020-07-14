# coding=utf-8
import sys

import pytest

from action.miniprogram.check_mini_program_goods_details import CheckMiniGoodsDetails

from action.miniprogram.mini_program_get_into_shihuituan import MiniDifferentName
from action.miniprogram.mini_program_goods_details import MiniGoodsDetails
from action.miniprogram.mini_program_login import Login

sys.path.append('F:\\shihuituan\\miniProgram')

import allure



class TestMiniNotStock():

    @pytest.mark.MiniLeaguenember
    @allure.step("库存不足商品验证购买数量")
    def test_mini_not_stock_add(self):
        with allure.step('1：小程序初始化'):
            mp_driver = Login().go_in()
        with allure.step('2：冀思雨小程序链接进入首页'):
            MiniDifferentName(mp_driver).mini_op_name_link_ji_si_yu()
        with allure.step('3：点击立即购买后添加数量'):
            MiniGoodsDetails(mp_driver).mini_op_goods_details_add_number_buy(mp_driver)
        with allure.step('4：断言'):
            buy_number_one = CheckMiniGoodsDetails(mp_driver).mini_check_buy_number_one()
            print(buy_number_one)
            assert "1" in buy_number_one

if __name__ == '__main__':
    pytest.main(['test_notstock.py'])
    pytest.main(['-m=LeagueMember', '--html=report.html'])