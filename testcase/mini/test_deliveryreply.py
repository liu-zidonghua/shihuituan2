# coding=utf-8

import allure
import pytest

from action.cms_online.cms_online_word_order import CmsOnlineOrderService
from action.miniprogram.check_mini_program_work_order import MiniCheckAftersSalesOrder
from action.miniprogram.mini_program_get_into_shihuituan import MiniDifferentName
from action.miniprogram.mini_program_login import Login
from action.miniprogram.mini_program_work_order import MiniAftersSalesOrder


class TestOnlineDeliveryClose():

    @allure.step("后台操作工单解决/关闭后，小程序撤单工单")
    def test_delivery_cancel(self,cms_web_in):
        with allure.step('1：小程序初始化'):
            mp_driver = Login().go_in()
        with allure.step('2：通过张珊珊小程序链接进入首页'):
            MiniDifferentName(mp_driver).mini_op_name_link_z()
        with allure.step('３:进入售后工单'):
            MiniAftersSalesOrder(mp_driver).mini_op_afters_sales_order(mp_driver)
        with allure.step('4:提交工单'):
            MiniAftersSalesOrder(mp_driver).mini_op_order_apply_for_work_order()
        with allure.step('5：后台查看工单状态为处理中'):
            self.driver, self.login_page = (cms_web_in)
            CmsOnlineOrderService(self.driver).cms_online_query_word_order_search()
        with allure.step('6：cms赔付工单'):
            CmsOnlineOrderService(self.driver).cms_online_op_word_order_paid()
        with allure.step('7:小程序撤销工单申请'):
            MiniAftersSalesOrder(mp_driver).mini_op_order_cancel_work_order()
        with allure.step('8:断言'):
            work_order_submit_success = MiniCheckAftersSalesOrder(mp_driver).mini_check_work_order_submit_success()
            print(work_order_submit_success)
            assert "撤销申请" in work_order_submit_success
        with allure.step('9：退出小程序，进入十荟团商城'):
            MiniAftersSalesOrder(mp_driver).mini_op_shopping_mall(mp_driver)
        with allure.step('10：回复工单'):
            self.driver, self.login_page = (cms_web_in)
            CmsOnlineOrderService(self.driver).cms_online_op_word_order_reply()
        with allure.step('11:断言'):
            work_order_mall_reply = MiniCheckAftersSalesOrder(mp_driver).mini_check_work_order_mall_reply()
            print(work_order_mall_reply)
            assert "尊敬的团长，客服人员已给您回复，请查看" in work_order_mall_reply
        with allure.step('12：cms关闭工单'):
            self.driver, self.login_page = (cms_web_in)
            CmsOnlineOrderService(self.driver).cms_online_op_word_order_close()
        with allure.step('13:小程序撤销工单申请'):
            MiniAftersSalesOrder(mp_driver).mini_op_mine_word_order(mp_driver)
        with allure.step('14:断言'):
            work_order_submit_success = MiniCheckAftersSalesOrder(mp_driver).mini_check_work_order_submit_success()
            print(work_order_submit_success)
            assert "撤销申请" in work_order_submit_success



if __name__ == '__main__':
    pytest.main(['test_deliveryclose.py'])