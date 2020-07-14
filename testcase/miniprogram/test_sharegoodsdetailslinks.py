# coding=utf-8


import sys

import pytest

from action.miniprogram.check_mini_program_goods_details import CheckMiniGoodsDetails
from action.miniprogram.check_mini_program_home_and_class import MiniCheckGroupBuy
from action.miniprogram.mini_program_get_into_shihuituan import MiniDifferentName
from action.miniprogram.mini_program_goods_details import MiniGoodsDetails
from action.miniprogram.mini_program_home_and_class import MiniGroupBuy
from action.miniprogram.mini_program_login import Login
from action.miniprogram.mini_program_mine import MiniLeagueMemberMine

sys.path.append('F:\\shihuituan\\miniProgram')
import allure



class TestMiniShareGoodsDetailsLinks():

    @pytest.mark.MiniShare
    @allure.step("存在默认团长商品详情分享进入验证")
    def test_mini_share_goods_details_links(self):
        with allure.step('1：小程序初始化'):
            mp_driver = Login().go_in()
        with allure.step('2：通冀思雨小程序链接进入首页'):
            MiniDifferentName(mp_driver).mini_op_name_link_z()
        with allure.step('3：切换默认团长为王大法'):
            MiniLeagueMemberMine(mp_driver).mini_op_switching_head_wang(mp_driver)
        with allure.step('4：团员退出后通过详情页链接进入小程序'):
            MiniDifferentName(mp_driver).mini_op_goods_details_links(mp_driver)
        with allure.step('5：断言'):
            other_leaders = MiniCheckGroupBuy(mp_driver).mini_check_other_leaders()
            assert "您进入了其他团长的团购" in other_leaders
        with allure.step('6：点击默认团长'):
            MiniGroupBuy(mp_driver).mini_op_regiment_commander(mp_driver)
        with allure.step('7：进入首页'):
            MiniGoodsDetails(mp_driver).mini_op_goods_details_jump_home(mp_driver)
        with allure.step('8：断言'):
            user_wang_da_fa = MiniCheckGroupBuy(mp_driver).mini_check_user_wang_da_fa()
            assert "王大法" in user_wang_da_fa
        with allure.step('9：退出小程序再进入'):
            MiniDifferentName(mp_driver).mini_op_goods_details_links(mp_driver)
        with allure.step('10：断言'):
            other_leaders = MiniCheckGroupBuy(mp_driver).mini_check_other_leaders()
            assert "您进入了其他团长的团购" in other_leaders
        with allure.step('11：点击默认团长'):
            MiniGroupBuy(mp_driver).mini_op_regiment_commander(mp_driver)
        with allure.step('12：断言'):
            user_wang_da_fa = MiniCheckGroupBuy(mp_driver).mini_check_user_wang_da_fa()
            assert "王大法" in user_wang_da_fa
        with allure.step('13：退出小程序再进入'):
            MiniDifferentName(mp_driver).mini_op_goods_details_links(mp_driver)
        with allure.step('14：断言'):
            other_leaders = MiniCheckGroupBuy(mp_driver).mini_check_other_leaders()
            assert "您进入了其他团长的团购" in other_leaders
        with allure.step('15：点击本次访问团长'):
            MiniGroupBuy(mp_driver).mini_op_this_regiment_commander(mp_driver)
        with allure.step('16：断言'):
            goods_details_buy_now = CheckMiniGoodsDetails(mp_driver).mini_check_goods_details_buy_now()
            assert "立即购买" in goods_details_buy_now
        with allure.step('17：退出小程序再进入'):
            MiniDifferentName(mp_driver).mini_op_goods_details_links(mp_driver)
        with allure.step('18：断言'):
            other_leaders = MiniCheckGroupBuy(mp_driver).mini_check_other_leaders()
            assert "您进入了其他团长的团购" in other_leaders
        with allure.step('19：下滑'):
            Login().swipe_down(mp_driver)
        with allure.step('20：断言'):
            other_leaders = MiniCheckGroupBuy(mp_driver).mini_check_other_leaders()
            assert "您进入了其他团长的团购" in other_leaders
        with allure.step('21：点击本次访问团长'):
            MiniGroupBuy(mp_driver).mini_op_this_regiment_commander(mp_driver)
        with allure.step('22：断言'):
            goods_details_buy_now = CheckMiniGoodsDetails(mp_driver).mini_check_goods_details_buy_now()
            assert "立即购买" in goods_details_buy_now
        with allure.step('23：进入首页'):
            MiniGoodsDetails(mp_driver).mini_op_goods_details_jump_home(mp_driver)
        with allure.step('24：切换默认团长张珊珊'):
            MiniLeagueMemberMine(mp_driver).mini_op_switching_head_z(mp_driver)
        with allure.step('25：退出小程序再进入'):
            MiniDifferentName(mp_driver).mini_op_goods_details_links(mp_driver)
        with allure.step('26：进入首页'):
            MiniGoodsDetails(mp_driver).mini_op_goods_details_jump_home(mp_driver)
        with allure.step('27：断言'):
            user_zh = MiniCheckGroupBuy(mp_driver).mini_check_user_zh()
            assert "张珊珊" in user_zh


if __name__ == '__main__':
    pytest.main(['test_sharegoodsdetailslinks.py'])
    #pytest.main(['-m=MiniShare', '--html=report.html'])
