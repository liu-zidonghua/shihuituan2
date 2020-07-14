# coding=utf-8


import time

from appium.webdriver.common.touch_action import TouchAction

from elements.mini_program_elements import *
from action.base_page import BasePage


# 确认订单类
class MiniConfirmOrder (BasePage):
    """使用微信手机号"""

    def mini_op_confirm_place_phone_number(self):
        # 使用微信手机号
        self.wait_presence_element(MINI_ELEMENT_MINE_CONFIRM_ORDER_PHONE).click()

    """优惠券"""

    def mini_op_confirm_place_coupon(self):
        # 优惠券
        self.wait_presence_element(MINI_ELEMENT_MINE_CONFIRM_ORDER_COUPON).click()

    """备注"""

    def mini_op_confirm_place_remark(self):
        # 备注
        self.wait_presence_element(MINI_BUTTON_MINE_CONFIRM_ORDER_REMARK).click()

    """备注信息输入"""

    def mini_op_confirm_place_remark_input(self):
        # 点击备注输入框
        self.wait_presence_element(MINI_INPUT_MINE_CONFIRM_ORDER_REMARKS_TEXT).click()
        # 输入备注信息
        self.wait_presence_element(MINI_INPUT_MINE_CONFIRM_ORDER_REMARKS_TEXT).send_keys("货到电联")

    """确认支付"""

    def mini_op_confirm_place_payment(self):
        # 确认支付
        self.wait_presence_element(MINI_BUTTON_MINE_CONFIRM_ORDER_PAYMENT).click()

    """自提"""

    def mini_op_confirm_place_self_mention(self):
        # 自提
        self.wait_presence_element(MINI_ELEMENT_MINE_SERVICE_SELF_MENTION).click()

    """完成"""

    def mini_op_confirm_place_accomplish(self):
        # 完成
        self.wait_presence_element(MINI_BUTTON_MINE_ARRIVAL_ACCOMPLISH).click()

    """查看订单"""

    def mini_op_confirm_view_orders(self):
        # 查看订单
        self.wait_presence_element(MINI_BUTTON_MINE_VIEW_ORDERS).click()

    """删除购买人信息"""

    def mini_op_confirm_buy_name_del(self):
        # 点击购买人输入框
        self.wait_presence_element(MINI_BUTTON_MINE_CONFIRM_ORDER_BUY_NAME).click()
        # 清除输入框信息
        self.wait_presence_element(MINI_BUTTON_MINE_CONFIRM_ORDER_BUY_NAME).clear()

    """删除手机号"""

    def mini_op_confirm_buy_phone_del(self):
        # 点击购买人手机号
        self.wait_presence_element(MINI_BUTTON_MINE_CONFIRM_ORDER_BUY_PHONE).click()
        # 清除输入框信息
        self.wait_presence_element(MINI_BUTTON_MINE_CONFIRM_ORDER_BUY_PHONE).clear()

    """输入购买人信息"""

    def mini_op_confirm_buy_name_send(self):
        # 点击购买人输入框默认文案
        self.wait_presence_element(MINI_BUTTON_MINE_CONFIRM_ORDER_BUY_NAME_MEWS).click()
        # 输入购买人信息
        self.wait_presence_element(MINI_BUTTON_MINE_CONFIRM_ORDER_BUY_NAME_MEWS).send_keys("测试2")

    """使用微信手机号弹框验证"""

    def mini_op_confirm_phone_frame(self):
        # 使用微信手机号
        self.wait_presence_element(MINI_ELEMENT_MINE_CONFIRM_ORDER_PHONE).click()
        # 拒绝
        self.wait_presence_element(MINI_BUTTON_MINE_CONFIRM_ORDER_REFUSE).click()
        # 使用微信手机号
        self.wait_presence_element(MINI_ELEMENT_MINE_CONFIRM_ORDER_PHONE).click()
        # 允许
        self.wait_presence_element(MINI_BUTTON_MINE_WEI_XIN_PERMIT).click()

    """不使用优惠券"""

    def mini_op_confirm_not_coupon(self):
        # 不使用优惠券
        self.wait_presence_element(MINI_BUTTON_MINE_COUPON_NOT_MAKE).click()

    """单价低于一元的商品进入确认订单页"""

    def mini_op_small_one_confirm_order(self):
        # 单价低于一元的商品
        self.wait_presence_element(MINI_BUTTON_HOME_PRODUCT_SMALL_ONE).click()
        # 立即购买
        self.wait_presence_element(MINI_BUTTON_GOODS_DETAILS_BUYING).click()
        # 确定
        self.wait_presence_element(MINI_BUTTON_MINE_ORDER_DETAILS_ORDER_SURE).click()
        time.sleep(2)

    """单价高于一元的商品进入确认订单页"""

    def mini_op_big_one_confirm_order(self):
        # 单价高于一元的商品
        self.wait_presence_element(MINI_BUTTON_HOME_PRODUCT_BIG_ONE).click()
        # 立即购买
        self.wait_presence_element(MINI_BUTTON_GOODS_DETAILS_BUYING).click()
        # 确定
        self.wait_presence_element(MINI_BUTTON_MINE_ORDER_DETAILS_ORDER_SURE).click()
        time.sleep(2)

    '''小于1商品下单'''

    def mini_op_goods_less_confirm_order(self):
        # 点击价格小于1
        self.wait_presence_element(MINI_BUTTON_HOME_PRODUCT_SMALL_ONE).click()
        # 立即购买
        self.wait_presence_element(MINI_BUTTON_GOODS_DETAILS_BUYING).click()
        # 确定
        self.wait_presence_element(MINI_BUTTON_MINE_ORDER_DETAILS_ORDER_SURE).click()
        # 确认支付
        self.wait_presence_element(MINI_BUTTON_MINE_CONFIRM_ORDER_PAYMENT).click()

    '''库存不足商品下单'''

    def mini_op_not_stock_confirm_order(self):
        # 点击库存不足
        self.wait_presence_element(MINI_BUTTON_HOME_PRODUCT_NOT_STOCK).click()
        # 立即购买
        self.wait_presence_element(MINI_BUTTON_GOODS_DETAILS_BUYING).click()
        # 确定
        self.wait_presence_element(MINI_BUTTON_MINE_ORDER_DETAILS_ORDER_SURE).click()
        # 确认支付
        self.wait_presence_element(MINI_BUTTON_MINE_CONFIRM_ORDER_PAYMENT).click()
        time.sleep(8)

        '''支付密码'''

    def mini_op_payment_password(self,mp_driver):

        TouchAction(mp_driver).tap(x=199, y=1864).perform()
        TouchAction(mp_driver).tap(x=199, y=1992).perform()
        TouchAction(mp_driver).tap(x=199, y=2140).perform()
        TouchAction(mp_driver).tap(x=902, y=1864).perform()
        TouchAction(mp_driver).tap(x=902, y=1992).perform()
        TouchAction(mp_driver).tap(x=902, y=2140).perform()