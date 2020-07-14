# coding=utf-8

import sys
import pytest

from action.miniprogram.check_mini_program_shopping_cart import MiniCheckShoppingCart
from action.miniprogram.mini_program_get_into_shihuituan import MiniDifferentName
from action.miniprogram.mini_program_home_and_class import MiniGroupBuy
from action.miniprogram.mini_program_login import Login
from action.miniprogram.mini_program_shopping_cart import MiniShoppingCart

sys.path.append('F:\\shihuituan\\miniProgram')
import allure


class TestKingGoodsAddCart():
    @pytest.mark.MiniLeaguenember
    @allure.step("验证热卖列表商品添加购物车")
    def test_king_goods_add_cart(self):
        with allure.step('1：小程序初始化'):
            mp_driver = Login().go_in()
        with allure.step('2：通过张珊珊小程序链接进入首页'):
            MiniDifferentName(mp_driver).mini_op_name_link_z()
        with allure.step('3：删除购物车商品'):
            MiniShoppingCart(mp_driver).mini_op_cart_del_goods(mp_driver)
        with allure.step('4：金刚分类单规格商品加购物车'):
            MiniGroupBuy(mp_driver).mini_op_home_king_single_specification(mp_driver)
        with allure.step('第4步：断言'):
            goods_number_one = MiniCheckShoppingCart(mp_driver).mini_check_cart_add_one()
            print(goods_number_one)
            assert ("1" in goods_number_one)
        with allure.step('第5步：多规格商品加购物车'):
            MiniGroupBuy(mp_driver).mini_op_home_king_multiple_specifications(mp_driver)
        with allure.step('第6步：断言'):
            goods_number_two = MiniCheckShoppingCart(mp_driver).mini_check_cart_add_two()
            print(goods_number_two)
            assert ("2" in goods_number_two)



if __name__ == '__main__':
    pytest.main(['test_kinggoodsaddcart.py'])
    pytest.main(['-m=LeagueMember', '--html=report.html'])




