# coding=utf-8


import time

from elements.mini_program_elements import *
from action.base_page import BasePage


"""售后订单类"""
class MpWordOrder(BasePage):

    """订单详情跳转售后工单"""
    def order_service(self):
        # 申请售后
        self.wait_presence_element(Customer_service_list).click()


    '''售后工单添加视频'''


    def order_add_video(self):
        # 点击添加视频
        self.wait_presence_element(MINI_BUTTON_MINE_CUSTOMER_SERVICE_ADD_VIDEO).click()
        # 从相册选择
        self.wait_presence_element(MINI_BUTTON_MINE_CUSTOMER_SERVICE_CHOICE_PHOTO).click()
        # 选择视频
        self.wait_presence_element(MINI_BUTTON_MINE_CUSTOMER_SERVICE_ADD_ONE_VIDEO).click()
        # 点击完成
        self.wait_presence_element(MINI_BUTTON_MINE_CUSTOMER_SERVICE_VIDEO_FINISH).click()
        time.sleep(30)

    '''售后工单添加照片'''

    def order_add_photo(self):
        # 点击添加照片
        self.wait_presence_element(MINI_BUTTON_MINE_CUSTOMER_SERVICE_ADD_PHOTO).click()
        # 从相册选择
        self.wait_presence_element(MINI_BUTTON_MINE_CUSTOMER_SERVICE_CHOICE_PHOTO).click()
        # 选择照片
        self.wait_presence_element(MINI_BUTTON_MINE_CUSTOMER_SERVICE_ADD_PHOTO_ONE).click()
        # 点击完成
        self.wait_presence_element(MINI_BUTTON_MINE_CUSTOMER_SERVICE_PHOTO_FINISH).click()
        time.sleep(5)

    '''提交售后工单'''

    def submission_work_order(self):
        # 　点击问题描述输入框
        self.wait_presence_element(MINI_INPUT_MINE_CUSTOMER_SERVICE_PROBLEM_DESCRIPTION).click()
        # 　完善问题描述
        self.wait_presence_element(MINI_INPUT_MINE_CUSTOMER_SERVICE_PROBLEM_DESCRIPTION).send_keys("11")
        # 提交售后工单
        self.wait_presence_element(MINI_BUTTON_MINE_CUSTOMER_SERVICE_SUBMIT_TO).click()
        # 返回列表
        self.wait_presence_element(MINI_BUTTON_MINE_CUSTOMER_SERVICE_RETURN_LIST).click()
        # 点击未处理
        self.wait_presence_element(MINI_INPUT_MINE_CUSTOMER_SERVICE_UNTREATED_ORDER).click()

    '''撤销售后工单'''

    def cancel_work_order(self):
        # 点击撤销申请
        time.sleep(30)
        self.wait_presence_element(MINI_BUTTON_MINE_CUSTOMER_SERVICE_APPLICATION_ORDER).click()
        # 确定
        self.wait_presence_element(MINI_BUTTON_MINE_CUSTOMER_SERVICE_ORDER_SURE).click()

    '''申请售后工单流程'''

    def work_order(self):
        # 申请售后
        self.wait_presence_element(Customer_service_list).click()
        # 点击添加照片
        self.wait_presence_element(MINI_BUTTON_MINE_CUSTOMER_SERVICE_ADD_VIDEO).click()
        time.sleep(2)
        # 从相册选择
        self.wait_presence_element(MINI_BUTTON_MINE_CUSTOMER_SERVICE_CHOICE_PHOTO).click()
        # 选择照片
        self.wait_presence_element(MINI_BUTTON_MINE_CUSTOMER_SERVICE_ADD_ONE_VIDEO).click()
        # 点击完成
        self.wait_presence_element(MINI_BUTTON_MINE_CUSTOMER_SERVICE_PHOTO_FINISH).click()
        time.sleep(20)
        # 　点击问题描述输入框
        self.wait_presence_element(MINI_INPUT_MINE_CUSTOMER_SERVICE_PROBLEM_DESCRIPTION).click()
        # 　完善问题描述
        self.wait_presence_element(MINI_INPUT_MINE_CUSTOMER_SERVICE_PROBLEM_DESCRIPTION).send_keys("11")
        # 点击完成
        self.wait_presence_element(MINI_BUTTON_MINE_CUSTOMER_SERVICE_PROBLEM_FINISH).click()

        # 提交售后工单
        self.wait_presence_element(MINI_BUTTON_MINE_CUSTOMER_SERVICE_SUBMIT_TO).click()
        time.sleep(15)
        # 返回列表
        self.wait_presence_element(MINI_BUTTON_MINE_CUSTOMER_SERVICE_RETURN_LIST).click()
        # 点击未处理
        self.wait_presence_element(MINI_INPUT_MINE_CUSTOMER_SERVICE_UNTREATED_ORDER).click()


"""业绩中心"""
class MyPerformance(BasePage):


    """进入我的业绩页面"""
    def see_all_performance(self):

        # 进入我的业绩页面
        time.sleep(4)
        self.wait_presence_element(MINI_BUTTON_MINE_PERFORMANCE_SEE_ALL).click()

    """月账单"""
    def monthly_performance(self):
        # 点击月账单
        self.wait_presence_element(MINI_ELEMENT_MINE_PERFORMANCE_MONTHLY_BILL).click()

    """团账单"""
    def group_performance(self):
        # 点击团账单
        self.wait_presence_element(MINI_ELEMENT_MINE_PERFORMANCE_REGIMENT_BILL).click()


"""我的团购"""
class MyGroupBuy(BasePage):

    """历史开团"""
    def my_group_buy(self):
        # 点击历史开团
        self.wait_presence_element(MINI_BUTTON_MINE_HISTORICAL_OPENING).click()

    """配送跟踪"""
    def distribution_tracking(self):
        # 点击配送跟踪
        self.wait_presence_element(MINI_BUTTON_MINE_DISTRIBUTION_TRACKING).click()

    """签收码"""
    def sign_code(self):
        # 点击签收码
        self.wait_presence_element(MINI_BUTTON_MINE_SIGN_CODE).click()

    """到货提醒"""
    def arrival_reminder(self):
        # 点击到货提醒
        self.wait_presence_element(MINI_BUTTON_MINE_ARRIVAL_REMINDER).click()

    """扫码提货"""
    def sweep_yards(self):
        # 点击扫码提货
        self.wait_presence_element(MINI_BUTTON_MINE_PICK_UP_BY_SCANNING_CODE).click()

    """扫一扫"""
    def scan(self):
        # 点击扫一扫
        self.wait_presence_element(MINI_BUTTON_MINE_SCANNING_SCAN).click()

    """点击手机/微信号查询"""
    def query(self):
        # 点击手机/微信号查询
        self.wait_presence_element(MINI_BUTTON_MINE_SCANNING_PHONE_WEI_XIN_SEARCH).click()

    """查询"""
    def query_add(self):
        # 点击查询
        self.wait_presence_element(MINI_INPUT_MINE_SCANNING_SEARCH_QUERY).click()

    """点击查询输入框"""
    def query_add_p(self):
        # 点击查询输入框
        self.wait_presence_element(MINI_INPUT_MINE_SCANNING_SEARCH_EDIT_TEXT).click()

    """查询不存在的号码"""
    def query_add_a(self):
        # 点击输入框
        self.wait_presence_element(MINI_INPUT_MINE_SCANNING_SEARCH_EDIT_TEXT).click()
        # 输入不存在的号码
        self.wait_presence_element(MINI_INPUT_MINE_SCANNING_SEARCH_EDIT_TEXT).send_keys("111")
        # 点击查询
        self.wait_presence_element(MINI_INPUT_MINE_SCANNING_SEARCH_QUERY).click()

    """查询存在的号码"""
    def query_add_b(self):
        # 点击输入框
        self.wait_presence_element(MINI_INPUT_MINE_SCANNING_SEARCH_ERROR).click()
        # 清除输入框内容
        self.wait_presence_element(MINI_INPUT_MINE_SCANNING_SEARCH_ERROR).clear()
        # 输入内容
        self.wait_presence_element(MINI_INPUT_MINE_SCANNING_SEARCH_EDIT_TEXT).send_keys("17330291054")
        # 点击查询
        self.wait_presence_element(MINI_INPUT_MINE_SCANNING_SEARCH_QUERY).click()

        """查询部分微信昵称"""
    def query_add_c(self):
        # 点击输入框
        self.wait_presence_element(MINI_INPUT_MINE_SCANNING_SEARCH_RIGHT_PHONE_NUMBER).click()
        # 清除输入框内容
        self.wait_presence_element(MINI_INPUT_MINE_SCANNING_SEARCH_RIGHT_PHONE_NUMBER).clear()
        # 查询部分微信昵称
        self.wait_presence_element(MINI_INPUT_MINE_SCANNING_SEARCH_EDIT_TEXT).send_keys("张")
        # 点击查询
        self.wait_presence_element(MINI_INPUT_MINE_SCANNING_SEARCH_QUERY).click()

    '''进入提货单页面'''
    def pick_order(self):
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
    def order_picked_up(self):
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
    def order_phone_not_list(self):
        # 切换手机号搜索
        self.wait_presence_element(MINI_BUTTON_MINE_ORDER_PICK_PHONE_NUMBER).click()
        # 点击搜索输入框
        self.wait_presence_element(MINI_INPUT_MINE_ORDER_PICK_EDIT_TEXT).click()
        # 输入手机号
        self.wait_presence_element(MINI_INPUT_MINE_ORDER_PICK_EDIT_TEXT).send_keys("18501355438")
    '''姓名搜索待提货订单'''
    def order_name_search(self):
        #选择姓名搜索
        self.wait_presence_element(MINI_BUTTON_MINE_ORDER_PICK_NAME).click()
        # 点击搜索输入框
        self.wait_presence_element(MINI_INPUT_MINE_ORDER_PICK_EDIT_TEXT).click()
        # 输入姓名
        self.wait_presence_element(MINI_INPUT_MINE_ORDER_PICK_EDIT_TEXT).send_keys("测试2")

    '''微信昵称搜索待提货订单'''
    def order_wei_search(self):
        #选择姓名搜索
        self.wait_presence_element(MINI_BUTTON_MINE_ORDER_PICK_WEI_XIN_NAME).click()
        # 点击搜索输入框
        self.wait_presence_element(MINI_INPUT_MINE_ORDER_PICK_EDIT_TEXT).click()
        # 输入微信昵称
        self.wait_presence_element(MINI_INPUT_MINE_ORDER_PICK_EDIT_TEXT).send_keys("jisiyu1008")

    '''售后反馈'''
    def after_sales_feedback(self):
        # 点击售后反馈
        self.wait_presence_element(MINI_ELEMENT_MINE_AFTER_SALES_FEEDBACK).click()

    '''送货上门'''
    def home_delivery_service(self):
        # 点击送货上门
        self.wait_presence_element(MINI_BUTTON_MINE_HOME_DELIVERY_SERVICE).click()

    '''输入运费'''
    def freight(self):
        # 点击请输入运费框
        self.wait_presence_element(MINI_INPUT_MINE_SERVICE_EDIT_TEXT).click()
        # 输入运费价格
        self.wait_presence_element(MINI_INPUT_MINE_SERVICE_EDIT_TEXT).send_keys("1")

    '''保存运费价格'''
    def save(self):
        # 点击保存
        self.wait_presence_element(MINI_BUTTON_MINE_SERVICE_SAVE).click()

    '''送货预告'''
    def delivery_notice(self):
        # 点击送货预告
        self.wait_presence_element(MINI_BUTTON_MINE_DELIVERY_NOTICE).click()

    '''佣金记录'''
    def commission_record(self):
        # 点击佣金记录
        self.wait_presence_element(MINI_BUTTON_MINE_COMMISSION_RECORD).click()

"""营销工具"""
class MyMarketingTools(BasePage):

    """开团海报"""
    def opening_poster(self):
        # 点击开团海报
        self.wait_presence_element(MINI_BUTTON_MINE_MARKETING_TOOL_OPENING_POSTER).click()

    """保存海报"""
    def save_poster(self):
        time.sleep(8)
        # 保存开团海报
        self.wait_presence_element(MINI_BUTTON_MINE_MARKETING_TOOL_OPENING_POSTER_SAVE).click()

"""我的页面-管理"""
class MineManage(BasePage):

    """副团长管理"""
    def deputy_head_management(self):
        # 点击副团长管理
        self.wait_presence_element(MINI_ELEMENT_MINE_MANAGE_DEPUTY_HEAD_MANAGEMENT).click()

    """团员管理"""
    def league_member_management(self):
        # 点击团员管理
        self.wait_presence_element(MINI_ELEMENT_MINE_MANAGE_LEAGUE_MEMBER_MANAGEMENT).click()

    """确认"""
    def deputy_head_sure(self):
        # 点击确认
        self.wait_presence_element(MINI_BUTTON_MINE_ORDER_DETAILS_ORDER_TRUE).click()

    """点击添加副团长按钮"""
    def deputy_head_add(self):
        # 点击添加副团长按钮
        self.wait_presence_element(MINI_BUTTON_MINE_MANAGE_DEPUTY_HEAD_USER_ADD).click()

    """点击添加按钮"""
    def user_add(self):
        # 点击添加按钮
        self.wait_presence_element(MINI_INPUT_MINE_MANAGE_DEPUTY_HEAD_ADD).click()

    """添加团员冀思雨"""
    def user_add_jisiyu(self):
        #请输入用户id输入框
        self.wait_presence_element(MINI_INPUT_MINE_MANAGE_DEPUTY_HEAD_USER_ID).click()
        # 输入冀思雨团员id
        self.wait_presence_element(MINI_INPUT_MINE_MANAGE_DEPUTY_HEAD_USER_ID).send_keys("84182263")
        # 点击添加
        self.wait_presence_element(MINI_INPUT_MINE_MANAGE_DEPUTY_HEAD_ADD).click()
        # 点击确认
        self.wait_presence_element(MINI_BUTTON_MINE_ORDER_DETAILS_ORDER_TRUE).click()

    """添加团员刘亭亭"""
    def user_add_liutingting(self):
        # 点击冀思雨ｉｄ
        self.wait_presence_element(MINI_INPUT_MINE_MANAGE_DEPUTY_HEAD_ADD_LEAGUE_MEMBER_ID).click()
        #　清除输入框内容冀思雨id
        self.wait_presence_element(MINI_INPUT_MINE_MANAGE_DEPUTY_HEAD_ADD_LEAGUE_MEMBER_ID).clear()
        # 输入刘亭亭团员id
        self.wait_presence_element(MINI_INPUT_MINE_MANAGE_DEPUTY_HEAD_USER_ID).send_keys("83669359")
        # 点击添加按钮
        self.wait_presence_element(Mine_add_user).click()
        # 点击确认按钮
        self.wait_presence_element(MINI_BUTTON_MINE_ORDER_DETAILS_ORDER_TRUE).click()