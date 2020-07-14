# coding=utf-8
import time

from elements.cms_online_elements import *
from action.base_page import BasePage
from selenium.webdriver.support.select import Select


class CmsOnlineRegimentalManage(BasePage):
    """角色管理-团管理页面-搜索團長"""

    def cms_online_query_regimental_search(self, Regimental_Search_date):
        # 点击系统管理
        self.wait_presence_element(CMS_BUTTON_SYSTEM_MANAGE).click()
        # 点击角色管理
        self.wait_presence_element(CMS_BUTTON_SYSTEM_ROLE).click()
        # 点击团长管理
        self.wait_presence_element(CMS_BUTTON_SYSTEM_ROLE_HEADS).click()
        ##实例化Select,按value选择option。   切换成按团长手机号搜索
        S = Select(self.driver.find_element_by_name('searchfield')).select_by_value('mobile')
        # 输入手机号
        self.wait_presence_element(CMS_INPUT_SYSTEM_ROLE_SEARCH_KEY).send_keys(Regimental_Search_date)
        # 点击搜索按钮
        self.wait_presence_element(CMS_BUTTON_SYSTEM_ROLE_HEADS_SEARCH).click()

       # le = self.driver.find_element_by_xpath('//*[@id="adminlist"]/tbody/tr/td[15]/a[3]')
        #self.driver.execute_script("return arguments[0].scrollIntoView(false);", le)

    """暂停团长"""

    def cms_online_op_regimental_suspend(self):
        # 进入团长详情
        self.wait_presence_element(CMS_BUTTON_SYSTEM_ROLE_HEADS_DETAILS_ONE).click()
        # 暂停团长
        time.sleep(4)
        self.wait_presence_element(CMS_BUTTON_SYSTEM_ROLE_HEADS_STOP_ONE).click()
        # 确定
        self.wait_presence_element(CMS_BUTTON_SYSTEM_ROLE_REPORTS_SALES_SEARCH).click()

    """开启团长"""

    def cms_online_op_regimental_open(self):
        time.sleep(2)
        # 开启
        self.wait_presence_element(CMS_BUTTON_SYSTEM_ROLE_HEADS_START_ONE).click()
        # 确定
        self.wait_presence_element(CMS_BUTTON_SYSTEM_ROLE_REPORTS_SALES_SEARCH).click()

    """关闭团长"""

    def cms_online_op_regimental_close(self):
        # 关闭团长
        self.wait_presence_element(CMS_BUTTON_SYSTEM_ROLE_HEADS_CLOSE_ONE).click()
        # 确定
        self.wait_presence_element(CMS_BUTTON_SYSTEM_ROLE_REPORTS_SALES_SEARCH).click()

    """重启团长"""

    def cms_online_op_regimental_restart(self):
        # 重启团长
        self.wait_presence_element(CMS_BUTTON_SYSTEM_ROLE_HEADS_START_TWO).click()
        # 确定
        self.wait_presence_element(CMS_BUTTON_SYSTEM_ROLE_REPORTS_SALES_SEARCH).click()
