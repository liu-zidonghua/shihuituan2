# coding=utf-8
import sys

from action.cms_online.cms_online_login import Login

sys.path.append('F:\\shi\\miniProgram')
import time
import pytest
from selenium import webdriver

#from pages.cms_login import Login


"""启动小程序"""
@pytest.fixture(scope="session")
def mini_login():
    desired_caps = {
        'platformName': 'Android',  # 系统名称
        'deviceName': 'a98efad',  # 设备名称
        'platformVersion': '9',  # 设备系统
        'appPackage': 'com.tencent.mm',  # 被测应用'appPackage'
        'appActivity': 'com.tencent.mm.ui.LauncherUI',
        'automationName': 'uiautomator2',
        'newCommandTimeout': 4000,
        # 'unicodeKeyboard': True,
        # 'resetKeyboard': True,
        'noReset': True,
        'chromeOptions': {'androidProcess': 'com.android.settings'}
   }
    mp_driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    return mp_driver


# cms 测试环境
#@pytest.fixture(scope="session")
#def init_web():
#    driver = webdriver.Chrome()
 #   login_page = LoginPage(driver)
  #  login_page.login_success()
 #   login_page.login_success_test()
 #   time.sleep(1)
  #  yield driver, login_page

# cms 线上环境



"""cms 线上环境"""
@pytest.fixture(scope="session")
def cms_web_in():
    driver = webdriver.Chrome()
    login_page = Login(driver)
    login_page.log_on_cms()
    time.sleep(5)

    yield driver, login_page


