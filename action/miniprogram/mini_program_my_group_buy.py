# coding=utf-8

from elements.mini_program_elements import *

from action.base_page import BasePage

"""我的团购"""
class MiniMyGroupBuy(BasePage):

    """历史开团"""
    def mini_op_mine_group_buy_historical_opening(self):
        # 点击历史开团
        self.wait_presence_element(MINI_BUTTON_MINE_HISTORICAL_OPENING).click()

    """配送跟踪"""
    def mini_op_mine_group_buy_distribution_tracking(self):
        # 点击配送跟踪
        self.wait_presence_element(MINI_BUTTON_MINE_DISTRIBUTION_TRACKING).click()

    """签收码"""
    def mini_op_mine_group_buy_sign_code(self):
        # 点击签收码
        self.wait_presence_element(MINI_BUTTON_MINE_SIGN_CODE).click()

    """到货提醒"""
    def mini_op_mine_group_buy_arrival_reminder(self):
        # 点击到货提醒
        self.wait_presence_element(MINI_BUTTON_MINE_ARRIVAL_REMINDER).click()

    """扫码提货"""
    def mini_op_mine_group_buy_sweep_yards(self):
        # 点击扫码提货
        self.wait_presence_element(MINI_BUTTON_MINE_PICK_UP_BY_SCANNING_CODE).click()

    """扫一扫"""
    def mini_op_mine_sweep_yards_scan(self):
        # 点击扫一扫
        self.wait_presence_element(MINI_BUTTON_MINE_SCANNING_SCAN).click()

    """点击手机/微信号查询"""
    def mini_query_mine_sweep_yards_phone(self):
        # 点击手机/微信号查询
        self.wait_presence_element(MINI_BUTTON_MINE_SCANNING_PHONE_WEI_XIN_SEARCH).click()

    """查询"""
    def mini_op_mine_sweep_yards_query(self):
        # 点击查询
        self.wait_presence_element(MINI_INPUT_MINE_SCANNING_SEARCH_QUERY).click()

    """点击查询输入框"""
    def mini_op_mine_sweep_yards_query_input(self):
        # 点击查询输入框
        self.wait_presence_element(MINI_INPUT_MINE_SCANNING_SEARCH_EDIT_TEXT).click()

    """查询不存在的号码"""
    def mini_op_mine_sweep_yards_query_no_phone(self):
        # 点击输入框
        self.wait_presence_element(MINI_INPUT_MINE_SCANNING_SEARCH_EDIT_TEXT).click()
        # 输入不存在的号码
        self.wait_presence_element(MINI_INPUT_MINE_SCANNING_SEARCH_EDIT_TEXT).send_keys("111")
        # 点击查询
        self.wait_presence_element(MINI_INPUT_MINE_SCANNING_SEARCH_QUERY).click()

    """查询存在的号码"""
    def mini_op_mine_sweep_yards_query_phone(self):
        # 点击输入框
        self.wait_presence_element(MINI_INPUT_MINE_SCANNING_SEARCH_ERROR).click()
        # 清除输入框内容
        self.wait_presence_element(MINI_INPUT_MINE_SCANNING_SEARCH_ERROR).clear()
        # 输入内容
        self.wait_presence_element(MINI_INPUT_MINE_SCANNING_SEARCH_EDIT_TEXT).send_keys("17330291054")
        # 点击查询
        self.wait_presence_element(MINI_INPUT_MINE_SCANNING_SEARCH_QUERY).click()

        """查询部分微信昵称"""
    def mini_op_mine_sweep_yards_query_wei_xin(self):
        # 点击输入框
        self.wait_presence_element(MINI_INPUT_MINE_SCANNING_SEARCH_RIGHT_PHONE_NUMBER).click()
        # 清除输入框内容
        self.wait_presence_element(MINI_INPUT_MINE_SCANNING_SEARCH_RIGHT_PHONE_NUMBER).clear()
        # 查询部分微信昵称
        self.wait_presence_element(MINI_INPUT_MINE_SCANNING_SEARCH_EDIT_TEXT).send_keys("张")
        # 点击查询
        self.wait_presence_element(MINI_INPUT_MINE_SCANNING_SEARCH_QUERY).click()

    '''进入提货单页面'''
    def mini_op_mine_sweep_yards_query_pick_order(self):
        # 进入扫码提货
        self.wait_presence_element(MINI_BUTTON_MINE_PICK_UP_BY_SCANNING_CODE).click()
        # 手机/微信查询
        self.wait_presence_element(MINI_BUTTON_MINE_SCANNING_PHONE_WEI_XIN_SEARCH).click()
        # 输入手机号
        self.wait_presence_element(MINI_INPUT_MINE_SCANNING_SEARCH_EDIT_TEXT).send_keys("18501355438")
        # 点击查询
        self.wait_presence_element(MINI_INPUT_MINE_SCANNING_SEARCH_QUERY).click()
        # 点击结果
        self.wait_presence_element(MINI_BUTTON_MINE_ORDER_DETAILS_ORDER_SURE).click()


    '''进入待提货订单页面'''
    def mini_op_mine_group_buy_order_picked_up(self):
        # 点击待提货订单
        self.wait_presence_element(MINI_BUTTON_MINE_ORDER_TO_BE_PICKED_UP).click()
    '''已提走列表'''
    def order_picked_end(self):
        # 点击待提货订单
        self.wait_presence_element(MINI_BUTTON_MINE_ORDER_TO_BE_PICKED_UP).click()
        # 点击已提走
        self.wait_presence_element(MINI_BUTTON_MINE_ORDER_PICK_TAKEN_AWAY).click()
    '''手机号搜索待提货订单'''
    def order_phone_search(self):
        # 点击待提货订单
        self.wait_presence_element(MINI_BUTTON_MINE_ORDER_TO_BE_PICKED_UP).click()
        # 点击搜索输入框
        self.wait_presence_element(MINI_INPUT_MINE_ORDER_PICK_EDIT_TEXT).click()
        # 输入手机号
        self.wait_presence_element(MINI_INPUT_MINE_ORDER_PICK_EDIT_TEXT).send_keys("17330291054")

    '''手机号搜索待提货列表无订单订单'''
    def mini_op_mine_order_picked_up_phone_not_list(self):
        # 切换手机号搜索
        self.wait_presence_element(MINI_BUTTON_MINE_ORDER_PICK_PHONE_NUMBER).click()
        # 点击搜索输入框
        self.wait_presence_element(MINI_INPUT_MINE_ORDER_PICK_EDIT_TEXT).click()
        # 输入手机号
        self.wait_presence_element(MINI_INPUT_MINE_ORDER_PICK_EDIT_TEXT).send_keys("18501355438")
    '''姓名搜索待提货订单'''
    def mini_op_mine_order_picked_up_name_search(self):
        #选择姓名搜索
        self.wait_presence_element(MINI_BUTTON_MINE_ORDER_PICK_NAME).click()
        # 点击搜索输入框
        self.wait_presence_element(MINI_INPUT_MINE_ORDER_PICK_EDIT_TEXT).click()
        # 输入姓名
        self.wait_presence_element(MINI_INPUT_MINE_ORDER_PICK_EDIT_TEXT).send_keys("测试2")

    '''微信昵称搜索待提货订单'''
    def mini_op_mine_order_picked_up_wei_xin_search(self):
        #选择姓名搜索
        self.wait_presence_element(MINI_BUTTON_MINE_ORDER_PICK_WEI_XIN_NAME).click()
        # 点击搜索输入框
        self.wait_presence_element(MINI_INPUT_MINE_ORDER_PICK_EDIT_TEXT).click()
        # 输入微信昵称
        self.wait_presence_element(MINI_INPUT_MINE_ORDER_PICK_EDIT_TEXT).send_keys("jisiyu1008")

    '''售后反馈'''
    def mini_op_mine_order_picked_up_after_sales_feedback(self):
        # 点击售后反馈
        self.wait_presence_element(MINI_ELEMENT_MINE_AFTER_SALES_FEEDBACK).click()

    '''送货上门'''
    def mini_op_mine_order_picked_up_home_delivery_service(self):
        # 点击送货上门
        self.wait_presence_element(MINI_BUTTON_MINE_HOME_DELIVERY_SERVICE).click()

    '''输入运费'''
    def mini_op_mine_order_picked_up_freight_input(self):
        # 点击请输入运费框
        self.wait_presence_element(MINI_INPUT_MINE_SERVICE_EDIT_TEXT).click()
        # 输入运费价格
        self.wait_presence_element(MINI_INPUT_MINE_SERVICE_EDIT_TEXT).send_keys("1")

    '''保存运费价格'''
    def mini_op_mine_order_picked_up_freight_save(self):
        # 点击保存
        self.wait_presence_element(MINI_BUTTON_MINE_SERVICE_SAVE).click()

    '''送货预告'''
    def mini_op_mine_group_buy_delivery_notice(self):
        # 点击送货预告
        self.wait_presence_element(MINI_BUTTON_MINE_DELIVERY_NOTICE).click()

    '''佣金记录'''
    def mini_op_mine_group_buy_commission_record(self):
        # 点击佣金记录
        self.wait_presence_element(MINI_BUTTON_MINE_COMMISSION_RECORD).click()
