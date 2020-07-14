# coding=utf-8


import sys
import pytest
sys.path.append('F:\\shihuituan\\miniProgram')
import allure
from action.base_page import *
import time


class TestDetail():

    @allure.step("验证商品详情")
    def test_good_detail(self):
        with allure.step('第1步：团长进入小程序'):
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
            Entry(mp_driver).regimental_link()
        with allure.step('第2步：切换分类'):
            time.sleep(6)
            MiniGroupBuy(mp_driver).treatment()
        with allure.step('第3步：断言'):
            time.sleep(1)
            detail =  mp_driver.find_element_by_android_uiautomator(
                'new UiSelector().text("爆款生鲜")').get_attribute("name")
            print(detail)
            assert "爆款生鲜" in detail
        with allure.step('第4步：告罄商品展示'):
            TouchAction(mp_driver).press(x=400, y=1279).move_to(x=900, y=1279).release().perform()
            MiniGroupBuy(mp_driver).sellers()
            TouchAction(mp_driver).press(x=400, y=1889).move_to(x=400, y=344).release().perform()
            TouchAction(mp_driver).press(x=400, y=1889).move_to(x=400, y=344).release().perform()
            TouchAction(mp_driver).press(x=400, y=1889).move_to(x=400, y=344).release().perform()
        with allure.step('第5步：断言'):
            time.sleep(5)
            roboed = mp_driver.find_element_by_android_uiautomator(
                'new UiSelector().text("抢光了")').get_attribute("name")
            print(roboed)
            assert "抢光了" in roboed
        with allure.step('第6步：点击告罄'):
            Purchase(mp_driver).sell_out()
        with allure.step('第7步：断言'):
            time.sleep(1)
            detail = mp_driver.find_element_by_android_uiautomator(
                'new UiSelector().text("商品详情")').get_attribute("name")
            print(detail)
            assert "商品详情" in detail
        with allure.step('第8步：点击告罄'):
            Purchase(mp_driver).sell_out()
        with allure.step('第9步：断言'):
            time.sleep(1)
            detail = mp_driver.find_element_by_android_uiautomator(
                'new UiSelector().text("商品详情")').get_attribute("name")
            print(detail)
            assert "商品详情" in detail
            spname = mp_driver.find_element_by_android_uiautomator(
                'new UiSelector().text("五级分拣")').get_attribute("name")
            print(spname)
            assert "五级分拣" in spname
            date1 = mp_driver.find_element_by_android_uiautomator(
                'new UiSelector().text("07月12日送达")').get_attribute("name")
            print(date1)
            date1 = "x" + date1[2]+"x"+date1[5:]
            assert "x月x日送达" in date1
            TouchAction(mp_driver).press(x=400, y=1279).move_to(x=900, y=1279).release().perform()
            specs = mp_driver.find_element_by_android_uiautomator(
                'new UiSelector().text("已选")').get_attribute("name")
            print(specs)
            assert "已选" in specs
            money = mp_driver.find_element_by_android_uiautomator(
                'new UiSelector().text("￥0.03￥11")').get_attribute("name")
            print(money)
            assert "￥0.03￥11" in money



if __name__ == '__main__':
    pytest.main(['test_kinggoodsaddcart.py'])