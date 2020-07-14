# coding=utf-8


import sys

from action.miniprogram.mini_program_home_and_class import MiniGroupBuy

sys.path.append('F:\\shihuituan\\testcase\\miniprogram')

import pytest

from action.miniprogram.check_mini_program_home_and_class import MiniCheckGroupBuy
from action.miniprogram.mini_program_get_into_shihuituan import MiniDifferentName
from action.miniprogram.mini_program_login import Login
from action.miniprogram.mini_program_mine import MiniLeagueMemberMine

import allure



class TestMiniShareHomeLinks():

    @pytest.mark.MiniShare
    @allure.step("存在默认团长分享首页链接进入")
    def test_mini_share_home_links(self):
        with allure.step('1：小程序初始化'):
            mp_driver = Login().go_in()
        with allure.step('2：通冀思雨小程序链接进入首页'):
            MiniDifferentName(mp_driver).mini_op_name_link_ji_si_yu()
        with allure.step('3：切换默认团长为王大法'):
            MiniLeagueMemberMine(mp_driver).mini_op_switching_head_wang(mp_driver)
        with allure.step('4：团员退出后再次进入小程序'):
            MiniDifferentName(mp_driver).mini_op_wei_xin_go_link(mp_driver)
        with allure.step('5：断言'):
            other_leaders = MiniCheckGroupBuy(mp_driver).mini_check_other_leaders()
            assert "您进入了其他团长的团购" in other_leaders
        with allure.step('6：点击默认团长'):
            MiniGroupBuy(mp_driver).mini_op_regiment_commander(mp_driver)
        with allure.step('7：断言'):
            user_wang_da_fa = MiniCheckGroupBuy(mp_driver).mini_check_user_wang_da_fa()
            assert "王大法" in user_wang_da_fa
        with allure.step('8：退出小程序再进入'):
            MiniDifferentName(mp_driver).mini_op_wei_xin_go_link(mp_driver)
        with allure.step('9：断言'):
            other_leaders = MiniCheckGroupBuy(mp_driver).mini_check_other_leaders()
            assert "您进入了其他团长的团购" in other_leaders
        with allure.step('10：点击本次团长'):
            MiniGroupBuy(mp_driver).mini_op_this_regiment_commander(mp_driver)
        with allure.step('11：断言'):
            user_zh = MiniCheckGroupBuy(mp_driver).mini_check_user_zh()
            assert "张珊珊" in user_zh
        with allure.step('12：退出小程序再进入'):
            MiniDifferentName(mp_driver).mini_op_wei_xin_go_link(mp_driver)
        with allure.step('13：断言'):
            other_leaders = MiniCheckGroupBuy(mp_driver).mini_check_other_leaders()
            assert "您进入了其他团长的团购" in other_leaders
        with allure.step('14：下滑'):
            Login().swipe_down(mp_driver)
        with allure.step('15：断言'):
            other_leaders = MiniCheckGroupBuy(mp_driver).mini_check_other_leaders()
            assert "您进入了其他团长的团购" in other_leaders
        with allure.step('16：点击本次访问团长'):
            MiniGroupBuy(mp_driver).mini_op_this_regiment_commander(mp_driver)
        with allure.step('17：断言'):
            user_zh = MiniCheckGroupBuy(mp_driver).mini_check_user_zh()
            assert "张珊珊" in user_zh
        with allure.step('18：更换默认团长为本次选择团长'):
            MiniLeagueMemberMine(mp_driver).mini_op_switching_head_z(mp_driver)
        with allure.step('19：退出小程序再进入'):
            MiniDifferentName(mp_driver).mini_op_wei_xin_go_link(mp_driver)
        with allure.step('20：断言'):
            user_zh = MiniCheckGroupBuy(mp_driver).mini_check_user_zh()
            assert "张珊珊" in user_zh


if __name__ == '__main__':
    pytest.main(['test_sharehomelinks.py'])
    pytest.main(['-m=MiniShare', '--html=report.html'])
