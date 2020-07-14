# coding=utf-8



import allure
import pytest

from action.cms_online.check_cms_online_add_goods import CmsOnlineCheckAddGoods
from date.add_data import add_goods_shju
from action.cms_online.cms_online_add_goods import CmsOnlineAddGoods


class TestCmsOnlineAddRotationChart():

    @pytest.mark.parametrize('data', add_goods_shju)
    @pytest.mark.OnlineAddGoods
    @allure.step("cms线上添加商品轮播图")
    def test_cms_online_add_rotation_chart(self, cms_web_in,data):
        with allure.step('1：登录'):
            self.driver, self.login_page = (cms_web_in)
        with allure.step('2：进入页面'):
            CmsOnlineAddGoods(self.driver).cms_op_new_goods_enter()
        with allure.step('3：进入商品编辑页面'):
            CmsOnlineAddGoods(self.driver).cms_online_op_commodity_shelves()
        with allure.step('4：添加轮播图'):
            CmsOnlineAddGoods(self.driver).cms_online_op_commodity_rotation_chart()
        with allure.step('5：断言'):
            rotation_chart_text = CmsOnlineCheckAddGoods(self.driver).mini_check_rotation_chart_text()
            print(rotation_chart_text)
            assert ("上传轮播图" in rotation_chart_text) # 断言
        with allure.step('6：只上传视频'):
            CmsOnlineAddGoods(self.driver).cms_online_op_commodity_rotation_chart_video()
        with allure.step('7：断言'):
            rotation_chart_upload_text = CmsOnlineCheckAddGoods(self.driver).mini_check_rotation_chart_upload_text()
            print(rotation_chart_upload_text)
            assert ("请上传轮播图片" in rotation_chart_upload_text) # 断言
        with allure.step('8：上传不符合大小图片'):
            CmsOnlineAddGoods(self.driver).cms_online_op_commodity_rotation_chart_error()
        with allure.step('9：断言'):
            rotation_chart_wrong_size = CmsOnlineCheckAddGoods(self.driver).mini_check_rotation_chart_wrong_size_text()
            print(rotation_chart_wrong_size)
            assert ("尺寸错误，请上传宽为640尺寸的图片" in rotation_chart_wrong_size) # 断言
        with allure.step('10：上传不符合500k的图片'):
            CmsOnlineAddGoods(self.driver).cms_online_op_commodity_cover_wrong_photo_five()
        with allure.step('11：断言'):
            rotation_chart_error_size = CmsOnlineCheckAddGoods(self.driver).mini_check_rotation_chart_error_size_text()
            print(rotation_chart_error_size)
            assert ("文件大小为：582.83K，请上传500K以内的文件" in rotation_chart_error_size)  # 断言
        with allure.step('12：上传符合规格的轮播图片'):
            CmsOnlineAddGoods(self.driver).cms_online_op_commodity_rotation_chart_upload()


if __name__ == '__main__':
    pytest.main(['test_addgoodsrotationchart.py'])
    pytest.main(['-m=OnlineAddGoods', '--html=report.html'])