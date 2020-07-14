# coding=utf-8


from appium import webdriver

import time


"""小程序登录方法"""
class Login():
    def go_in(self):
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
        time.sleep(30)
        return mp_driver



    """屏幕向上滑动"""
    def swipe_up(self,mp_driver,t=500):
        l = mp_driver.get_window_size()
        x1 = int(l['width'] * 0.5)  # x坐标
        y1 = int(l['height'] * 0.75)  # 起始y坐标
        y2 = int(l['height'] * 0.55)  # 终点y坐标
        mp_driver.swipe(x1, y1, x1, y2, t)

    # 屏幕向下滑动
    def swipe_down(t,mp_driver):
        l = mp_driver.get_window_size()
        x1 = int(l[0] * 0.5)  # x坐标
        y1 = int(l[1] * 0.25)  # 起始y坐标
        y2 = int(l[1] * 0.75)  # 终点y坐标
        mp_driver.swipe(x1, y1, x1, y2, t)

    # 屏幕向左滑动
    def swip_left(t,mp_driver):
        l = mp_driver.get_window_size()
        x1 = int(l[0] * 0.75)
        y1 = int(l[1] * 0.5)
        x2 = int(l[0] * 0.05)
        mp_driver.swipe(x1, y1, x2, y1, t)

    # 屏幕向右滑动
    def swip_right(t,mp_driver):
        l = mp_driver.get_window_size()
        x1 = int(l[0] * 0.05)
        y1 = int(l[1] * 0.5)
        x2 = int(l[0] * 0.75)
        mp_driver.swipe(x1, y1, x2, y1, t)