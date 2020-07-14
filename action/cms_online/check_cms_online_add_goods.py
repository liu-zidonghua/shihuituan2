# coding=utf-8


from elements.cms_online_elements import *
from action.base_page import BasePage
import time
from selenium.webdriver.support.select import Select


class CmsOnlineAddGoods(BasePage):

    """进入商品上架页面"""
    def wms_op_new_goods_enter(self):
        # 点击商品管理
        self.wait_presence_element(WMS_BUTTON_GOODS_MANAGE).click()
        # 点击商品上架
        self.wait_presence_element(WMS_BUTTON_GOODS_MANAGE_GOODS_LIST).click()

    """编辑页面--添加商品"""

    def cms_online_op_commodity_add_goods(self, goodsname1, goodssimplename1, maidian1, production1):
        time.sleep(4)
        # 点击添加商品
        self.wait_presence_element(WMS_BUTTON_COMMODITY_SHELVES_ADD_GOODS).click()
        # 选择寻味师
        self.wait_presence_element(WMS_BUTTON_COMMODITY_SHELVES_TASTER).click()
        self.wait_presence_element(WMS_BUTTON_COMMODITY_SHELVES_TASTER_FIRST).click()
        # 添加商品名称
        self.wait_presence_element(WMS_INPUT_COMMODITY_SHELVES_GOODS_NAME).send_keys(goodsname1)
        # 添加商品简称
        self.wait_presence_element(WMS_INPUT_COMMODITY_SHELVES_GOODS_ABBREVIATION).send_keys(goodssimplename1)
        # 实例化Select,按value选择option。   切换所属站点，选择北京市
        # 变更需要更新value值
        time.sleep(2)
        S = Select(self.driver.find_element_by_name('city_id')).select_by_visible_text("总部3站")
        time.sleep(2)
        # 卖点介绍
        self.wait_presence_element(WMS_BUTTON_COMMODITY_SHELVES_USP).send_keys(maidian1)
        # 添加产地哦
        self.wait_presence_element(WMS_BUTTON_COMMODITY_SHELVES_PRODUCTION).send_keys(production1)
        # 点击确认按钮
        self.wait_presence_element(WMS_BUTTON_COMMODITY_SHELVES_SURE).click()
        time.sleep(2)

    """编辑页面--总部3站商品简称搜索测试-自动化"""

    def cms_online_op_commodity_shelves(self):
        # 点击主站选择框
        time.sleep(3)
        self.wait_presence_element(WMS_BUTTON_COMMODITY_SHELVES_SELECT_MASTER_STATION).click()
        # 输入主站总部3
        self.wait_presence_element(WMS_INPUT_COMMODITY_SHELVES_MASTER_STATION_NAME).send_keys("总部3站")
        # 点击选中的总部3
        self.wait_presence_element(WMS_BUTTON_COMMODITY_SHELVES_MASTER_STATION_NAME).click()
        time.sleep(3)
        # 点击子站选择框
 #       self.wait_presence_element(WMS_BUTTON_COMMODITY_SHELVES_SELECT_SON_STATION).click()
        # 输入测试子站1
  #      self.wait_presence_element(WMS_INPUT_COMMODITY_SHELVES_SON_STATION_NAME).send_keys("测试子站1")
        # 点击选中的总部测试子站1
   #     self.wait_presence_element(WMS_BUTTON_COMMODITY_SHELVES_SON_STATION_NAME).click()
        time.sleep(2)
        # 商品简称搜索框中输入
        self.wait_presence_element(WMS_BUTTON_COMMODITY_SHELVES_SEARCH).send_keys("测试-自动化")
        # 点击搜索按钮
        self.wait_presence_element(WMS_BUTTON_COMMODITY_SHELVES_SEARCH_BUTTON).click()
        # 点击第一个编辑按钮
        self.wait_presence_element(WMS_BUTTON_COMMODITY_SHELVES_FIRST_EDIT).click()
        time.sleep(2)

    """编辑页面--总部3站商品简称搜索测试-自动化-a"""

    def cms_online_op_commodity_shelves_search(self):
        # 点击主站选择框
        time.sleep(3)
        self.wait_presence_element(WMS_BUTTON_COMMODITY_SHELVES_SELECT_MASTER_STATION).click()
        # 输入主站总部3
        self.wait_presence_element(WMS_INPUT_COMMODITY_SHELVES_MASTER_STATION_NAME).send_keys("总部3站")
        # 点击选中的总部3
        self.wait_presence_element(WMS_BUTTON_COMMODITY_SHELVES_MASTER_STATION_NAME).click()
        time.sleep(3)
        # 点击子站选择框
        #       self.wait_presence_element(WMS_BUTTON_COMMODITY_SHELVES_SELECT_SON_STATION).click()
        # 输入测试子站1
        #      self.wait_presence_element(WMS_INPUT_COMMODITY_SHELVES_SON_STATION_NAME).send_keys("测试子站1")
        # 点击选中的总部测试子站1
        #     self.wait_presence_element(WMS_BUTTON_COMMODITY_SHELVES_SON_STATION_NAME).click()
        time.sleep(2)
        # 商品简称搜索框中输入
        self.wait_presence_element(WMS_BUTTON_COMMODITY_SHELVES_SEARCH).send_keys("自动化-b")
        # 点击搜索按钮
        self.wait_presence_element(WMS_BUTTON_COMMODITY_SHELVES_SEARCH_BUTTON).click()
        # 点击第一个编辑按钮
        self.wait_presence_element(WMS_BUTTON_COMMODITY_SHELVES_FIRST_EDIT).click()
        time.sleep(2)

    """编辑页面--上传不符合图片大小图片验证"""

    def cms_online_op_commodity_cover_wrong_photo_three(self):
        #           le = self.driver.find_element_by_name('city_id')
        #           self.driver.execute_script("return arguments[0].scrollIntoView(false);", le)
        # 点击封面信息
        self.wait_presence_element(WMS_BUTTON_COMMODITY_SHELVES_COVER).click()
        # 选择封面图片
        S = Select(self.driver.find_element_by_name('cover_type')).select_by_visible_text("图片")
        # 点击上传图片
        self.wait_clickable_element(WMS_BUTTON_COMMODITY_SHELVES_COVER_UPLOAD_PHOTO).click()
        # 选择文件不满足300x300图片
        #       self.wait_clickable_element(WMS_BUTTON_COMMODITY_SHELVES_EDIT_SKU_CHOOSE_FILE).click()
        time.sleep(2)
        self.wait_clickable_element(WMS_BUTTON_COMMODITY_SHELVES_EDIT_SKU_CHOOSE_FILE).send_keys("F:\\image\\chicun.jpg")

        time.sleep(2)
    """编辑页面--上传不符合300x300图片提示"""

    def mini_check_photo_wrong_size_text(self):
        # 尺寸错误，请上传宽为300尺寸的图片
        photo_wrong_size = self.wait_presence_element(WMS_BUTTON_COMMODITY_SHELVES_COVER_WRONG_PHOTO).get_attribute('textContent')
        return photo_wrong_size

    """编辑页面--上传不符合图片500k验证"""
    def cms_online_op_commodity_cover_wrong_photo_five(self):

        # 点击失败提示的确定按钮
        self.wait_clickable_element(WMS_BUTTON_COMMODITY_SHELVES_EDIT_SKU_UPLOAD_SURE).click()
        # 选择大于500k图片
        time.sleep(2)
        self.wait_clickable_element(WMS_BUTTON_COMMODITY_SHELVES_EDIT_SKU_CHOOSE_FILE).send_keys("F:\\image\\1.png")
        time.sleep(2)

    """编辑页面--上传不符合500k提示"""

    def mini_check_photo_error_size_text(self):
        # 尺文件大小为：582.83K，请上传500K以内的文件
        photo_error_size = self.wait_presence_element(WMS_BUTTON_COMMODITY_SHELVES_COVER_ERROR_PHOTO).get_attribute('textContent')
        return photo_error_size

    """编辑页面--上传符合图片验证"""
    def cms_online_op_commodity_cover_photo(self):
        # 点击失败提示的确定按钮
        self.wait_clickable_element(WMS_BUTTON_COMMODITY_SHELVES_EDIT_SKU_UPLOAD_SURE).click()
        # 点击上传文件的取消按钮
        self.wait_clickable_element(WMS_BUTTON_COMMODITY_SHELVES_COVER_CANCEL).click()
        # 点击商品管理
        self.wait_clickable_element(WMS_BUTTON_PAGE_GOODS_MANAGE).click()
        # 点击主站选择框
        time.sleep(3)
        self.wait_presence_element(WMS_BUTTON_COMMODITY_SHELVES_SELECT_MASTER_STATION).click()
        # 输入主站总部3
        self.wait_presence_element(WMS_INPUT_COMMODITY_SHELVES_MASTER_STATION_NAME).send_keys("总部3站")
        # 点击选中的总部3
        self.wait_presence_element(WMS_BUTTON_COMMODITY_SHELVES_MASTER_STATION_NAME).click()
        time.sleep(3)
        # 商品简称搜索框中输入
        self.wait_presence_element(WMS_BUTTON_COMMODITY_SHELVES_SEARCH).send_keys("自动化-add")
        # 点击搜索按钮
        self.wait_presence_element(WMS_BUTTON_COMMODITY_SHELVES_SEARCH_BUTTON).click()
        # 点击第一个编辑按钮
        self.wait_presence_element(WMS_BUTTON_COMMODITY_SHELVES_FIRST_EDIT).click()
        time.sleep(2)
        self.wait_clickable_element(WMS_BUTTON_COMMODITY_SHELVES_EDIT_SPEC).click()
        # 点击封面信息
        self.wait_presence_element(WMS_BUTTON_COMMODITY_SHELVES_COVER).click()
        # 点击封面图片
        S = Select(self.driver.find_element_by_name('cover_type')).select_by_visible_text("图片")
        # 点击上传图片
        self.wait_clickable_element(WMS_BUTTON_COMMODITY_SHELVES_COVER_UPLOAD_PHOTO).click()
        # 选择符合要求图片
        time.sleep(2)
        self.wait_clickable_element(WMS_BUTTON_COMMODITY_SHELVES_EDIT_SKU_CHOOSE_FILE).send_keys("F:\\image\\tupian.jpg")
        time.sleep(2)
        #点击上传文件
        self.wait_clickable_element(WMS_BUTTON_COMMODITY_SHELVES_EDIT_SKU_UPLOAD_FILE).click()
        time.sleep(2)
    """编辑页面--上传符合要求提示"""

    def mini_check_photo_text(self):
        # 符合要求
        qd = self.driver.find_element_by_xpath("//*[@id='form']/table/tfoot/tr/td/button")
        self.driver.execute_script("return arguments[0].scrollIntoView(false);", qd)
        photo_text = qd.get_attribute('textContent')
        return photo_text





    """编辑页面--上传不符合视频验证"""

    def cms_online_op_commodity_cover_error_video(self):

        # 点击封面信息
        self.wait_presence_element(WMS_BUTTON_COMMODITY_SHELVES_COVER).click()
        # 后台统计分类
        self.wait_presence_element(WMS_BUTTON_COMMODITY_SHELVES_COVER_BUCK_STAGE).click()
        # 前端展示分类
        self.wait_presence_element(WMS_BUTTON_COMMODITY_SHELVES_COVER_RECEPTION).click()
        # 商品辅助分类
        self.wait_presence_element(WMS_BUTTON_COMMODITY_SHELVES_COVER_ASSIST).click()
        # 拣货分类
        self.wait_presence_element(WMS_BUTTON_COMMODITY_SHELVES_COVER_PICKING).click()
        # 保质期
        self.wait_presence_element(WMS_BUTTON_COMMODITY_SHELVES_COVER_EXP).send_keys("111")
        # 保存方式
        self.wait_presence_element(WMS_BUTTON_COMMODITY_SHELVES_COVER_SAVE).send_keys("111")
        # 封面价格
        self.wait_presence_element(WMS_BUTTON_COMMODITY_SHELVES_COVER_ORIG).clear()
        self.wait_presence_element(WMS_BUTTON_COMMODITY_SHELVES_COVER_ORIG).send_keys("11")
        # 选择封面视频
        S = Select(self.driver.find_element_by_name('cover_type')).select_by_visible_text("视频")
        # 点击上传视频
        self.wait_clickable_element(WMS_BUTTON_COMMODITY_SHELVES_COVER_UPLOAD_VIDEO).click()
        time.sleep(2)
        self.wait_clickable_element(WMS_BUTTON_COMMODITY_SHELVES_EDIT_SKU_CHOOSE_FILE).send_keys("F:\\image\\1.mp4")

        time.sleep(2)

    """编辑页面--上传不符合视频验证检查提示"""

    def mini_check_video_error_size_text(self):
        # 15.23M，请上传10M以内的文件
        video_error_size = self.wait_presence_element(WMS_BUTTON_COMMODITY_SHELVES_COVER_UPLOAD_ERROR_VIDEO).get_attribute('textContent')
        return video_error_size

    """编辑页面--不符合后上传符合视频验证"""
    def cms_online_op_commodity_cover_video(self):
        # 点击失败提示的确定按钮
        self.wait_clickable_element(WMS_BUTTON_COMMODITY_SHELVES_EDIT_SPEC_SURE_TWO).click()
        # 点击视频
        time.sleep(2)
        self.wait_clickable_element(WMS_BUTTON_COMMODITY_SHELVES_EDIT_SKU_CHOOSE_FILE).send_keys("F:\\image\\shipin.mp4")
        time.sleep(2)
        #点击上传文件
        self.wait_clickable_element(WMS_BUTTON_COMMODITY_SHELVES_EDIT_SKU_UPLOAD_FILE).click()
        time.sleep(5)
        qd = self.driver.find_element_by_xpath("//*[@id='form']/table/tfoot/tr/td/button")
        self.driver.execute_script("return arguments[0].scrollIntoView(false);", qd)
        # 点击确定
        self.wait_clickable_element(WMS_BUTTON_COMMODITY_SHELVES_COVER_SURE_BUTTON).click()
        time.sleep(9)
    """编辑页面--只上传符合视频检查提示"""

    def mini_check_video_only_video_text(self):
        # 选择视频封面，需上传封面+视频封面图
        video_only_video = self.wait_presence_element(WMS_BUTTON_COMMODITY_SHELVES_COVER_UPLOAD_ONLY_VIDEO).get_attribute('textContent')
        return video_only_video


    """编辑页面--上传符合视频图片验证"""
    def cms_online_op_commodity_cover_video_photo(self):
        # 点击失败提示的确定按钮
        self.wait_clickable_element(WMS_BUTTON_COMMODITY_SHELVES_EDIT_SKU_UPLOAD_SURE).click()
        # 点击创建规格
        self.wait_clickable_element(WMS_BUTTON_COMMODITY_SHELVES_EDIT_SPEC).click()
        # 点击封面信息
        self.wait_presence_element(WMS_BUTTON_COMMODITY_SHELVES_COVER).click()
        # 后台统计分类
        self.wait_presence_element(WMS_BUTTON_COMMODITY_SHELVES_COVER_BUCK_STAGE).click()
        # 前端展示分类
        self.wait_presence_element(WMS_BUTTON_COMMODITY_SHELVES_COVER_RECEPTION).click()
        # 商品辅助分类
        self.wait_presence_element(WMS_BUTTON_COMMODITY_SHELVES_COVER_ASSIST).click()
        # 拣货分类
        self.wait_presence_element(WMS_BUTTON_COMMODITY_SHELVES_COVER_PICKING).click()
        # 保质期
        self.wait_presence_element(WMS_BUTTON_COMMODITY_SHELVES_COVER_EXP).send_keys("111")
        # 保存方式
        self.wait_presence_element(WMS_BUTTON_COMMODITY_SHELVES_COVER_SAVE).send_keys("111")
        # 封面价格
        self.wait_presence_element(WMS_BUTTON_COMMODITY_SHELVES_COVER_ORIG).clear()
        self.wait_presence_element(WMS_BUTTON_COMMODITY_SHELVES_COVER_ORIG).send_keys("11")
        # 选择封面视频
        S = Select(self.driver.find_element_by_name('cover_type')).select_by_visible_text("视频")
        # 点击上传图片
        self.wait_clickable_element(WMS_BUTTON_COMMODITY_SHELVES_COVER_UPLOAD_VIDEO_PHOTO).click()
        time.sleep(2)
        self.wait_clickable_element(WMS_BUTTON_COMMODITY_SHELVES_EDIT_SKU_CHOOSE_FILE).send_keys("F:\\image\\tupian2.jpg")
        time.sleep(2)
        #点击上传文件
        self.wait_clickable_element(WMS_BUTTON_COMMODITY_SHELVES_EDIT_SKU_UPLOAD_FILE).click()
        time.sleep(2)
        # 点击确定
        self.wait_clickable_element(WMS_BUTTON_COMMODITY_SHELVES_COVER_SURE_BUTTON).click()
        time.sleep(9)
        """编辑页面--只上传符合图片检查提示"""

    def mini_check_video_only_photo_text(self):
            # 选择视频封面，需上传封面+视频封面图
        video_only_photo = self.wait_presence_element(
                WMS_BUTTON_COMMODITY_SHELVES_COVER_UPLOAD_ONLY_PHOTO).get_attribute('textContent')
        return video_only_photo

    """编辑页面--上传符合视频+图片验证"""

    def cms_online_op_commodity_cover_video_and_photo(self):
        # 点击失败提示的确定按钮
        self.wait_clickable_element(WMS_BUTTON_COMMODITY_SHELVES_EDIT_SPEC_SURE_TWO).click()
        # 点击商品管理
        self.wait_clickable_element(WMS_BUTTON_PAGE_GOODS_MANAGE).click()
        # 点击主站选择框
        time.sleep(3)
        self.wait_presence_element(WMS_BUTTON_COMMODITY_SHELVES_SELECT_MASTER_STATION).click()
        # 输入主站总部3
        self.wait_presence_element(WMS_INPUT_COMMODITY_SHELVES_MASTER_STATION_NAME).send_keys("总部3站")
        # 点击选中的总部3
        self.wait_presence_element(WMS_BUTTON_COMMODITY_SHELVES_MASTER_STATION_NAME).click()
        time.sleep(3)

        # 商品简称搜索框中输入
        self.wait_presence_element(WMS_BUTTON_COMMODITY_SHELVES_SEARCH).send_keys("自动化-add")
        # 点击搜索按钮
        self.wait_presence_element(WMS_BUTTON_COMMODITY_SHELVES_SEARCH_BUTTON).click()
        # 点击第一个编辑按钮
        self.wait_presence_element(WMS_BUTTON_COMMODITY_SHELVES_FIRST_EDIT).click()
        time.sleep(2)
        self.wait_clickable_element(WMS_BUTTON_COMMODITY_SHELVES_EDIT_SPEC).click()
        # 点击封面信息
        self.wait_presence_element(WMS_BUTTON_COMMODITY_SHELVES_COVER).click()
        # 后台统计分类
        self.wait_presence_element(WMS_BUTTON_COMMODITY_SHELVES_COVER_BUCK_STAGE).click()
        # 前端展示分类
        self.wait_presence_element(WMS_BUTTON_COMMODITY_SHELVES_COVER_RECEPTION).click()
        # 商品辅助分类
        self.wait_presence_element(WMS_BUTTON_COMMODITY_SHELVES_COVER_ASSIST).click()
        # 拣货分类
        self.wait_presence_element(WMS_BUTTON_COMMODITY_SHELVES_COVER_PICKING).click()
        # 保质期
        self.wait_presence_element(WMS_BUTTON_COMMODITY_SHELVES_COVER_EXP).send_keys("111")
        # 保存方式
        self.wait_presence_element(WMS_BUTTON_COMMODITY_SHELVES_COVER_SAVE).send_keys("111")
        # 封面价格
        self.wait_presence_element(WMS_BUTTON_COMMODITY_SHELVES_COVER_ORIG).clear()
        self.wait_presence_element(WMS_BUTTON_COMMODITY_SHELVES_COVER_ORIG).send_keys("11")
        # 选择封面视频
        S = Select(self.driver.find_element_by_name('cover_type')).select_by_visible_text("视频")

        # 点击上传视频
        self.wait_clickable_element(WMS_BUTTON_COMMODITY_SHELVES_COVER_UPLOAD_VIDEO).click()
        time.sleep(2)
        self.wait_clickable_element(WMS_BUTTON_COMMODITY_SHELVES_EDIT_SKU_CHOOSE_FILE).send_keys("F:\\image\\shipin.mp4")
        # 上传文件
        time.sleep(2)
        self.wait_clickable_element(WMS_BUTTON_COMMODITY_SHELVES_EDIT_SKU_UPLOAD_FILE).click()
        # 查找封面图片栏确定按钮
        time.sleep(5)
        qd = self.driver.find_element_by_xpath("//*[@id='form']/table/tfoot/tr/td/button")
        self.driver.execute_script("return arguments[0].scrollIntoView(false);", qd)
        # 点击上传图片
        self.wait_clickable_element(WMS_BUTTON_COMMODITY_SHELVES_COVER_UPLOAD_VIDEO_PHOTO).click()
        time.sleep(2)
        self.wait_clickable_element(WMS_BUTTON_COMMODITY_SHELVES_EDIT_SKU_CHOOSE_FILE).send_keys("F:\\image\\tupian2.jpg")
        time.sleep(2)
        #点击上传文件
        self.wait_clickable_element(WMS_BUTTON_COMMODITY_SHELVES_EDIT_SKU_UPLOAD_FILE).click()
        time.sleep(2)

        # 点击确定
        self.wait_clickable_element(WMS_BUTTON_COMMODITY_SHELVES_COVER_SURE_BUTTON).click()
        time.sleep(9)






        """编辑页面--添加轮播图"""
    def cms_online_op_commodity_rotation_chart(self):
        # 点击轮播图
        self.wait_clickable_element(WMS_BUTTON_COMMODITY_SHELVES_EDIT_ROTATION_CHART).click()
        time.sleep(2)
        # 点击删除此项
        self.wait_clickable_element(WMS_BUTTON_COMMODITY_SHELVES_EDIT_ROTATION_CHART_DEL).click()
        # 点击确定
        self.wait_clickable_element(WMS_BUTTON_SYSTEM_ROLE_REPORTS_SALES_SEARCH).click()
        time.sleep(2)
        # 点击添加轮播图
        self.wait_clickable_element(WMS_BUTTON_COMMODITY_SHELVES_EDIT_ROTATION_CHART_ADD).click()
        time.sleep(2)
        """编辑页面--轮播图页面上传视频"""
    def cms_online_op_commodity_rotation_chart_video(self):
        # 点击上传视频文件
        self.wait_clickable_element(WMS_BUTTON_COMMODITY_SHELVES_EDIT_ROTATION_CHART_VIDEO).click()

        time.sleep(2)
        # 选择上传视频
        self.wait_clickable_element(WMS_BUTTON_COMMODITY_SHELVES_EDIT_SKU_CHOOSE_FILE).send_keys("F:\\image\\shipin.mp4")
        time.sleep(2)
        # 点击上传文件
        self.wait_clickable_element(WMS_BUTTON_COMMODITY_SHELVES_EDIT_SKU_UPLOAD_FILE).click()
        time.sleep(30)
        # 点击确定
        self.wait_clickable_element(WMS_BUTTON_COMMODITY_SHELVES_COVER_SURE_BUTTON).click()

        time.sleep(2)
    """编辑页面--上传不符合大小轮播图片验证"""

    def cms_online_op_commodity_rotation_chart_error(self):
        time.sleep(2)
        # 点击失败提示的确定按钮
        self.wait_clickable_element(WMS_BUTTON_COMMODITY_SHELVES_EDIT_ROTATION_CHART_SURE).click()
        # 点击上传轮播图片
        self.wait_clickable_element(WMS_BUTTON_COMMODITY_SHELVES_EDIT_ROTATION_CHART_UPLOAD).click()
        # 选择文件不满足650x650的要求的图片
        #       self.wait_clickable_element(WMS_BUTTON_COMMODITY_SHELVES_EDIT_SKU_CHOOSE_FILE).click()
        time.sleep(2)
        self.wait_clickable_element(WMS_BUTTON_COMMODITY_SHELVES_EDIT_SKU_CHOOSE_FILE).send_keys("F:\\image\\chicun.jpg")
        time.sleep(2)

    """编辑页面--上传符合大小轮播图片验证"""

    def cms_online_op_commodity_rotation_chart_upload(self):
        time.sleep(2)
        # 点击失败提示的确定按钮
        self.wait_clickable_element(WMS_BUTTON_COMMODITY_SHELVES_EDIT_ROTATION_CHART_SURE_500).click()

        # 选择符合规格图片
        time.sleep(2)
        self.wait_clickable_element(WMS_BUTTON_COMMODITY_SHELVES_EDIT_SKU_CHOOSE_FILE).send_keys("F:\\image\\lunbotu.jpg")
        time.sleep(2)
        #点击上传文件
        self.wait_clickable_element(WMS_BUTTON_COMMODITY_SHELVES_EDIT_SKU_UPLOAD_FILE).click()
        time.sleep(5)
        qd = self.driver.find_element_by_xpath("//*[@id='form']/table/tfoot/tr/td/button")
        self.driver.execute_script("return arguments[0].scrollIntoView(false);", qd)
        # 点击确定
        self.wait_clickable_element(WMS_BUTTON_COMMODITY_SHELVES_COVER_SURE_BUTTON).click()
        time.sleep(9)
    """检查存在上传轮播图"""
    def mini_check_rotation_chart_text(self):
        # 上传轮播图
        rotation_chart_text = self.wait_presence_element(WMS_BUTTON_COMMODITY_SHELVES_EDIT_ROTATION_CHART_UPLOAD).get_attribute('textContent')
        return rotation_chart_text
    """检查存在请上传轮播图"""
    def mini_check_rotation_chart_upload_text(self):
        # 请上传轮播图
        rotation_chart_upload_text = self.wait_presence_element(WMS_BUTTON_COMMODITY_SHELVES_EDIT_ROTATION_CHART_PLEASE_UPLOAD).get_attribute('textContent')
        return rotation_chart_upload_text
    """检查存在尺寸错误轮播图"""
    def mini_check_rotation_chart_wrong_size_text(self):
        # 尺寸错误，请上传宽为640尺寸的图片
        rotation_chart_wrong_size = self.wait_presence_element(WMS_BUTTON_COMMODITY_SHELVES_EDIT_ROTATION_CHART_WRONG_SIZE).get_attribute('textContent')
        return rotation_chart_wrong_size
    """检查存在大小错误轮播图"""
    def mini_check_rotation_chart_error_size_text(self):
        # 文件大小为：582.83K，请上传500K以内的文件
        rotation_chart_error_size = self.wait_presence_element(WMS_BUTTON_COMMODITY_SHELVES_EDIT_ROTATION_CHART_ERROR_SIZE).get_attribute('textContent')
        return rotation_chart_error_size