# coding=utf-8

from appium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
import  traceback


from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from appium.webdriver.common.touch_action import TouchAction


class BasePage:
    """测试的基类，存放每个页面都可以用到的方法比如显示等待"""

    def __init__(self, driver: object) -> object:
        self.driver = driver

    def wait_presence_element(self, locator, timeout=80, poll_frequency=0.1):
        wait = WebDriverWait(self.driver, timeout, poll_frequency)
        find_element = wait.until(ec.presence_of_element_located(locator))
        return find_element

    def wait_clickable_element(self, locator):
        wait = WebDriverWait(self.driver, timeout=10, poll_frequency=0.1)
        find_element = wait.until(ec.element_to_be_clickable(locator))
        return find_element

        # 重写获取toast方法

    def find_toast(self, message, timeout, poll_frequency):
        u'''获取toast信息文本并验证'''
        message1 = "//*[@text=\'{}\']".format(message)
        element = WebDriverWait(self.driver, timeout, poll_frequency).until(
            ec.presence_of_element_located((By.XPATH, message1)))
        return element.text