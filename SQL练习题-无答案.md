# SQL 练习题（无答案版）

> **用法：先自己写，全部写完再看 `sql_practice.py` 里的答案对照。**
> 数据表见下方，或参考 `SQL练习数据表.md`。
> 共 **28 题**，建议限时 **60 分钟**，写不出的先跳过，最后统一对答案。

---

## 数据表（对照用）

**account（账户表）**

| id | account_no | customer_name | balance | status |
|---|---|---|---|---|
| 1 | 1001 | 张三 | 50000.00 | ACTIVE |
| 2 | 1002 | 李四 | 12000.50 | ACTIVE |
| 3 | 1003 | 王五 | 300.00 | FROZEN |
| 4 | 1004 | 赵六 | 0.00 | ACTIVE |
| 5 | 1005 | 钱七 | 8000.00 | ACTIVE |

**trans（交易流水表）**

| id | account_no | amount | trans_type | status | create_time |
|---|---|---|---|---|---|
| 1 | 1001 | 5000.00 | TRANSFER | SUCCESS | 2026-09-01 10:00:00 |
| 2 | 1001 | 1200.00 | WITHDRAW | SUCCESS | 2026-09-02 11:30:00 |
| 3 | 1001 | 800.00 | TRANSFER | FAIL | 2026-09-03 09:15:00 |
| 4 | 1002 | 3000.00 | TRANSFER | SUCCESS | 2026-09-01 14:20:00 |
| 5 | 1002 | 15000.00 | DEPOSIT | SUCCESS | 2026-09-04 16:45:00 |
| 6 | 1002 | 200.00 | WITHDRAW | SUCCESS | 2026-09-05 08:10:00 |
| 7 | 1003 | 100.00 | TRANSFER | FAIL | 2026-09-02 19:00:00 |
| 8 | 1005 | 900.00 | TRANSFER | SUCCESS | 2026-09-03 12:00:00 |
| 9 | 1005 | 900.00 | TRANSFER | SUCCESS | 2026-09-03 12:00:00 |
| 10 | 1001 | 250.00 | WITHDRAW | PENDING | 2026-09-06 10:30:00 |

---

# 第一类：基础查询（WHERE / ORDER BY / LIMIT / LIKE / BETWEEN）

### 第 1 题
查询账号为 `1001` 的所有交易记录。

```sql select * from trans where account_no = '1001'

```

### 第 2 题
查询账号为 `1001` 的最近 3 笔交易（按时间倒序）。

```sql select * from trans where account_no = '1001' order by create_time desc limit 3

```

### 第 3 题
查询所有**成功**的**转账**（TRANSFER）交易，只显示 id、account_no、amount、create_time。

```sql select id,account_no,amount,create_time from trans where status = 'SUCCESS' and trans_type = 'TRANSFER'

```

### 第 4 题
查询所有金额大于 1000 的交易，按金额从大到小排序。

```sql select * from trans where amount > 1000 order by amount

```

### 第 5 题
查询所有余额为 0 或者状态为 FROZEN 的账户。

```sql select account_no,customer_name,balance from account where balance = o or status = 'FROZEN'

```

### 第 6 题
查询客户姓名以「张」开头的账户。

```sql select * from account where customer_name like '张%'

```

### 第 7 题
查询金额在 500 到 5000 之间的交易（含边界）。

```sql select * from trans where amount between 500 and 5000

```

---

# 第二类：聚合与分组（COUNT / SUM / AVG / GROUP BY / HAVING）

### 第 8 题
统计交易表一共有多少笔交易。

```sql select count(id) from trans 

```

### 第 9 题
统计每个账户的交易笔数和总金额。

```sql select account_no,count(id),sum(amount) from trans group by account_no

```

### 第 10 题
统计每个账户的**成功**交易总金额（只算 status = 'SUCCESS'）。

```sql select account_no,sum(amount) from trans where status = 'SUCCESS' group by account_no

```

### 第 11 题
找出总金额超过 5000 的账户。

```sql select account_no,sum(amount) from trans group by account_no having  sum(amount) > 5000

```

### 第 12 题
按交易状态（status）分组，统计每种状态的交易笔数和总金额，按笔数倒序。

```sql select status,count(id),sum(amount) from trans group by status order by count(id) desc

```

### 第 13 题
统计每种交易类型（trans_type）的平均金额，保留 2 位小数。

```sql select trans_type,round(avg(amount),2) from trans group by trans_type

```

### 第 14 题
查询交易笔数大于 2 的账户。

```sql select account_no,count(id) from trans group by account_no having count(id)> 2

```

---

# 第三类：多表连接（JOIN）

### 第 15 题
查询每笔交易对应的客户姓名（交易 + 账户，内连接）。

```sql select b.id,b.amount,b.account_no,a.customer_name from account a join trans b on a.account_no = b.account_no

```

### 第 16 题
统计每个客户的成功交易总金额，按金额从高到低排序。

```sql select b.account_no,a.customer_name,sum(b.amount) from account a join trans b on a.account_no = b.account_no where b.status = 'SUCCESS'  group by b.account_no order by sum(b.amount) desc

```

### 第 17 题
查询所有账户及其交易笔数，**包括没有交易记录的账户**（交易笔数显示 0）。
```sql select a.account_no,a.customer_name,count(b.id) from account a left join trans b on a.account_no = b.account_no group by a.account_no,a.customer_name 

```

### 第 18 题 ★
找出**没有任何交易记录**的账户。

```sql select a.account_no, a.customer_name from account a left join trans b on a.account_no = b.account_no where b.id is null

```

### 第 19 题
查询所有冻结账户（status = 'FROZEN'）的交易记录。

```sql select b.id,b.account_no,b.amount,b.status from account a join trans b on a.account_no = b.account_no  where a.status = 'FROZEN' 

```

---

# 第四类：子查询

### 第 20 题
查询金额高于全部交易平均金额的交易。

```sql select id,account_no, amount from trans where  amount >  (select avg(amount) from trans)

```

### 第 21 题
查询有过成功交易的账户（用 IN 子查询）。

```sql select account_no, customer_name from account where  account_no in  (select  account_no from trans where status = 'SUCCESS')

```

### 第 22 题
查询余额大于 5000 **且**有过交易的账户（用 EXISTS 子查询）。

```sql select a.account_no,a.balance from account a where a.balance > 5000 and EXISTS(select 1 from trans t where t.account_no= a.account_no)

```

---

# 第五类：数据校验（测试岗重点）★

### 第 23 题 ★
找出交易表中**重复**的记录（同账号、同时间、同金额出现多次），
显示账号、时间、金额和重复次数。

```sql select account_no,create_time,amount,count(id) as 重复次数 from trans group by account_no,create_time,amount having count(id)>1

```

### 第 24 题 ★
找出交易表中存在、但账户表中**不存在的账号**（孤儿数据）。

```sql select  t.account_no from trans t left join account a  on t.account_no = a.account_no where a.id is null 

```

### 第 25 题 ★
找出金额**小于等于 0** 的异常交易。

```sql select * from trans where amount <= 0

```

### 第 26 题 ★
找出所有状态为 **FAIL 但金额大于 0** 的交易（业务逻辑异常：失败却产生了金额）。

```sql select * from trans where status = 'FAIL' and amount > 0

```

---

# 第六类：窗口函数

### 第 27 题 ★
查询每个账户**金额最大**的那一笔交易，显示账号、id、金额。

```sql select * from (select account_no, id, amount,row_number() over (partition by account_no order by amount desc) as rn from trans) where rn =1 

```

### 第 28 题 ★
查询账号 `1001` 的每笔交易，并显示**按时间累计的金额**（累计求和）。

```sql select * from(select account_no, id, amount,create_time, sum(amount) over(partition by account_no order by create_time )as 累计金额 from trans where account_no='1001' order by create_time

```

---

## 附加题（可选，难度更高）

### 第 29 题
查询每个账户的交易金额排名，显示账号、id、金额、排名。
（用 RANK 和 DENSE_RANK 各写一版，观察区别）

```-- RANK 版select account_no, id, amount,rank() over (partition by account_no order by amount desc) as 排名from transorder by account_no, 排名
```

### 第 30 题
查询账号 `1001` 每笔交易金额与**上一笔**交易的差额。

```sql select id,account_no,amount,lag(amount,1) over(partition by account_no order by create_time) as 上一笔,amount - lag(amount, 1) over (partition by account_no order by create_time) as 差额 from trans where account_no = '1001' order by create_time;

```

---

## 写完之后的对照方法

```powershell
cd D:\work\python\api-test-framework
D:\work\python\python310\python.exe sql_practice.py
```

**脚本里每条查询都有标题和注释，对照你写的看。**

**对照时重点看这三件事：**

| 检查 | 说明 |
|---|---|
| **结果对不对** | 行数、数值是否一致 |
| **写法是否等价** | 你的写法可能和答案不同但结果一样——**这也是对的** |
| **漏了什么** | 比如忘记 `GROUP BY`、用错 `WHERE`/`HAVING` |

---

## 自评标准

| 类别 | 目标 |
|---|---|
| 第一类（1-7） | 全对，不看表 |
| 第二类（8-14） | 全对，**注意 `WHERE` 和 `HAVING` 别用混** |
| 第三类（15-19） | **第 18 题必须会**（左连接 + IS NULL） |
| 第四类（20-22） | 能写出来 |
| 第五类（23-26） | **全部要会**——这是测试岗面试的考点 ⭐ |
| 第六类（27-28） | 第 27 题必须会（分组取 TOP1） |

**打成这个标准，SQL 这块面试就没问题了。**
