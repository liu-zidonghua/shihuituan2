# coding=utf-8

from selenium.webdriver.common.by import By


# 登录页面
# 手机号输入框
WMS_LOGIN_TELPHONE = (By.ID,"telphone")
# 密码输入框
WMS_LOGIN_CAPTCHA = (By.ID,"captcha")
# 登录按钮##
WMS_LOGIN_BUTTEN = (By.XPATH,"/html/body/form/div/div[1]/button")
# 十荟团首页
# 定位登录的用户名   ---------和放配置文件的区别??
WMS_INDEX_LOGIN_NAME = (By.XPATH,"//span[contains(text(),'欢迎') and contains(text(),'wangdafa') ]")
# 定位商品管理
WMS_INDEX_GOODS_MANAGE = (By.XPATH,"//span[text()='商品管理']")
# 定位商品列表
WMS_INDEX_GOODS_LIST = (By.XPATH,"//span[text()='商品上架']")
####################################################################################################################################################################################
# 商品管理
# 商品上架
# 商品管理菜单按钮
WMS_COMMODITY_GOOD = (By.ID,"navi318")
# 商品上架菜单按钮
WMS_COMMODITY_SHELVES = (By.ID,"navi309")
# 添加商品按钮
WMS_COMMODITY_SHELVES_NEW =( By.XPATH,"/html[@class='no-js']/body[@class='page-sidebar-closed-hide-logo']/div[@class='page-container']/div[@class='page-content-wrapper']/div[@class='page-content']/div[@class='portlet light']/div[@class='portlet-body']/form[@id='search_form']/div[@class='row'][2]/div[@class='col-md-12 margin-bottom-10']/div[@class='form-group pull-right']/a[@class='btn btn-primary']")
# 寻味师按钮
WMS_COMMODITY_SHELVES_XUNWEI = ( By.XPATH,"/html/body/div[3]/div[2]/div/div[2]/div/form/table/tbody/tr[1]/td[2]/div/div/button/span[1]")
# 选择第一个寻味师
WMS_COMMODITY_SHELVES_XUNWEI_FIRST = ( By.XPATH,"/html/body/div[3]/div[2]/div/div[2]/div/form/table/tbody/tr[1]/td[2]/div/div/div/ul/li[2]/a")
# 商品名称输入框
WMS_COMMODITY_SHELVES_GOODS_NAME = ( By.XPATH,"/html/body/div[3]/div[2]/div/div[2]/div/form/table/tbody/tr[2]/td[2]/input")
# 商品简称输入框
WMS_COMMODITY_SHELVES_GOODS_ABBREVIATION = ( By.XPATH,"/html/body/div[3]/div[2]/div/div[2]/div/form/table/tbody/tr[3]/td[2]/input")
# 商品卖点介绍
WMS_COMMODITY_SHELVES_MAIDIAN = ( By.XPATH,"/html/body/div[3]/div[2]/div/div[2]/div/form/table/tbody/tr[6]/td[2]/input")
# 产地
WMS_COMMODITY_SHELVES_PRODUCTION = ( By.XPATH,"/html/body/div[3]/div[2]/div/div[2]/div/form/table/tbody/tr[7]/td[2]/input")
# 虚拟购买数量
# 确认按钮
WMS_COMMODITY_SHELVES_BUTTON = ( By.XPATH,"/html/body/div[3]/div[2]/div/div[2]/div/form/table/tfoot/tr/td/button")
############################################################################################################################################################################################
# 商品管理搜索特定团
# 商品上架页搜索框
WMS_COMMODITY_SHELVES_SEARCH = ( By.NAME,"search_key")
# 搜索按钮
WMS_COMMODITY_SHELVES_SEARCH_BUTTON = ( By.XPATH,"/html[@class='no-js']/body[@class='page-sidebar-closed-hide-logo']/div[@class='page-container']/div[@class='page-content-wrapper']/div[@class='page-content']/div[@class='portlet light']/div[@class='portlet-body']/form[@id='search_form']/div[@class='row'][2]/div[@class='col-md-12 margin-bottom-10']/div[@class='input-group']/div[@class='input-group-btn']/button[@class='btn btn-primary']/i[@class='fa fa-search']")
# 搜索后第一个商品的编辑按钮
WMS_COMMODITY_SHELVES_EDIT = ( By.XPATH,"//a[contains(text(),'编辑')]")
############################################################################################################################################################################################
# 封面信息标签
WMS_COMMODITY_SHELVES_FENGMIAN = ( By.XPATH,"/html/body/div[3]/div[2]/div/div[2]/div/ul/li[4]/a")
# 后台统计分类
WMS_COMMODITY_SHELVES_FENGMIAN_HOUTAI = ( By.XPATH,"/html/body/div[3]/div[2]/div/div[2]/div/form/table/tbody/tr[1]/td[2]/label[1]/input")
# 前台展示分类
WMS_COMMODITY_SHELVES_FENGMIAN_QIANTAI = ( By.XPATH,"/html/body/div[3]/div[2]/div/div[2]/div/form/table/tbody/tr[2]/td[2]/label[1]/input")
# 商品辅助分类
WMS_COMMODITY_SHELVES_FENGMIAN_FUZHU = ( By.XPATH,"/html/body/div[3]/div[2]/div/div[2]/div/form/table/tbody/tr[3]/td[2]/label[1]/input")
# 拣货分类
WMS_COMMODITY_SHELVES_FENGMIAN_JIANHUO = ( By.XPATH,"/html/body/div[3]/div[2]/div/div[2]/div/form/table/tbody/tr[4]/td[2]/label[1]/input")
# 保质期
WMS_COMMODITY_SHELVES_FENGMIAN_BAOZHIQI = ( By.NAME,"expiration_date")
# 保存方式
WMS_COMMODITY_SHELVES_FENGMIAN_BAOCUN = ( By.NAME,"saveway")
# 封面原价
WMS_COMMODITY_SHELVES_FENGMIAN_YUANJIA = ( By.NAME,"origin_price")
# 团长专属
WMS_COMMODITY_SHELVES_FENGMIAN_TUANZHANG = ( By.XPATH,"/html/body/div[3]/div[2]/div/div[2]/div/form/table/tbody/tr[9]/td[2]/input")
# 确定按钮
WMS_COMMODITY_SHELVES_FENGMIAN_BUTTEN = ( By.XPATH,"/html/body/div[3]/div[2]/div/div[2]/div/form/table/tfoot/tr/td/button")
############################################################################################################################################################################################
# 创建规格标签
# 定位创建规格tab键
WMS_EDITGOODS_GUIGETAB = (By.XPATH,"/html/body/div[3]/div[2]/div/div[2]/div/ul/li[5]/a")
# 选择主规格
WMS_EDITGOODS_GUIGE_MAIN = (By.XPATH,"//button[@data-id='attribute_id']")
# 主规格选择一级属性1
WMS_EDITGOODS_CHOOSE_GUIGE_MAIN = (By.XPATH,"//a/span[contains(text(),'一级属性1')]")
# 选择属性
WMS_EDITGOODS_GUIGE_SHUXING = (By.XPATH,"//button[@data-id='spec_id']")
# 属性选择二级属性1
WMS_EDITGOODS_CHOOSE_GUIGE_SHUXING = (By.XPATH,"//a/span[contains(text(),'二级属性1')]")
# 选择确定按钮
WMS_EDITGOODS_GUIGE_CONFIRM =(By.XPATH,"//button[@id='saveAttribute']")
# 二次确定按钮
WMS_EDITGOODS_GUIGE_TWICECONFIRM =(By.XPATH,"//div[@class='btn sure']")
############################################################################################################################################################################################
# 定位绑定SKU-tab键
WMS_EDITGOODS_SKUTAB = (By.XPATH,"//a[text()='商品绑定SKU']")
# 规格图片-点击上传按钮
WMS_EDITGOODS_SKU_UPLOADIMAGE =(By.XPATH,"//a[contains(text(),'点击上传')]")
# 选择文件
WMS_EDITGOODS_SKU_CHOOSEFILE =(By.XPATH,"//input[@id='file2upload']")
# 上传文件
WMS_EDITGOODS_SKU_UPLOADFILE =(By.XPATH,"//button[@id='btnfileupload']")
# 点击上传成功后的确定按钮
WMS_EDITGOODS_SKU_IMAGECONFIRM = (By.XPATH,"//div[@class='btn sure']")
# 输入规格名称
WMS_EDITGOODS_SKU_GUIGENAME = (By.XPATH,"//input[@name='merchtype_name[]']")
# 输入主站团购价
WMS_EDITGOODS_SKU_TUANGOUPRICE =(By.XPATH,"//input[@name='price[]']")
# 输入佣金比例
WMS_EDITGOODS_SKU_YONGJIN = (By.XPATH,"//input[@name='brokerage[]']")
# 输入预计成本
WMS_EDITGOODS_SKU_COST = (By.XPATH,"//input[@name='supplyprice[]']")
# 确定按钮
WMS_EDITGOODS_SKU_CONFIRM = (By.XPATH,"//td/button[@type='button']")
# 点击二次确定按钮
WMS_EDITGOODS_SKU_TWICECONFIRM = (By.XPATH,"//div[@class='btn sure']")
# 编辑按钮
WMS_EDITGOODS_SKU_EDITBUTTON= (By.XPATH,"//a[contains(text(),'编辑')]")
"""编辑商品页面--绑定SKU--编辑SKU"""
# 搜索ID 4134
WMS_EDITGOODS_SKU_EDITSEARCHID = (By.XPATH,"//button[@data-id='js-skuid-select']")
# 搜索输入4134
WMS_EDITGOODS_SKU_EDITINPUTID = (By.XPATH,"//input[@class='form-control']")
# 选择4134
WMS_EDITGOODS_SKU_EDITCHOOSEID =(By.XPATH,"//a/span[contains(text(),'4134')]")
# 点击添加按钮
WMS_EDITGOODS_SKU_EDITADD = (By.XPATH,"//a[contains(text(),'添加')]")
# 保存按钮
WMS_EDITGOODS_SKU_EDITSAVE = (By.XPATH,"//button[@id='saveBtn']")
# 点击二次确定按钮
WMS_EDITGOODS_SKU_EDITCONFIRM = (By.XPATH,"//div[@class='btn sure']")
# #######################################################################################################################################################################################################
# 商品属性
# 商品属性
WMS_COMMODITY_SHELVES_ATTRIBUTES = ( By.ID,"navi347")
# 搜索框
WMS_COMMODITY_SHELVES_ATTRIBUTES_SEARCH = ( By.ID,"search_key")
# 搜索按钮
WMS_COMMODITY_SHELVES_ATTRIBUTES_SEARCHBUTTEN = ( By.XPATH,"//*[@id=""search_form""]/div[1]/div/div[2]/button")
# 新增属性
WMS_COMMODITY_SHELVES_ATTRIBUTES_ADD = ( By.XPATH,"//a[text()='新增属性']")
# 新增子属性
WMS_COMMODITY_SHELVES_ATTRIBUTES_ADDSON = ( By.XPATH,"//*[@id=""search_form""]/table/tbody/tr[1]/td[9]/a[1]")
# 停用
WMS_COMMODITY_SHELVES_ATTRIBUTES_STOP = ( By.XPATH,"//a[text()='停用']")
# 确认停用
WMS_COMMODITY_SHELVES_ATTRIBUTES_STOP_Y = ( By.XPATH,"/html/body/div[5]/div/div/div[2]/div")
# 取消停用#
WMS_COMMODITY_SHELVES_ATTRIBUTES_STOP_N = ( By.XPATH,"/html/body/div[5]/div/div/div[1]/div")
# 编辑
WMS_COMMODITY_SHELVES_ATTRIBUTES_BIANJI = ( By.XPATH,"//*[@id=""search_form""]/table/tbody/tr[1]/td[9]/a[3]")
# 删除
WMS_COMMODITY_SHELVES_ATTRIBUTES_DEL = ( By.XPATH,"//*[@id=""search_form""]/table/tbody/tr[1]/td[9]/a[4]")
# 启用
WMS_COMMODITY_SHELVES_ATTRIBUTES_START = (By.XPATH,"//a[text()='启用']")
# 规格名称
WMS_COMMODITY_SHELVES_ATTRIBUTES_NAME = ( By.XPATH,"//*[@id=""search_form""]/table/tbody/tr[1]/td[2]/a[2]")
# 属性名称
WMS_COMMODITY_SHELVES_ATTRIBUTES_ADD_NAME = ( By.XPATH,"//*[@id=""form""]/table/tbody/tr[2]/td[2]/input")
# 显示排序
WMS_COMMODITY_SHELVES_ATTRIBUTES_SORT = ( By.NAME,"rank")
# 确定按钮
WMS_COMMODITY_SHELVES_ATTRIBUTES_BUTTEN = ( By.XPATH,"/html/body/div[3]/div[2]/div/div[2]/div/form/table/tfoot/tr/td/button")
# #######################################################################################################################################################################################################
# 站点设置
WMS_SITE_ENTER = ( By.ID,"navi474")
# 搜索按确定按钮
WMS_SITE_SEARCH = ( By.CSS_SELECTOR,".btn-primary")
WMS_SITE_SEARCH_ZHU = ( By.ID,"warehousesite_id_label")
# 关闭按钮
WMS_SITE_CLOSE = ( By.XPATH,"//a[text()='关闭']")
# 开启
WMS_SITE_START = ( By.XPATH,"//a[text()='开启']")
# 编辑按钮
WMS_SITE_EDIT = ( By.XPATH,"//a[text()='编辑']")
# 查看按钮
WMS_SITE_SEE = ( By.XPATH,"//a[text()='查看']")
# 查看-取消
WMS_SITE_SEE_EXIT = ( By.CSS_SELECTOR,"div.modal-footer:nth-child(3) > button:nth-child(1)]")
# 二次确认
WMS_SUTE_SURE = ( By.CSS_SELECTOR,".sure")
# 二次取消
WMS_SUTE_EXIT = ( By.CSS_SELECTOR,".exit")
# 编辑-排序
WMS_SITE_EDIT_SORT = ( By.CSS_SELECTOR,".table > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(5) > input:nth-child(1)")
# 编辑-修改
WMS_SITE_EDIT_UPDATE = ( By.XPATH,"//a[text()='修改']")
# 编辑-上线
WMS_SITE_EDIT_ONL = ( By.XPATH,"//a[text()='上线']")
# 编辑-下线#
WMS_SITE_EDIT_OFFL = ( By.XPATH,"//a[text()='下线']")
# #######################################################################################################################################################################################################
#进入金刚页面
WMS_DISMOND_ENTER = ( By.ID,"navi475")
# 金刚页面搜索框
WMS_DISMOND_SEARCH = ( By.CSS_SELECTOR,"input.form-control:nth-child(2)")
# 搜索按钮
WMS_DISMOND_SEARCH_BTN= ( By.ID,"searchBtn")
# 新建金刚
WMS_DISMOND_ADD = ( By.XPATH,"//a[text()='新建金刚']")
# 上线按钮
WMS_DISMOND_ON_LINE = ( By.XPATH,"//a[text()='上线']")
# 下线按钮
WMS_DISMOND_OFF_LINE = ( By.XPATH,"//a[text()='下线']")
# 编辑按钮
WMS_DISMOND_EDIT = ( By.XPATH,"//a[text()='编辑']")
# 金刚名称
WMS_DISMOND_NAME = ( By.CSS_SELECTOR,"#kingkong-title")
# 上传图片按钮
WMS_DISMOND_UPPIC = ( By.XPATH,"//a[text()='上传图片']")
# 选图按钮
WMS_DISMOND_SEARCHPIC = ( By.ID,"file2upload")
# 上传文件
WMS_DISMOND_UPDATA = ( By.ID,"btnfileupload")
# 取消上传按钮
WMS_DISMOND_UPDATA_N = ( By.CSS_SELECTOR,"#qcloud_uploader_modal > div:nth-child(2) > div:nth-child(1) > div:nth-child(3) > button:nth-child(1)")
# 关联分类
WMS_DISMOND_RELATION = ( By.ID,"kingkong-classification-pintor")
# 选择分类
WMS_DISMOND_SEARCH_RELATION = ( By.CSS_SELECTOR,"#add_starttime > label:nth-child(1) > input:nth-child(1)")
# 分类保存按钮
WMS_DISMOND_PRESERVATION = ( By.NAME,"myloadding")
# 排序
WMS_DISMOND_SORT = ( By.ID,"kingkong-rank")
# 新建金刚保存按钮
WMS_DISMOND_ADD_Y = ( By.NAME,"myloadding")
# 新建金刚取消按钮#
WMS_DISMOND_ADD_N = ( By.ID,"navi475")
## #######################################################################################################################################################################################################
# 售价控制
# 站点售价控制
WMS_PRICE_CONTROL  = ( By.ID,"navi355")
# 新增按钮
WMS_PRICE_CONTROL_ADD = ( By.XPATH,"//a[text()=' 新增']")
# 编辑
WMS_PRICE_CONTROL_BIANJI = ( By.XPATH,"/html/body/div[3]/div[2]/div/div[2]/div/form/table/tbody/tr[1]/td[11]/a[1]")
# 失效按钮
WMS_PRICE_CONTROL_INVALID = ( By.XPATH,"/html/body/div[3]/div[2]/div/div[2]/div/form/table/tbody/tr[1]/td[11]/a[2]")
# 团长佣金返利倍数
WMS_PRICE_CONTROL_AMOUNT_RATIO = ( By.NAME,"amount_ratio")
# 营销费占比
WMS_PRICE_CONTROL_MARK_COST_PROPORTION = ( By.NAME,"mark_cost_proportion")
# 仓配费占比
WMS_PRICE_CONTROL_RATIO_WAREHOUSE_PROPORTION = ( By.NAME,"ratio_warehouse_proportion")
# 经营利润占比
WMS_PRICE_CONTROL_PROFIT_PROPORTION = ( By.NAME,"profit_proportion")
# 确认按钮
WMS_PRICE_CONTROL_ADD_Y = ( By.ID,"sub")
#取消按钮 #
WMS_PRICE_CONTROL_ADD_N = ( By.ID,"cancel_btn")
# #######################################################################################################################################################################################################
# 团购管理
# 团购管理
WMS_GROUP = ( By.ID,"navi464")
# 开团管理
WMS_OPEN_GROUP = ( By.ID,"navi199")
# 新建团购
WMS_OPEN_GROUP_ADD = ( By.XPATH,"//button[@onclick='editgroupon()']")
# 开团时间  05:25:00
WMS_OPEN_GROUP_ADD_START = ( By.CSS_SELECTOR,"#add_starttime > input:nth-child(1)")
# 截团时间  2019-09-19 10:30:13
WMS_OPEN_GROUP_ADD_END = ( By.CSS_SELECTOR,"#add_endtime > input:nth-child(1)")
# 团购介绍
WMS_OPEN_GROUP_ADD_JIESHAO = ( By.NAME,"groupon_title")
# 保存
WMS_OPEN_GROUP_ADD_BAOCUN = ( By.CSS_SELECTOR,"div.modal-footer:nth-child(4) > button:nth-child(2)")
WMS_OPEN_GROUP_ADD_S = ( By.NAME,"groupon_id")
WMS_OPEN_GROUP_ADD_OPEN = ( By.XPATH,"/html/body/div[3]/div[2]/div/div[2]/div/form/div/div/div[3]/select/option[last()]")
# 取消
WMS_OPEN_GROUP_ADD_QUXIAO = ( By.XPATH,"//*[@id=""add_groupon_modal""]/div[2]/div/form/div[2]/button[1]")
# 复制团购
WMS_OPEN_GROUP_ADD_COPY = ( By.XPATH,"/html/body/div[3]/div[2]/div/div[2]/div/div[1]/div/div/button[1]")
# 停团
WMS_OPEN_GROUP_ADD_STOP = ( By.ID,"stopgroupon")
# 关联活动
WMS_OPEN_GROUP_ADD_RELEVANCE = ( By.XPATH,"/html/body/div[3]/div[2]/div/div[2]/div/span[2]/a")
# 编辑
WMS_OPEN_GROUP_ADD_EDIT = ( By.CSS_SELECTOR,"a.btn-xs:nth-child(2)")
# 选择商品
WMS_OPEN_GROUP_ADD_XUANZE = ( By.CSS_SELECTOR,".filter-option")
# 商品搜索框
WMS_OPEN_GROUP_ADD_SEARCH = ( By.CSS_SELECTOR,".bs-searchbox > input:nth-child(1)")
#选择搜索结果中第一个商品
WMS_OPEN_GROUP_ADD_SEARCHFIRST = ( By.CSS_SELECTOR,".inner > li:nth-child(1) > a:nth-child(1)")
# 添加按钮
WMS_OPEN_GROUP_ADD_ADD = ( By.XPATH,"/html/body/div[3]/div[2]/div/div[2]/div/div[2]/div/a")
# 一键保存
WMS_OPEN_GROUP_ADD_ONESAVE = ( By.ID,"one-click-save")
# 一键起售
WMS_OPEN_GROUP_ADD_ONESALE = ( By.ID,"one-click-sale")
# 送货时间
WMS_OPEN_GROUP_ADD_TIME = ( By.NAME,"deliveryday[]")
# 生产日期
WMS_OPEN_GROUP_ADD_PRODUCE = ( By.NAME,"produce_day[]")
# 最大售卖
WMS_OPEN_GROUP_ADD_MAX = ( By.XPATH,"//*[@id=""contents""]/tr/td[11]/input")
# 限购数量5
WMS_OPEN_GROUP_ADD_LIMIT = ( By.XPATH,"//*[@id=""contents""]/tr/td[13]/input")
# 售卖区域及价格
WMS_OPEN_GROUP_ADD_QUYU = ( By.ID,"one-click-sale")
# 排序
WMS_OPEN_GROUP_ADD_RANK = ( By.NAME,"rank[]")
# 不可用券
WMS_OPEN_GROUP_ADD_COUPON = ( By.XPATH,"//*[@id=""contents""]/tr/td[19]/input")
# 保存
WMS_OPEN_GROUP_ADD_SALE = ( By.NAME,"save")
#一键保存
#一键起售
#起售
#保存
# #######################################################################################################################################################################################################
# 订单管理
WMS_ORDER1 = ( By.ID,"navi171")
# 查看订单
WMS_ORDER_SEE= ( By.ID,"navi307")
# 团长ID
WMS_ORDER_USERID = ( By.NAME,"userid")
# 团购ID
WMS_ORDER_GROUPONID = ( By.NAME,"grouponid")
# 用户ID
WMS_ORDER_USERIDSINGLE = ( By.NAME,"useridsingle")
# 搜索框
WMS_ORDER_SEARCHCONTENT = ( By.NAME,"searchcontent")
WMS_ORDER_SEARCH_BUT = ( By.XPATH,"//button[@title='搜索']")
# #######################################################################################################################################################################################################
#营销管理
WMS_MARKETING = ( By.ID,"navi324")
# 优惠券
WMS_COUPON1  = ( By.ID,"navi311")
# 标题搜索框
WMS_COUPON_SEARCH  = ( By.NAME,"title")
# 搜索按钮
WMS_COUPON_SEARCH_BUT  = ( By.XPATH,"//*[@id=""search_form""]/div/div/div[2]/div/button/i")
# 添加优惠券
WMS_COUPON_ADDS  = ( By.XPATH,"//a[contains(text(),'添加优惠券')]")
# 标题
WMS_COUPON_ADD_TIT = ( By.XPATH,"/html/body/div[3]/div[2]/div/div[2]/div/form/table/tbody[1]/tr[1]/td[2]/input")
# 备注
WMS_COUPON_ADD_REMARK  = ( By.XPATH,"/html/body/div[3]/div[2]/div/div[2]/div/form/table/tbody[1]/tr[2]/td[2]/input")
# ###发放主站
####Coupon_Add  = ( By.XPATH,"//*[@id=""search_form""]/div/div/div[3]")
# 优惠券类型
# 通用券
WMS_COUPON_ADD_CURRENCY  = ( By.XPATH,"/html/body/div[3]/div[2]/div/div[2]/div/form/table/tbody[1]/tr[4]/td[2]/label[1]/input")
# 新人券
WMS_COUPON_ADD_NEW  = ( By.XPATH,"/html/body/div[3]/div[2]/div/div[2]/div/form/table/tbody[1]/tr[4]/td[2]/label[2]/input")
# 品类券
WMS_COUPON_ADD_CATEGORY  = ( By.XPATH,"/html/body/div[3]/div[2]/div/div[2]/div/form/table/tbody[1]/tr[4]/td[2]/label[3]/input")
# 社区券
WMS_COUPON_ADD_COMMUNITY  = ( By.XPATH,"/html/body/div[3]/div[2]/div/div[2]/div/form/table/tbody[1]/tr[4]/td[2]/label[4]/input")
# 单品券
WMS_COUPON_ADD_SINGLE  = ( By.XPATH,"/html/body/div[3]/div[2]/div/div[2]/div/form/table/tbody[1]/tr[4]/td[2]/label[5]/input")
# 数量
WMS_COUPON_ADD_NUM  = ( By.XPATH,"/html/body/div[3]/div[2]/div/div[2]/div/form/table/tbody[1]/tr[5]/td[2]/input")
# 抵扣金额
WMS_COUPON_ADD_MONEY  = ( By.XPATH,"/html/body/div[3]/div[2]/div/div[2]/div/form/table/tbody[1]/tr[6]/td[2]/input")
# 重复领取
WMS_COUPON_ADD_REPEAT_Y  = ( By.XPATH,"/html/body/div[3]/div[2]/div/div[2]/div/form/table/tbody[1]/tr[7]/td[2]/div/label[1]/input")
WMS_COUPON_ADD_REPEAT_N  = ( By.XPATH,"/html/body/div[3]/div[2]/div/div[2]/div/form/table/tbody[1]/tr[7]/td[2]/div/label[2]/input")
# 启用金额
WMS_COUPON_ADD_AMOUNT  = ( By.XPATH,"/html/body/div[3]/div[2]/div/div[2]/div/form/table/tbody[2]/tr[1]/td[2]/div/label/input")
# 使用有效期
WMS_COUPON_ADD_VALIDTYPE  = ( By.ID,"dateday")
#有效期天数
WMS_COUPON_ADD_VALIDTYPE_DAY = (By.NAME,"coupon[validday]")
# 确定按钮
WMS_COUPON_ADD_BUT  = ( By.ID,"submit")
#发放优惠券按钮
WMS_COUPON_ADD_GRANT = ( By.XPATH,"//a[contains(text(),'发放优惠券')]")
#发送用户ID
WMS_COUPON_ADD_GRANT_USERID = ( By.CSS_SELECTOR,"#send_form > table > tbody > tr:nth-child(1) > td:nth-child(2) > textarea")
# faf
WMS_COUPON_DEAL_GRANT = (By.XPATH,"//a[contains(text(),'发放优惠券')]")
#发送数量
WMS_COUPON_ADD_GRANT_NUM = (By.NAME,"num")
#发送按钮
WMS_COUPON_ADD_GRANT_SEND = (By.CSS_SELECTOR,"#send_form > table > tfoot > tr > td > button")
# 添加数量
WMS_COUPON_ADD_NUM  = (By.XPATH,"//*[@id=""adminlist""]/tbody/tr[1]/td[13]/a[1]")
# 增加优惠券数量
WMS_COUPON_NUM  = (By.NAME,"couponnum")
# 确定按钮
WMS_COUPON_NUM_Y = (By.XPATH,"//*[@id=""couponnum""]/div[2]/div/div[3]/button[1]")
# 取消按钮
WMS_COUPON_NUM_N = (By.XPATH,"//*[@id=""couponnum""]/div[2]/div/div[3]/button[2]")
# 开始
WMS_COUPON_DEAL_ACTION = (By.XPATH,"//a[contains(text(),'启动')]")
# 开始二次确认
WMS_COUPON_DEAL_ACTION_Y = (By.CSS_SELECTOR,"body > div.myModa > div > div > div:nth-child(2) > div")
# 三次确认
WMS_COUPON_DEAL_ACTION_3= (By.CSS_SELECTOR,"body > div.myModa > div > div")
WMS_COUPON_DEAL_ACTION_N = (By.XPATH,"/html/body/div[5]/div/div/div[1]/div")
# 删除
WMS_COUPON_DEAL_DEL = (By.XPATH,"//a[contains(text(),'删除')]")
# 停止
WMS_COUPON_STOP = (By.XPATH,"//*[@id=""adminlist""]/tbody/tr[1]/td[13]/a[2]")
# 停止二次确认
WMS_COUPON_STOP_Y = (By.XPATH,"/html/body/div[5]/div/div/div[2]/div")
WMS_COUPON_STOP_N = (By.XPATH,"/html/body/div[5]/div/div/div[1]/div")
# 复制
WMS_COUPON_COPY = (By.XPATH,"//a[contains(text(),'复制')]")
# 编辑
WMS_COUPON_BIANJI = (By.XPATH,"//*[@id=""adminlist""]/tbody/tr[1]/td[13]/a[4]")
# 标题
WMS_COUPON_BIANJI_TIT = (By.XPATH,"/html/body/div[3]/div[2]/div/div[2]/div/form/table/tbody/tr[1]/td[2]/input")
# 备注#
WMS_COUPON_BIANJI_BEIZHU  = (By.XPATH,"/html/body/div[3]/div[2]/div/div[2]/div/form/table/tbody/tr[2]/td[2]/input[1]")
# 活动管理
WMS_ACTIVITY = (By.XPATH,"//*[@id=""adminlist""]/tbody/tr[1]/td[13]/a[3]")
# 活动名称输入输入框
WMS_ACTIVITY_SERCH = (By.XPATH,"//*[@id=""search_form""]/div/div/div[1]/input")
# 活动名称搜索按钮
WMS_ACTIVITY_SERCH_BUT = (By.XPATH,"//*[@id=""search_form""]/div/div/div[1]/div/button/i")
# 添加活动
WMS_ACTIVITY_ADD = (By.XPATH,"//*[@id=""search_form""]/div/div/div[2]/a")
# 启动??????????
WMS_ACTIVITY_START = (By.XPATH,"//*[@id=""adminlist""]/tbody/tr[1]/td[13]/a[3]")
# 停止???????????
WMS_ACTIVITY_STOP = (By.XPATH,"//*[@id=""adminlist""]/tbody/tr[1]/td[13]/a[3]")
# 编辑????????????
WMS_ACTIVITY_BIANJI = (By.XPATH,"//*[@id=""adminlist""]/tbody/tr[1]/td[13]/a[3]")
# 天降红包
WMS_RED_ENVELOPES1 = (By.ID,"navi467")
# 活动时间
WMS_RED_ENVELOPES_ACTIVITY_TIME = (By.NAME,"activity_time")
# 活动名称
WMS_RED_ENVELOPES_ACTIVITY_NAME = (By.NAME,"activity_name")
# 活动ID
WMS_RED_ENVELOPES_SKYWARD_REWARD_ID = (By.NAME,"skyward_reward_id")
# 创建人
WMS_RED_ENVELOPES_CREATE_NAME = (By.NAME,"create_name")
# 创建时间
WMS_RED_ENVELOPES_CREATE_TIME = (By.NAME,"create_time")
# 查询
WMS_RED_ENVELOPES_SEARCHBTN = (By.ID,"searchBtn")
# 查看
WMS_RED_ENVELOPES_SEE = (By.XPATH,"//*[@id=""adminlist""]/tbody/tr[1]/td[10]/a[1]")
# 下线
WMS_RED_ENVELOPES_UP = (By.XPATH,"//*[@id=""adminlist""]/tbody/tr[1]/td[10]/a[2]")
# 复制
WMS_RED_ENVELOPES_COPY = (By.XPATH,"//*[@id=""adminlist""]/tbody/tr[1]/td[10]/a[3]")
# 数据
WMS_RED_ENVELOPES_COUPONDATA = (By.XPATH,"//*[@id=""adminlist""]/tbody/tr[1]/td[10]/a[4]")
# 新建
WMS_RED_ENVELOPES_ADD = (By.XPATH,"//a[@onclick='add()']")
# 活动名称
WMS_RED_ENVELOPES_ADD_ACTIVITY_NAME  = (By.XPATH,"/html/body/div[3]/div[2]/div/div[2]/div/form/table/tbody/tr[1]/td[2]/input")
# 添加券
WMS_RED_ENVELOPES_ADD_COUPON_IDS  = (By.XPATH,"/html/body/div[3]/div[2]/div/div[2]/div/form/table/tbody/tr[6]/td[2]/input")
# 校验
WMS_RED_ENVELOPES_ADD_CHECKCOUPON  = (By.ID,"checkcoupon")
WMS_RED_ENVELOPES_ADD_CHECKCOUPON_Y = (By.XPATH,"/html/body/div[8]/div/div")
# 确定#
WMS_RED_ENVELOPES_ADD_SUBMIT  = (By.XPATH,"//button[@id='submit']")
# 秒杀管理
WMS_KILL_ENTER = (By.ID,"navi329")
# 新建秒杀
WMS_KILL_ADD = (By.CSS_SELECTOR,".fa-plus")
# 秒杀开始时间
WMS_KILL_STARTTIME = (By.CSS_SELECTOR,"#add_starttime > input:nth-child(1)")
# 秒杀结束时间
WMS_KILL_ENDTIME = (By.CSS_SELECTOR,"#add_endtime > input:nth-child(1)")
# 保存
WMS_KILL_SAVE = (By.ID,"save_seckill")
# 编辑
WMS_KILL_EDIT = (By.ID,"edit_merchandise")
# 选择商品
WMS_KILL_CHOOSE = (By.CSS_SELECTOR,".filter-option")
# 搜索输入框
WMS_KILL_SEARCH = (By.CSS_SELECTOR,".bs-searchbox > input:nth-child(1)")
# 选定商品
WMS_KILL_CHOOSE_SURE = (By.CSS_SELECTOR,".inner > li:nth-child(1) > a:nth-child(1) > span:nth-child(1)")
# 添加按钮
WMS_KILL_ADDTO = (By.XPATH,"//a[contains(text(),'添加')]")
# 上传
WMS_KILL_UP = (By.XPATH,"//a[contains(text(),'上传')]")
# 选择图片
WMS_KILL_BROW = (By.ID,"file2upload")
# 上传文件
WMS_KILL_UPFILE = (By.CSS_SELECTOR,"#btnfileupload")
# 送货时间
WMS_KILL_SENDTIME = (By.CSS_SELECTOR,".merchandiseid_22 > td:nth-child(8) > input:nth-child(1)")
# 选择送货时间
WMS_KILL_SENDTIME_CHOOSE = (By.CSS_SELECTOR,".datetimepicker-days > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(5) > td:nth-child(7)")
# 保存
WMS_KILL_EDIT_SURE = (By.ID,"one-click-save")
# 修改
WMS_KILL_UPDATE = (By.XPATH,"//a[contains(text(),'修改')]")
# 秒杀详情
WMS_KILL_DETAILS  = (By.CSS_SELECTOR,".page-breadcrumb > li:nth-child(2) > a:nth-child(1) > samp:nth-child(1)")
# 启售
WMS_KILL_START = (By.XPATH,"//a[contains(text(),'启售')]")
WMS_KILL_START_SURE = (By.CSS_SELECTOR,"div.btn")
# 起售div.btn
WMS_KILL_ALLSTART = (By.XPATH,"//a[contains(text(),'起售')]")
WMS_KILL_ALLSTART_SURE = (By.CSS_SELECTOR,".sure")
# 停售
# 全部停售
# #######################################################################################################################################################################################################
# 出库管理
WMS_OUT_STOCK1 = (By.ID,"navi460")
# 波次统计
WMS_WAVE_STATISTICS = (By.ID,"navi471")
# 发起拣货开始时间
WMS_WAVE_STATISTICS_STARTTIME = (By.NAME,"starttime")
# 发起拣货结束时间
WMS_WAVE_STATISTICS_ENDTIME = (By.NAME,"endtime")
# 查询按钮
WMS_WAVE_STATISTICS_SEARCH = (By.XPATH,"//button[@value='search']")
# 导出按钮#
WMS_WAVE_STATISTICS_EXPORT = (By.XPATH,"//button[@value='export']")
# #######################################################################################################################################################################################################
# 客服工单#
WMS_SERVICE_WORK = (By.ID,"navi343")
# 工单列表
WMS_SERVICE_WORK_LIST = (By.ID,"navi344")
# 第一个搜索框
WMS_SERVICE_WORK_LIST_SEARCHCONTENT1 = (By.ID,"searchcontent1")
# 第二个搜索框
WMS_SERVICE_WORK_LIST_SEARCHCONTENT2 = (By.ID,"searchcontent2")
# 搜索按钮#
WMS_SERVICE_WORK_ACTION = (By.NAME,"action")
# 售后统计
WMS_SERVICE_WORK_STATISTICS = (By.ID,"navi346")
# 第一个搜索框
WMS_SERVICE_WORK_STATISTICS_SEARCHCONTENT1 = (By.ID,"searchcontent1")
# 第二个搜索框
WMS_SERVICE_WORK_STATISTICS_SEARCHCONTENT2 = (By.ID,"searchcontent2")
# 搜索按钮
WMS_SERVICE_WORK_STATISTICS_SEARCH = (By.XPATH,"//*[@id=""search_form""]/div[3]/div/button[1]/i")
# 导出
WMS_SERVICE_WORK_STATISTICS_EXPORT = (By.XPATH,"//*[@id=""search_form""]/div[3]/div/button[2]")
# 批改责任归属#
WMS_SERVICE_WORK_STATISTICS_MODIFY = (By.XPATH,"//*[@id=""search_form""]/div[3]/div/span")
# 售后审核
WMS_SERVICE_WORK_EXAMINE = (By.ID,"navi358")
# 第一个搜索框
WMS_SERVICE_WORK_EXAMINE_SEARCHCONTENT1 = (By.ID,"searchcontent1")
# 第二个搜索框
WMS_SERVICE_WORK_EXAMINE_SEARCHCONTENT2 = (By.ID,"searchcontent2")
# 搜索按钮
WMS_SERVICE_WORK_EXAMINE_SEARCH = (By.XPATH,"//*[@id=""search_form""]/div[3]/div/button[1]/i")
# #######################################################################################################################################################################################################
# 数据报表
WMS_REPORTS = (By.ID,"navi312")
# 团购报表
WMS_REPORTS_GROUP = (By.ID,"searchcontent2")
# 确认按钮
WMS_REPORTS_GROUP_SEARCHBTN = (By.ID,"searchBtn")
# 导出
WMS_REPORTS_GROUP_EXPORT_BTN = (By.ID,"export_btn")
# 商品报表
WMS_REPORTS_GOOD = (By.ID,"navi314")
# 搜索框
WMS_REPORTS_GOOD_SEARCH_KEY = (By.NAME,"search_key")
# 确认按钮
WMS_REPORTS_GOOD_SEARCHBTN = (By.ID,"searchBtn")
# 导出
WMS_REPORTS_GOOD_EXPORT_BTN = (By.ID,"export_btn")
# 团长销量统计
WMS_REPORTS_SALES = (By.ID,"navi315")
# 搜索框
WMS_REPORTS_SALES_SEARCH_KEY = (By.NAME,"search_key")
# 确认按钮
WMS_REPORTS_SALES_SEARCHBTN = (By.ID,"searchBtn")
# 导出
WMS_REPORT_SALES_EXPORT_BTN = (By.ID,"export_btn")
# 漏发记录
WMS_REPORTS_MISSING = (By.ID,"navi472")
# 搜索框
WMS_REPORTS_MISSING_SEARCH_KEY = (By.NAME,"search_key")
# 确认按钮
WMS_REPORTS_MISSING_SEARCHBTN = (By.ID,"searchBtn")
# #######################################################################################################################################################################################################
# 系统管理
WMS_SYSTEM = (By.ID,"navi2")
# 角色管理
WMS_SYSTEM_ROLE = (By.ID,"navi316")
# 团长管理
WMS_SYSTEM_ROLE_HEADS = (By.ID,"navi308")
# 搜索框
WMS_SYSTEM_ROLE_HEADS_SEARCH_KEY  = (By.NAME,"search_key")
# 搜索按钮
WMS_SYSTEM_ROLE_HEADS_BUTTEN  = (By.XPATH,"//*[@id=""search_form""]/div[2]/div/div[3]/button")
# 未启用团长################
# 查看副团长
WMS_SYSTEM_ROLE_HEADS_VICE  = (By.XPATH,"//*[@id=""adminlist""]/tbody/tr/td[14]/a[1]")
# 提现
WMS_SYSTEM_ROLE_HEADS_WITHDRAWAL  = (By.XPATH,"//*[@id=""adminlist""]/tbody/tr/td[14]/a[2]")
# 停用
WMS_SYSTEM_ROLE_HEADS_STOP  = (By.XPATH,"//*[@id=""adminlist""]/tbody/tr/td[14]/a[3]")
# 开启
WMS_SYSTEM_ROLE_HEADS_START  = (By.XPATH,"//*[@id=""adminlist""]/tbody/tr/td[14]/a[4]")
# 详情
WMS_SYSTEM_ROLE_HEADS_DETAILS = (By.XPATH,"//*[@id=""adminlist""]/tbody/tr/td[14]/a[5]")
### 详情 ###
# 同步
WMS_SYSTEM_ROLE_HEADS_SYNCHRONIZATION  = (By.XPATH,"/html/body/div[3]/div[2]/div/div[2]/div/table[1]/thead/tr/th/div/button[1]")
# 提现余额
WMS_SYSTEM_ROLE_HEADS_WITHDRAWAL_A  = (By.XPATH,"/html/body/div[3]/div[2]/div/div[2]/div/table[1]/thead/tr/th/div/button[2]")
# 停用
WMS_SYSTEM_ROLE_HEADS_STOP_A = (By.XPATH,"/html/body/div[3]/div[2]/div/div[2]/div/table[1]/thead/tr/th/div/button[3]")
# 开启
WMS_SYSTEM_ROLE_HEADS_START_A  = (By.XPATH,"/html/body/div[3]/div[2]/div/div[2]/div/table[1]/thead/tr/th/div/button[4]")
# 编辑
WMS_SYSTEM_ROLE_HEADS_BIANJI  = (By.XPATH,"/html/body/div[3]/div[2]/div/div[2]/div/table[1]/thead/tr/th/div/button[5]")
# 团长统计查看
WMS_SYSTEM_ROLE_HEADS_STATISTICS  = (By.XPATH,"/html/body/div[3]/div[2]/div/div[2]/div/table[1]/tbody/tr[3]/td[2]/a")
# 团长收益查看
WMS_SYSTEM_ROLE_HEADS_PROFIT  = (By.XPATH,"/html/body/div[3]/div[2]/div/div[2]/div/table[1]/tbody/tr[8]/td[2]/a")
# 提现记录查看
WMS_SYSTEM_ROLE_HEADS_WITHDRAWAL_1  = (By.XPATH,"/html/body/div[3]/div[2]/div/div[2]/div/table[1]/tbody/tr[9]/td[4]/a")
# 配送小区添加
WMS_SYSTEM_ROLE_HEADS_ADD  = (By.ID,"navi472")
# 配送小区同步#
WMS_SYSTEM_ROLE_HEADS_SYNCHRONIZATION_2  = (By.ID,"navi472")
# 启用团长################
# 查看副团长
WMS_SYSTEM_ROLE_HEADS_VICE2  = (By.XPATH,"//*[@id=""adminlist""]/tbody/tr/td[14]/a[1]")
# 关闭团长
WMS_SYSTEM_ROLE_HEADS_CLOSE  = (By.XPATH,"//*[@id=""adminlist""]/tbody/tr/td[14]/a[2]")
# 详情
WMS_SYSTEM_ROLE_HEADS_DETAILS2  = (By.XPATH,"//*[@id=""adminlist""]/tbody/tr/td[14]/a[3]")
#角色管理
WMS_CHARACTER = (By.ID,"navi316")
#团长管理
WMS_CHARACTER_TUANZHANG =( By.ID,"navi308")
#搜索框
WMS_CHARACTER_SEARCH =( By.NAME,"search_key")
#搜索条件
WMS_CHARACTER_SEARCH_CONDITION =( By.ID,"searchfield")
#搜索项
WMS_CHARACTER_SEARCH_TERM =( By.XPATH,"//*[@id=""searchfield""]/option[4]")
#搜索按钮
WMS_CHARACTER_SEARCH_BUTTEN =( By.XPATH,"//*[@id=""search_form""]/div[3]/div/div/div[1]/div/button")
# 商品列表页面
# 定位主站-辽宁省
WMS_CHOOSE_ZHUZHAN = (By.XPATH,"//a[contains(text(),'辽宁省')]")
# 定位分类-水果分类
WMS_CHOOSE_FENLEI = (By.XPATH,"//a[contains(text(),'水果分类')]")
# 定位添加商品按钮
WMS_ADD_GOODS = (By.XPATH,"//a[@class='btn btn-primary' and contains(@href,'add')]")
# 添加商品页面
# 定位寻味师
WMS_XUNWEISHI_ELE = (By.XPATH,"//div/label[contains(text(),'范桂萍')]")
# 定位商品名称输入框
WMS_GOODS_NAME = (By.XPATH,"//input[@name='title']")
# 定位商品简称输入框
WMS_GOODS_SIMPLE_NAME = (By.XPATH,"//input[@name='abbreviation']")
# 定位所属站点
WMS_SUOSHUZHANDIAN = (By.XPATH,"//select[@name='city_id']")
# 定位站点选择
WMS_CHOOSE_ZHANDIAN = (By.XPATH,"//option[text()='王大法']")
# 定位卖点介绍
WMS_MAIDIAN_JIESHAO = (By.XPATH,"//input[@name='content']")
# 定位产地
WMS_CHANDI_NAME = (By.XPATH,"//input[@name='growarea']")
# 定位虚拟购买数量
WMS_BUY_AMOUNT = (By.XPATH,"//input[@name='manualsetbuyertotal']")

# 定位确定按钮
WMS_CONFIRM_BUTTON = (By.XPATH,"//button[@class='btn btn-primary']")