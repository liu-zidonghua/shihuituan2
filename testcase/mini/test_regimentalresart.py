# coding=utf-8
import sys

from action.cms_online.cms_online_regimental_manage import CmsOnlineRegimentalManage
from action.miniprogram.mini_program_mine import MiniLeagueMemberMine
sys.path.append('F:\\shi\\miniProgram')
import pytest
from action.miniprogram.check_mini_program_mine_manage import MiniCheckMineManage
from action.miniprogram.mini_program_get_into_shihuituan import MiniDifferentName
from action.miniprogram.mini_program_login import Login
import allure
from date.regimental_data import *


class TestRegimentalRestart():

    @pytest.mark.parametrize('data', regimental_search)
    @allure.step("后台重启团长验证副团长状态")
    def test_regimental_restart(self, cms_web_in, data):
        with allure.step('1：登录'):
            self.driver, self.login_page = (cms_web_in)
        with allure.step('2：cms进入团长页面'):
            CmsOnlineRegimentalManage(self.driver).cms_online_query_regimental_search(data['Regimental_Search_date'], )
        with allure.step('3：小程序初始化'):
            mp_driver = Login().go_in()
        with allure.step('4：通过副团长小程序链接进入首页'):
            MiniDifferentName(mp_driver).mini_op_name_link_ji_si_yu()
        with allure.step('5：进入副团长账号我的页面'):
            MiniLeagueMemberMine(mp_driver).mini_op_mine()
        with allure.step('6：断言'):
            deputy_head = MiniCheckMineManage(mp_driver).mini_check_deputy_head()
            print(deputy_head)
            assert "副团长" in deputy_head
        with allure.step('7：cms暂停团长'):
            self.driver, self.login_page = (cms_web_in)
            CmsOnlineRegimentalManage(self.driver).cms_online_op_regimental_suspend()
        with allure.step('8：退出小程序再进入'):
            MiniDifferentName(mp_driver).mini_op_wei_xin_go_link(mp_driver)
        with allure.step('9：断言'):
            select_ta = MiniCheckMineManage(mp_driver).mini_check_select_ta()
            print(select_ta)
            assert "选TA" in select_ta
        with allure.step('10：cms开启团长'):
            self.driver, self.login_page = (cms_web_in)
            CmsOnlineRegimentalManage(self.driver).cms_online_op_regimental_open()
        with allure.step('11：退出小程序再进入'):
            MiniDifferentName(mp_driver).mini_op_wei_xin_go_link_mine(mp_driver)
        with allure.step('12：断言'):
            deputy_head = MiniCheckMineManage(mp_driver).mini_check_deputy_head()
            print(deputy_head)
            assert "副团长" in deputy_head


if __name__ == '__main__':
    pytest.main(['test_regimentalresart.py'])