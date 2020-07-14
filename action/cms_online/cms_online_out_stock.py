# coding=utf-8


from elements.cms_online_elements import *
from action.base_page import BasePage
import time
from selenium.webdriver.support.select import Select


class CmsOnlineOutStock(BasePage):
    '''出库管理'''

    '''查看总部3站出库管理'''

    def cms_online_op_out_stock(self):
        # 点击出库管理菜单
        self.wait_presence_element(CMS_BUTTON_OUT_STOCK_MANAGE).click()
        # 点击订单出库
        self.wait_presence_element(CMS_BUTTON_OUT_STOCK_ORDER).click()
        # 实例化Select,按value选择option。   切换所属站点仓库，选择十荟团测试(前置仓)
        # 变更需要更新value值
        time.sleep(2)
        S = Select(self.driver.find_element_by_name('warehouseid')).select_by_visible_text("十荟团测试(前置仓)")
        # 点击子站
        time.sleep(3)
        self.wait_presence_element(CMS_BUTTON_OUT_STOCK_DELIVERY_WAREHOUSE_STATION).click()
        # 输入测试子站1
        self.wait_presence_element(CMS_INPUT_OUT_STOCK_DELIVERY_WAREHOUSE).send_keys("测试子站1")
        # 点击选中的总部测试子站1
        self.wait_presence_element(CMS_INPUT_OUT_STOCK_DELIVERY_WAREHOUSE_STATION_ONE).click()
        time.sleep(2)
        # 选择已同步
        S = Select(self.driver.find_element_by_name('deliverystatus')).select_by_visible_text("已同步")
        # 搜索
        self.wait_presence_element(CMS_INPUT_OUT_STOCK_DELIVERY_SEARCH).click()
        # 查看出库
        self.wait_presence_element(CMS_BUTTON_OUT_STOCK_DELIVERY_ORDER_LIST).click()
        time.sleep(2)
        # 确定出库
        self.wait_presence_element(CMS_BUTTON_OUT_STOCK_DELIVERY_STOCK).click()
        # 二次确定出库
        self.wait_presence_element(CMS_BUTTON_OUT_STOCK_DELIVERY_STOCK_TWO).click()
        # 三次确定出库
        self.wait_presence_element(CMS_BUTTON_OUT_STOCK_DELIVERY_STOCK_THREE).click()


