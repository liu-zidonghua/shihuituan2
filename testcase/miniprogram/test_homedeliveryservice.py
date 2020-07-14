# coding=utf-8
import pytest
from action.miniprogram.check_mini_program_home_delivery_service import CheckMiniHomeDeliveryService
from action.miniprogram.mini_program_get_into_shihuituan import MiniDifferentName
from action.miniprogram.mini_program_home_delivery_service import MiniHomeDeliveryService
from action.miniprogram.mini_program_login import Login
import allure


class TestMiniDeliverGoods():
    @pytest.mark.Minileader
    @allure.step("打开送货上门设置")
    def test_mini_deliver_goods(self):
        with allure.step('1：小程序初始化'):
            mp_driver = Login().go_in()
        with allure.step('2：通过张珊珊小程序链接进入首页'):
            MiniDifferentName(mp_driver).mini_op_name_link_z()
        with allure.step('3：进入送货上门设置页'):
            MiniHomeDeliveryService(mp_driver).mini_op_mine_order_picked_up_home_delivery_service(mp_driver)
        with allure.step('4：断言'):
            provide_home_delivery_service = CheckMiniHomeDeliveryService(mp_driver).mini_check_mine_provide_home_delivery_service()
            print(provide_home_delivery_service)
            assert "自提/送货设置" in provide_home_delivery_service
        with allure.step('5：关闭送货上门开关'):
            MiniHomeDeliveryService(mp_driver).mini_op_mine_order_picked_up_freight_open(mp_driver)
        with allure.step('6：打开送货上门开关'):
            MiniHomeDeliveryService(mp_driver).mini_op_mine_order_picked_up_freight_open(mp_driver)
        with allure.step('7：断言'):
            provide_home_delivery_service_freight = CheckMiniHomeDeliveryService(mp_driver).mini_check_mine_provide_home_delivery_service_freight()
            print(provide_home_delivery_service_freight)
            assert "运费" in provide_home_delivery_service_freight
        with allure.step('8：输入运费'):
            MiniHomeDeliveryService(mp_driver).mini_op_mine_order_picked_up_freight_input()
        with allure.step('9：断言'):
            provide_home_delivery_service_freight_money = CheckMiniHomeDeliveryService(mp_driver).mini_check_mine_provide_home_delivery_service_freight_money()
            print(provide_home_delivery_service_freight_money)
            assert "1" in provide_home_delivery_service_freight_money




if __name__ == '__main__':
    pytest.main(['test_homedeliveryservice.py'])
    #pytest.main(['-m=Minileader', '--html=report.html'])