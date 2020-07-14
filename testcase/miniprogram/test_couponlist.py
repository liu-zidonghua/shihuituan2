# coding=utf-8
import sys
import pytest
from action.miniprogram.check_mini_program_mine import MiniCheckLeagueMemberMine
from action.miniprogram.mini_program_get_into_shihuituan import MiniDifferentName
from action.miniprogram.mini_program_login import Login
from action.miniprogram.mini_program_mine import MiniLeagueMemberMine
sys.path.append('F:\\shihuituan\\miniProgram')
import allure

class TestCouponList():
    @pytest.mark.MiniLeaguenember
    @pytest.mark.minicoupon
    @allure.step("验证优惠券列表展示")
    def test_coupon_list(self):
        with allure.step('1：小程序初始化'):
            mp_driver = Login().go_in()
        with allure.step('2：通过张珊珊小程序链接进入首页'):
            MiniDifferentName(mp_driver).mini_op_name_link_z()
        with allure.step('3：进入优惠券页面'):
            MiniLeagueMemberMine(mp_driver).mini_op_mine_coupon()
        with allure.step('4：断言'):
            coupon_one_cut_one = MiniCheckLeagueMemberMine(mp_driver).mini_check_mine_coupon_one_cut_one()
            print(coupon_one_cut_one)
            assert "订单满1 减 1" in coupon_one_cut_one
        with allure.step('5：上滑'):
            Login().swipe_up(mp_driver)
        with allure.step('6：断言'):
            coupon_single_item = MiniCheckLeagueMemberMine(mp_driver).mini_check_mine_coupon_single_item()
            print(coupon_single_item)
            assert "自动化单品券84183035(1702840)" in coupon_single_item


if __name__ == '__main__':
    pytest.main(['test_couponlist.py'])
    pytest.main(['-m=minicoupon', '--html=report.html'])
 #   pytest.main(['-m=LeagueMember', '--html=report.html'])
