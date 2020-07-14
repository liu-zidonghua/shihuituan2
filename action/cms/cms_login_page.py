# Author：yangyang
# Time：2019/7/9 10:59
# File: login.py

#登录页面
import time


from locators.wms_locators import *
from pages.base_page import BasePage


class LoginPage(BasePage):
    """登录相关类，其他的类调用这个类来进行登录，通过添加cookies的方式"""
    url = "https://cms-test.nicetuan.net"

    def login_success(self):
        # 访问登录页面
        self.driver.get(self.url)
        self.driver.maximize_window()
        # 通过添加cookie来登录

        self.wait_presence_element(WMS_LOGIN_TELPHONE).send_keys("18801455438")
        self.wait_presence_element(WMS_LOGIN_CAPTCHA).send_keys("123456")
        self.wait_presence_element(WMS_LOGIN_BUTTEN).click()


        """
        c1 = {'domain': 'shihuituan-test.youhaodongxi.com',
              'name': 'adminid',
              'value': '198',
              'path': '/admin',
              'httpOnly': False,
              'secure': True}

        c2 = {'domain': 'shihuituan-test.youhaodongxi.com',
              'name': 'adminname',
              'value': 'wwyy',
              'path': '/admin',
              'httpOnly': False,
              'secure': True}

        c3 = {'domain': 'shihuituan-test.youhaodongxi.com',
              'name': 'adminpassword',
              'value': '0985c783bc6190f12e303a27a57378e1',
              'path': '/admin',
              'httpOnly': False,
              'secure': True}

        c4 = {'domain': 'shihuituan-test.youhaodongxi.com',
              'name': 'token',
              'value': '521b9cba93d566044a2a87a67342a121',
              'path': '/admin',
              'httpOnly': False,
              'secure': True}

        self.driver.add_cookie(c1)
        self.driver.add_cookie(c2)
        self.driver.add_cookie(c3)
        self.driver.add_cookie(c4)

        time.sleep(3)
        #强制刷新
        self.driver.refresh()"""


