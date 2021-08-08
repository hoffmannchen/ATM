# 项目的说明书
# 项目: ATM+购物车
# 项目需求
    作业需求：

    模拟实现一个ATM + 购物商城程序

    1 .额度 15000或自定义
    2. 实现购物商城，买东西加入 购物车，调用信用卡接口结账
    3. 可以提现，手续费5%
    ## 每月22号出账单，每月10号为还款日，过期未还，按欠款总额 万分之5 每日计息
    4. 支持多账户登录
    5. 支持账户间转账
    6. 记录每月日常消费流水
    7. 提供还款接口
    8. ATM记录操作日志 
    9. 提供管理接口，包括添加账户、用户额度，冻结账户等。。。
    10. 用户认证用装饰器
    示例代码 https://github.com/triaquae/py3_training/tree/master/atm　

    简易流程图：https://www.processon.com/view/link/589eb841e4b0999184934329  


# 一个项目是如何从无到有
## 一 需求分析
    1。 拿到项目，会在客户那讨论需求，商量项目的功能是否能实现，周期与价格,得到需求文档。
    2。 公司内部开会，最终得到开发文档，交给不同岗位程序员进行开发。
        - Python： 后端、爬虫
        - 不同的岗位:
            - UI界面设计: 
                - 设计软件的布局，根据软件的外观切成一张张的图片
            - 前端：
                - 拿到UI的图片，搭建网站页面
                - 页面中哪些位置需要接收数据，哪些位置需要交互
            - 后端：
                - 核心业务逻辑，调度数据库进行数据的增删改查
            - 测试： 
                - 代码全面测试，如压力测试、界面测试
            - 运维: 
                - 部署项目
## 二 程序的架构分析
### 1、程序设计的好处
    1、思路清晰
    2、不会写了一半代码推翻重写
    3、方便维护
## 三 分任务开发
## 四 测试
## 五 上线