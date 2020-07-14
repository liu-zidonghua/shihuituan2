# coding=utf-8

import allure
import pytest

from action.cms_online.check_cms_online_add_goods import *
from date.add_data import add_goods_shju
from action.cms_online.cms_online_add_goods import *



class TestCmsOnlineAddPhoto():

    @pytest.mark.parametrize('data', add_goods_shju)
    @pytest.mark.OnlineAddGoods
    @allure.step("后台添加封面图片")
    def test_cms_online_add_photo(self, cms_web_in,data):
        with allure.step('1：登录'):
            self.driver, self.login_page = (cms_web_in)
        with allure.step('2：进入页面'):
            CmsOnlineAddGoods(self.driver).cms_op_new_goods_enter()
        with allure.step('3：进入商品编辑页面'):
            CmsOnlineAddGoods(self.driver).cms_online_op_commodity_shelves_search()
        with allure.step('4：选择不满足300x300图片'):
            CmsOnlineAddGoods(self.driver).cms_online_op_commodity_cover_wrong_photo_three()
        with allure.step('5：断言'):
            photo_wrong_size = CmsOnlineCheckAddGoods(self.driver).mini_check_photo_wrong_size_text()
            print(photo_wrong_size)
            assert ("尺寸错误，请上传宽为300尺寸的图片" in photo_wrong_size) # 断言
        with allure.step('6：选择不满足500k图片'):
            CmsOnlineAddGoods(self.driver).cms_online_op_commodity_cover_wrong_photo_five()
        with allure.step('7：断言'):
            photo_error_size = CmsOnlineCheckAddGoods(self.driver).mini_check_photo_error_size_text()
            print(photo_error_size)
            assert ("文件大小为：582.83K，请上传500K以内的文件" in photo_error_size) # 断言
        with allure.step('8：选择满足要求图片'):
            CmsOnlineAddGoods(self.driver).cms_online_op_commodity_cover_photo()
        with allure.step('9：断言'):
            photo_text = CmsOnlineCheckAddGoods(self.driver).mini_check_photo_text()
            assert ("确定" in photo_text) # 断言



if __name__ == '__main__':
    pytest.main(['test_addgoodsphoto.py'])
    pytest.main(['-m=OnlineAddGoods', '--html=report.html'])