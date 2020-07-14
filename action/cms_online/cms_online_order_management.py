# coding=utf-8

from elements.cms_online_elements import *
from action.base_page import BasePage
import time
from selenium.webdriver.support.select import Select


class CmsOnlineOrderManage(BasePage):


    '''查看总部3站修改发货时间'''

    def cms_online_op_delivery_time_revise(self):
        # 点击订单管理菜单
        self.wait_presence_element(CMS_BUTTON_ORDER).click()
        # 点击查看订单
        self.wait_presence_element(CMS_BUTTON_ORDER_SEE).click()
        # 实例化Select切换所属站点，选择总部3站
        time.sleep(2)
        S = Select(self.driver.find_element_by_name('city_id')).select_by_visible_text("总部3站")
        # 选择子站
        time.sleep(3)
        S = Select(self.driver.find_element_by_name('sub_site_id')).select_by_visible_text("总部测试子站1")
        # 查询
        self.wait_presence_element(CMS_BUTTON_ORDER_SEARCH).click()
        # 查看详情
        self.wait_presence_element(CMS_BUTTON_ORDER_SEARCH_DETAILS).click()
        time.sleep(5)
        # 打印所有句柄
        handles = list(self.driver.window_handles)
        print(handles)
        # 切换新页面句柄
        handle2 = handles[2]
        self.driver.switch_to.window(handle2)
        time.sleep(2)
        print(handle2)
        # 修改送货时间
        self.wait_presence_element(CMS_BUTTON_ORDER_DELIVER_TIME).click()
        # 获取当前日期
#        b = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        # 点击新送货时间输入框
        self.wait_presence_element(CMS_BUTTON_ORDER_DELIVER_TIME_NEW).click()
        # 输入当前日期
        self.wait_presence_element(CMS_BUTTON_ORDER_DELIVER_TIME_NEW_NOW).click()
  #      js = "$('input[name=deliveryday]').attr('readonly','')"  # 4.jQuery，设置为空（同3）
   #     js = "$('input:eq(0)').removeAttr('readonly')"
    #    self.driver.execute_script(js)
        time.sleep(2)
      #  self.wait_presence_element(CMS_BUTTON_ORDER_DELIVER_TIME_NEW).send_keys("2020-04-08")
        # 修改原因
        self.wait_presence_element(CMS_BUTTON_ORDER_DELIVER_TIME_REASONS).send_keys("其它")
        # 修改责任归属
        self.wait_presence_element(CMS_BUTTON_ORDER_MODIFY_RESPONSIBILITY_ATTRIBUTION).send_keys("其它")
        # 保存
        self.wait_presence_element(CMS_BUTTON_ORDER_DELIVER_TIME_SAVE).click()
        # 确定
        self.wait_presence_element(CMS_BUTTON_ORDER_DELIVER_TIME_SAVE_TWO ).click()
        time.sleep(400)
