# coding=utf-8
import sys

sys.path.append('F:\\shihuituan\\miniProgram')
from action.miniprogram.mini_program_get_into_shihuituan import MiniDifferentName
import allure
from action.miniprogram.mini_program_mine_manage import *
import pytest
from action.miniprogram.check_mini_program_mine_manage import MiniCheckMineManage

class TestMiniAddDeputyRegimental():
    @pytest.mark.Minileader
    @allure.step("添加副团长验证")
    def test_mini_add_deputy_regimental(self):
        with allure.step('1：小程序初始化'):
            mp_driver = Login().go_in()
        with allure.step('2：通过张珊珊小程序链接进入首页'):
            MiniDifferentName(mp_driver).mini_op_name_link_z()
        with allure.step('3：进入副团长管理页面'):
            MiniMineManage(mp_driver).mini_op_mine_manage_deputy_head_management(mp_driver)
        with allure.step('4：删除已添加的副团长'):
            MiniMineManage(mp_driver).mini_op_mine_del_deputy_head(mp_driver)
        with allure.step('5：断言'):
            deputy_head_no_add = MiniCheckMineManage(mp_driver).mini_check_mine_deputy_head_no_add()
            print(deputy_head_no_add)
            assert "还未添加副团长" in deputy_head_no_add
        with allure.step('6：进入添加副团长页面'):
            MiniMineManage(mp_driver).mini_op_mine_deputy_head_add()
        with allure.step('7：断言'):
            deputy_head_input_user_id = MiniCheckMineManage(mp_driver).mini_check_mine_deputy_head_input_user_id()
            print(deputy_head_input_user_id)
            assert "输入用户ID" in deputy_head_input_user_id
        with allure.step('8：点击添加'):
            MiniMineManage(mp_driver).mini_op_mine_deputy_head_user_add()
        with allure.step('9：断言'):
            deputy_head_input_id = MiniCheckMineManage(mp_driver).mini_check_mine_deputy_head_input_id()
            print(deputy_head_input_id)
            assert "请输入副团长id" in deputy_head_input_id
        with allure.step('10：添加副团长冀思雨'):
            MiniMineManage(mp_driver).mini_op_mine_deputy_head_user_add_ji_si_yu()
        with allure.step('11：断言'):
            deputy_head_ji_si_yu = MiniCheckMineManage(mp_driver).mini_check_mine_deputy_head_ji_si_yu()
            print(deputy_head_ji_si_yu)
            assert "冀思雨" in deputy_head_ji_si_yu
        with allure.step('12：进入添加副团长页面'):
            MiniMineManage(mp_driver).mini_op_mine_deputy_head_add()
        with allure.step('13：再次添加副团长冀思雨'):
            MiniMineManage(mp_driver).mini_op_mine_deputy_head_user_add_ji_si_yu()
        with allure.step('14：断言'):
            deputy_head_exist = MiniCheckMineManage(mp_driver).mini_check_mine_deputy_head_exist()
            print(deputy_head_exist)
            assert "该用户已经是副团长" in deputy_head_exist
        with allure.step('15：添加副团长刘亭亭'):
            MiniMineManage(mp_driver).mini_op_mine_deputy_head_user_add_liu_ting_ting()
        with allure.step('16：断言'):
            deputy_head_liu_ting_ting = MiniCheckMineManage(mp_driver).mini_check_mine_deputy_head_liu_ting_ting()
            print(deputy_head_liu_ting_ting)
            assert "刘亭亭" in deputy_head_liu_ting_ting
        with allure.step('17：删除副团长'):
            MiniMineManage(mp_driver).mini_op_mine_deputy_head_management_del(mp_driver)



if __name__ == '__main__':
    pytest.main(['test_adddeputyregimental.py'])
    pytest.main(['-m=Minileader', '--html=report.html'])
