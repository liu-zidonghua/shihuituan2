# coding=utf-8



import allure

from action.base_page import *
from pages.mp_homename import *
from pages.mp_homebuy import Purchase


class TestDelivery():

    @allure.step("配送日期")
    def test_delivery(self):
        with allure.step('第1步：团员进入小程序'):
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
            Entry(mp_driver).league_link()
        with allure.step('第2步：查看今日配送'):

            TouchAction(mp_driver).press(x=400, y=1889).move_to(x=400, y=780).release().perform()
            time.sleep(2)
            TouchAction(mp_driver).press(x=400, y=1889).move_to(x=400, y=780).release().perform()
            time.sleep(2)
            TouchAction(mp_driver).press(x=400, y=1889).move_to(x=400, y=780).release().perform()
            time.sleep(2)
            Purchase(mp_driver).specs()
            time.sleep(2)
        with allure.step('第5步：断言'):
            time1 = mp_driver.find_element_by_android_uiautomator(
                'new UiSelector().text("今日达")').get_attribute("name")
            print(time1)
            assert "今日达" in time1
        with allure.step('第6步：查看次日配送'):
            TouchAction(mp_driver).tap(x=76, y=141).perform()
            time.sleep(2)
            TouchAction(mp_driver).press(x=400, y=1889).move_to(x=400, y=780).release().perform()

            time.sleep(2)
            TouchAction(mp_driver).press(x=400, y=1889).move_to(x=400, y=780).release().perform()
            Purchase(mp_driver).mini_op_goods_video()
            time.sleep(2)
        with allure.step('第5步：断言'):
            time2 = mp_driver.find_element_by_android_uiautomator(
                'new UiSelector().text("次日达")').get_attribute("name")
            print(time2)
            assert "次日达" in time2