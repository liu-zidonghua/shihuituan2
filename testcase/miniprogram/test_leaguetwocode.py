# coding=utf-8


import sys

import allure
import pytest

from action.miniprogram.check_mini_program_mine import MiniCheckLeagueMemberMine
from action.miniprogram.check_mini_program_my_order import MiniCheckMineOrder
from action.miniprogram.mini_program_get_into_shihuituan import MiniDifferentName
from action.miniprogram.mini_program_login import Login
from action.miniprogram.mini_program_mine import MiniLeagueMemberMine
from action.miniprogram.mini_program_my_order import MiniMineOrder

sys.path.append('F:\\shihuituan\\miniProgram')

class TestLeagueTwoCode():
    @pytest.mark.MiniLeaguenember
    @allure.step("团员二维码展示")
    def test_league_two_code(self):
        with allure.step('1：小程序初始化'):
            mp_driver = Login().go_in()
        with allure.step('2：进入团员首页'):
            MiniDifferentName(mp_driver).mini_op_name_link_ji_si_yu()
        with allure.step('3：进入我的页面'):
            MiniLeagueMemberMine(mp_driver).mini_op_mine()
        with allure.step('4：断言'):
            two_code_word_text = MiniCheckLeagueMemberMine(mp_driver).mini_check_mine_two_code_word_text()
            print(two_code_word_text)
            assert "向团长出示二维码取货" in two_code_word_text
        with allure.step('5：进入我的订单页面'):
            MiniMineOrder(mp_driver).mini_op_my_order_jump_two_code()
        with allure.step('6：断言'):
            two_code_pick_up_goods = MiniCheckMineOrder(mp_driver).mini_check_mine_two_code_pick_up_goods()
            print(two_code_pick_up_goods)
            assert "取货二维码" in two_code_pick_up_goods
if __name__ == '__main__':
    pytest.main(['test_leaguetwocode.py'])
    pytest.main(['-m=LeagueMember', '--html=report.html'])
