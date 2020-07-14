# coding=utf-8

import sys

sys.path.append('F:\\shihuituan\\miniProgram')
import pytest
from action.miniprogram.check_mini_program_home_and_class import MiniCheckGroupBuy
from action.miniprogram.mini_program_get_into_shihuituan import MiniDifferentName
from action.miniprogram.mini_program_home_and_class import MiniGroupBuy
from action.miniprogram.mini_program_login import Login
import allure


class TestKingClassifyGoods():
    @pytest.mark.MiniLeaguenember
    @allure.step("首页金刚分类商品")
    def test_king_classify_goods(self):
        with allure.step('1：小程序初始化'):
            mp_driver = Login().go_in()
        with allure.step('2：通过张珊珊小程序链接进入首页'):
            MiniDifferentName(mp_driver).mini_op_name_link_z()
        with allure.step('3：点击采购中'):
            MiniGroupBuy(mp_driver).mini_op_group_buy_procure_go_on()
        with allure.step('4：断言'):
            home_hot = MiniCheckGroupBuy(mp_driver).mini_check_home_hot()
            assert "热卖" in home_hot
        with allure.step('5：左滑首页金刚'):
            Login().swipe_left_two(mp_driver)
        with allure.step('6：断言'):
            home_vegetables = MiniCheckGroupBuy(mp_driver).mini_check_home_vegetables()
            assert "新鲜蔬菜" in home_vegetables
        with allure.step('7：进入金刚子页面'):
            MiniGroupBuy(mp_driver).mini_op_group_buy_fresh_vegetables()
        with allure.step('8：断言'):
            home_king_vegetables = MiniCheckGroupBuy(mp_driver).mini_check_home_king_vegetables()
            assert "蔬菜" in home_king_vegetables
        with allure.step('9：进入生活服务'):
            MiniGroupBuy(mp_driver).mini_op_group_buy_life_service(mp_driver)
        with allure.step('10：断言'):
            home_king_left_service_goods = MiniCheckGroupBuy(mp_driver).mini_check_home_king_left_service_goods()
            assert "生活美妆" in home_king_left_service_goods
        with allure.step('11：上滑到底部'):
            MiniGroupBuy(mp_driver).mini_op_cycle_up_slip(mp_driver)
    #    with allure.step('12：断言'):
 #           check_home_king_end_line = MiniCheckGroupBuy(mp_driver).mini_check_home_king_end_line()
  #          assert "我们是有底线的" in check_home_king_end_line
        with allure.step('13：金刚子页面切换分类'):
            MiniGroupBuy(mp_driver).mini_op_group_buy_drinks_dairy_products(mp_driver)
        with allure.step('14：断言'):
            home_king_dairy_products = MiniCheckGroupBuy(mp_driver).mini_check_home_king_dairy_products()
            assert "肉禽蛋品" in home_king_dairy_products


if __name__ == '__main__':
    pytest.main(['test_kingclassifygoods.py'])
    pytest.main(['-m=LeagueMember', '--html=report.html'])
