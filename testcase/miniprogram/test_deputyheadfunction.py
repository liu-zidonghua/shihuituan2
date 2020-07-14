# coding=utf-8


import allure
import pytest

from action.miniprogram.check_mini_program_head_my_page import MiniCheckMyPage
from action.miniprogram.check_mini_program_home_and_class import MiniCheckGroupBuy
from action.miniprogram.check_mini_program_mine import MiniCheckLeagueMemberMine
from action.miniprogram.check_mini_program_mine_manage import MiniCheckMineManage
from action.miniprogram.check_mini_program_work_order import MiniCheckAftersSalesOrder
from action.miniprogram.check_mini_program_scan_pick_up_goods import MiniCheckScanPickGoods
from action.miniprogram.mini_program_get_into_shihuituan import MiniDifferentName
from action.miniprogram.mini_program_head_my_page import MiniMyPage
from action.miniprogram.mini_program_home_and_class import MiniGroupBuy
from action.miniprogram.mini_program_login import Login
from action.miniprogram.mini_program_mine import MiniLeagueMemberMine
from action.miniprogram.mini_program_mine_manage import MiniMineManage
from action.miniprogram.mini_program_my_order import MiniMineOrder


class TestDeputyHeadFunction():

    @allure.step("副团长验证")
    def test_deputy_head_function(self):
        with allure.step('1：小程序初始化'):
            mp_driver = Login().go_in()
        with allure.step('2：进入副团长首页'):
            MiniDifferentName(mp_driver).mini_op_name_link_ji_si_yu()
        with allure.step('３：查看不存在团长专属产品'):
            MiniGroupBuy(mp_driver).mini_op_move_head_vip(mp_driver)
        with allure.step('４：进入我的页面'):
            MiniLeagueMemberMine(mp_driver).mini_op_mine()
        with allure.step('５：断言不存在的功能'):
            MiniMineManage(mp_driver).mini_op_mine_deputy_head_not_function(mp_driver)
        with allure.step('６：断言存在的功能'):
            deputy_head = MiniCheckMineManage(mp_driver).mini_check_deputy_head()
            print(deputy_head)
            assert "副团长" in deputy_head
            distribution_tracking = MiniCheckMyPage(mp_driver).mini_check_distribution_tracking()
            print(distribution_tracking)
            assert "配送跟踪" in distribution_tracking
            sign_code = MiniCheckMyPage(mp_driver).mini_check_sign_code()
            print(sign_code)
            assert "签收码" in sign_code
            arrival_reminder = MiniCheckMyPage(mp_driver).mini_check_arrival_reminder()
            print(arrival_reminder)
            assert "到货提醒" in arrival_reminder
            pick_up_goods_order_prompt = MiniCheckScanPickGoods(mp_driver).mini_check_scan_pick_up_goods()
            print(pick_up_goods_order_prompt)
            assert "扫码提货" in pick_up_goods_order_prompt
            picked_up_after_sales_feedback = MiniCheckAftersSalesOrder(mp_driver).mini_check_picked_up_after_sales_feedback()
            print(picked_up_after_sales_feedback)
            assert "售后反馈" in picked_up_after_sales_feedback
            opening_poster = MiniCheckMyPage(mp_driver).mini_check_opening_poster()
            print(opening_poster)
            assert "开团海报" in opening_poster
        with allure.step('７：我的订单跳转列表'):
            MiniMineOrder(mp_driver).mini_op_mine_order_deputy_head_state_jump(mp_driver)
        with allure.step('８：资质信息'):
            MiniLeagueMemberMine(mp_driver).mini_op_mine_qualification_message(mp_driver)
        with allure.step('９：断言'):
            qualification = MiniCheckLeagueMemberMine(mp_driver).mini_check_mine_qualification()
            print(qualification)
            assert "资质" in qualification


if __name__ == '__main__':
    pytest.main(['test_deputyheadfunction.py'])