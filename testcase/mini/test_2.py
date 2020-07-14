# coding=utf-8
import time

import allure
import pytest

from action.miniprogram.check_mini_program_confirm_order import CheckMiniConfirmOrder
from action.miniprogram.check_mini_program_home_and_class import MiniCheckGroupBuy
from action.miniprogram.mini_program_confirm_order import MiniConfirmOrder
import allure
import pytest
from action.miniprogram.check_mini_program_confirm_order import CheckMiniConfirmOrder
from action.miniprogram.check_mini_program_mine import MiniCheckLeagueMemberMine
from action.miniprogram.check_mini_program_shopping_cart import MiniCheckShoppingCart
from action.miniprogram.mini_program_confirm_order import MiniConfirmOrder
from action.miniprogram.mini_program_mine import MiniLeagueMemberMine
from action.miniprogram.mini_program_shopping_cart import MiniShoppingCart


import allure
import pytest

from action.miniprogram.mini_program_get_into_shihuituan import MiniDifferentName
from action.miniprogram.mini_program_login import Login
from action.miniprogram.mini_program_my_order import MiniMineOrder
from action.miniprogram.mini_program_work_order import MiniAftersSalesOrder

class TestMiniWorkOrderCancel():

        @pytest.mark.webtest
        @pytest.mark.webtest
        @allure.step("验证优惠券数量")
        def test_coupon_number(self):
            with allure.step('1：小程序初始化'):
                p_driver = Login().go_in()
            with allure.step('2：通过张珊珊小程序链接进入首页'):
                MiniDifferentName(p_driver).mini_op_name_link_z()
            with allure.step('3：进入我的页面'):
                MiniLeagueMemberMine(p_driver).mini_op_mine()


if __name__ == '__main__':
    pytest.main(['-m=webtest','--html=report.html'])