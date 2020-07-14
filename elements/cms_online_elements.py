# coding=utf-8

from selenium.webdriver.common.by import By

# 登录页面
# 手机号输入框
WMS_INPUT_LOGIN_TELEPHONE = (By.ID, "telphone")
# 密码输入框
WMS_INPUT_LOGIN_CAPTCHA = (By.ID, "captcha")
# 登录按钮##
WMS_BUTTON_LOGIN = (By.XPATH, "/html/body/form/div/div[1]/button")

# 十荟团首页
# 定位登录的用户名   ---------和放配置文件的区别??
WMS_BUTTON_INDEX_LOGIN_NAME = (By.XPATH, "//span[contains(text(),'欢迎') and contains(text(),'wangdafa') ]")
####################################################################################################################################################################################
# 商品管理
# 商品管理-定位商品管理
WMS_BUTTON_GOODS_MANAGE = (By.XPATH, "//span[text()='商品管理']")
# 商品管理-定位商品列表
WMS_BUTTON_GOODS_MANAGE_GOODS_LIST = (By.XPATH, "//span[text()='商品上架']")
# 商品管理-商品管理菜单按钮
WMS_BUTTON_COMMODITY_GOODS = (By.ID, "navi318")
# # 商品管理-商品上架-商品上架菜单按钮
WMS_BUTTON_COMMODITY_SHELVES = (By.ID, "navi309")
# 商品管理-商品上架-选择主站
WMS_BUTTON_COMMODITY_SHELVES_SELECT_MASTER_STATION = (By.ID, "city_id_label")
# 商品管理-商品上架-总部三站
WMS_BUTTON_COMMODITY_SHELVES_MASTER_STATION_NAME = (By.XPATH, "//*[@class='text'][4]")
# 商品管理-商品上架-添加商品按钮
WMS_BUTTON_COMMODITY_SHELVES_ADD_GOODS = (By.XPATH,
                         "/html[@class='no-js']/body[@class='page-sidebar-closed-hide-logo']/div[@class='page-container']/div[@class='page-content-wrapper']/div[@class='page-content']/div[@class='portlet light']/div[@class='portlet-body']/form[@id='search_form']/div[@class='row'][2]/div[@class='col-md-12 margin-bottom-10']/div[@class='form-group pull-right']/a[@class='btn btn-primary']")
# 商品管理-商品上架-寻味师按钮
WMS_BUTTON_COMMODITY_SHELVES_TASTER = (
By.XPATH, "/html/body/div[3]/div[2]/div/div[2]/div/form/table/tbody/tr[1]/td[2]/div/div/button/span[1]")
# 商品管理-商品上架-选择第一个寻味师
WMS_BUTTON_COMMODITY_SHELVES_TASTER_FIRST = (
By.XPATH, "/html/body/div[3]/div[2]/div/div[2]/div/form/table/tbody/tr[1]/td[2]/div/div/div/ul/li[2]/a")
# 商品管理-商品上架-商品名称输入框
WMS_INPUT_COMMODITY_SHELVES_GOODS_NAME = (By.XPATH, "/html/body/div[3]/div[2]/div/div[2]/div/form/table/tbody/tr[2]/td[2]/input")
# 商品管理-商品上架-商品简称输入框
WMS_INPUT_COMMODITY_SHELVES_GOODS_ABBREVIATION = (
By.XPATH, "/html/body/div[3]/div[2]/div/div[2]/div/form/table/tbody/tr[3]/td[2]/input")
# 商品管理-商品上架-商品卖点介绍
WMS_BUTTON_COMMODITY_SHELVES_USP = (By.XPATH, "/html/body/div[3]/div[2]/div/div[2]/div/form/table/tbody/tr[6]/td[2]/input")
# 商品管理-商品上架-产地
WMS_BUTTON_COMMODITY_SHELVES_PRODUCTION = (By.XPATH, "/html/body/div[3]/div[2]/div/div[2]/div/form/table/tbody/tr[7]/td[2]/input")
# 商品管理-商品上架-确认按钮
WMS_BUTTON_COMMODITY_SHELVES_SURE = (By.XPATH, "/html/body/div[3]/div[2]/div/div[2]/div/form/table/tfoot/tr/td/button")

# 商品管理-搜索特定团
# 商品管理-商品上架-商品上架页搜索框
WMS_BUTTON_COMMODITY_SHELVES_SEARCH = (By.NAME, "search_key")
# 商品管理-商品上架-搜索按钮
WMS_BUTTON_COMMODITY_SHELVES_SEARCH_BUTTON = (By.XPATH,
                    "/html[@class='no-js']/body[@class='page-sidebar-closed-hide-logo']/div[@class='page-container']/div[@class='page-content-wrapper']/div[@class='page-content']/div[@class='portlet light']/div[@class='portlet-body']/form[@id='search_form']/div[@class='row'][2]/div[@class='col-md-12 margin-bottom-10']/div[@class='input-group']/div[@class='input-group-btn']/button[@class='btn btn-primary']/i[@class='fa fa-search']")
# 商品管理-商品上架-搜索后第一个商品的编辑按钮
WMS_BUTTON_COMMODITY_SHELVES_FIRST_EDIT = (By.XPATH, "//a[contains(text(),'编辑')]")
################################################################################################################################################################################################################################################################################################################################
# 商品管理-商品上架-封面信息标签
WMS_BUTTON_COMMODITY_SHELVES_COVER = (By.XPATH, "/html/body/div[3]/div[2]/div/div[2]/div/ul/li[4]/a")
# 商品管理-商品上架-后台统计分类
WMS_BUTTON_COMMODITY_SHELVES_COVER_BUCK_STAGE = (
By.XPATH, "/html/body/div[3]/div[2]/div/div[2]/div/form/table/tbody/tr[1]/td[2]/label[1]/input")
# 商品管理-商品上架-前台展示分类
WMS_BUTTON_COMMODITY_SHELVES_COVER_RECEPTION = (
By.XPATH, "/html/body/div[3]/div[2]/div/div[2]/div/form/table/tbody/tr[2]/td[2]/label[1]/input")
# 商品管理-商品上架-商品辅助分类
WMS_BUTTON_COMMODITY_SHELVES_COVER_ASSIST = (
By.XPATH, "/html/body/div[3]/div[2]/div/div[2]/div/form/table/tbody/tr[3]/td[2]/label[1]/input")
# 商品管理-商品上架-拣货分类
WMS_BUTTON_COMMODITY_SHELVES_COVER_PICKING = (
By.XPATH, "/html/body/div[3]/div[2]/div/div[2]/div/form/table/tbody/tr[4]/td[2]/label[1]/input")
# 商品管理-商品上架-保质期
WMS_BUTTON_COMMODITY_SHELVES_COVER_EXP = (By.NAME, "expiration_date")
# 商品管理-商品上架-保存方式
WMS_BUTTON_COMMODITY_SHELVES_COVER_SAVE = (By.NAME, "saveway")
# 商品管理-商品上架-封面原价
WMS_BUTTON_COMMODITY_SHELVES_COVER_ORIG = (By.NAME, "origin_price")
# 商品管理-商品上架-封面图片
WMS_BUTTON_COMMODITY_SHELVES_COVER_PHOTO = (By.NAME, "cover_type")
# 商品管理-商品上架-团长专属
WMS_BUTTON_COMMODITY_SHELVES_COVER_REGIMENTAL_VIP = (
By.XPATH, "/html/body/div[3]/div[2]/div/div[2]/div/form/table/tbody/tr[9]/td[2]/input")
# 商品管理-商品上架-确定按钮
WMS_BUTTON_COMMODITY_SHELVES_COVER_SURE = (By.XPATH, "/html/body/div[3]/div[2]/div/div[2]/div/form/table/tfoot/tr/td/button")
# 商品管理-商品上架-上传图片
WMS_BUTTON_COMMODITY_SHELVES_COVER_UPLOAD_PHOTO = (By.ID, "upload_cover_image")
# 商品管理-商品上架-上传视频
WMS_BUTTON_COMMODITY_SHELVES_COVER_UPLOAD_VIDEO = (By.ID, "upload_cover_video")
# 商品管理-商品上架-上传视频中的图片
WMS_BUTTON_COMMODITY_SHELVES_COVER_UPLOAD_VIDEO_PHOTO = (By.ID, "upload_cover_video_image")
# 商品管理-商品上架-封面信息页面确定
WMS_BUTTON_COMMODITY_SHELVES_COVER_SURE_BUTTON = (By.XPATH, "//*[@id='form']/table/tfoot/tr/td/button")
############################################################################################################################################################################################
# 创建规格标签
# 定位创建规格tab键
WMS_BUTTON_COMMODITY_SHELVES_EDIT_SPEC = (By.XPATH, "/html/body/div[3]/div[2]/div/div[2]/div/ul/li[5]/a")
# 选择主规格
WMS_BUTTON_COMMODITY_SHELVES_EDIT_MAIN_SPEC = (By.XPATH, "//button[@data-id='attribute_id']")
# 主规格选择一级属性1
WMS_BUTTON_COMMODITY_SHELVES_EDIT_MAIN_SPEC_LEVEL = (By.XPATH, "//a/span[contains(text(),'一级属性1')]")
# 选择属性
WMS_BUTTON_COMMODITY_SHELVES_EDIT_ATTRIBUTE = (By.XPATH, "//button[@data-id='spec_id']")
# 属性选择二级属性1
WMS_BUTTON_COMMODITY_SHELVES_EDIT_ATTRIBUTE_LEVEL = (By.XPATH, "//a/span[contains(text(),'二级属性1')]")
# 选择确定按钮
WMS_BUTTON_COMMODITY_SHELVES_EDIT_SPEC_SURE = (By.XPATH, "//button[@id='saveAttribute']")
# 二次确定按钮
WMS_BUTTON_COMMODITY_SHELVES_EDIT_SPEC_SURE_TWO = (By.XPATH, "//div[@class='btn sure']")

############################################################################################################################################################################################
# 定位绑定SKU-tab键
WMS_BUTTON_COMMODITY_SHELVES_EDIT_SKU = (By.XPATH, "//a[text()='商品绑定SKU']")
# 规格图片-点击上传按钮
WMS_BUTTON_COMMODITY_SHELVES_EDIT_SKU_UPLOAD = (By.XPATH, "//a[contains(text(),'点击上传')]")
# 选择文件
WMS_BUTTON_COMMODITY_SHELVES_EDIT_SKU_CHOOSE_FILE = (By.XPATH, "//input[@id='file2upload']")
# 上传文件
WMS_BUTTON_COMMODITY_SHELVES_EDIT_SKU_UPLOAD_FILE = (By.XPATH, "//button[@id='btnfileupload']")
# 点击二次确定按钮
WMS_BUTTON_COMMODITY_SHELVES_EDIT_SKU_UPLOAD_FILE_TWO_SURE = (By.XPATH, "//div[@class='class='btn btn-primary']")
# 点击上传成功后的确定按钮
WMS_BUTTON_COMMODITY_SHELVES_EDIT_SKU_UPLOAD_SURE = (By.XPATH, "//div[@class='btn sure']")
# 输入规格名称
WMS_INPUT_COMMODITY_SHELVES_EDIT_SKU_SPEC_NAME = (By.XPATH, "//input[@name='merchtype_name[]']")
# 输入主站团购价
WMS_INPUT_COMMODITY_SHELVES_EDIT_SKU_GROUP_PRICE = (By.XPATH, "//input[@name='price[]']")
# 输入佣金比例
WMS_INPUT_COMMODITY_SHELVES_EDIT_SKU_COMMISSION = (By.XPATH, "//input[@name='brokerage[]']")
# 输入预计成本
WMS_INPUT_COMMODITY_SHELVES_EDIT_SKU_COST = (By.XPATH, "//input[@name='supplyprice[]']")
# 确定按钮
WMS_BUTTON_COMMODITY_SHELVES_EDIT_SKU_SURE = (By.XPATH, "//td/button[@type='button']")
# 点击二次确定按钮
WMS_BUTTON_COMMODITY_SHELVES_EDIT_SKU_SURE_TWO = (By.XPATH, "//div[@class='btn sure']")
# 编辑按钮
WMS_BUTTON_COMMODITY_SHELVES_EDIT_SKU_EDIT = (By.XPATH, "//a[contains(text(),'编辑')]")

"""编辑商品页面--绑定SKU--编辑SKU"""
# 搜索ID 4134
WMS_BUTTON_COMMODITY_SHELVES_EDIT_SKU_SEARCH_ID = (By.XPATH, "//button[@data-id='js-skuid-select']")
# 搜索输入4134
WMS_INPUT_COMMODITY_SHELVES_EDIT_SKU_SEARCH_ID = (By.XPATH, "//input[@class='form-control']")
# 选择4134
WMS_BUTTON_COMMODITY_SHELVES_EDIT_SKU_CHOOSE_ID = (By.XPATH, "//a/span[contains(text(),'4134')]")
# 点击添加按钮
WMS_BUTTON_COMMODITY_SHELVES_EDIT_SKU_ADD = (By.XPATH, "//a[contains(text(),'添加')]")
# 保存按钮
WMS_BUTTON_COMMODITY_SHELVES_EDIT_SKU_SAVE = (By.XPATH, "//button[@id='saveBtn']")
# 点击二次确定按钮
WMS_BUTTON_COMMODITY_SHELVES_EDIT_SKU_SAVE_SURE = (By.XPATH, "//div[@class='btn sure']")
##############################################################################################################################
# 轮播图
WMS_BUTTON_COMMODITY_SHELVES_EDIT_ROTATION_CHART = (By.XPATH, "/html/body/div[3]/div[2]/div/div[2]/div/ul/li[2]/a")
# 添加轮播图
WMS_BUTTON_COMMODITY_SHELVES_EDIT_ROTATION_CHART_ADD = (By.XPATH, "//*[@id='addcarousel']")
# 删除此项
WMS_BUTTON_COMMODITY_SHELVES_EDIT_ROTATION_CHART_DEL = (By.XPATH, "//*[@id='form']/table/tbody/tr/td[3]/a")
# 上传视频文件
WMS_BUTTON_COMMODITY_SHELVES_EDIT_ROTATION_CHART_VIDEO = (By.XPATH, "//*[@id='newbie_teaching_video20']")
# 上传轮播图
WMS_BUTTON_COMMODITY_SHELVES_EDIT_ROTATION_CHART_UPLOAD = (By.XPATH, "//*[@id='upload_merch_image20']")
# 提示点击确定
WMS_BUTTON_COMMODITY_SHELVES_EDIT_ROTATION_CHART_SURE = (By.XPATH, "/html/body/div[6]/div/div")
# 提示确定（500k）
WMS_BUTTON_COMMODITY_SHELVES_EDIT_ROTATION_CHART_SURE_500 = (By.XPATH, "/html/body/div[5]/div/div")
# #######################################################################################################################################################################################################
# 商品管理-商品属性
WMS_BUTTON_COMMODITY_SHELVES_ATTRIBUTES = (By.ID, "navi347")
# 商品管理-商品属性，搜索框
WMS_BUTTON_COMMODITY_SHELVES_ATTRIBUTES_SEARCH = (By.ID, "search_key")
# 商品管理-商品属性，搜索按钮
WMS_BUTTON_COMMODITY_SHELVES_ATTRIBUTES_SEARCH_BUTTON = (By.XPATH, "//*[@id=""search_form""]/div[1]/div/div[2]/button")
# 商品管理-商品属性，新增属性
WMS_BUTTON_COMMODITY_SHELVES_ATTRIBUTES_ADD = (By.XPATH, "//a[text()='新增属性']")
# 商品管理-商品属性，新增子属性
WMS_BUTTON_COMMODITY_SHELVES_ATTRIBUTES_ADD_SON = (By.XPATH, "//*[@id=""search_form""]/table/tbody/tr[1]/td[9]/a[1]")
# 商品管理-商品属性，停用
WMS_BUTTON_COMMODITY_SHELVES_ATTRIBUTES_STOP = (By.XPATH, "//a[text()='停用']")
# 商品管理-商品属性，确认停用
WMS_BUTTON_COMMODITY_SHELVES_ATTRIBUTES_STOP_YES = (By.XPATH, "/html/body/div[5]/div/div/div[2]/div")
# 商品管理-商品属性，取消停用#
WMS_BUTTON_COMMODITY_SHELVES_ATTRIBUTES_STOP_NO = (By.XPATH, "/html/body/div[5]/div/div/div[1]/div")
# 商品管理-商品属性，编辑
WMS_BUTTON_COMMODITY_SHELVES_ATTRIBUTES_EDIT = (By.XPATH, "//*[@id=""search_form""]/table/tbody/tr[1]/td[9]/a[3]")
# 商品管理-商品属性，删除
WMS_BUTTON_COMMODITY_SHELVES_ATTRIBUTES_DEL = (By.XPATH, "//*[@id=""search_form""]/table/tbody/tr[1]/td[9]/a[4]")
# 商品管理-商品属性，启用
WMS_BUTTON_COMMODITY_SHELVES_ATTRIBUTES_START = (By.XPATH, "//a[text()='启用']")
# 商品管理-商品属性，规格名称
WMS_BUTTON_COMMODITY_SHELVES_ATTRIBUTES_NAME = (By.XPATH, "//*[@id=""search_form""]/table/tbody/tr[1]/td[2]/a[2]")
# 商品管理-商品属性，属性名称
WMS_BUTTON_COMMODITY_SHELVES_ATTRIBUTES_ADD_NAME = (By.XPATH, "//*[@id=""form""]/table/tbody/tr[2]/td[2]/input")
# 商品管理-商品属性，显示排序
WMS_BUTTON_COMMODITY_SHELVES_ATTRIBUTES_SORT = (By.NAME, "rank")
# 商品管理-商品属性，确定按钮
WMS_BUTTON_COMMODITY_SHELVES_ATTRIBUTES_SURE = (
By.XPATH, "/html/body/div[3]/div[2]/div/div[2]/div/form/table/tfoot/tr/td/button")

# #######################################################################################################################################################################################################
# 站点设置
WMS_BUTTON_SITE_ENTER = (By.ID, "navi474")
# 搜索按确定按钮
WMS_BUTTON_SITE_SEARCH = (By.CSS_SELECTOR, ".btn-primary")

WMS_BUTTON_SITE_SEARCH_MASTER = (By.ID, "warehousesite_id_label")
# 关闭按钮
WMS_BUTTON_SITE_CLOSE = (By.XPATH, "//a[text()='关闭']")
# 开启
WMS_BUTTON_SITE_START = (By.XPATH, "//a[text()='开启']")
# 编辑按钮
WMS_BUTTON_SITE_EDIT = (By.XPATH, "//a[text()='编辑']")
# 查看按钮
WMS_BUTTON_SITE_SEE = (By.XPATH, "//a[text()='查看']")
# 查看-取消
WMS_BUTTON_SITE_SEE_EXIT = (By.CSS_SELECTOR, "div.modal-footer:nth-child(3) > button:nth-child(1)]")
# 二次确认
WMS_BUTTON_SITE_SEE_EXIT_SURE = (By.CSS_SELECTOR, ".sure")
# 二次取消
WMS_BUTTON_SITE_SEE_EXIT_TWO = (By.CSS_SELECTOR, ".exit")
# 编辑-排序
WMS_BUTTON_SITE_EDIT_SORT = (
By.CSS_SELECTOR, ".table > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(5) > input:nth-child(1)")
# 编辑-修改
WMS_BUTTON_SITE_EDIT_UPDATE = (By.XPATH, "//a[text()='修改']")
# 编辑-上线
WMS_BUTTON_SITE_EDIT_ONLINE = (By.XPATH, "//a[text()='上线']")
# 编辑-下线#
WMS_BUTTON_SITE_EDIT_OFFLINE = (By.XPATH, "//a[text()='下线']")
## #######################################################################################################################################################################################################
# 售价控制
# 站点售价控制
WMS_BUTTON_PRICE_CONTROL = (By.ID, "navi355")
# 新增按钮
WMS_BUTTON_PRICE_CONTROL_ADD = (By.XPATH, "//a[text()=' 新增']")
# 编辑
WMS_BUTTON_PRICE_CONTROL_EDIT = (By.XPATH, "/html/body/div[3]/div[2]/div/div[2]/div/form/table/tbody/tr[1]/td[11]/a[1]")
# 失效按钮
WMS_BUTTON_PRICE_CONTROL_INVALID = (By.XPATH, "/html/body/div[3]/div[2]/div/div[2]/div/form/table/tbody/tr[1]/td[11]/a[2]")
# 团长佣金返利倍数
WMS_BUTTON_PRICE_CONTROL_AMOUNT_RATIO = (By.NAME, "amount_ratio")
# 营销费占比
WMS_BUTTON_PRICE_CONTROL_MAKE_COST_PROPORTION = (By.NAME, "mark_cost_proportion")
# 仓配费占比
WMS_BUTTON_PRICE_CONTROL_RATIO_WAREHOUSE_PROPORTION = (By.NAME, "ratio_warehouse_proportion")
# 经营利润占比
WMS_BUTTON_PRICE_CONTROL_PROFIT_PROPORTION = (By.NAME, "profit_proportion")
# 确认按钮
WMS_BUTTON_PRICE_CONTROL_ADD_YES = (By.ID, "sub")
# 取消按钮 #
WMS_BUTTON_PRICE_CONTROL_ADD_NO = (By.ID, "cancel_btn")
# #######################################################################################################################################################################################################
# 团购管理
# 团购管理
WMS_BUTTON_GROUP = (By.ID, "navi464")
# 团购管理-开团管理
WMS_BUTTON_OPEN_GROUP = (By.ID, "navi199")
# 团购管理-开团管理,新建团购
WMS_BUTTON_OPEN_GROUP_ADD = (By.XPATH, "//button[@onclick='editgroupon()']")
# 团购管理-开团管理,开团时间  05:25:00
WMS_BUTTON_WMS_BUTTON_OPEN_GROUP_ADD_START = (By.CSS_SELECTOR, "#add_starttime > input:nth-child(1)")
# 团购管理-开团管理,截团时间  2019-09-19 10:30:13
WMS_BUTTON_OPEN_GROUP_ADD_END = (By.CSS_SELECTOR, "#add_endtime > input:nth-child(1)")
# 团购管理-开团管理,团购介绍
WMS_BUTTON_OPEN_GROUP_ADD_INTRODUCE = (By.NAME, "groupon_title")
# 团购管理-开团管理,保存
WMS_BUTTON_OPEN_GROUP_ADD_SAVE = (By.CSS_SELECTOR, "div.modal-footer:nth-child(4) > button:nth-child(2)")
WMS_BUTTON_OPEN_GROUP_ADD_S = (By.NAME, "groupon_id")
WMS_BUTTON_OPEN_GROUP_ADD_OPEN = (By.XPATH, "/html/body/div[3]/div[2]/div/div[2]/div/form/div/div/div[3]/select/option[last()]")
# 团购管理-开团管理,取消
WMS_BUTTON_OPEN_GROUP_ADD_CANCEL = (By.XPATH, "//*[@id=""add_groupon_modal""]/div[2]/div/form/div[2]/button[1]")
# 团购管理-开团管理,复制团购
WMS_BUTTON_OPEN_GROUP_ADD_COPY = (By.XPATH, "/html/body/div[3]/div[2]/div/div[2]/div/div[1]/div/div/button[1]")
# 团购管理-开团管理,停团
WMS_BUTTON_OPEN_GROUP_ADD_STOP = (By.ID, "stopgroupon")
# 团购管理-开团管理,关联活动
WMS_BUTTON_OPEN_GROUP_ADD_RELEVANCE = (By.XPATH, "/html/body/div[3]/div[2]/div/div[2]/div/span[2]/a")
# 团购管理-开团管理,编辑
WMS_BUTTON_OPEN_GROUP_ADD_EDIT = (By.CSS_SELECTOR, "a.btn-xs:nth-child(2)")
# 团购管理-开团管理,选择商品
WMS_BUTTON_OPEN_GROUP_ADD_SELECT = (By.CSS_SELECTOR, ".filter-option")
# 团购管理-开团管理,商品搜索框
WMS_INPUT_OPEN_GROUP_ADD_SEARCH = (By.CSS_SELECTOR, ".bs-searchbox > input:nth-child(1)")
# 团购管理-开团管理,选择搜索结果中第一个商品
WMS_BUTTON_OPEN_GROUP_ADD_SEARCH_FIRST = (By.CSS_SELECTOR, ".inner > li:nth-child(1) > a:nth-child(1)")
# 团购管理-开团管理,添加按钮
WMS_BUTTON_OPEN_GROUP_ADD_ADD_BUTTON = (By.XPATH, "/html/body/div[3]/div[2]/div/div[2]/div/div[2]/div/a")
# 团购管理-开团管理,一键保存
WMS_BUTTON_OPEN_GROUP_ADD_ONE_SAVE = (By.ID, "one-click-save")
# 团购管理-开团管理,一键起售
WMS_BUTTON_OPEN_GROUP_ADD_ONE_SALE = (By.ID, "one-click-sale")
# 团购管理-开团管理,送货时间
WMS_BUTTON_OPEN_GROUP_ADD_DELIVERY_TIME = (By.NAME, "deliveryday[]")
# 团购管理-开团管理,生产日期
WMS_BUTTON_OPEN_GROUP_ADD_PRODUCE = (By.NAME, "produce_day[]")
# 团购管理-开团管理,最大售卖
WMS_BUTTON_OPEN_GROUP_ADD_MAX = (By.XPATH, "//*[@id=""contents""]/tr/td[11]/input")
# 团购管理-开团管理,限购数量5
WMS_BUTTON_OPEN_GROUP_ADD_NUMBER = (By.XPATH, "//*[@id=""contents""]/tr/td[13]/input")
# 团购管理-开团管理,售卖区域及价格
WMS_BUTTON_OPEN_GROUP_ADD_AREA = (By.ID, "one-click-sale")
# 团购管理-开团管理,排序
WMS_BUTTON_OPEN_GROUP_ADD_RANK = (By.NAME, "rank[]")
# 团购管理-开团管理,不可用券
WMS_BUTTON_OPEN_GROUP_ADD_NOT_COUPON = (By.XPATH, "//*[@id=""contents""]/tr/td[19]/input")
# 团购管理-开团管理,保存
WMS_BUTTON_OPEN_GROUP_SAVE = (By.NAME, "save")
# #######################################################################################################################################################################################################
# 团购管理-金剛管理
# 团购管理-金剛管理，进入金刚页面
WMS_BUTTON_GROUP_BUYING_DIAMOND_ENTER = (By.ID, "navi475")
# 团购管理-金剛管理，金刚页面搜索框
WMS_INPUT_GROUP_BUYING_DIAMOND_SEARCH = (By.CSS_SELECTOR, "input.form-control:nth-child(2)")
# 团购管理-金剛管理，搜索按钮
WMS_BUTTON_GROUP_BUYING_DIAMOND_SEARCH = (By.ID, "searchBtn")
# 团购管理-金剛管理，新建金刚
WMS_BUTTON_GROUP_BUYING_DIAMOND_ADD = (By.XPATH, "//a[text()='新建金刚']")
# 团购管理-金剛管理，上线按钮
WMS_BUTTON_GROUP_BUYING_DIAMOND_ON_LINE = (By.XPATH, "//a[text()='上线']")
# 团购管理-金剛管理，下线按钮
WMS_BUTTON_GROUP_BUYING_DIAMOND_OFF_LINE = (By.XPATH, "//a[text()='下线']")
# 团购管理-金剛管理，编辑按钮
WMS_BUTTON_GROUP_BUYING_DIAMOND_EDIT = (By.XPATH, "//a[text()='编辑']")
# 团购管理-金剛管理，金刚名称
WMS_BUTTON_GROUP_BUYING_DIAMOND_NAME = (By.CSS_SELECTOR, "#kingkong-title")
# 团购管理-金剛管理，上传图片按钮
WMS_BUTTON_GROUP_BUYING_DIAMOND_UPLOAD_PHOTO = (By.XPATH, "//a[text()='上传图片']")
# 团购管理-金剛管理，选图按钮
WMS_BUTTON_GROUP_BUYING_DIAMOND_SEARCH_PHOTO = (By.ID, "file2upload")
# 团购管理-金剛管理，上传文件
WMS_BUTTON_GROUP_BUYING_DIAMOND_UPLOAD_FILE = (By.ID, "btnfileupload")
# 团购管理-金剛管理，取消上传按钮
WMS_BUTTON_GROUP_BUYING_DIAMOND_UPLOAD_UNDO = (By.CSS_SELECTOR,
                    "#qcloud_uploader_modal > div:nth-child(2) > div:nth-child(1) > div:nth-child(3) > button:nth-child(1)")
# 团购管理-金剛管理，关联分类
WMS_BUTTON_GROUP_BUYING_DIAMOND_RELATION = (By.ID, "kingkong-classification-pintor")
# 团购管理-金剛管理，选择分类
WMS_BUTTON_GROUP_BUYING_DIAMOND_SEARCH_RELATION = (By.CSS_SELECTOR, "#add_starttime > label:nth-child(1) > input:nth-child(1)")
# 团购管理-金剛管理，分类保存按钮
WMS_BUTTON_GROUP_BUYING_DIAMOND_ORESERVATION = (By.NAME, "myloadding")
# 团购管理-金剛管理，排序
WMS_BUTTON_GROUP_BUYING_DIAMOND_SORT = (By.ID, "kingkong-rank")
# 团购管理-金剛管理，新建金刚保存按钮
WMS_BUTTON_GROUP_BUYING_DIAMOND_SAVE = (By.NAME, "myloadding")
# 团购管理-金剛管理，新建金刚取消按钮#
WMS_BUTTON_GROUP_BUYING_DIAMOND_SAVE_CANCEL = (By.ID, "navi475")
# #######################################################################################################################################################################################################
# 订单管理
WMS_BUTTON_ORDER = (By.ID, "navi171")
# 订单管理-查看订单
Order_see = (By.ID, "navi307")
#  订单管理-查看订单,团长ID
WMS_BUTTON_ORDER_USER_ID = (By.NAME, "userid")
# 订单管理-查看订单,团购ID
WMS_BUTTON_ORDER_GROUP_ID = (By.NAME, "grouponid")
# 订单管理-查看订单,用户ID
WMS_BUTTON_ORDER_USER_ID_SINGLE = (By.NAME, "useridsingle")
# 订单管理-查看订单,搜索框
WMS_BUTTON_ORDER_SEARCH_CONTENT = (By.NAME, "searchcontent")
# #订单管理-查看订单,搜索
WMS_BUTTON_ORDER_SEARCH = (By.XPATH, "//button[@title='搜索']")
# 订单管理-查看订单,查看详情
WMS_BUTTON_ORDER_SEARCH_DETAILS = (By.XPATH, "//*[@id='adminlist']/tbody/tr[1]/td[12]/a")
# 订单管理-查看订单,修改送货时间
WMS_BUTTON_ORDER_DELIVER_TIME = (By.XPATH, "//a[contains(@href,'javascript:updateDeliveryday')]")
# 订单管理-查看订单,新送货时间
WMS_BUTTON_ORDER_DELIVER_TIME_NEW = (By.XPATH, "//*[@id='add_endtime']/span/input")
# 　订单管理-查看订单,当前日期
WMS_BUTTON_ORDER_DELIVER_TIME_NEW_NOW = (
By.CSS_SELECTOR, "body > div:nth-child(16) > div.datetimepicker-days > table > tbody > tr:nth-child(2) > td.day.active")
# 订单管理-查看订单,修改原因输入框
WMS_BUTTON_ORDER_DELIVER_TIME_REASONS = (By.XPATH, "//*[@id='modifyreasonid']")
# 订单管理-查看订单,修改责任归属
WMS_BUTTON_ORDER_MODIFY_RESPONSIBILITY_ATTRIBUTION = (By.XPATH, "//*[@id='responsibilityid']")
# 订单管理-查看订单,保存
WMS_BUTTON_ORDER_DELIVER_TIME_SAVE = (By.XPATH, "//*[@id='updateDeliveryday']/div[2]/div/form/div[2]/button[2]")
# 订单管理-查看订单,二次确定
WMS_BUTTON_ORDER_DELIVER_TIME_SAVE_TWO = (By.XPATH, "/html/body/div[9]/div/div")
######################################################################################################################
# 出库管理
WMS_BUTTON_OUT_STOCK_MANAGE = (By.ID, "navi460")
# 出库管理-波次统计
WMS_BUTTON_WAVE_STATISTICS = (By.ID, "navi471")
# 出库管理-波次统计,发起拣货开始时间
WMS_BUTTON_WAVE_STATISTICS_START_TIME = (By.NAME, "starttime")
# 出库管理-波次统计,发起拣货结束时间
WMS_BUTTON_WAVE_STATISTICS_END_TIME = (By.NAME, "endtime")
# 出库管理-波次统计,查询按钮
WMS_BUTTON_WAVE_STATISTICS_SEARCH = (By.XPATH, "//button[@value='search']")
# 出库管理-波次统计,导出按钮#
WMS_BUTTON_WAVE_STATISTICS_EXPORT = (By.XPATH, "//button[@value='export']")
###########################################################################################################
# 出库管理-订单出库
WMS_BUTTON_OUT_STOCK_ORDER = (By.XPATH, '//*[@id="navi297"]')
# 出库管理-订单出库,发货仓库
WMS_BUTTON_OUT_STOCK_DELIVERY_WAREHOUSE = (By.ID, "warehouseid")
# 出库管理-订单出库,发货仓库子站
WMS_BUTTON_OUT_STOCK_DELIVERY_WAREHOUSE_STATION = (By.XPATH, "//*[@id='subsite_select_label']/div")
# 　出库管理-订单出库,测试子站输入框
WMS_INPUT_OUT_STOCK_DELIVERY_WAREHOUSE = (By.XPATH, "//*[@id='subsite_select_label']/div/div/div/input")
# 出库管理-订单出库,总部测试子站1
WMS_INPUT_OUT_STOCK_DELIVERY_WAREHOUSE_STATION_ONE = (By.XPATH, "//*[@id='subsite_select_label']/div/div/ul/li[5]/a/span")
# 出库管理-订单出库,查询
WMS_INPUT_OUT_STOCK_DELIVERY_SEARCH = (By.XPATH, "//*[@id='searchBtn']")
# 出库管理-订单出库,配送状态
WMS_BUTTON_OUT_STOCK_DELIVERY_STATE = (By.XPATH, "//*[@id='deliverystatus']")
# 出库管理-订单出库,订单出库产品预览
WMS_BUTTON_OUT_STOCK_DELIVERY_ORDER_LIST = (By.XPATH, "//*[@id='storageout']")
# 出库管理-订单出库,确定出库
WMS_BUTTON_OUT_STOCK_DELIVERY_STOCK = (By.XPATH, "//*[@id='revokeorder_modal']/div[2]/div/div[3]/button[2]")
# 　出库管理-订单出库,二次确定出库
WMS_BUTTON_OUT_STOCK_DELIVERY_STOCK_TWO = (By.XPATH, "/html/body/div[8]/div/div/div[2]/div")
# 出库管理-订单出库,三次 确定
WMS_BUTTON_OUT_STOCK_DELIVERY_STOCK_THREE = (By.XPATH, "/html/body/div[10]/div/div")
###############################################################################################################################
# 客服工单#
WMS_BUTTON_CUSTOMER_SERVICE_WORK = (By.ID, "navi343")
# 客服工单-工单列表
WMS_BUTTON_CUSTOMER_SERVICE_WORK_LIST = (By.ID, "navi344")
# 客服工单-工单列表,第一个搜索框
WMS_BUTTON_CUSTOMER_SERVICE_WORK_LIST_SEARCH_BAR_ONE = (By.ID, "searchcontent1")
# 客服工单-工单列表,第二个搜索框
WMS_BUTTON_CUSTOMER_SERVICE_WORK_LIST_SEARCH_BAR_TWO = (By.ID, "searchcontent2")
# 客服工单-工单列表,搜索按钮#
WMS_BUTTON_CUSTOMER_SERVICE_WORK_ACTION = (By.NAME, "action")
# 客服工单-工单列表,勾选工单
WMS_BUTTON_CUSTOMER_SERVICE_WORK_CHECK = (By.NAME, "checkboxs")
# 客服工单-工单列表,批量受理工单
WMS_BUTTON_CUSTOMER_SERVICE_WORK_BATCH_MANAGE = (By.XPATH, "//*[@id='grabAllWorkOrder']")
# 客服工单-工单列表,确定受理
WMS_BUTTON_CUSTOMER_SERVICE_WORK_MANAGE_SURE = (By.XPATH, "/html/body/div[6]/div/div/div[2]/div")
# 客服工单-工单列表,二次确定
WMS_BUTTON_CUSTOMER_SERVICE_WORK_MANAGE_SURE_TWO = (By.XPATH, "/html/body/div[6]/div/div/div[2]/div")
# 客服工单-工单列表,处理中
WMS_BUTTON_CUSTOMER_SERVICE_WORK_HANDLE = (By.XPATH, '//*[@id="status"]/li[2]/a/h4')
# 客服工单-工单列表,处理
WMS_BUTTON_CUSTOMER_SERVICE_WORK_HANDLES = (By.XPATH, '//*[@id="adminlist"]/tbody/tr[1]/td[1]/a[1]')
# 　客服工单-工单列表,订单赔付
WMS_BUTTON_CUSTOMER_SERVICE_WORK_PAID = (By.XPATH, '/html/body/div[3]/div[2]/div/div[2]/div/div[1]/div/div[1]/button[2]')
# 客服工单-工单列表,查看工单页面主站
WMS_BUTTON_CUSTOMER_SERVICE_WORK_MASTER = (By.XPATH, '//*[@id="city_id_label"]/div/button/span[1]')
# 客服工单-工单列表,取消
WMS_BUTTON_CUSTOMER_SERVICE_WORK_REMOVE = (By.XPATH, '//*[@id="city_id_label"]/div/div/div[2]/div/button[2]')
# 客服工单-工单列表,主站输入框
WMS_INPUT_CUSTOMER_SERVICE_WORK_MASTER = (By.XPATH, '//*[@id="city_id_label"]/div/div/div[1]/input')
# 客服工单-工单列表,选择的总部3站
WMS_BUTTON_CUSTOMER_SERVICE_WORK_MASTER_THREE = (By.XPATH, '//*[@id="city_id_label"]/div/div/ul/li[3]/a')
# 客服工单-工单列表,赔付一级原因
WMS_BUTTON_CUSTOMER_SERVICE_WORK_PAID_ONE_CAUSE = (
By.XPATH, '//*[@id="compensate_modal"]/div[2]/div/div[2]/table/tbody/tr[1]/td[2]/div[1]/button')
# 客服工单-工单列表,赔付一级搜索输入框
WMS_INPUT_CUSTOMER_SERVICE_WORK_PAID_ONE = (
By.XPATH, '//*[@id="compensate_modal"]/div[2]/div/div[2]/table/tbody/tr[1]/td[2]/div[1]/div/div/input')
# 客服工单-工单列表,赔付一级选的客户原因
WMS_BUTTON_CUSTOMER_SERVICE_WORK_PAID_ONE_USER = (
By.XPATH, '//*[@id="compensate_modal"]/div[2]/div/div[2]/table/tbody/tr[1]/td[2]/div[1]/div/ul/li[12]/a/span[1]')
# # 客服工单-工单列表.赔付二级原因
WMS_BUTTON_CUSTOMER_SERVICE_WORK_PAID_TWO_CAUSE = (
By.XPATH, '//*[@id="compensate_modal"]/div[2]/div/div[2]/table/tbody/tr[1]/td[2]/div[2]/button')
# # 客服工单-工单列表,二级搜索输入框
WMS_INPUT_CUSTOMER_SERVICE_WORK_PAID_TWO = (
By.XPATH, '//*[@id="compensate_modal"]/div[2]/div/div[2]/table/tbody/tr[1]/td[2]/div[2]/div/div/input')
# # 客服工单-工单列表,二级不想要
WMS_BUTTON_CUSTOMER_SERVICE_WORK_PAID_TWO_USER = (
By.XPATH, '//*[@id="compensate_modal"]/div[2]/div/div[2]/table/tbody/tr[1]/td[2]/div[2]/div/ul/li[2]/a/span[1]')
# 客服工单-工单列表,责任归属其他
WMS_BUTTON_CUSTOMER_SERVICE_WORK_RESPONSIBILITY_ATTRIBUTION = (
By.XPATH, '//*[@id="compensate_modal"]/div[2]/div/div[2]/table/tbody/tr[2]/td[2]/input[6]')
# 客服工单-工单列表,金额输入框
WMS_INPUT_CUSTOMER_SERVICE_WORK_MONEY_PAID = (By.XPATH, '//*[@id="price"]')
# 客服工单-工单列表,赔付原因输入框
WMS_INPUT_CUSTOMER_SERVICE_WORK_PAID_CAUSE = (By.XPATH, '//*[@id="compensate-content"]')
# 　客服工单-工单列表,确定
WMS_BUTTON_CUSTOMER_SERVICE_WORK_PAID_SURE = (By.XPATH, '//*[@id="docompensatedisable"]')
# 　客服工单-工单列表,二次确定
WMS_BUTTON_CUSTOMER_SERVICE_WORK_PAID_SURE_TWO = (By.XPATH, '/html/body/div[9]/div/div/div[2]/div')
# 　客服工单-工单列表,三次确定
WMS_BUTTON_CUSTOMER_SERVICE_WORK_PAID_SURE_THREE = (By.XPATH, '')
# 　客服工单-工单列表,已解决
WMS_BUTTON_CUSTOMER_SERVICE_WORK_OFF = (By.XPATH, '//*[@id="status"]/li[5]/a/h4')
# 　客服工单-工单列表,第一个已解决工单
WMS_BUTTON_CUSTOMER_SERVICE_WORK_OFF_ONE = (By.XPATH, '//*[@id="adminlist"]/tbody/tr/td[1]/a')
# 　客服工单-工单列表,关闭工单
WMS_BUTTON_CUSTOMER_SERVICE_WORK_CLOSE = (By.XPATH, '/html/body/div[3]/div[2]/div/div[2]/div/div[1]/div/div[1]/button')
# 　客服工单-工单列表,未勾选回复框
WMS_BUTTON_CUSTOMER_SERVICE_WORK_NOT_NEWS = (By.XPATH, '/html/body/div[3]/div[2]/div/div[2]/div/div[1]/div/div[7]/div[2]/table/tbody/tr[1]/td/div/input')
#  客服工单-工单列表,回复记录输入框
WMS_INPUT_CUSTOMER_SERVICE_WORK_NEWS = (By.XPATH, '//*[@id="content"]')
# 客服工单-工单列表,　回复按钮
WMS_BUTTON_CUSTOMER_SERVICE_WORK_NEWS = (By.XPATH, '/html/body/div[3]/div[2]/div/div[2]/div/div[1]/div/div[7]/div[2]/table/tbody/tr[2]/td/button')
############################################################################################################################################################################
# 客服工单-售后统计
WMS_BUTTON_CUSTOMER_SERVICE_WORK_STATISTICS = (By.ID, "navi346")
# 客服工单-售后统计,第一个搜索框
WMS_INPUT_CUSTOMER_SERVICE_WORK_STATISTICS_SEARCH_ONE = (By.ID, "searchcontent1")
# 客服工单-售后统计,第二个搜索框
WMS_INPUT_CUSTOMER_SERVICE_WORK_STATISTICS_SEARCH_TWO = (By.ID, "searchcontent2")
# 客服工单-售后统计,搜索按钮
WMS_INPUT_CUSTOMER_SERVICE_WORK_STATISTICS_SEARCH = (By.XPATH, "//*[@id=""search_form""]/div[3]/div/button[1]/i")
# 客服工单-售后统计,导出
WMS_BUTTON_CUSTOMER_SERVICE_WORK_STATISTICS_EXPORT = (By.XPATH, "//*[@id=""search_form""]/div[3]/div/button[2]")
# 客服工单-售后统计,批改责任归属#
WMS_BUTTON_CUSTOMER_SERVICE_WORK_STATISTICS_MODIFY = (By.XPATH, "//*[@id=""search_form""]/div[3]/div/span")
#######################################################################################################################################
# 客服工单-售后审核
WMS_BUTTON_CUSTOMER_SERVICE_WORK_EXAMINE = (By.ID, "navi358")
# 客服工单-售后审核,第一个搜索框
WMS_INPUT_CUSTOMER_SERVICE_WORK_EXAMINE_SEARCH_ONE = (By.ID, "searchcontent1")
# 客服工单-售后审核,第二个搜索框
WMS_INPUT_CUSTOMER_SERVICE_WORK_EXAMINE_SEARCH_TWO = (By.ID, "searchcontent2")
# 客服工单-售后审核,搜索按钮
WMS_BUTTON_CUSTOMER_SERVICE_WORK_EXAMINE_SEARCH = (By.XPATH, "//*[@id=""search_form""]/div[3]/div/button[1]/i")
# #######################################################################################################################################################################################################
# 系统管理
WMS_BUTTON_SYSTEM_MANAGE = (By.ID, "navi2")
# 系统管理-角色管理
WMS_BUTTON_SYSTEM_ROLE = (By.ID, "navi316")
# 系统管理-角色管理,团长管理
WMS_BUTTON_SYSTEM_ROLE_HEADS = (By.ID, "navi308")
# 系统管理-角色管理-团长管理,滚动条
WMS_BUTTON_SYSTEM_ROLE_MOVE = (By.XPATH, "//*[@id='tab_merchtypes']/div[1]")
# 系统管理-角色管理-团长管理,搜索框
WMS_INPUT_SYSTEM_ROLE_SEARCH_KEY = (By.NAME, "search_key")
# 系统管理-角色管理-团长管理，搜索条件-手机号
WMS_SELECT_SYSTEM_ROLE_PHONE_SEARCH = (By.ID, "searchfield")
# 系统管理-角色管理-团长管理,搜索按钮
WMS_BUTTON_SYSTEM_ROLE_HEADS_SEARCH = (By.XPATH, "//*[@id='search_form']/div[2]/div/button/i")
# 系统管理-角色管理-团长管理-未启用团长################
# 系统管理-角色管理-团长管理-未启用团长,查看副团长
WMS_BUTTON_SYSTEM_ROLE_HEADS_VICE = (By.XPATH, "//*[@id=""adminlist""]/tbody/tr/td[14]/a[1]")
# 系统管理-角色管理-团长管理-未启用团长,提现
WMS_BUTTON_SYSTEM_ROLE_HEADS_WITHDRAWAL = (By.XPATH, "//*[@id=""adminlist""]/tbody/tr/td[14]/a[2]")
# 系统管理-角色管理-团长管理-未启用团长,停用
WMS_BUTTON_SYSTEM_ROLE_HEADS_STOP = (By.XPATH, "//*[@id=""adminlist""]/tbody/tr/td[14]/a[3]")
# 系统管理-角色管理-团长管理-未启用团长,开启
WMS_BUTTON_SYSTEM_ROLE_HEADS_START = (By.XPATH, "//*[@id=""adminlist""]/tbody/tr/td[14]/a[4]")
# 系统管理-角色管理-团长管理-未启用团长,详情
WMS_BUTTON_SYSTEM_ROLE_HEADS_DETAILS = (By.XPATH, "//*[@id='adminlist']/tbody/tr/td[15]/a[3]")
### 详情 ###
# 系统管理-角色管理-团长管理-详情，同步
WMS_BUTTON_SYSTEM_ROLE_HEADS_SYNCHRONIZATION = (
By.XPATH, "/html/body/div[3]/div[2]/div/div[2]/div/table[1]/thead/tr/th/div/button[1]")
# 系统管理-角色管理-团长管理-详情，提现余额
WMS_BUTTON_SYSTEM_ROLE_HEADS_WITHDRAWAL_ONE = (
By.XPATH, "/html/body/div[3]/div[2]/div/div[2]/div/table[1]/thead/tr/th/div/button[2]")
# 系统管理-角色管理-团长管理-详情，停用
WMS_BUTTON_SYSTEM_ROLE_HEADS_STOP_ONE = (By.XPATH, "/html/body/div[3]/div[2]/div/div[2]/div/table[1]/thead/tr/th/div/button[2]")
# 系统管理-角色管理-团长管理-详情，详情页停用团长点击 确定
WMS_BUTTON_SYSTEM_ROLE_REPORTS_SALES_SEARCH = (By.XPATH, "//div[@class='btn sure']")
# 系统管理-角色管理-团长管理-详情，开启
WMS_BUTTON_SYSTEM_ROLE_HEADS_START_ONE = (By.XPATH, "/html/body/div[3]/div[2]/div/div[2]/div/table[1]/thead/tr/th/div/button[4]")
# 系统管理-角色管理-团长管理-详情，编辑
WMS_BUTTON_SYSTEM_ROLE_HEADS_EDIT = (By.XPATH, "/html/body/div[3]/div[2]/div/div[2]/div/table[1]/thead/tr/th/div/button[5]")
# 系统管理-角色管理-团长管理-详情，团长统计查看
WMS_BUTTON_SYSTEM_ROLE_HEADS_STATISTICS = (By.XPATH, "/html/body/div[3]/div[2]/div/div[2]/div/table[1]/tbody/tr[3]/td[2]/a")
# 系统管理-角色管理-团长管理-详情，团长收益查看
WMS_BUTTON_SYSTEM_ROLE_HEADS_PROFIT = (By.XPATH, "/html/body/div[3]/div[2]/div/div[2]/div/table[1]/tbody/tr[8]/td[2]/a")
# 系统管理-角色管理-团长管理-详情，提现记录查看
WMS_BUTTON_SYSTEM_ROLE_HEADS_WITHDRAWAL_RECORD = (By.XPATH, "/html/body/div[3]/div[2]/div/div[2]/div/table[1]/tbody/tr[9]/td[4]/a")
# 系统管理-角色管理-团长管理-详情，配送小区添加
WMS_BUTTON_SYSTEM_ROLE_HEADS_ADD = (By.ID, "navi472")
# 系统管理-角色管理-团长管理-详情，配送小区同步#
WMS_BUTTON_SYSTEM_ROLE_HEADS_SYNCHRONIZATION_TWO = (By.ID, "navi472")
# 系统管理-角色管理-团长管理-启用团长################
#  系统管理-角色管理-团长管理-启用团长，查看副团长
WMS_BUTTON_SYSTEM_ROLE_HEADS_VICE_TWO = (By.XPATH, "//*[@id=""adminlist""]/tbody/tr/td[14]/a[1]")
#  系统管理-角色管理-团长管理-启用团长，关闭团长
WMS_BUTTON_SYSTEM_ROLE_HEADS_CLOSE = (By.XPATH, "//*[@id='adminlist']/tbody/tr/td[15]/a[2]")
# 系统管理-角色管理-团长管理-启用团长，详情
WMS_BUTTON_SYSTEM_ROLE_HEADS_DETAILS_TWO = (By.XPATH, "//*[@id=""adminlist""]/tbody/tr/td[14]/a[3]")
# 系统管理-角色管理-团长管理-启用团长，重起团长
WMS_BUTTON_SYSTEM_ROLE_HEADS_START_TWO = (By.XPATH, "//*[@id='adminlist']/tbody/tr/td[15]/a[4]")
##########################################################################################################
# 数据报表
WMS_BUTTON_REPORTS = (By.ID, "navi312")
# 数据报表-团购报表
WMS_BUTTON_REPORTS_GROUP = (By.ID, "searchcontent2")
# 数据报表-团购报表,确认按钮
WMS_BUTTON_REPORTS_GROUP_SEARCH = (By.ID, "searchBtn")
# 数据报表-团购报表,导出
WMS_BUTTON_REPORTS_GROUP_EXPORT = (By.ID, "export_btn")
# 数据报表-商品报表
WMS_BUTTON_REPORTS_GOODS = (By.ID, "navi314")
# 数据报表-商品报表,搜索框
WMS_INPUT_REPORTS_GOODS_SEARCH = (By.NAME, "search_key")
# 数据报表-商品报表,确认按钮
WMS_BUTTON_REPORTS_GOODS_SEARCH = (By.ID, "searchBtn")
# 数据报表-商品报表,导出
WMS_BUTTON_REPORTS_GOODS_EXPORT = (By.ID, "export_btn")
# 数据报表-团长销量统计
WMS_BUTTON_REPORTS_SALES = (By.ID, "navi315")
# 数据报表-团长销量统计-搜索框
WMS_INPUT_REPORTS_SALES_SEARCH_KEY = (By.NAME, "search_key")
# 数数据报表-团长销量统计-确认按钮
WMS_BUTTON_REPORTS_SALES_SEARCH = (By.ID, "searchBtn")
# 数据报表-团长销量统计-导出
WMS_BUTTON_REPORTS_SALES_EXPORT = (By.ID, "export_btn")
# 数据报表-漏发记录
WMS_BUTTON_REPORTS_MISSING = (By.ID, "navi472")
# 数据报表-漏发记录-搜索框
WMS_INPUT_REPORTS_MISSING_SEARCH_KEY = (By.NAME, "search_key")
# 数据报表-漏发记录-确认按钮
WMS_BUTTON_REPORTS_MISSING_SEARCH = (By.ID, "searchBtn")
# #######################################################################################################################################################################################################
# 营销管理
WMS_BUTTON_MARKETING_MANGE = (By.ID, "navi324")
# 营销管理-优惠券
WMS_BUTTON_MARKETING_COUPON = (By.ID, "navi311")
# 营销管理-优惠券,标题搜索框
WMS_INPUT_MARKETING_COUPON_SEARCH = (By.NAME, "title")
# 营销管理-优惠券,搜索按钮
WMS_BUTTON_MARKETING_COUPON_SEARCH = (By.XPATH, "//*[@id=""search_form""]/div/div/div[2]/div/button/i")
# 营销管理-优惠券-添加优惠券
WMS_BUTTON_MARKETING_COUPON_ADD = (By.XPATH, "//a[contains(text(),'添加优惠券')]")
# 营销管理-优惠券-添加优惠券,标题
WMS_BUTTON_MARKETING_COUPON_ADD_TIT = (By.XPATH, "/html/body/div[3]/div[2]/div/div[2]/div/form/table/tbody[1]/tr[1]/td[2]/input")
# 营销管理-优惠券-添加优惠券,备注
WMS_BUTTON_MARKETING_COUPON_ADD_REMARK = (By.XPATH, "/html/body/div[3]/div[2]/div/div[2]/div/form/table/tbody[1]/tr[2]/td[2]/input")
# ###发放主站
####Coupon_Add  = ( By.XPATH,"//*[@id=""search_form""]/div/div/div[3]")
# 营销管理-优惠券-添加优惠券-优惠券类型
# 营销管理-优惠券-添加优惠券-优惠券类型,通用券
WMS_BUTTON_MARKETING_COUPON_ADD_CURRENCY = (
By.XPATH, "/html/body/div[3]/div[2]/div/div[2]/div/form/table/tbody[1]/tr[4]/td[2]/label[1]/input")
# 营销管理-优惠券-添加优惠券-优惠券类型,新人券
WMS_BUTTON_MARKETING_COUPON_ADD_NEW = (By.XPATH, "/html/body/div[3]/div[2]/div/div[2]/div/form/table/tbody[1]/tr[4]/td[2]/label[2]/input")
# 营销管理-优惠券-添加优惠券-优惠券类型,品类券
WMS_BUTTON_MARKETING_COUPON_ADD_CATEGORY = (
By.XPATH, "/html/body/div[3]/div[2]/div/div[2]/div/form/table/tbody[1]/tr[4]/td[2]/label[3]/input")
# 营销管理-优惠券-添加优惠券-优惠券类型,社区券
WMS_BUTTON_MARKETING_COUPON_ADD_COMMUNITY = (
By.XPATH, "/html/body/div[3]/div[2]/div/div[2]/div/form/table/tbody[1]/tr[4]/td[2]/label[4]/input")
# 营销管理-优惠券-添加优惠券-优惠券类型,单品券
WMS_BUTTON_MARKETING_COUPON_ADD_SINGLE = (By.XPATH, "/html/body/div[3]/div[2]/div/div[2]/div/form/table/tbody[1]/tr[4]/td[2]/label[5]/input")
# 营销管理-优惠券-添加优惠券,数量
WMS_BUTTON_MARKETING_COUPON_ADD_NUMBER = (By.XPATH, "/html/body/div[3]/div[2]/div/div[2]/div/form/table/tbody[1]/tr[5]/td[2]/input")
# 营销管理-优惠券-添加优惠券,抵扣金额
WMS_BUTTON_MARKETING_COUPON_ADD_MONEY = (By.XPATH, "/html/body/div[3]/div[2]/div/div[2]/div/form/table/tbody[1]/tr[6]/td[2]/input")
# 营销管理-优惠券-添加优惠券,重复领取
WMS_BUTTON_MARKETING_COUPON_ADD_REPEAT_YES = (
By.XPATH, "/html/body/div[3]/div[2]/div/div[2]/div/form/table/tbody[1]/tr[7]/td[2]/div/label[1]/input")
WMS_BUTTON_MARKETING_COUPON_ADD_REPEAT_NO = (
By.XPATH, "/html/body/div[3]/div[2]/div/div[2]/div/form/table/tbody[1]/tr[7]/td[2]/div/label[2]/input")
# 营销管理-优惠券-添加优惠券,启用金额
WMS_BUTTON_MARKETING_COUPON_ADD_AMOUNT = (
By.XPATH, "/html/body/div[3]/div[2]/div/div[2]/div/form/table/tbody[2]/tr[1]/td[2]/div/label/input")
# 营销管理-优惠券-添加优惠券,使用有效期
WMS_BUTTON_MARKETING_COUPON_ADD_VALID_DAY = (By.ID, "dateday")
# 营销管理-优惠券-添加优惠券,有效期天数
WMS_BUTTON_MARKETING_COUPON_ADD_VALID_DAY_DAYS = (By.NAME, "coupon[validday]")
# 营销管理-优惠券-添加优惠券,确定按钮
WMS_BUTTON_MARKETING_COUPON_ADD_SURE = (By.ID, "submit")
# 营销管理-优惠券-发放优惠券按钮
WMS_BUTTON_MARKETING_COUPON_ADD_GRANT = (By.XPATH, "//a[contains(text(),'发放优惠券')]")
# 营销管理-优惠券-发放优惠券,发送用户ID
WMS_BUTTON_MARKETING_COUPON_ADD_GRANT_USER_ID = (By.CSS_SELECTOR, "#send_form > table > tbody > tr:nth-child(1) > td:nth-child(2) > textarea")
# faf
WMS_BUTTON_MARKETING_COUPON_ADD_GRANT_COUPON = (By.XPATH, "//a[contains(text(),'发放优惠券')]")
# 营销管理-优惠券-发放优惠券,发送数量
WMS_BUTTON_MARKETING_COUPON_ADD_GRANT_NUMBER = (By.NAME, "num")
# 营销管理-优惠券-发放优惠券,发送按钮
WMS_BUTTON_MARKETING_COUPON_ADD_GRANT_SEND = (By.CSS_SELECTOR, "#send_form > table > tfoot > tr > td > button")
# 营销管理-优惠券-添加数量
WMS_BUTTON_MARKETING_COUPON_QUANTITY_ADD = (By.XPATH, "//*[@id=""adminlist""]/tbody/tr[1]/td[13]/a[1]")
# 营销管理-优惠券-添加数量,增加优惠券数量
WMS_BUTTON_MARKETING_COUPON_QUANTITY_ADD_NUMBER = (By.NAME, "couponnum")
# 营销管理-优惠券-添加数量,确定按钮
WMS_BUTTON_MARKETING_COUPON_QUANTITY_ADD_SURE = (By.XPATH, "//*[@id=""couponnum""]/div[2]/div/div[3]/button[1]")
# 营销管理-优惠券-添加数量,取消按钮
WMS_BUTTON_MARKETING_COUPON_QUANTITY_ADD_CANCEL = (By.XPATH, "//*[@id=""couponnum""]/div[2]/div/div[3]/button[2]")
# 营销管理-优惠券-开始
WMS_BUTTON_MARKETING_COUPON_START = (By.XPATH, "//a[contains(text(),'启动')]")
# 营销管理-优惠券-开始,开始二次确认
WMS_BUTTON_MARKETING_COUPON_START_SURE = (By.CSS_SELECTOR, "body > div.myModa > div > div > div:nth-child(2) > div")
# 营销管理-优惠券-开始,三次确认
WMS_BUTTON_MARKETING_COUPON_START_SURE_ONE = (By.CSS_SELECTOR, "body > div.myModa > div > div")
WMS_BUTTON_MARKETING_COUPON_START_SURE_NO = (By.XPATH, "/html/body/div[5]/div/div/div[1]/div")
# 营销管理-优惠券-删除
WMS_BUTTON_MARKETING_COUPON_DEL = (By.XPATH, "//a[contains(text(),'删除')]")
# 营销管理-优惠券-停止
WMS_BUTTON_MARKETING_COUPON_STOP = (By.XPATH, "//*[@id=""adminlist""]/tbody/tr[1]/td[13]/a[2]")
# 营销管理-优惠券-停止,停止二次确认
WMS_BUTTON_MARKETING_COUPON_STOP_SURE = (By.XPATH, "/html/body/div[5]/div/div/div[2]/div")
WMS_BUTTON_MARKETING_COUPON_STOP_NO = (By.XPATH, "/html/body/div[5]/div/div/div[1]/div")
# 营销管理-优惠券-复制
WMS_BUTTON_MARKETING_COUPON_COPY = (By.XPATH, "//a[contains(text(),'复制')]")
# 营销管理-优惠券-编辑
WMS_BUTTON_MARKETING_COUPON_EDIT = (By.XPATH, "//*[@id=""adminlist""]/tbody/tr[1]/td[13]/a[4]")
# 营销管理-优惠券-编辑,标题
WMS_BUTTON_MARKETING_COUPON_EDIT_TIT = (By.XPATH, "/html/body/div[3]/div[2]/div/div[2]/div/form/table/tbody/tr[1]/td[2]/input")
# 营销管理-优惠券-编辑,备注#
WMS_BUTTON_MARKETING_COUPON_EDIT_REMARKS = (By.XPATH, "/html/body/div[3]/div[2]/div/div[2]/div/form/table/tbody/tr[2]/td[2]/input[1]")
##########################################################################################################################################
# 营销管理-活动管理
WMS_BUTTON_MARKETING_ACTIVITY = (By.XPATH, "//*[@id=""adminlist""]/tbody/tr[1]/td[13]/a[3]")
# 营销管理-活动管理-活动名称输入输入框
WMS_INPUT_MARKETING_ACTIVITY_SEARCH = (By.XPATH, "//*[@id=""search_form""]/div/div/div[1]/input")
# 营销管理-活动管理-活动名称搜索按钮
WMS_BUTTON_MARKETING_ACTIVITY_SEARCH = (By.XPATH, "//*[@id=""search_form""]/div/div/div[1]/div/button/i")
# 营销管理-活动管理-添加活动
WMS_BUTTON_MARKETING_ACTIVITY_ADD = (By.XPATH, "//*[@id=""search_form""]/div/div/div[2]/a")
# 营销管理-活动管理-启动??????????
WMS_BUTTON_MARKETING_ACTIVITY_START = (By.XPATH, "//*[@id=""adminlist""]/tbody/tr[1]/td[13]/a[3]")
# 营销管理-活动管理-停止???????????
WMS_BUTTON_MARKETING_ACTIVITY_STOP = (By.XPATH, "//*[@id=""adminlist""]/tbody/tr[1]/td[13]/a[3]")
# 营销管理-活动管理-编辑????????????
WMS_BUTTON_MARKETING_ACTIVITY_EDIT = (By.XPATH, "//*[@id=""adminlist""]/tbody/tr[1]/td[13]/a[3]")
#######################################################################################################################################
# 营销管理-天降红包
WMS_BUTTON_MARKETING_RED_ENVELOPES = (By.ID, "navi467")
# 营销管理-天降红包,活动时间
WMS_BUTTON_MARKETING_RED_ENVELOPES_ACTIVITY_TIME = (By.NAME, "activity_time")
# 营销管理-天降红包,活动名称
WMS_BUTTON_MARKETING_RED_ENVELOPES_ACTIVITY_NAME = (By.NAME, "activity_name")
# 营销管理-天降红包,活动ID
WMS_BUTTON_MARKETING_RED_ENVELOPES_REWARD_ID = (By.NAME, "skyward_reward_id")
# 营销管理-天降红包,创建人
WMS_BUTTON_MARKETING_RED_ENVELOPES_CREATE_NAME = (By.NAME, "create_name")
# 营销管理-天降红包,创建时间
WMS_BUTTON_MARKETING_RED_ENVELOPES_CREATE_TIME = (By.NAME, "create_time")
# 营销管理-天降红包,查询
WMS_BUTTON_MARKETING_RED_ENVELOPES_SEARCH = (By.ID, "searchBtn")
# 营销管理-天降红包,查看
WMS_BUTTON_MARKETING_RED_ENVELOPES_SEE = (By.XPATH, "//*[@id=""adminlist""]/tbody/tr[1]/td[10]/a[1]")
# 营销管理-天降红包,下线
WMS_BUTTON_MARKETING_RED_ENVELOPES_UP = (By.XPATH, "//*[@id=""adminlist""]/tbody/tr[1]/td[10]/a[2]")
# 营销管理-天降红包,复制
WMS_BUTTON_MARKETING_RED_ENVELOPES_COPY = (By.XPATH, "//*[@id=""adminlist""]/tbody/tr[1]/td[10]/a[3]")
# 营销管理-天降红包,数据
WMS_BUTTON_MARKETING_RED_ENVELOPES_COUPON_DATA = (By.XPATH, "//*[@id=""adminlist""]/tbody/tr[1]/td[10]/a[4]")
# 营销管理-天降红包,新建
WMS_BUTTON_MARKETING_RED_ENVELOPES_ADD = (By.XPATH, "//a[@onclick='add()']")
# 营销管理-天降红包,活动名称
WMS_BUTTON_MARKETING_RED_ENVELOPES_ADD_ACTIVITY_NAME = (
By.XPATH, "/html/body/div[3]/div[2]/div/div[2]/div/form/table/tbody/tr[1]/td[2]/input")
# 营销管理-天降红包,添加券
WMS_BUTTON_MARKETING_RED_ENVELOPES_ADD_COUPON_ID = (By.XPATH, "/html/body/div[3]/div[2]/div/div[2]/div/form/table/tbody/tr[6]/td[2]/input")
# 营销管理-天降红包,校验
WMS_BUTTON_MARKETING_RED_ENVELOPES_ADD_CHECK_COUPON = (By.ID, "checkcoupon")
# 营销管理-天降红包,校验確定
WMS_BUTTON_MARKETING_RED_ENVELOPES_ADD_CHECK_COUPON_SURE = (By.XPATH, "/html/body/div[8]/div/div")
# 营销管理-天降红包,确定#
WMS_BUTTON_MARKETING_RED_ENVELOPES_ADD_SUBMIT = (By.XPATH, "//button[@id='submit']")
################################################################################################################
# 营销管理-秒杀管理
WMS_BUTTON_MARKETING_KILL = (By.ID, "navi329")
# 营销管理-秒杀管理,新建秒杀
WMS_BUTTON_MARKETING_KILL_ADD = (By.CSS_SELECTOR, ".fa-plus")
# 营销管理-秒杀管理,秒杀开始时间
WMS_BUTTON_MARKETING_KILL_START_TIME = (By.CSS_SELECTOR, "#add_starttime > input:nth-child(1)")
# 营销管理-秒杀管理,秒杀结束时间
WMS_BUTTON_MARKETING_KILL_END_TIME = (By.CSS_SELECTOR, "#add_endtime > input:nth-child(1)")
# 营销管理-秒杀管理,保存
WMS_BUTTON_MARKETING_KILL_SAVE = (By.ID, "save_seckill")
# 营销管理-秒杀管理-编辑
WMS_BUTTON_MARKETING_KILL_EDIT = (By.ID, "edit_merchandise")
# 营销管理-秒杀管理-编辑, 选择商品
WMS_BUTTON_MARKETING_KILL_EDIT_CHOOSE = (By.CSS_SELECTOR, ".filter-option")
# 营销管理-秒杀管理-编辑,搜索输入框
WMS_INPUT_MARKETING_KILL_EDIT_SEARCH = (By.CSS_SELECTOR, ".bs-searchbox > input:nth-child(1)")
# 营销管理-秒杀管理-编辑,选定商品
WMS_BUTTON_MARKETING_KILL_EDIT_CHOOSE_SURE = (By.CSS_SELECTOR, ".inner > li:nth-child(1) > a:nth-child(1) > span:nth-child(1)")
# 营销管理-秒杀管理-编辑,添加按钮
WMS_BUTTON_MARKETING_KILL_EDIT_ADD = (By.XPATH, "//a[contains(text(),'添加')]")
# 营销管理-秒杀管理-编辑,上传
WMS_BUTTON_MARKETING_KILL_EDIT_UPLOAD = (By.XPATH, "//a[contains(text(),'上传')]")
# 营销管理-秒杀管理-编辑,选择图片
WMS_BUTTON_MARKETING_KILL_EDIT_UPLOAD_PHOTO = (By.ID, "file2upload")
# 营销管理-秒杀管理-编辑,上传文件
WMS_BUTTON_MARKETING_KILL_EDIT_UPLOAD_FILE = (By.CSS_SELECTOR, "#btnfileupload")
# 营销管理-秒杀管理-编辑,送货时间
WMS_BUTTON_MARKETING_KILL_EDIT_DELIVER_GOODS_TIME = (By.CSS_SELECTOR, ".merchandiseid_22 > td:nth-child(8) > input:nth-child(1)")
# 营销管理-秒杀管理-编辑,选择送货时间
WMS_BUTTON_MARKETING_KILL_EDIT_SELECT_DELIVER_GOODS_TIME = (
By.CSS_SELECTOR, ".datetimepicker-days > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(5) > td:nth-child(7)")
# 营销管理-秒杀管理-编辑,保存
WMS_BUTTON_MARKETING_KILL_EDIT_SAVE = (By.ID, "one-click-save")
# 营销管理-秒杀管理-编辑,修改
WMS_BUTTON_MARKETING_KILL_EDIT_UPDATE = (By.XPATH, "//a[contains(text(),'修改')]")
# 营销管理-秒杀管理-编辑,秒杀详情
WMS_BUTTON_MARKETING_KILL_EDIT_DETAILS = (By.CSS_SELECTOR, ".page-breadcrumb > li:nth-child(2) > a:nth-child(1) > samp:nth-child(1)")
# 营销管理-秒杀管理,启售
WMS_BUTTON_MARKETING_KILL_OPEN = (By.XPATH, "//a[contains(text(),'启售')]")
WMS_BUTTON_MARKETING_KILL_OPEN_SURE = (By.CSS_SELECTOR, "div.btn")
# 营销管理-秒杀管理-编辑,起售div.btn
WMS_BUTTON_MARKETING_KILL_START = (By.XPATH, "//a[contains(text(),'起售')]")
WMS_BUTTON_MARKETING_KILL_START_SURE = (By.CSS_SELECTOR, ".sure")
# 停售
# 全部停售
# #######################################################################################################################################################################################################
