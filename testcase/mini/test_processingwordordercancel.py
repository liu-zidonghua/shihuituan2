# coding=utf-8

import allure
import pytest

from action.cms_online.check_cms_online_word_order import CmsOnlineCheckOrderService
from action.cms_online.cms_online_word_order import CmsOnlineOrderService
from action.miniprogram.check_mini_program_work_order import MiniCheckAftersSalesOrder
from action.miniprogram.mini_program_get_into_shihuituan import MiniDifferentName
from action.miniprogram.mini_program_login import Login
from action.miniprogram.mini_program_work_order import MiniAftersSalesOrder


class TestMiniWorkOrderCancel():

    @allure.step("售后工单")
    def test_mini_work_order_cancel(self,cms_web_in):
        with allure.step('1：小程序初始化'):
            mp_driver = Login().go_in()
        with allure.step('2：通过张珊珊小程序链接进入首页'):
            MiniDifferentName(mp_driver).mini_op_name_link_z()
        with allure.step('３:进入售后工单'):
            MiniAftersSalesOrder(mp_driver).mini_op_afters_sales_order(mp_driver)
        with allure.step('４:断言'):
            upload_video_photo = MiniCheckAftersSalesOrder(mp_driver).mini_check_upload_video_photo()
            print(upload_video_photo)
            assert "上传视频/照片" in upload_video_photo
        with allure.step('５:添加视频验证'):
            MiniAftersSalesOrder(mp_driver).mini_op_afters_sales_order_add_video()
        with allure.step('６:无添加视频文本'):
            MiniAftersSalesOrder(mp_driver).mini_op_not_add_video()
        with allure.step('７:添加照片验证'):
            MiniAftersSalesOrder(mp_driver).mini_op_afters_sales_order_add_photo(mp_driver)
        with allure.step('８:无添加照片文本'):
            MiniAftersSalesOrder(mp_driver).mini_op_not_add_photo()
        with allure.step('９:提交工单'):
            MiniAftersSalesOrder(mp_driver).mini_op_order_submission_work_order()
        with allure.step('１０:断言'):
            work_order_submit_success = MiniCheckAftersSalesOrder(mp_driver).mini_check_work_order_submit_success()
            print(work_order_submit_success)
            assert "撤销申请" in work_order_submit_success
        with allure.step('１１：后台查看工单状态为未处理'):
            self.driver, self.login_page = (cms_web_in)
            CmsOnlineOrderService(self.driver).cms_online_query_word_order_untreated_search()
        with allure.step('１２:断言'):
            self.driver, self.login_page = (cms_web_in)
            word_order_untreated = CmsOnlineCheckOrderService(self.driver).cms_online_check_word_order_untreated()
            print(word_order_untreated)
            assert "单规格小于1" in word_order_untreated
        with allure.step('１３:小程序撤销工单'):
            MiniAftersSalesOrder(mp_driver).mini_op_order_cancel_work_order()
        with allure.step('１４:断言'):
            work_order_cancel_success = MiniCheckAftersSalesOrder(mp_driver).mini_check_work_order_cancel_success()
            print(work_order_cancel_success)
            assert "撤销成功" in work_order_cancel_success

if __name__ == '__main__':
    pytest.main(['test_wordordercancel.py'])