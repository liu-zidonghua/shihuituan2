# coding=utf-8

import allure
import pytest

from action.cms_online.check_cms_online_add_goods import CmsOnlineCheckAddGoods
from action.cms_online.cms_online_add_goods import CmsOnlineAddGoods
from date.add_data import add_goods_shju


class TestCmsOnlineAddVideo():

    @pytest.mark.parametrize('data', add_goods_shju)
    @pytest.mark.OnlineAddGoods
    @allure.step("cms线上添加商品视频")
    def test_cms_online_add_video(self, cms_web_in,data):
        with allure.step('1：登录'):
            self.driver, self.login_page = (cms_web_in)
        with allure.step('2：进入页面'):
            CmsOnlineAddGoods(self.driver).cms_op_new_goods_enter()
        with allure.step('3：进入商品编辑页面'):
            CmsOnlineAddGoods(self.driver).cms_online_op_commodity_shelves_search()
        with allure.step('4：选择不满足规格视频'):
            CmsOnlineAddGoods(self.driver).cms_online_op_commodity_cover_error_video()
        with allure.step('5：断言'):
            video_error_size = CmsOnlineCheckAddGoods(self.driver).mini_check_video_error_size_text()
            print(video_error_size)
            assert ("15.23M，请上传10M以内的文件" in video_error_size) # 断言
        with allure.step('6：只上传视频'):
            CmsOnlineAddGoods(self.driver).cms_online_op_commodity_cover_video()
        with allure.step('7：断言'):
            video_only_video = CmsOnlineCheckAddGoods(self.driver).mini_check_video_only_video_text()
            print(video_only_video)
            assert ("选择视频封面，需上传封面+视频封面图" in video_only_video) # 断言
        with allure.step('8：只上传图片'):
            CmsOnlineAddGoods(self.driver).cms_online_op_commodity_cover_video_photo()
#        with allure.step('9：断言'):
#            video_only_photo = CmsOnlineCheckAddGoods(self.driver).mini_check_video_only_photo_text()
#            print(video_only_photo)
 #           assert ("选择视频封面，需上传封面+视频封面图" in video_only_photo) # 断言
        with allure.step('10：上传封面+视频'):
            CmsOnlineAddGoods(self.driver).cms_online_op_commodity_cover_video_and_photo()


if __name__ == '__main__':
   # pytest.main(['test_addgoodsvideo.py'])
    pytest.main(['-m=OnlineAddGoods', '--html=report.html'])