# coding=utf-8

import sys

sys.path.append('F:\\shihuituan\\testcase\\miniprogram')
from action.miniprogram.check_mini_program_shopping_cart import *
import pytest
from action.miniprogram.mini_program_get_into_shihuituan import *
from action.miniprogram.mini_program_home_and_class import *
from action.miniprogram.mini_program_shopping_cart import *
import time
import allure
from action.miniprogram.check_mini_program_home_and_class import *


class TestMiniAddShoppingCart():
    @pytest.mark.MiniLeaguenember
    @allure.step("首页商品加入购物车验证")
    def test_mini_home_goods_add_shopping_cart(self):
        with allure.step('1：小程序初始化'):
            mp_driver = Login().go_in()
        with allure.step('2：通过张珊珊小程序链接进入首页'):
            MiniDifferentName(mp_driver).mini_op_name_link_z()
        with allure.step('3：删除购物车商品'):
            MiniShoppingCart(mp_driver).mini_op_cart_del_goods(mp_driver)
        with allure.step('3：单规格商品首页加号加购物车'):
            MiniGroupBuy(mp_driver).mini_op_goods_single_specification_add_cart(mp_driver)
        with allure.step('4：断言'):
            goods_number_one = MiniCheckShoppingCart(mp_driver).mini_check_cart_add_one()
            print(goods_number_one)
            assert ("1" in goods_number_one)
        with allure.step('5：多规格商品加购物车'):
            MiniGroupBuy(mp_driver).mini_op_goods_selection_specification(mp_driver)
        with allure.step('6：断言：'):
            goods_number_two = MiniCheckShoppingCart(mp_driver).mini_check_cart_add_two()
            print(goods_number_two)
            assert ("2" in goods_number_two)



if __name__ == '__main__':
    pytest.main(['test_addshoppingchart.py'])
  #  pytest.main(['-m=LeagueMember', '--html=report.html'])
