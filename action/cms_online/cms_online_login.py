# coding=utf-8
import time

from action.base_page import BasePage


class Login(BasePage):
    '''登录类'''

    url = "https://cms.nicetuan.net"
    # 登录小程序线上环境
    def log_on_cms(self):
        self.driver.get(self.url)
        self.driver.maximize_window()


        c1 = {'domain': 'cms.nicetuan.net',
              'name': 'city_ids',
              'value': '1%2C5906%2C10227',
              'path': '/admin',
              'httpOnly': False,
              'secure': True}

        c2 = {'domain': 'cms.nicetuan.net',
              'name': 'adminid',
              'value': '2821',
              'path': '/admin',
              'httpOnly': False,
              'secure': True}

        c3 = {'domain': 'cms.nicetuan.net',
              'name': 'adminname',
              'value': '%E5%88%98%E4%BA%AD%E4%BA%AD',
              'path': '/admin',
              'httpOnly': False,
              'secure': True}

        c4 = {'domain': 'cms.nicetuan.net',
              'name': 'adminpassword',
              'value': '745e81a629928b0b80730103f57c10f9',
              'path': '/admin',
              'httpOnly': False,
              'secure': True}

        c5 = {'domain': 'cms.nicetuan.net',
              'name': 'token',
              'value': '745e81a629928b0b80730103f57c10f9',
              'path': '/admin',
              'httpOnly': False,
              'secure': True}

        c6 = {'domain': 'cms.nicetuan.net',
              'name': 'backpage',
              'value': '1',
              'path': '/admin',
              'httpOnly': False,
              'secure': True}

        self.driver.add_cookie(c1)
        self.driver.add_cookie(c2)
        self.driver.add_cookie(c3)
        self.driver.add_cookie(c4)
        self.driver.add_cookie(c5)
        self.driver.add_cookie(c6)
        time.sleep(3)
        #强制刷新
        self.driver.refresh()

