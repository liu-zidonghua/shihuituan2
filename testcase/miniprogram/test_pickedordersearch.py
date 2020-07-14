# coding=utf-8
import pytest

from action.miniprogram.check_mini_program_order_pick_up import *
from action.miniprogram.mini_program_get_into_shihuituan import MiniDifferentName
from action.miniprogram.mini_program_login import Login
from action.miniprogram.mini_program_my_group_buy import MiniMyGroupBuy
import allure

from action.miniprogram.mini_program_order_picked_up import MiniOrderPickedUp


class TestMiniPickedOrderSearch():
    @pytest.mark.Minileader
    @allure.step("验证待提货订单无订单")
    def test_mini_picked_order_search(self):
        with allure.step('1：小程序初始化'):
            mp_driver = Login().go_in()
        with allure.step('2：通过张珊珊小程序链接进入首页'):
            MiniDifferentName(mp_driver).mini_op_name_link_z()
        with allure.step('3：进入待提货订单页面'):
            MiniOrderPickedUp(mp_driver).mini_op_mine_group_buy_order_picked_up(mp_driver)
        with allure.step('4：断言未提货'):
            not_pick_up_order_prompt = MiniCheckOrderPickedUp(mp_driver).mini_check_not_pick_up_order_prompt()
            print(not_pick_up_order_prompt)
            assert "未提走：商品已到货，团员还没来取货" in not_pick_up_order_prompt
        with allure.step('5：待提货订单微信手机号搜索'):
            MiniOrderPickedUp(mp_driver).order_phone_search(mp_driver)
        with allure.step('6：断言'):
            user_z =  MiniCheckOrderPickedUp(mp_driver).mini_check_user_z()
            print(user_z)
            assert "张珊珊" in user_z
        with allure.step('5：待提货订单姓名搜索'):
            MiniOrderPickedUp(mp_driver).mini_op_mine_order_picked_up_name_search(mp_driver)
        with allure.step('6：断言'):
            user_z =  MiniCheckOrderPickedUp(mp_driver).mini_check_user_z()
            print(user_z)
            assert "张珊珊" in user_z
        with allure.step('7：待提货订单昵称搜索'):
            MiniOrderPickedUp(mp_driver).mini_op_mine_order_picked_up_wei_xin_search(mp_driver)
        with allure.step('8：断言'):
            user_z =  MiniCheckOrderPickedUp(mp_driver).mini_check_user_z()
            print(user_z)
            assert "张珊珊" in user_z
        with allure.step('9：无待取货订单'):
            MiniOrderPickedUp( mp_driver).order_picked_end()
        with allure.step('10：断言'):
            not_pick_up_order = MiniCheckOrderPickedUp(mp_driver).mini_check_not_pick_up_order()
            print(not_pick_up_order)
            assert "没有待取货订单" in not_pick_up_order


if __name__ == '__main__':
    pytest.main(['test_pickedordersearch.py'])
  #  pytest.main(['-m=Minileader', '--html=report.html'])