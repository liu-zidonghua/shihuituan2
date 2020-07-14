# coding=utf-8

import allure
import pytest

from action.miniprogram.check_mini_program_home_and_class import MiniCheckGroupBuy
from action.miniprogram.mini_program_get_into_shihuituan import MiniDifferentName
from action.miniprogram.mini_program_home_and_class import MiniGroupBuy
from action.miniprogram.mini_program_login import Login
class TestMiniGoodsVideo():
    @pytest.mark.MiniLeaguenember
    @allure.step("检查商品存在视频")
    def test_mini_goods_video(self):
        with allure.step('1：小程序初始化'):
            mp_driver = Login().go_in()
        with allure.step('2：通过张珊珊小程序链接进入首页'):
            MiniDifferentName(mp_driver).mini_op_name_link_z()
        with allure.step('3：进入金刚子页面查看视频'):
            MiniGroupBuy(mp_driver).mini_op_goods_diamond_move_video(mp_driver)
        with allure.step('4：断言'):
            present_video = MiniCheckGroupBuy(mp_driver).mini_check_present_video()
            print(present_video)
            assert "android.widget.Image" in present_video
        with allure.step('5：首页查看存在视频'):
            MiniGroupBuy(mp_driver).mini_op_goods_home_move_video(mp_driver)
        with allure.step('6：断言'):
            present_video = MiniCheckGroupBuy(mp_driver).mini_check_present_video()
            print(present_video)
            assert "android.widget.Image" in present_video
        with allure.step('7：进入商品详情验证轮播图'):
            MiniGroupBuy(mp_driver).mini_op_goods_detailed_video(mp_driver)
        with allure.step('8：断言'):
            present_video_time = MiniCheckGroupBuy(mp_driver).mini_check_present_video_time()
            print(present_video_time)
            assert "00:10" in present_video_time
        with allure.step('9：进入分类验证轮播图'):
            MiniGroupBuy(mp_driver).mini_op_goods_class_video(mp_driver)
        with allure.step('10：断言'):
            present_video = MiniCheckGroupBuy(mp_driver).mini_check_present_video()
            print(present_video)
            assert "android.widget.Image" in present_video


if __name__ == '__main__':
    pytest.main(['test_goodsvideo.py'])
    pytest.main(['-m=LeagueMember', '--html=report.html'])
