# coding=utf-8

import sys
import pytest
from action.miniprogram.check_mini_program_scan_pick_up_goods import *
from action.miniprogram.mini_program_login import Login
from action.miniprogram.mini_proguram_scan_pick_up_goods import MiniScanPickGoods
sys.path.append('F:\\shihuituan\\miniProgram')
import allure
from action.miniprogram.mini_program_get_into_shihuituan import MiniDifferentName
from action.miniprogram.mini_program_mine import MiniLeagueMemberMine

class TestMiniDeputyHeadOfTheGroup():

    @allure.step("副团长扫码提货验证")
    def test_mini_deputy_head_of_the_group(self):
        with allure.step('1：小程序初始化'):
            mp_driver = Login().go_in()
        with allure.step('2：进入副团长首页'):
            MiniDifferentName(mp_driver).mini_op_name_link_ji_si_yu()
        with allure.step('3：进入我的页面'):
            MiniLeagueMemberMine(mp_driver).mini_op_mine()
        with allure.step('4：断言存在扫码提货'):
            scan_pick_up_goods = MiniCheckScanPickGoods(mp_driver).mini_check_scan_pick_up_goods()
            print(scan_pick_up_goods)
            assert "扫码提货" in scan_pick_up_goods
        with allure.step('5：点击扫码提货'):
            MiniScanPickGoods(mp_driver).mini_op_mine_group_buy_sweep_yards()
        with allure.step('6：断言'):
            scan_text = MiniCheckScanPickGoods(mp_driver).mini_check_scan_text()
            print(scan_text)
            assert "扫一扫" in scan_text
            search_phone = MiniCheckScanPickGoods(mp_driver).mini_check_search_phone()
            print(search_phone)
            assert "手机/微信昵称查询" in search_phone
        with allure.step('7：点击手机/微信查询'):
            MiniScanPickGoods(mp_driver).mini_query_mine_sweep_yards_phone()
        with allure.step('8：不输入信息查询'):
            MiniScanPickGoods(mp_driver).mini_query_mine_sweep_yards_phone()
        with allure.step('9：断言'):
            input_phone_search = MiniCheckScanPickGoods(mp_driver).mini_check_input_phone_search()
            print(input_phone_search)
            assert "请输入手机/微信昵称" in input_phone_search
        with allure.step('10：查询不存在的号码'):
            MiniScanPickGoods(mp_driver).mini_op_mine_sweep_yards_query_no_phone()
        with allure.step('11：断言'):
            search_not_user = MiniCheckScanPickGoods(mp_driver).mini_check_search_not_user()
            print(search_not_user)
            assert "未搜索到用户~" in search_not_user
        with allure.step('12：查询完整手机号'):
            MiniScanPickGoods(mp_driver).mini_op_mine_sweep_yards_query_phone(mp_driver)
        with allure.step('13：断言'):
            user_z = MiniCheckScanPickGoods(mp_driver).mini_check_user_z()
            print(user_z)
            assert "张珊珊" in user_z
        with allure.step('14：查询部分微信昵称'):
            MiniScanPickGoods(mp_driver).mini_op_mine_sweep_yards_query_wei_xin(mp_driver)
        with allure.step('第15步：断言'):
            user_z = MiniCheckScanPickGoods(mp_driver).mini_check_user_z()
            print(user_z)
            assert "张珊珊" in user_z
        with allure.step('15：点击查询结果'):
            MiniDifferentName(mp_driver).mini_op_mine_name_z()
        with allure.step('16：断言'):
            pick_up_goods_order = MiniCheckScanPickGoods(mp_driver).mini_check_scan_pick_up_goods_order()
            print(pick_up_goods_order)
            assert "取货单" in pick_up_goods_order
#        with allure.step('5：断言提示'):
#            pick_up_goods_order_prompt = MiniCheckScanPickGoods(mp_driver).mini_check_scan_pick_up_goods_order_prompt()
#            print(pick_up_goods_order_prompt)
#            assert "仅展示2019年8月30日扫码功能上线之后的订单" in pick_up_goods_order_prompt


if __name__ == '__main__':
    pytest.main(['test_deputyheadofthegroup.py'])
    pytest.main(['-m=LeagueMember', '--html=report.html'])
