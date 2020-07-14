# coding=utf-8



import allure
import pytest
import time

from action.miniprogram.check_mini_program_confirm_order import CheckMiniConfirmOrder
from action.miniprogram.mini_program_confirm_order import MiniConfirmOrder
from action.miniprogram.mini_program_get_into_shihuituan import MiniDifferentName
from action.miniprogram.mini_program_login import Login
from action.miniprogram.mini_program_shopping_cart import MiniShoppingCart


class TestConfirmOrderGoodsNumber():
    @pytest.mark.Minileader
    @allure.step("验证确认订单页多个商品")
    def test_confirm_order_goods_number(self):
        with allure.step('1：小程序初始化'):
            mp_driver = Login().go_in()
        with allure.step('2：通过张珊珊小程序链接进入首页'):
            MiniDifferentName(mp_driver).mini_op_name_link_z()
        with allure.step('3：删除购物车商品'):
            MiniShoppingCart(mp_driver).mini_op_cart_del_goods(mp_driver)
        with allure.step('4：添加4个商品至确认订单页面'):
            MiniShoppingCart(mp_driver).mini_op_add_four_goods_chart(mp_driver)
        with allure.step('5：断言'):
            confirm_order_expand_more = CheckMiniConfirmOrder(mp_driver).mini_check_confirm_order_expand_more()
            print(confirm_order_expand_more)
            assert "展开更多" in confirm_order_expand_more
        with allure.step('6：点击收起'):
            MiniConfirmOrder(mp_driver).mini_op_expand_more()
        with allure.step('7：断言'):
            confirm_order_pack_up = CheckMiniConfirmOrder(mp_driver).mini_check_confirm_order_pack_up()
            print(confirm_order_pack_up)
            assert "收起" in confirm_order_pack_up


if __name__ == '__main__':
    pytest.main(['test_confirmordergoodsnumber.py'])
  #  pytest.main(['-m=Minileader', '--html=report.html'])
