# coding=utf-8

import allure
import pytest
from action.miniprogram.check_mini_program_confirm_order import CheckMiniConfirmOrder
from action.miniprogram.check_mini_program_mine import MiniCheckLeagueMemberMine
from action.miniprogram.check_mini_program_shopping_cart import MiniCheckShoppingCart
from action.miniprogram.mini_program_confirm_order import MiniConfirmOrder
from action.miniprogram.mini_program_get_into_shihuituan import MiniDifferentName
from action.miniprogram.mini_program_login import Login
from action.miniprogram.mini_program_mine import MiniLeagueMemberMine
from action.miniprogram.mini_program_my_order import MiniMineOrder
from action.miniprogram.mini_program_shopping_cart import MiniShoppingCart


class TestCouponNumber():
    @pytest.mark.MiniLeaguenember
    @pytest.mark.minicoupon
    @allure.step("验证优惠券数量")
    def test_coupon_number(self):
        with allure.step('1：小程序初始化'):
            mp_driver = Login().go_in()
        with allure.step('2：通过张珊珊小程序链接进入首页'):
            MiniDifferentName(mp_driver).mini_op_name_link_z()
        with allure.step('3：进入我的页面'):
            MiniLeagueMemberMine(mp_driver).mini_op_mine()
        with allure.step('4：当前优惠券数量'):
            coupon_number =MiniCheckLeagueMemberMine(mp_driver).mini_check_mine_coupon_number()
            print(coupon_number)
            assert "19" in coupon_number
        with allure.step('5：删除购物车商品'):
            MiniShoppingCart(mp_driver).mini_op_cart_del_goods(mp_driver)
        with allure.step('6：单品券商品加入购物车'):
            MiniShoppingCart(mp_driver).mini_op_cart_add_more_specs(mp_driver)
        with allure.step('7：断言'):
            cart_go_pay =  MiniCheckShoppingCart(mp_driver).mini_check_cart_go_pay()
            assert "去支付" in cart_go_pay
        with allure.step('8：进入确认订单页'):
            MiniShoppingCart(mp_driver).mini_op_cart_pay()
        with allure.step('9：断言'):
            confirm_order = CheckMiniConfirmOrder(mp_driver).mini_check_confirm_order()
            assert "确认订单" in confirm_order
        with allure.step('10：支付'):
            MiniConfirmOrder(mp_driver).mini_op_confirm_place_payment()
        with allure.step('11：返回我的页面'):
            MiniMineOrder(mp_driver).mini_op_my_order_order_jump_mine(mp_driver)
        with allure.step('12：断言'):
            coupon_number_two = MiniCheckLeagueMemberMine(mp_driver).mini_check_mine_coupon_number_two()
            print(coupon_number_two)
            assert "18" in coupon_number_two
        with allure.step('13：取消订单'):
            MiniMineOrder(mp_driver).mini_op_my_order_mine_jump_order_cancel_mine(mp_driver)
        with allure.step('14：断言'):
            coupon_number = MiniCheckLeagueMemberMine(mp_driver).mini_check_mine_coupon_number()
            print(coupon_number)
            assert "19" in coupon_number


if __name__ == '__main__':
    pytest.main(['test_couponnumber.py'])
 #   pytest.main(['-m=minicoupon', '--html=report.html'])
  #  pytest.main(['-m=LeagueMember', '--html=report.html'])
