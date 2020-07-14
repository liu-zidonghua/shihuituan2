# coding=utf-8


import pytest
from action.miniprogram.check_mini_program_home_and_class import MiniCheckGroupBuy
from action.miniprogram.mini_program_get_into_shihuituan import MiniDifferentName
from action.miniprogram.mini_program_home_and_class import MiniGroupBuy
from action.miniprogram.mini_program_login import Login
import allure


class TestMiniKingSearchGoods():
    @pytest.mark.MiniLeaguenember
    @allure.step("验证热卖列表商品添加购物车")
    def test_mini_king_search_goods(self):
        with allure.step('1：小程序初始化'):
            mp_driver = Login().go_in()
        with allure.step('2：通过张珊珊小程序链接进入首页'):
            MiniDifferentName(mp_driver).mini_op_name_link_z()
        with allure.step('3：查看金刚子页面搜索商品'):
            MiniGroupBuy(mp_driver).mini_op_group_buy_fresh_vegetables()
        with allure.step('4：断言'):
            search_goods = MiniCheckGroupBuy(mp_driver).mini_check_search_goods()
            print(search_goods)
            assert "搜索商品" in search_goods
        with allure.step('5： 跳转搜索子页面'):
            MiniGroupBuy(mp_driver).mini_op_search_goods()
        with allure.step('6：断言'):
            input_goods_name_search = MiniCheckGroupBuy(mp_driver).mini_check_input_goods_name_search()
            print(input_goods_name_search)
            assert "请输入商品名称进行搜索" in input_goods_name_search
        with allure.step('7： 输入不存在的商品'):
            MiniGroupBuy(mp_driver).mini_op_search_no_goods()
        with allure.step('8：断言'):
            unqualified_goods = MiniCheckGroupBuy(mp_driver).mini_check_unqualified_goods()
            print(unqualified_goods)
            assert "抱歉，当前团购未找到符合条件的商品" in unqualified_goods
        with allure.step('9： 清除搜索框'):
            MiniGroupBuy(mp_driver).mini_op_search_del_search_text(mp_driver)
        with allure.step('10：断言'):
            input_goods_name_search = MiniCheckGroupBuy(mp_driver).mini_check_input_goods_name_search()
            print(input_goods_name_search)
            assert "请输入商品名称进行搜索" in input_goods_name_search
        with allure.step('11： 搜索有效商品'):
            MiniGroupBuy(mp_driver).mini_op_search_have_goods()
        with allure.step('12：断言'):
            not_enough_money = MiniCheckGroupBuy(mp_driver).mini_check_not_enough_money()
            print(not_enough_money)
            assert "零钱金额不足" in not_enough_money


if __name__ == '__main__':

    pytest.main(['test_kingsearchgoods.py'])
    pytest.main(['-m=LeagueMember', '--html=report.html'])
