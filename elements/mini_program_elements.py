# coding=utf-8
# coding=utf-8

from appium.webdriver.common.mobileby import MobileBy

# 进入微信我的
WeChar_mine = (MobileBy.ANDROID_UIAUTOMATOR, 'text("我")')
# 进入微信首页
WeChar_home = (MobileBy.ANDROID_UIAUTOMATOR, 'text("微信")')
# 进入微信设置
WeChar_set = (MobileBy.ANDROID_UIAUTOMATOR, 'text("设置")')
# 进入切换账号
WeChar_switch = (MobileBy.ANDROID_UIAUTOMATOR, 'text("切换账号")')
#######################################################################3
#  进入团员端聊天页面
Mine_name_liutingting = (MobileBy.ANDROID_UIAUTOMATOR, 'text("刘亭亭")')
Mine_name_xingxing = (MobileBy.ANDROID_UIAUTOMATOR, 'text("星星")')
#  进入团长端聊天页面
Mine_regimental = (MobileBy.ANDROID_UIAUTOMATOR, 'text("sht@2")')
Mine_regimental_zhangshanshan = (MobileBy.ANDROID_UIAUTOMATOR, 'text("张珊珊")')
Mine_regimental_jisiyu = (MobileBy.ANDROID_UIAUTOMATOR, 'text("冀思雨")')
# 打开小程序
Mine_shihuituan = (MobileBy.ANDROID_UIAUTOMATOR, 'text("十荟团")')
# 设置为默认团长

Mine_default_leader = (MobileBy.ANDROID_UIAUTOMATOR, 'text("设置默认团长")')
# 选择其他团长
Mine_other_leader = (MobileBy.ANDROID_UIAUTOMATOR, 'text("选择其他团长")')
# 您进入了其他团长的团购
Mine_other = (MobileBy.ANDROID_UIAUTOMATOR, 'text("您进入了其他团长的团购")')
# 本次访问团长
# Mine_default = (MobileBy.ANDROID_UIAUTOMATOR, '("text("本次访问的团长")')

# 选择默认团长
# Mine_select = (MobileBy.ANDROID_UIAUTOMATOR, 'className( "选择")')
# Mine_select = (MobileBy.ANDROID_UIAUTOMATOR, 'className("十荟团")')
# 我的页面
# 我的按钮
Mine_button = (MobileBy.ANDROID_UIAUTOMATOR, 'text("我的")')

# 获取微信信息页面
# 取消
Mine_cancel = (MobileBy.ANDROID_UIAUTOMATOR, 'text( "取消")')
# 允许
Mine_permit = (MobileBy.ANDROID_UIAUTOMATOR, 'text( "允许")')
# 刷新信息提示
Mine_renovate = (MobileBy.ANDROID_UIAUTOMATOR, 'text( "是否更新您的个人信息，每天止咳刷新一次")')
# 刷新按钮
Mine_renovate_button = (MobileBy.ANDROID_UIAUTOMATOR, 'text( "刷新")')

# 累计收益
Mine_profit = (MobileBy.ANDROID_UIAUTOMATOR, 'text( "累计收益(元)")')
# 累计收益页面
# 我的收益标题
Mine_my_profit = (MobileBy.ANDROID_UIAUTOMATOR, 'text( "我的收益")')
# 以获得收益
Mine_profit_money = (MobileBy.ANDROID_UIAUTOMATOR, 'text( "恭喜您通过十荟团开团已获得收益")')
# 月收益
Mine_monthly_income = (MobileBy.ANDROID_UIAUTOMATOR, 'text( "月收益")')
# 已到账
Mine_arrival_accounts = (MobileBy.ANDROID_UIAUTOMATOR, 'text( "已到账")')
# 未到账
Mine_outstanding_account = (MobileBy.ANDROID_UIAUTOMATOR, 'text( "未到账")')
# 应到账
Mine_payable_account = (MobileBy.ANDROID_UIAUTOMATOR, 'text( "未到账")')

# 账户余额
Mine_balance = (MobileBy.ANDROID_UIAUTOMATOR, 'text( "账户余额(元)")')
# 账户页面
# 我的账户标题
Mine_my_accounts = (MobileBy.ANDROID_UIAUTOMATOR, 'text( "我的账户")')
# 账户余额
Mine_account_balances = (MobileBy.ANDROID_UIAUTOMATOR, 'text( "账户余额")')
# 我的银行卡
Mine_bankcard = (MobileBy.ANDROID_UIAUTOMATOR, 'text( "我的银行卡")')
# 交易记录
Mine_records = (MobileBy.ANDROID_UIAUTOMATOR, 'text( "交易记录")')
# 申请提现
Mine_withdraw = (MobileBy.ANDROID_UIAUTOMATOR, 'text( "申请提现")')
# 关注提现状态
Mine_withdrawal_status = (MobileBy.ANDROID_UIAUTOMATOR, 'text( "点击关注提现状态")')
# 提现说明
Mine_explain = (MobileBy.ANDROID_UIAUTOMATOR, 'text( "提现说明")')
# 知道了按钮
Mine_see = (MobileBy.ANDROID_UIAUTOMATOR, 'text( "知道了")')

# 消息
Mine_news = (MobileBy.ANDROID_UIAUTOMATOR, 'text( "android.widget.Image")')
# 消息页面
# 退出参团提示
Mine_quit_news = (MobileBy.ANDROID_UIAUTOMATOR, 'text( "退出参团")')
# 新订单提示
Mine_new_order = (MobileBy.ANDROID_UIAUTOMATOR, 'text( "新订单")')
# 参团成功
Mine_successful_delegation = (MobileBy.ANDROID_UIAUTOMATOR, 'text( "参团成功")')

# 销量排行
Mine_sales_rankings = (MobileBy.ANDROID_UIAUTOMATOR, 'text("查看销量排行")')

# 查看销量排行页面
# 月销量排名
Mine_monthly_sales_rankings = (MobileBy.ANDROID_UIAUTOMATOR, 'text("月销量排名")')
# 排名TOP5
Mine_monthlyTOP5 = (MobileBy.ANDROID_UIAUTOMATOR, 'text("团长月销量TOP5")')

# 业绩中心功能
Mine_performance = (MobileBy.ANDROID_UIAUTOMATOR, 'text("业绩中心")')
# 查看全部
Mine_see_all = (MobileBy.ANDROID_UIAUTOMATOR, 'text("查看全部 ")')

# 当前团销售额
Mine_current_group_sales = (MobileBy.ANDROID_UIAUTOMATOR, 'text("当前团销售额(元)")')
# 主订单数量
Mine_quantity_order = (MobileBy.ANDROID_UIAUTOMATOR, 'text("主订单数量")')
# 当前团赚
Mine_team = (MobileBy.ANDROID_UIAUTOMATOR, 'text("当前团赚(元)")')
# 当前没有团
Mine_no_team = (MobileBy.ANDROID_UIAUTOMATOR, 'text( "若当前没有团，显示上一个团的销售额和应到账收益")')

# 业绩中心页面
# 我的销售业绩
Mine_sales_performance = (MobileBy.ANDROID_UIAUTOMATOR, 'text( "我的销售业绩")')
# 提示
Mine_prompt = (MobileBy.ANDROID_UIAUTOMATOR, 'text( "提示:销售业绩会随着订单取消或售后退款而变化，仅供参考")')
# 月账单
Mine_monthly_bill = (MobileBy.ANDROID_UIAUTOMATOR, 'text( "月账单")')
# 团账单
Mine_regiment_bill = (MobileBy.ANDROID_UIAUTOMATOR, 'text( "团账单")')
# 合计业绩
Mine_aggregate_performance = (MobileBy.ANDROID_UIAUTOMATOR, 'text( "合计业绩")')
# 销售额
Mine_sales_volume = (MobileBy.ANDROID_UIAUTOMATOR, 'text( "销售额")')
# 赚
Mine_profits = (MobileBy.ANDROID_UIAUTOMATOR, 'text( "赚")')
# 业绩中心返回
Mine_go_back = (MobileBy.ANDROID_UIAUTOMATOR, 'resourceId( "com.tencent.mm:id/q0")')

# 我的团购功能
# 我的团购
Mine_group_buy = (MobileBy.ANDROID_UIAUTOMATOR, 'text( "我的团购")')
# 历史开团
Mine_historical_opening = (MobileBy.ANDROID_UIAUTOMATOR, 'text( "历史开团")')
# 配送跟踪
Mine_distribution_tracking = (MobileBy.ANDROID_UIAUTOMATOR, 'text( "配送跟踪")')
# 签收码
Mine_sign_code = (MobileBy.ANDROID_UIAUTOMATOR, 'text( "签收码")')
# 到货提醒
Mine_arrival_reminder = (MobileBy.ANDROID_UIAUTOMATOR, 'text( "到货提醒")')
# 扫码提货
Mine_sweep_yards = (MobileBy.ANDROID_UIAUTOMATOR, 'text( "扫码提货")')
# 待提货订单
Mine_order_picked_up = (MobileBy.ANDROID_UIAUTOMATOR, 'text( "待提货订单")')
# 待提货手机号
#phone_a = 18501355438
#待提货姓名
#name_a = 测试2
# 售后反馈
Mine_after_sales_feedback = (MobileBy.ANDROID_UIAUTOMATOR, 'text( "售后反馈")')
# 送货上门设置
Mine_home_delivery_service = (MobileBy.ANDROID_UIAUTOMATOR, 'text( "送货上门设置")')
# 送货预告
Mine_delivery_notice = (MobileBy.ANDROID_UIAUTOMATOR, 'text( "送货预告")')
# 佣金记录
Mine_commission_record = (MobileBy.ANDROID_UIAUTOMATOR, 'text( "佣金记录")')

# 历史开团页面
# 我的开团
Mine_my_regimen = (MobileBy.ANDROID_UIAUTOMATOR, 'text( "我的开团")')
# 用户id
Mine_user_id = (MobileBy.ANDROID_UIAUTOMATOR, 'text( "用户ID ：")')
# 搜索按钮
Mine_search_button = (MobileBy.ANDROID_UIAUTOMATOR, 'text("订单搜索")')

# 订单搜索页面
# 手机号
Mine_phone = (MobileBy.ANDROID_UIAUTOMATOR, 'text("手机号")')
# 商品名
Mine_goods = (MobileBy.ANDROID_UIAUTOMATOR, 'text("商品名")')
# 输入框
Mine_edit = (MobileBy.ANDROID_UIAUTOMATOR, 'text("请输入用户ID/微信昵称/手机号")')
# 搜索
Mine_search = (MobileBy.ANDROID_UIAUTOMATOR, 'text("搜索")')

# 团购订单
Mine_group_purchase_order = (MobileBy.ANDROID_UIAUTOMATOR, 'text("团购订单")')
# 秒杀订单
Mine_spike_order = (MobileBy.ANDROID_UIAUTOMATOR, 'text("秒杀订单")')
# 未结束
Mine_not_finished = (MobileBy.ANDROID_UIAUTOMATOR, 'text("距离结束")')
# 已结束
Mine_ends = (MobileBy.ANDROID_UIAUTOMATOR, 'text("距离结束")')
# 团购ID
Mine_offer_id = (MobileBy.ANDROID_UIAUTOMATOR, 'text("团购ID")')
# 参团人数
Mine_offer_number = (MobileBy.ANDROID_UIAUTOMATOR, 'text("参团人数")')
# 团员订单
Mine_offer_order = (MobileBy.ANDROID_UIAUTOMATOR, 'text("团员订单")')
# 下载订单
Mine_down_load_order = (MobileBy.ANDROID_UIAUTOMATOR, 'text("下载订单")')
# 已经到底通知
Mine_end_new = (MobileBy.ANDROID_UIAUTOMATOR, 'text("已经到底了~")')

# 团员订单页面
# 搜索团员订单
Mine_search_order = (MobileBy.ANDROID_UIAUTOMATOR, 'text("请输入序号/姓名/手机号")')
# 本团预计收益
Mine_prospective_yield = (MobileBy.ANDROID_UIAUTOMATOR, 'text("本团预计收益")')
# 本团总计实付
Mine_total_paid_in = (MobileBy.ANDROID_UIAUTOMATOR, 'text("本团总计实付")')
# 查看明细
Mine_details_view = (MobileBy.ANDROID_UIAUTOMATOR, 'text("查看明细")')

# 签收码页面
# 查看路线
Mine_straight = (MobileBy.ANDROID_UIAUTOMATOR, 'text("查看路线")')
# 文字提示
Mine_text_prompt = (MobileBy.ANDROID_UIAUTOMATOR, 'text("司机师傅配送完成后，请向司机师傅展示签收二维码")')

# 到货通知页面
# 发送到货通知标题
Mine_send_notice = (MobileBy.ANDROID_UIAUTOMATOR, 'text("发送到货通知")')
# 今日到货商品
Mine_today_goods = (MobileBy.ANDROID_UIAUTOMATOR, 'text("今日到货商品")')
# 预计到货商品
Mine_estimate_goods = (MobileBy.ANDROID_UIAUTOMATOR, 'text("预计到货商品")')
# 搜索框
Mine_search_goods = (MobileBy.ANDROID_UIAUTOMATOR, 'text("请输入商品名称进行搜索")')
# 已经移出的商品
Mine_leave_goods = (MobileBy.ANDROID_UIAUTOMATOR, 'text("已经移出的商品")')
# 备注
Mine_remarks = (MobileBy.ANDROID_UIAUTOMATOR, 'text("备注")')
# 复制到货信息
Mine_copy = (MobileBy.ANDROID_UIAUTOMATOR, 'text("复制到货信息")')
# 确认发送
Mine_confirm = (MobileBy.ANDROID_UIAUTOMATOR, 'text("确认发送")')
# 完成
Mine_accomplish = (MobileBy.ANDROID_UIAUTOMATOR, 'text("完成")')
# 无内容显示
Mine_no_content = (MobileBy.ANDROID_UIAUTOMATOR, 'text("暂无内容")')

# 扫码提货页面
# 扫一扫
Mine_sweep = (MobileBy.ANDROID_UIAUTOMATOR, 'text("扫一扫")')
# 手机微信昵称查询
Mine_phone_inquires = (MobileBy.ANDROID_UIAUTOMATOR, 'text("手机/微信昵称查询")')
# 查询输入框
Mine_phone_text = (MobileBy.ANDROID_UIAUTOMATOR, 'text("请输入手机/微信昵称")')
# 查询按钮
Mine_inquiries_button = (MobileBy.ANDROID_UIAUTOMATOR, 'text("查询")')
# 查询不存在内容
Mine_inquiries_a = (MobileBy.ANDROID_UIAUTOMATOR, 'text("111")')
# 查询手机号
Mine_inquiries_b = (MobileBy.ANDROID_UIAUTOMATOR, 'text("17330291054")')

# 待提货订单页面
# 手机号
Mine_phone_number = (MobileBy.ANDROID_UIAUTOMATOR, 'text("手机号")')
# 微信昵称
Mine_pet_name = (MobileBy.ANDROID_UIAUTOMATOR, 'text("微信昵称")')
# 姓名
Mine_names = (MobileBy.ANDROID_UIAUTOMATOR, 'text("姓名")')
# 搜索框
Mine_name_edit_text = (MobileBy.ANDROID_UIAUTOMATOR, 'text("请输入微信昵称/姓名/手机号")')
# 未提走
Mine_no_lift_away = (MobileBy.ANDROID_UIAUTOMATOR, 'text( "未提走")')
# 已提走
Mine_lift_away = (MobileBy.ANDROID_UIAUTOMATOR, 'text("已提走")')

# 售后反馈页面
# 售后页面标题
Mine_aftermarket = (MobileBy.ANDROID_UIAUTOMATOR, 'text("售后/反馈")')
# 全部
Mine_all_aftermarket = (MobileBy.ANDROID_UIAUTOMATOR, 'text("全部")')
# 待审核
Mine_auditing = (MobileBy.ANDROID_UIAUTOMATOR, 'text("待审核")')
# 进行中
Mine_goon = (MobileBy.ANDROID_UIAUTOMATOR, 'text("进行中")')
# 已完成
Mine_done = (MobileBy.ANDROID_UIAUTOMATOR, 'text("已完成")')
# 售后单搜索
Mine_after_sale_list = (MobileBy.ANDROID_UIAUTOMATOR, 'text("商品名称\\团员昵称\\手机号后四位进行搜索")')
# 无工单提示
Mine_no_sale_list = (MobileBy.ANDROID_UIAUTOMATOR, 'text("您没有处理中的工单哦")')
# 创建工单按钮
Mine_job_order = (MobileBy.ANDROID_UIAUTOMATOR, 'text("创建工单")')

# 送货设置页面
# 自提/送货设置
Mine_settings = (MobileBy.ANDROID_UIAUTOMATOR, 'text("自提/送货设置")')
# 自提
Mine_self_mention = (MobileBy.ANDROID_UIAUTOMATOR, 'text("自提")')
# 送货上门
Mine_door = (MobileBy.ANDROID_UIAUTOMATOR, 'text("送货上门")')
Mine_door_a = (MobileBy.ANDROID_UIAUTOMATOR, 'text("送货上门".index(2))')


# 运费
Mine_freight = (MobileBy.ANDROID_UIAUTOMATOR, 'text("运费")')
# 运费输入框
Mine_im_freight = (MobileBy.ANDROID_UIAUTOMATOR, 'text("请输入运费")')
# 保存
Mine_save = (MobileBy.ANDROID_UIAUTOMATOR, 'index(1)')

# 送货预告页面
# 送货提示
Mine_delivery_tips = (MobileBy.ANDROID_UIAUTOMATOR, 'text("您可下载配送总单和分拣单")')
# 下载送货清单
Mine_download = (MobileBy.ANDROID_UIAUTOMATOR, 'text("下载送货清单")')
# 今日送货
Mine_deliver_today = (MobileBy.ANDROID_UIAUTOMATOR, 'text("今日送货")')
# 明日送货
Mine_deliver_tomorrow = (MobileBy.ANDROID_UIAUTOMATOR, 'text("明日送货")')
# 无待取货订单
Mine_noorder = (MobileBy.ANDROID_UIAUTOMATOR, 'text("无待取货订单")')

# 佣金记录页面
# 查询
Mine_inquiries = (MobileBy.ANDROID_UIAUTOMATOR, 'text("查询")')
# 佣金总计
Mine_total_commission = (MobileBy.ANDROID_UIAUTOMATOR, 'text("佣金总计")')
# 待到账
Mine_wait_account = (MobileBy.ANDROID_UIAUTOMATOR, 'text("待到账")')
# 已到账
Mine_arrival_account = (MobileBy.ANDROID_UIAUTOMATOR, 'text("已到账")')
# 实付
Mine_nhr = (MobileBy.ANDROID_UIAUTOMATOR, 'text("实付")')
# 比例
Mine_proportion = (MobileBy.ANDROID_UIAUTOMATOR, 'text("比例")')

# 营销工具功能
# 营销工具
Mine_marketing_tools = (MobileBy.ANDROID_UIAUTOMATOR, 'text("营销工具")')
# 投票
Mine_vote = (MobileBy.ANDROID_UIAUTOMATOR, 'text("点击为你想要的功能投票")')
# 开团海报页面
# 开团海报
Mine_opening_poster = (MobileBy.ANDROID_UIAUTOMATOR, 'text("开团海报")')
# 开团海报提示
Mine_poster_tips = (MobileBy.ANDROID_UIAUTOMATOR, 'text("点击图片预览，长按保存图片，发送至群即可")')
# 保存海报
Mine_save_poster = (MobileBy.ANDROID_UIAUTOMATOR, 'text("保存海报")')

# 管理功能
# 管理
Mine_manage = (MobileBy.ANDROID_UIAUTOMATOR, 'text("管理")')
# 副团长管理
Mine_deputy_head_management = (MobileBy.ANDROID_UIAUTOMATOR, 'text("副团长管理")')
# 团员管理
Mine_league_member_management = (MobileBy.ANDROID_UIAUTOMATOR, 'text("团员管理")')

# 副团长管理页面
# 未添加副团长
Mine_deputy_head_not_add = (MobileBy.ANDROID_UIAUTOMATOR, 'text("还未添加副团长")')
# 最多添加
Mine_maximum_add = (MobileBy.ANDROID_UIAUTOMATOR, 'text("最多添加20名副团长")')
# 通过用户id添加
Mine_user_id_add = (MobileBy.ANDROID_UIAUTOMATOR, 'text("通过用户ID添加副团长")')
# 添加副团长页面
# 输入用户id
Mine_enter_id = (MobileBy.ANDROID_UIAUTOMATOR, 'text("输入用户ID")')
# 请输入用户id
Mine_p_enter_id = (MobileBy.ANDROID_UIAUTOMATOR, 'text("请输入用户ID")')
# 添加
Mine_add_user = (MobileBy.ANDROID_UIAUTOMATOR, 'text("添加 ")')
# 冀思雨团员id
Mine_add_user_a = (MobileBy.ANDROID_UIAUTOMATOR, 'text("84182263")')

# 团员管理页面
# 团员id输入
Mine_league_id = (MobileBy.ANDROID_UIAUTOMATOR, 'text("团员ID/昵称")')
# 粉丝数量
Mine_fans_number = (MobileBy.ANDROID_UIAUTOMATOR, 'text("粉丝数量")')
# 月购买人数
Mine_monthly_number = (MobileBy.ANDROID_UIAUTOMATOR, 'text("月购买人数")')
# 团员详情
Mine_details_league_members = (MobileBy.ANDROID_UIAUTOMATOR, 'text("团员详情")')

# 我的订单功能
# 我的订单
Mine_my_order = (MobileBy.ANDROID_UIAUTOMATOR, 'text("我的订单")')

# 待支付
Mine_paid = (MobileBy.ANDROID_UIAUTOMATOR, 'text( "待支付")')
# 待收货
Mine_received = (MobileBy.ANDROID_UIAUTOMATOR, 'text("待收货")')
# 已完成
Mine_finish = (MobileBy.ANDROID_UIAUTOMATOR, 'text("已完成")')
# 已取消
Mine_can_cell = (MobileBy.ANDROID_UIAUTOMATOR, 'text("已取消")')
# 全部
Mine_all = (MobileBy.ANDROID_UIAUTOMATOR, 'text("全部")')
# 我的二维码
Mine_code = (MobileBy.ANDROID_UIAUTOMATOR, '.clickable(false).index(3)')

# 我的订单页面
# 没有符合条件的订单
Mine_no_qualified_orders = (MobileBy.ANDROID_UIAUTOMATOR, 'text("没有符合条件的订单")')
# 已参团
Mine_offered = (MobileBy.ANDROID_UIAUTOMATOR, 'text("已参团")')
# 自提
Mine_self_mentions = (MobileBy.ANDROID_UIAUTOMATOR, 'text("自提")')
# 序号
Mine_order_number = (MobileBy.ANDROID_UIAUTOMATOR, 'text("序号")')
# 订单详情页
Mine_order_details_page = (MobileBy.ANDROID_UIAUTOMATOR, 'text("订单详情")')
# 商品金额
Mine_commodity_amount = (MobileBy.ANDROID_UIAUTOMATOR, 'text("商品金额")')
# 总计
Mine_amount = (MobileBy.ANDROID_UIAUTOMATOR, 'text("总计")')
# 订单编号
Mine_order_id = (MobileBy.ANDROID_UIAUTOMATOR, 'text("订单编号")')
# 收货电话
Mine_receiving_telephone = (MobileBy.ANDROID_UIAUTOMATOR, 'text("收货电话")')
# 下单时间
Mine_order_time = (MobileBy.ANDROID_UIAUTOMATOR, 'text("下单时间")')
# 取消订单
Mine_order_cancel = (MobileBy.ANDROID_UIAUTOMATOR, 'text("取消订单 ")')
# 确定
Mine_sure = (MobileBy.ANDROID_UIAUTOMATOR, 'text("确定 ")')
# 取消订单的确定
Cart_sure = (MobileBy.ANDROID_UIAUTOMATOR, 'text("确定")')
# 确认
Mine_true = (MobileBy.ANDROID_UIAUTOMATOR, 'text("确认")')

# 取消
Mine_cancelled = (MobileBy.ANDROID_UIAUTOMATOR, 'text("取消")')
# 再想想
Mine_think = (MobileBy.ANDROID_UIAUTOMATOR, 'text("再想想")')
# 查看订单
Mine_view_orders = (MobileBy.ANDROID_UIAUTOMATOR, 'text("查看订单")')
# 支付成功
Mine_pay_success = (MobileBy.ANDROID_UIAUTOMATOR, 'text("支付成功")')
# 继续逛
Mine_go_on = (MobileBy.ANDROID_UIAUTOMATOR, 'text("继续逛")')
# 分享给团长，提醒接单
Mine_warm = (MobileBy.ANDROID_UIAUTOMATOR, 'text("分享给团长，提醒接单")')
# 优惠券
Mine_coupon = (MobileBy.ANDROID_UIAUTOMATOR, 'text("优惠券")')
# 优惠券页面
# 通用券
Mine_universal_coupon = (MobileBy.ANDROID_UIAUTOMATOR, 'text("通用券")')

# 订单满1减1
Mine_minus = (MobileBy.ANDROID_UIAUTOMATOR, 'text("订单满1减1")')
# 查看历史优惠券
Mine_historical_coupon = (MobileBy.ANDROID_UIAUTOMATOR, 'text("查看历史优惠券")')
# 优惠券数量
Mine_number_coupon = (MobileBy.ANDROID_UIAUTOMATOR, 'text("19 张")')

# 已使用
Mine_have_made = (MobileBy.ANDROID_UIAUTOMATOR, 'text("已使用")')
# 暂无可用
Mine_cannot = (MobileBy.ANDROID_UIAUTOMATOR, 'text("暂无可用")')
# 不使用优惠券
Mine_not_make = (MobileBy.ANDROID_UIAUTOMATOR, 'text("不使用优惠券")')
# 单品券
Mine_single = (MobileBy.ANDROID_UIAUTOMATOR, 'text("自动化单品券84183035(1702840)")')

# 我的银行卡
Mine_my_bankcard = (MobileBy.ANDROID_UIAUTOMATOR, 'text("我的银行卡")')
# 关于十荟团
Mine_about = (MobileBy.ANDROID_UIAUTOMATOR, 'text("关于十荟团")')

# 关于十荟团页面
# 资质信息
Mine_qualification = (MobileBy.ANDROID_UIAUTOMATOR, 'text("资质信息")')
# 隐私权政策
Mine_privacy = (MobileBy.ANDROID_UIAUTOMATOR, 'text("隐私权政策")')

# 邀请注册团长
Mine_invite = (MobileBy.ANDROID_UIAUTOMATOR, 'text("邀请好友注册团长")')
# 邀请注册页面
# 微信好友
Mine_friends = (MobileBy.ANDROID_UIAUTOMATOR, 'text("微信好友")')
# 页面提示
Mine_friends_text = (MobileBy.ANDROID_UIAUTOMATOR, 'text("好友扫一扫二维码即可注册成为团长")')
# 保存图片
Mine_save_images = (MobileBy.ANDROID_UIAUTOMATOR, 'text("保存图片")')

# 休息
Mine_rest = (MobileBy.ANDROID_UIAUTOMATOR, 'text("休息")')
# 声音开关
Mine_sound = (MobileBy.ANDROID_UIAUTOMATOR, 'text("声音开关")')
# 服务通知电话显示
Mine_notice = (MobileBy.ANDROID_UIAUTOMATOR, 'text("服务通知电话显示")')
# 文本通知显示提货码
Mine_text_notice = (MobileBy.ANDROID_UIAUTOMATOR, 'text("文本通知显示提货码")')

Home_friend = (MobileBy.ANDROID_UIAUTOMATOR, 'text("微信好友")')
# 微信好友:团员
Home_my_friend_zhongguo = (MobileBy.ANDROID_UIAUTOMATOR, 'text("中国联通")')
# 发送
Home_send = (MobileBy.ANDROID_UIAUTOMATOR, 'text("发送")')
# 生成海报
Home_create = (MobileBy.ANDROID_UIAUTOMATOR, 'text("生成海报")')
# 下载图片
Home_picture = (MobileBy.ANDROID_UIAUTOMATOR, 'text("下载图片")')

# 团长名称
Home_commander = (MobileBy.ANDROID_UIAUTOMATOR, 'text("王大法")')
# 粉丝
Home_fans = (MobileBy.ANDROID_UIAUTOMATOR, 'text("粉丝")')
# 十荟团
Home_sht = (MobileBy.ANDROID_UIAUTOMATOR, 'text("十荟团")')
# 分享
Home_share = (MobileBy.ANDROID_UIAUTOMATOR, 'text("分享")')
# 今日团购
Home_group = (MobileBy.ANDROID_UIAUTOMATOR, 'text("今日团购")')
# 结束时间
Home_end_time = (MobileBy.ANDROID_UIAUTOMATOR, 'text("距结束")')

# 热卖
Home_best_sellers = (MobileBy.ANDROID_UIAUTOMATOR, 'text("热卖")')
# 精选特惠
Home_preferential_treatment = (MobileBy.ANDROID_UIAUTOMATOR, 'text("精选特惠")')
# 荟精选
Home_selected = (MobileBy.ANDROID_UIAUTOMATOR, 'text("荟精选")')
# 爆款生鲜
Home_fresh = (MobileBy.ANDROID_UIAUTOMATOR, 'text("爆款生鲜")')
# 新人专享
Home_vip = (MobileBy.ANDROID_UIAUTOMATOR, 'text("新人专享")')
# 团长专享
Home_vip_regimental = (MobileBy.ANDROID_UIAUTOMATOR, 'text("新人专享")')
# 大于1元商品名称
Home_product_big_one = (MobileBy.ANDROID_UIAUTOMATOR, 'text("单规格大于1")')
# 小于1元商品名称
Home_product_small_one = (MobileBy.ANDROID_UIAUTOMATOR, 'text("单规格小于1")')
# 零钱金额不足商品名称
Home_product_not_money = (MobileBy.ANDROID_UIAUTOMATOR, 'text("零钱金额不足")')
# 多规格商品名称
Home_product_more_specs = (MobileBy.ANDROID_UIAUTOMATOR, 'text("17028401702840")')
# 库存不足商品名称
Home_product_not_stock = (MobileBy.ANDROID_UIAUTOMATOR, 'text("库存不足库存不足")')
# 存在轮播图的商品
Home_product_video = (MobileBy.ANDROID_UIAUTOMATOR, 'text("测试麻辣")')
# 复制拼团
Home_copy = (MobileBy.ANDROID_UIAUTOMATOR, 'text("复制拼团")')
# 搜索商品
Home_search_goods = (MobileBy.ANDROID_UIAUTOMATOR, 'text("搜索商品")')
# 搜索
Home_search = (MobileBy.ANDROID_UIAUTOMATOR, 'text("搜索")')
# 搜索框内容
Home_input_search = (MobileBy.ANDROID_UIAUTOMATOR, 'text("请输入商品名称进行搜索")')
# 删除
# Home_goods_del= (MobileBy.ANDROID_UIAUTOMATOR, '.clickable(false).index(2)')

# 立即买
Home_imm_buy = (MobileBy.ANDROID_UIAUTOMATOR, 'text("立即买")')

# 二级分类菜单

# 金刚子页面—新鲜蔬菜文本
Home_vegetables_sub_vegetables = (MobileBy.ANDROID_UIAUTOMATOR, 'text("新鲜蔬菜")')
# 金刚子页面—蔬菜
Home_sub_vegetables = (MobileBy.ANDROID_UIAUTOMATOR, 'text("蔬菜")')
# 金刚子页面—绿植
Home_green = (MobileBy.ANDROID_UIAUTOMATOR, 'text("绿植")')
# 金刚子页面—累计销量
Home_sales = (MobileBy.ANDROID_UIAUTOMATOR, 'text("累计销量")')
# 金刚子页面—已团
Home_regiment = (MobileBy.ANDROID_UIAUTOMATOR, 'text("已团")')
# 金刚子页面—剩余
Home_surplus = (MobileBy.ANDROID_UIAUTOMATOR, ' text("剩余")')

# 商品详情页

# 金刚子页面—商品详情页—购物车
Home_cart = (MobileBy.ANDROID_UIAUTOMATOR, '.text("购物车")')
# 金刚子页面—商品详情页—购买数量
Home_purchase_quantity = (MobileBy.ANDROID_UIAUTOMATOR, 'text("购买数量")')
# 加购物车
Home_add_cart = (MobileBy.ANDROID_UIAUTOMATOR, '.className("android.widget.Button").index(3)')

# 立刻购买
Home_buying = (MobileBy.ANDROID_UIAUTOMATOR, '.className("android.widget.Button").index(4)')
# 分类—商品详情页—购买数量
Category_number = (MobileBy.ANDROID_UIAUTOMATOR, 'text("购买数量")')
# 分类—商品详情页—配送
Category_delivery = (MobileBy.ANDROID_UIAUTOMATOR, 'text("配送")')
# 分类—商品详情页—已选
Category_choice = (MobileBy.ANDROID_UIAUTOMATOR, 'text("已选")')
# 分类—商品详情页—参团成员
Category_member = (MobileBy.ANDROID_UIAUTOMATOR, 'text("参团成员")')
# 分类—商品详情页—首页
Category_hge = (MobileBy.ANDROID_UIAUTOMATOR, 'text("首页")')

# 分类—商品详情页—商品详情
Category_details = (MobileBy.ANDROID_UIAUTOMATOR, 'text("商品详情")')
# 分类—商品详情页—分享
Category_share = (MobileBy.ANDROID_UIAUTOMATOR, 'text("分享")')
# 售罄(蒙层)，这个定位方式应该是错误的，后期优化
Category_sell = (MobileBy.ANDROID_UIAUTOMATOR, 'text("售罄")')

##分类##
# 分类
Category_classify = (MobileBy.ANDROID_UIAUTOMATOR, 'text("分类")')
# 猜您喜欢
Category_like = (MobileBy.ANDROID_UIAUTOMATOR, 'text("猜您喜欢")')
# 妈妈食材
Category_mother = (MobileBy.ANDROID_UIAUTOMATOR, 'text("妈妈食材")')
# 精选特惠
Category_preferential_treatment = (MobileBy.ANDROID_UIAUTOMATOR, 'text("精选特惠")')
# 荟精选
Category_selected = (MobileBy.ANDROID_UIAUTOMATOR, 'text("荟精选")')
# 爆款生鲜
Category_fresh = (MobileBy.ANDROID_UIAUTOMATOR, 'text("爆款生鲜")')
# 新人专享
Category_vip = (MobileBy.ANDROID_UIAUTOMATOR, 'text("新人专享")')
# 新鲜蔬菜
Category_vegetables = (MobileBy.ANDROID_UIAUTOMATOR, 'text("新鲜蔬菜")')
# 酒水乳品
Category_wine = (MobileBy.ANDROID_UIAUTOMATOR, 'text("酒水乳品")')
# 时令水果
Category_fruits = (MobileBy.ANDROID_UIAUTOMATOR, 'text("时令水果")')
# 休闲食品
Category_snacks = (MobileBy.ANDROID_UIAUTOMATOR, 'text("休闲食品")')
# 水产冻品
Category_product = (MobileBy.ANDROID_UIAUTOMATOR, 'text("水产冻品")')
# 生活美妆
Category_Beauty = (MobileBy.ANDROID_UIAUTOMATOR, 'text("生活美妆")')
# 肉禽蛋品
Category_meat_eggs = (MobileBy.ANDROID_UIAUTOMATOR, 'text("肉禽蛋品")')
# 生活服务
Category_life_service = (MobileBy.ANDROID_UIAUTOMATOR, 'text("生活服务")')
# 粮油调味
Category_oil = (MobileBy.ANDROID_UIAUTOMATOR, 'text("粮油调味")')
# 居家百货
Category_department = (MobileBy.ANDROID_UIAUTOMATOR, 'text("居家百货")')
# 采购中
Category_procure = (MobileBy.ANDROID_UIAUTOMATOR, 'text("采购中")')

# 选规格
Category_specifications = (MobileBy.ANDROID_UIAUTOMATOR, 'text("选规格")')
# +，这个定位方式应该是错误的，后期优化
Category_add = (MobileBy.ANDROID_UIAUTOMATOR, 'text("+")')
# 已售罄，这个定位方式应该是错误的，后期优化
Category_sell_out = (MobileBy.ANDROID_UIAUTOMATOR, 'text("抢光了")')
# 分类—进入商品详情页
Category_detail = (MobileBy.ANDROID_UIAUTOMATOR, 'text("结算对账第二个品581103")')

##购物车##

# 增加商品数量
Shopping_cart_add = (MobileBy.ANDROID_UIAUTOMATOR, '.className("android.widget.Image").index(3)')
# 减少商品数量
Shopping_cart_reduce = (MobileBy.ANDROID_UIAUTOMATOR, '.className("android.widget.Image").index(1)')
# 全选
Shopping_cart_selected = (MobileBy.ANDROID_UIAUTOMATOR, 'text("全选")')
# 删除
Shopping_cart_delete = (MobileBy.ANDROID_UIAUTOMATOR, 'text("删除")')
# 十荟精选
Shopping_cart_deli = (MobileBy.ANDROID_UIAUTOMATOR, 'text("十荟精选")')
# 合计
Shopping_cart_total = (MobileBy.ANDROID_UIAUTOMATOR, 'text("合计")')
# 去支付
# Shopping_cart_pay = (MobileBy.ANDROID_UIAUTOMATOR, 'className("android.widget.Button")')
Shopping_cart_pay = (MobileBy.ANDROID_UIAUTOMATOR, 'text("去支付 ")')

# 确认订单页

# 购物车—确认订单页—团长
Shopping_cart_commander = (MobileBy.ANDROID_UIAUTOMATOR, 'text("团长")')
# 购物车—确认订单页—自提点
Shopping_cart_self_point = (MobileBy.ANDROID_UIAUTOMATOR, 'text("自提点")')
# 购物车—确认订单页—购买人
Shopping_cart_purchaser = (MobileBy.ANDROID_UIAUTOMATOR, 'text("购买人")')
# 购物车—确认订单页—手机号
Shopping_cart_phone_number = (MobileBy.ANDROID_UIAUTOMATOR, 'text("手机号")')
# 购物车—确认订单页—使用微信手机号
Shopping_cart_phone = (MobileBy.ANDROID_UIAUTOMATOR, 'text("使用微信手机号 ")')
# 购物车—确认订单页—商品金额
Shopping_cart_amount = (MobileBy.ANDROID_UIAUTOMATOR, 'text("商品金额")')
# 购物车—确认订单页—优惠券
Shopping_cart_coupon = (MobileBy.ANDROID_UIAUTOMATOR, 'text("优惠券")')
# 购物车—确认订单页—备注输入框
Shopping_cart_remarks = (MobileBy.ANDROID_UIAUTOMATOR, 'text("备注特殊要求或给团长留言")')
# 备注
Shopping_cart_remark = (MobileBy.ANDROID_UIAUTOMATOR, 'text("备注")')
# 购物车—确认订单页—总计
Shopping_cart_calculation = (MobileBy.ANDROID_UIAUTOMATOR, 'text("总计")')
# 金刚子页面—确认订单页—确认订单
Home_order = (MobileBy.ANDROID_UIAUTOMATOR, 'text("确认订单")')
# 金刚子页面—确认订单页—请先设置收货地址
Home_receiving_address = (MobileBy.ANDROID_UIAUTOMATOR, 'text("请先设置收货地址")')
# 金刚子页面—确认订单页—商品金额
Home_amount = (MobileBy.ANDROID_UIAUTOMATOR, 'text("商品金额")')
# 金刚子页面—确认订单页—优惠券
Home_coupon = (MobileBy.ANDROID_UIAUTOMATOR, 'text("优惠券")')
# 金刚子页面—确认订单页—新增地址
Home_new_address = (MobileBy.ANDROID_UIAUTOMATOR, 'text("新增地址")')
# 确认支付
Shopping_cart_payment = (MobileBy.ANDROID_UIAUTOMATOR, 'text("确认支付")')
# 购买人信息
Home_buy_name = (MobileBy.ANDROID_UIAUTOMATOR, 'text("测试2")')
# 购买人输入框默认文案
Home_buy_copy = (MobileBy.ANDROID_UIAUTOMATOR, 'text("请填写姓名")')

# 手机号信息
Home_buy_phone = (MobileBy.ANDROID_UIAUTOMATOR, 'text("17330291054")')
# 购买人输入框默认文案
Home_phone_copy = (MobileBy.ANDROID_UIAUTOMATOR, 'text("请输入您的手机号")')

# 拒绝
Home_refuse = (MobileBy.ANDROID_UIAUTOMATOR, 'text("拒绝")')
#
# 订单详情
# 购物车—订单详情页—订单编号
Shopping_cart_order_number = (MobileBy.ANDROID_UIAUTOMATOR, 'text("订单编号")')
# 购物车—订单详情页—订单时间
Shopping_cart_order_time = (MobileBy.ANDROID_UIAUTOMATOR, 'text("订单时间")')

# 看好货
Promising_good = (MobileBy.ANDROID_UIAUTOMATOR, 'text("看好货")')


########################################################################################################################
#　售后工单
# 申请售后
Customer_service_list = (MobileBy.ANDROID_UIAUTOMATOR, 'text("申请售后")')
# 添加视频
Customer_add_video = (MobileBy.ANDROID_UIAUTOMATOR, 'text("添加视频")')
# 添加照片
Customer_add_photo = (MobileBy.ANDROID_UIAUTOMATOR, 'text("添加照片")')
# 从相册选择
Customer_add_photos = (MobileBy.ANDROID_UIAUTOMATOR, 'text("从相册选择")')
#　提交
Customer_submit_to = (MobileBy.ANDROID_UIAUTOMATOR, 'text("提交")')
#　视频
Customer_video1 = (MobileBy.ANDROID_UIAUTOMATOR, 'className("android.widget.CheckBox")')
#　照片
Customer_video = (MobileBy.ANDROID_UIAUTOMATOR, 'resourceId("com.tencent.mm:id/dj4")')

#　选择视频完成
Customer_finish = (MobileBy.ANDROID_UIAUTOMATOR, 'text("完成")')
#　选择照片完成
Customer_finish1 = (MobileBy.ANDROID_UIAUTOMATOR, 'className("android.widget.Button")')
#　问题描述
Customer_problem_formulation = (MobileBy.ANDROID_UIAUTOMATOR, 'text("请描述申请售后服务的具体原因，建议至少上传一张售后凭证照片，描述限200字以内")')
#　问题描述点击完成
Customer_problem = (MobileBy.ANDROID_UIAUTOMATOR, 'text("完成")')

# 返回列表
Customer_return_list = (MobileBy.ANDROID_UIAUTOMATOR, 'text("返回列表")')
#　未处理
Customer_untreated_list = (MobileBy.ANDROID_UIAUTOMATOR, 'text("未处理")')
#　撤销申请
Customer_application_order = (MobileBy.ANDROID_UIAUTOMATOR, 'text("撤销申请")')
# 确定
Customer_sure_order = (MobileBy.ANDROID_UIAUTOMATOR, 'text("确定")')
