# SauceDemo 测试用例

## 测试环境
- 网址：https://www.saucedemo.com
- 浏览器：Chrome
- 账号：standard_user / secret_sauce

## 用例清单

| 编号     | 模块 | 用例标题       | 前置条件 | 操作步骤                                                   | 预期结果                                     | 优先级 |
|--------|---|------------|---|--------------------------------------------------------|------------------------------------------|----|
| TC-001 | 登录 | 正确账号密码登录成功 | 打开登录页 | 1.输入 standard_user 2.输入 secret_sauce 3.点击 Login        | 跳转商品列表页，展示 6 个商品                         | 高  |
| TC-002 | 登录 | 错误密码登录失败   | 打开登录页 | 1.输入 standard_user 2.输入 123 3.点击 Login                 | 提示Epic sadface: Username and password do not match any user in this service                          | 高  |
| TC-003 | 登录 | 不存在用户名登录失败 | 打开登录页 | 1.输入 standard_user2 2.输入 secret_sauce 3.点击 Login       | 提示Epic sadface: Username and password do not match any user in this service                           | 中  |
| TC-004 | 登录 | 空密码登录失败    | 打开登录页 | 1.输入 standard_user  2.点击 Login                         | 提示Epic sadface: Password is required                                | 高  |
| TC-005 | 登录 | 空用户名密码登录失败 | 打开登录页 | 1.点击 Login                                             | 提示Epic sadface: Username is required                       | 高  |
| TC-006 | 登录 | 用户名输入特殊字符  | 打开登录页 | 1.输入 @#￥%#@！￥2 2.输入 secret_sauce 3.点击 Login            | 提示Epic sadface: Username and password do not match any user in this service          | 中  |
| TC-007 | 登录 | 锁定账号无法登录   | 打开登录页 | 1.输入 locked_out_user 2.输入 secret_sauce 3.点击 Login      | 提示Epic sadface: Sorry, this user has been locked out. | 高  |
| TC-008 | 登录 | 输入超长字符用户名  | 打开登录页 | 1.输入standard_userstandard_userstandard_user 2.输入 secret_sauce 3.点击 Login | 提示Epic sadface: Username and password do not match any user in this service                         | 中  |
| TC-009 | 登录 | 输入超长字符密码   | 打开登录页 | 1.输入standard_user 2.输入 secret_saucesecret_saucesecret_sauce 3.点击 Login | 提示Epic sadface: Username and password do not match any user in this service                           | 中  |
| TC-010 | 登录 | 断网情况登录     | 打开登录页 | 1.输入standard_user 2.输入 secret_sauce 3.关闭网络 4.点击 Login  | 请求发送失败，页面不跳转，浏览器显示网络错误提示（非 404、非白屏） | 低  |
| TC-011 | 登录 | 登录后退出登录 | 已成功登录 | 1.点击左上角菜单图标<br>2.点击 Logout | 返回登录页，登录态被清除，直接访问 inventory.html 会被跳回登录页 | 高 |


| 编号     | 模块 | 用例标题       | 前置条件 | 操作步骤                                                   | 预期结果                                     | 优先级 |
|--------|---|------------|---|--------------------------------------------------------|------------------------------------------|----|
| TC-001 | 商品列表 | 正确显示六个商品 | 已登录 | 1.观察页面 | 跳转商品列表页，展示 6 个商品| 高  |
| TC-002 | 商品列表 | 商品显示详情 | 已登录 | 1.点击商品名称或图片  | 跳转商品详情页面，显示点击商品的图片，名称，详情和add to card标签  | 高  |
| TC-003 | 商品列表 | 价格格式显示 | 已登录 | 1.观察价格显示 | 各商品价格显示格式为$数字，保留两位小数点形式 | 高  |
| TC-004 | 商品列表 | 详情页价格格式显示 | 已登录 | 1.点击商品名称或图片 | 商品价格显示格式为$数字，保留两位小数点形式 | 高  |
| TC-005 | 商品列表 | 商品排序  | 已登录 | 1.观察商品名称排序 | 商品显示页面默认排序为A-Z 列表第一个商品为 "Sauce Labs Backpack"，最后一个为 "Test.allTheThings() T-Shirt (Red)"| 中  |
| TC-006 | 商品列表 | 修改商品排序为Name(Z to A)  | 已登录 | 1.点击排序栏按钮，点击Name(Z to A)| 商品按照Name(Z to A)排序显示 列表第一个商品为"Test.allTheThings() T-Shirt (Red)" ，最后一个为 "Sauce Labs Backpack" | 高  |
| TC-007 | 商品列表 | 修改商品排序为Price(low to high)  | 已登录 | 1.点击排序栏按钮，点击Price(low to high)  | 商品按照Price(low to high)排序显示 列表第一个商品为"Sauce Labs Onesie" ，最后一个为 "Sauce Labs Fleece Jacket"  | 中  |
| TC-008 | 商品列表 | 修改商品排序为Price(high to low)  | 已登录 | 1.点击排序栏按钮，点击Price(high to low)   | 商品按照Price(high to low) 排序显示  列表第一个商品为"Sauce Labs Fleece Jacket" ，最后一个为"Sauce Labs Onesie"| 中  |
| TC-009 | 商品列表 | 更多    | 已登录 | 1.点击顶部栏左边的三条横线按钮 | 右侧滑出侧边栏，包含 All Items、Dynamic Catalog、About、Logout、Reset App State 五个菜单项和右上角关闭按钮（X） | 低  |
| TC-010 | 商品列表 | 商品显示 | 已登录 | 1.三条横线按钮 2.点击 Logout 3.登录另一个账号 | 跳转商品列表页，展示 6 个商品 | 高 |
| TC-011 | 商品列表 | 社交媒体跳转 | 在商品详细界面 | 1.点击左下角的社交媒体图标 | 跳转对应的社交媒体主页| 低 |


| 编号     | 模块 | 用例标题                  | 前置条件                     | 操作步骤                                                            | 预期结果                                                                         | 优先级 |
|--------|---|-----------------------|--------------------------|-----------------------------------------------------------------|------------------------------------------------------------------------------|----|
| TC-001 | 购物车 | 正确显示购物车页面             | 已登录，商品未添加到购物车            | 1.点击右上角的购物车图标                                                   | 跳转购物车详情页，默认没有添加商品，显示Your Cart，QTY，Description，Continue Shopping按钮和Checkout按钮 | 高  |
| TC-002 | 购物车 | 商品页面添加一个商品            | 已登录，商品未添加到购物车            | 1.点击商品下的add to cart 2.观察右上角购物车图标                                | 右上角购物车图标出现数字1                                                                | 高  |
| TC-003 | 购物车 | 商品页面添加多个商品            | 已登录，商品未添加到购物车            | 1.点击多个商品下的add to cart 2.观察右上角购物车图标                              | 右上角购物车图标出现点击商品的数量                                                            | 高  |
| TC-004 | 购物车 | 商品详情页添加商品             | 已登录，商品未添加到购物车            | 1.点击商品名称或图片，跳转商品详情页面 2.点击add to cart 3.观察右上角购物车图标               | 右上角购物车图标出现数字1                                                                | 高  |
| TC-005 | 购物车 | 商品详情页添加多个商品           | 已登录，商品未添加到购物车            | 1.点击商品名称或图片，跳转商品详情页面 2.点击add to cart 3.对其他商品重复步骤一二 4.观察右上角购物车图标 | 右上角购物车图标出现添加商品的数字                                                            | 中  |
| TC-006 | 购物车 | 商品状态显示                | 已登录，商品未添加到购物车            | 1.观察商品页面的商品价格旁的按钮 2.点击按钮                                        | 按钮从add to cart变为Remove                                                       | 高  |
| TC-007 | 购物车 | 商品详情页显示               | 已登录，商品未添加到购物车            | 1.点击已添加到购物车的商品图片或名称 2.点击按钮 3. 观察商品详情页面的商品价格旁的按钮                 | 按钮从add to cart变为Remove                                                       | 中  |
| TC-008 | 购物车 | 商品页面删除一个商品            | 已登录，商品已添加到购物车            | 1.点击商品下的remove 2.观察右上角购物车图标                                     | 右上角购物车图标数字1消失                                                                | 中  |
| TC-009 | 购物车 | 商品页面删除多个商品            | 已登录，商品已添加到购物车            | 1.点击多个商品下的remove 2.观察右上角购物车图标                                   | 右上角购物车图标数字减少对应值                                                              | 低  |
| TC-010 | 购物车 | 商品详情页删除商品             | 已登录，商品已添加到购物车            | 1.点击商品名称或图片，跳转商品详情页面 2.点击remove   3.观察右上角购物车图标                  | 右上角购物车图标数字1消失                                                                | 高 |
| TC-011 | 购物车 | 商品详情页删除多个商品           | 已登录，商品已添加到购物车            | 1.点击商品名称或图片，跳转商品详情页面 2.点击remove  3.对其他商品重复步骤一二 4.观察右上角购物车图标     | 右上角购物车图标数字减少对应值                                                              | 低 |
| TC-012 | 购物车 | 商品状态显示                | 已登录，商品已添加到购物车            | 1.观察商品页面的商品价格旁的按钮 2.点击按钮                                        | 按钮从remove变为add to cart                                                       | 高  |
| TC-013 | 购物车 | 商品详情页显示               | 已登录，商品已添加到购物车            | 1.点击已添加到购物车的商品图片或名称 2.点击按钮 3. 观察商品详情页面的商品价格旁的按钮                 | 按钮从remove变为add to cart                                                       | 中  |
| TC-014 | 购物车 | 购物车详情展示               | 已登录，商品已添加到购物车            | 1.点击右上角购物车图标 2.观察商品详情页面的商品价格旁的按钮                                | 在 TC-001 的基础上，列表显示商品的 QTY、名称、描述、价格和 Remove 按钮                                | 中  |
| TC-015 | 购物车 | 购物车删除商品               | 已登录，购物车中只有 1 个商品（角标显示 1） | 1.点击右上角购物车图标 2.点击商品右边的remove按钮                                  | 商品被移除，右上角购物车角标消失，页面回到无角标状态                                                   | 中  |
| TC-016 | 购物车 | 购物车继续购物               | 已登录，商品已添加到购物车            | 1.点击右上角购物车图标 2.点击左边的continue shopping 3.观察跳转页面和购物车数量 4.点击购物车图标  | 跳转回商品显示页面，购物车数量未变，并再次进入购物车详情，商品存在                                            | 中  |
| TC-017 | 购物车 | 购物车刷新                 | 已登录，商品已添加到购物车            | 1.点击右上角购物车图标 2.点击f5刷新                                           | 仍然处于购物车界面，商品和数量不变                                                            | 中  |
| TC-018 | 购物车 | 同一用户重新登录购物车数据保持       | A 已登录且加购 2 件            | 1.点击左上角三横线按钮 2.点击logout 3.登录统一用户 4.观察购物车角标 5.点击购物车 6.观察购物车界面    | 购物车角标仍为2，购物车内商品和数量不变                                                         | 中  |
| TC-019 | 购物车 | 切换用户后购物车数据隔离（目标用户无数据） | A 已登录且加购 2 件           | 1.点击左上角三横线按钮 2.点击logout 3.登录另一用户 4.观察购物车角标 5.点击购物车 6.观察购物车界面    | 以 B 登录后角标不显示，购物车为空                                                           | 中  |
| TC-020 | 购物车 | 切换用户后购物车数据隔离（目标用户有数据） | A 加购 2 件，B 加购 1 件            | 1.会话失效 2.点击购物车图标 3.观察点击后跳转 4.观察购物车角标 5.点击购物车 6.观察购物车界面          | 分别登录，各自看到自己的数量，互不影响                                                          | 中  |
| TC-021 | 购物车 | 会话失效后购物车              | 已登录，商品已添加到购物车            | 1.会话失效 2.点击购物车图标 3.观察点击后跳转 4.观察购物车角标 5.点击购物车 6.观察购物车界面          | 跳转进登录界面                                                                      | 中  |



| 编号     | 模块   | 用例标题              | 前置条件                                  | 操作步骤                                                                                            | 预期结果                                                                                                                                                                                                | 优先级 |
|--------|------|-------------------|---------------------------------------|-------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----|
| TC-001 | 下单   | 正确显示下单页面          | 已登录，在购物车界面,购物车有商品                     | 1.点击Checkout                                                                                    | 跳转页面，左上角显示Checkout: Your Information， 中间显示first name last name zip/postal code输入栏，左下角显示cancel按钮，右下角显示continue按钮                                                                                     | 高  |
| TC-002 | 下单   | 正确显示下单页面          | 已登录，在购物车界面,购物车无商品                     | 1.点击Checkout                                                                                    | 提示购物车没有商品                                                                                                                                                                                           | 高  |
| TC-003 | 下单   | 下单信息输入            | 在Checkout: Your Information页面         | 1.正确输入firstname，lastname，zip/postal code，点击continue                                             | 跳转页面，左上角显示Checkout: Overview，中间显示在购物车 TC-014 的基础上，列表显示商品的 QTY、名称、描述、价格，去掉remove，接着显示Payment Information:，Shipping Information:，Price Total里面包含了Item total: Tax: ，最后有个Total:，左下角cancel按钮，右下角finish按钮 | 高  |
| TC-004 | 下单   | 下单信息输入            | 在Checkout: Your Information页面         | 1.不输入firstname，lastname，zip/postal code，点击continue                                              | 提示Error: First Name is required                                                                                                                                                                     | 高  |
| TC-005 | 下单   | 下单信息输入            | 在Checkout: Your Information页面         | 1.正确输入firstname，lastname，zip/postal code，点击cancel 2.点击Checkout                                  | 输入的firstname，lastname，zip/postal code清空，需重新输入，点击输入框有历史输入提示，                                                                                                                                         | 中  |
| TC-006 | 下单   | 下单信息输入            | 在Checkout: Your Information页面         | 1.正确输入firstname，lastname，zip/postal code，点击checkout 2.点击cancel 3.点击购物车 4.点击checkout 5.依次点击输入框   | 输入的firstname，lastname，zip/postal code清空，需重新输入，点击输入框有历史输入提示                                                                                                                                          | 高  |
| TC-007 | 下单   | 最终下单结果确认          | 在Checkout: Overview页面，已添加两件商品         | 1.点击cancel 2.观察购物车角标 3.点击购物车                                                                    | 显示TC-003的预期结果，然后跳转回商品页面，正确显示六个商品，购物车角标为2，购物车里有两个商品                                                                                                                                                  | 中  |
| TC-008 | 下单   | 最终下单结果确认          | 在Checkout: Overview页面，已添加两件商品         | 1.点击finish                                                                                      | 跳转页面，左上角显示Checkout: Complete!中间出现提示 Thank you for your order!Your order has been dispatched, and will arrive just as fast as the pony can get there! 左下角出现backhome按钮，右下角出现generate pdf order        | 中  |
| TC-009 | 下单   | 完成下单后             | 在Checkout: Complete!页面                | 1.点击左下角back home 2.观察购物车角标 3.点击购物车                                                              | 跳转回商品页面，显示六个商品，购物车角标为0，购物车无商品                                                                                                                                                                       | 中  |
| TC-010 | 下单   | 完成下单后             | 在Checkout: Complete!页面                | 1.点击右下角generate pdf order 2.观察按钮状态 3.点击浏览器下载中心                                                  | 按钮从generate pdf order变为generating，过会后下载中心显示pdf，按钮从generating变为generate pdf order                                                                                                                    | 高  |
| TC-011 | 下单   | 退出后下单信息输入(同一用户)   | 在Checkout: Your Information页面         | 1.正确输入firstname，lastname，zip/postal code，点击三横线 2.点击logout 3.登录同一账户 4.点击购物车 5.点击checkout 6.点击输入栏 | 输入的fisrtname，lastname，zip/postal code清空，需重新输入，点击输入框有历史输入提示                                                                                                                                          | 高  |
| TC-012 | 下单   | 退出后下单信息输入(不同用户)   | 在Checkout: Your Information页面         | 1.正确输入firstname，lastname，zip/postal code，点击三横线 2.点击logout 3.登录另一账户 4.点击购物车 5.点击checkout 6.点击输入栏 | 输入的fisrtname，lastname，zip/postal code清空，需重新输入，点击输入框有历史输入提示                                                                                                                                          | 高  |
| TC-013 | 下单   | 退出后下单最终结果确认(同一用户) | 在Checkout: Overview页面，已添加两件商品         | 1.点击logout 2.登录同一账户 3.观察购物车角标 4.点击购物车                                                           | 商品页面正确显示六个商品，购物车角标为2，购物车里有两个商品                                                                                                                                                                      | 高  |
| TC-014 | 下单   | 退出后下单最终结果确认(不同用户) | 在Checkout: Overview页面，a已添加两件商品，b未添加商品 | 1.点击logout 2.登录另一账户 3.观察购物车角标 4.点击购物车                                                           | 商品页面正确显示六个商品，购物车角标为0，购物车里有零个商品                                                                                                                                                                      | 高  |
| TC-015 | 下单   | 完成下单后退出(同一用户)     | 在Checkout: Complete!页面                | 1.点击logout 2.登录同一账户 3.观察购物车角标 4.点击购物车                                                           | 商品页面正确显示六个商品，购物车角标为0，购物车里有0个商品                                                                                                                                                                      | 高  |
| TC-016 | 下单   | 价格计算正确性             | 在Checkout: Overview页面，已添加两件商品，总额为$39.98    | 1.记录各商品的单价 2.记录 Item total、Tax、Total 三个数值 3.核对计算关系                                              | Item total = 各商品单价之和；Tax = Item total × 税率；Total = Item total + Tax                                                                                                                                 | 高  |


12有问题 2有问题