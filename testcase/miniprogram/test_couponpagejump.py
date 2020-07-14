# coding=utf-8

import sys
import pytest
from action.miniprogram.mini_program_get_into_shihuituan import MiniDifferentName
from action.miniprogram.mini_program_login import Login
from action.miniprogram.mini_program_mine import MiniLeagueMemberMine
from action.miniprogram.check_mini_program_mine import MiniCheckLeagueMemberMine
sys.path.append('F:\\shihuituan\\miniProgram')
import allure




class TestCouponPageJump():
    @pytest.mark.MiniLeaguenember
    @pytest.mark.minicoupon
    @allure.step("验证优惠券正常跳转页面")
    def test_coupon_page_jump(self):
        with allure.step('1：小程序初始化'):
            mp_driver = Login().go_in()
        with allure.step('2：通过张珊珊小程序链接进入首页'):
            MiniDifferentName(mp_driver).mini_op_name_link_z()
        with allure.step('3：进入优惠券页面'):
            MiniLeagueMemberMine(mp_driver).mini_op_mine_coupon()
        with allure.step('4：断言'):
            coupon_general_voucher = MiniCheckLeagueMemberMine(mp_driver).mini_check_mine_coupon_general_voucher()
            print(coupon_general_voucher)
            assert "通用券" in coupon_general_voucher
        with allure.step('5：进入历史优惠券'):
            MiniLeagueMemberMine(mp_driver).mini_op_historical_coupons(mp_driver)
        with allure.step('6：断言'):
            coupon_general_voucher = MiniCheckLeagueMemberMine(mp_driver).mini_check_mine_coupon_history()
            print(coupon_general_voucher)
            assert "历史优惠券" in coupon_general_voucher
        with allure.step('7：返回'):
            MiniLeagueMemberMine(mp_driver).mini_op_historical_coupons_back(mp_driver)
        with allure.step('8：断言'):
            coupon = MiniCheckLeagueMemberMine(mp_driver).mini_check_mine_coupon()
            print(coupon)
            assert "优惠券" in coupon

if __name__ == '__main__':
    pytest.main(['test_couponpagejump.py'])
   # pytest.main(['-m=minicoupon', '--html=report.html'])
  #  pytest.main(['-m=LeagueMember', '--html=report.html'])
