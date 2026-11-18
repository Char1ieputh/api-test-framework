"""SQL 练习脚本（SQLite 版）——软件测试数据校验常用查询

用法：
    D:\\work\\python\\python310\\python.exe sql_practice.py

特点：
    - 用 Python 内置的 sqlite3，不需要安装任何数据库
    - 数据存在内存里，跑完即弃，随便改
    - 每条查询都打印结果，边跑边看

练习建议：先跑一遍看结果，再对照注释闭卷默写。
"""
import sqlite3

# ============================================================
# 一、建表 + 造数据
# ============================================================

SCHEMA = """
CREATE TABLE account (
    id            INTEGER PRIMARY KEY,
    account_no    TEXT,
    customer_name TEXT,
    balance       REAL,
    status        TEXT
);

CREATE TABLE trans (
    id          INTEGER PRIMARY KEY,
    account_no  TEXT,
    amount      REAL,
    trans_type  TEXT,
    status      TEXT,
    create_time TEXT
);
"""

ACCOUNTS = [
    (1, "1001", "张三", 50000.00, "ACTIVE"),
    (2, "1002", "李四", 12000.50, "ACTIVE"),
    (3, "1003", "王五", 300.00, "FROZEN"),
    (4, "1004", "赵六", 0.00, "ACTIVE"),      # 无交易记录，用于左连接测试
    (5, "1005", "钱七", 8000.00, "ACTIVE"),
]

TRANS = [
    (1,  "1001", 5000.00,  "TRANSFER", "SUCCESS", "2026-09-01 10:00:00"),
    (2,  "1001", 1200.00,  "WITHDRAW", "SUCCESS", "2026-09-02 11:30:00"),
    (3,  "1001", 800.00,   "TRANSFER", "FAIL",    "2026-09-03 09:15:00"),
    (4,  "1002", 3000.00,  "TRANSFER", "SUCCESS", "2026-09-01 14:20:00"),
    (5,  "1002", 15000.00, "DEPOSIT",  "SUCCESS", "2026-09-04 16:45:00"),
    (6,  "1002", 200.00,   "WITHDRAW", "SUCCESS", "2026-09-05 08:10:00"),
    (7,  "1003", 100.00,   "TRANSFER", "FAIL",    "2026-09-02 19:00:00"),
    (8,  "1005", 900.00,   "TRANSFER", "SUCCESS", "2026-09-03 12:00:00"),
    (9,  "1005", 900.00,   "TRANSFER", "SUCCESS", "2026-09-03 12:00:00"),  # 故意重复，用于查重复
    (10, "1001", 250.00,   "WITHDRAW", "PENDING", "2026-09-06 10:30:00"),
]


def build_db():
    """建库、建表、插入数据，返回连接对象。"""
    conn = sqlite3.connect(":memory:")
    conn.executescript(SCHEMA)
    conn.executemany("INSERT INTO account VALUES (?,?,?,?,?)", ACCOUNTS)
    conn.executemany("INSERT INTO trans VALUES (?,?,?,?,?,?)", TRANS)
    conn.commit()
    return conn


def show(conn, title, sql, note=""):
    """执行查询并打印结果。"""
    print("\n" + "=" * 70)
    print(f"【{title}】")
    if note:
        print(f"  说明：{note}")
    print("-" * 70)
    print(f"  SQL: {' '.join(sql.split())}")
    print("-" * 70)
    try:
        cur = conn.execute(sql)
        rows = cur.fetchall()
        cols = [d[0] for d in cur.description] if cur.description else []
        if not rows:
            print("  (无数据)")
            return
        print("  " + " | ".join(cols))
        print("  " + "-" * 60)
        for r in rows:
            print("  " + " | ".join(str(v) for v in r))
        print(f"\n  共 {len(rows)} 行")
    except sqlite3.Error as e:
        print(f"  [SQL 错误] {e}")


def main():
    conn = build_db()
    print("SQLite 版本:", sqlite3.sqlite_version)

    # --------------------------------------------------------
    # 第一类：条件 + 排序 + 限制
    # --------------------------------------------------------
    show(conn, "1-1 查询指定账户的最近 3 笔交易",
         "SELECT * FROM trans WHERE account_no='1001' ORDER BY create_time DESC LIMIT 3",
         "WHERE 过滤 → ORDER BY 排序 → LIMIT 限制")

    show(conn, "1-2 查询成功的转账交易",
         "SELECT id, account_no, amount, create_time FROM trans "
         "WHERE status='SUCCESS' AND trans_type='TRANSFER'",
         "多条件用 AND / OR 连接")

    show(conn, "1-3 模糊查询：账户号以 100 开头",
         "SELECT account_no, customer_name FROM account WHERE account_no LIKE '100%'",
         "LIKE 配合 % 做模糊匹配")

    show(conn, "1-4 范围查询：金额在 500 到 5000 之间的交易",
         "SELECT id, amount FROM trans WHERE amount BETWEEN 500 AND 5000 ORDER BY amount",
         "BETWEEN 是闭区间，包含两端")

    # --------------------------------------------------------
    # 第二类：聚合 + 分组 + 过滤分组
    # --------------------------------------------------------
    show(conn, "2-1 每个账户的交易笔数和总金额",
         "SELECT account_no, COUNT(*) AS 笔数, SUM(amount) AS 总金额 "
         "FROM trans GROUP BY account_no",
         "GROUP BY 分组后，聚合函数按组计算")

    show(conn, "2-2 总金额超过 10000 的账户",
         "SELECT account_no, SUM(amount) AS 总金额 FROM trans "
         "GROUP BY account_no HAVING SUM(amount) > 10000",
         "HAVING 过滤分组结果，WHERE 过滤原始行")

    show(conn, "2-3 统计各状态交易的数量和金额",
         "SELECT status, COUNT(*) AS 笔数, SUM(amount) AS 金额 FROM trans "
         "GROUP BY status ORDER BY 笔数 DESC",
         "按状态分组统计")

    show(conn, "2-4 每类交易的平均金额（保留 2 位小数）",
         "SELECT trans_type, ROUND(AVG(amount), 2) AS 平均金额 FROM trans "
         "GROUP BY trans_type",
         "ROUND 保留小数位")

    # --------------------------------------------------------
    # 第三类：多表关联（JOIN）
    # --------------------------------------------------------
    show(conn, "3-1 内连接：交易 + 账户信息",
         "SELECT t.id, t.amount, a.customer_name FROM trans t "
         "INNER JOIN account a ON t.account_no = a.account_no "
         "WHERE t.status='SUCCESS' LIMIT 5",
         "INNER JOIN 只返回两表都匹配的行")

    show(conn, "3-2 内连接 + 分组：每个客户的交易总额",
         "SELECT a.customer_name, COUNT(t.id) AS 笔数, SUM(t.amount) AS 总额 "
         "FROM account a INNER JOIN trans t ON a.account_no = t.account_no "
         "GROUP BY a.customer_name ORDER BY 总额 DESC",
         "JOIN 后可以继续 GROUP BY")

    show(conn, "3-3 左连接：所有账户及其交易数（含无交易的）",
         "SELECT a.account_no, a.customer_name, COUNT(t.id) AS 交易笔数 "
         "FROM account a LEFT JOIN trans t ON a.account_no = t.account_no "
         "GROUP BY a.account_no, a.customer_name",
         "LEFT JOIN 保留左表全部行；无匹配时 COUNT(t.id) 为 0")

    show(conn, "3-4 左连接经典用法：找出没有交易记录的账户",
         "SELECT a.account_no, a.customer_name FROM account a "
         "LEFT JOIN trans t ON a.account_no = t.account_no WHERE t.id IS NULL",
         "★ 高频面试题：WHERE 右表主键 IS NULL")

    # --------------------------------------------------------
    # 第四类：子查询
    # --------------------------------------------------------
    show(conn, "4-1 查询金额高于平均值的交易",
         "SELECT id, account_no, amount FROM trans "
         "WHERE amount > (SELECT AVG(amount) FROM trans)",
         "标量子查询：先算出平均值，再作为条件")

    show(conn, "4-2 IN 子查询：查询有成功交易的账户",
         "SELECT account_no, customer_name FROM account WHERE account_no IN "
         "(SELECT DISTINCT account_no FROM trans WHERE status='SUCCESS')",
         "IN 子查询：先查出账户列表，再筛选")

    show(conn, "4-3 EXISTS 子查询：查询余额大于 5000 且有交易的账户",
         "SELECT a.account_no, a.balance FROM account a WHERE a.balance > 5000 "
         "AND EXISTS (SELECT 1 FROM trans t WHERE t.account_no = a.account_no)",
         "EXISTS 关心'存不存在'，不关心具体值")

    # --------------------------------------------------------
    # 第五类：数据校验（测试最常用）★
    # --------------------------------------------------------
    show(conn, "5-1 ★ 查重复数据：同一账户同一时间的重复交易",
         "SELECT account_no, create_time, amount, COUNT(*) AS 重复次数 "
         "FROM trans GROUP BY account_no, create_time, amount HAVING COUNT(*) > 1",
         "★ 银行测试高频：账务重复是重大缺陷")

    show(conn, "5-2 ★ 查孤儿数据：交易表里有、账户表里没有的账户号",
         "SELECT DISTINCT t.account_no FROM trans t "
         "LEFT JOIN account a ON t.account_no = a.account_no WHERE a.id IS NULL",
         "★ 数据一致性校验：外键完整性")

    show(conn, "5-3 ★ 查异常金额：金额为 0 或负数",
         "SELECT id, account_no, amount FROM trans WHERE amount <= 0",
         "★ 业务规则校验：金额不应为负")

    show(conn, "5-4 ★ 查金额与流水不符：账户余额与交易流水汇总不一致",
         "SELECT a.account_no, a.balance AS 账户余额, "
         "IFNULL(SUM(t.amount), 0) AS 流水汇总, "
         "a.balance - IFNULL(SUM(t.amount), 0) AS 差额 "
         "FROM account a LEFT JOIN trans t ON a.account_no = t.account_no "
         "WHERE t.status = 'SUCCESS' OR t.id IS NULL "
         "GROUP BY a.account_no, a.balance",
         "★ 前后端数据一致性：余额 vs 流水（本例数据未对齐，正是要发现的差异）")

    show(conn, "5-5 ★ 查状态异常：已失败的交易却有金额入账记录",
         "SELECT * FROM trans WHERE status='FAIL' AND amount > 0",
         "★ 业务逻辑校验")

    # --------------------------------------------------------
    # 第六类：窗口函数（面试常问，牛客高频）
    # --------------------------------------------------------
    show(conn, "6-1 ROW_NUMBER：每个账户的交易按时间排名",
         "SELECT account_no, id, amount, create_time, "
         "ROW_NUMBER() OVER (PARTITION BY account_no ORDER BY create_time) AS rn "
         "FROM trans",
         "ROW_NUMBER：不重复的序号（1,2,3,4）")

    show(conn, "6-2 RANK / DENSE_RANK：金额排名",
         "SELECT id, amount, "
         "RANK() OVER (ORDER BY amount DESC) AS rnk, "
         "DENSE_RANK() OVER (ORDER BY amount DESC) AS drnk "
         "FROM trans ORDER BY amount DESC",
         "RANK 跳号（1,2,2,4）；DENSE_RANK 不跳号（1,2,2,3）")

    show(conn, "6-3 ★ 取每个账户金额最大的一笔（分组取 TOP1）",
         "SELECT * FROM ("
         "  SELECT account_no, id, amount, create_time, "
         "  ROW_NUMBER() OVER (PARTITION BY account_no ORDER BY amount DESC) AS rn "
         "  FROM trans"
         ") WHERE rn = 1",
         "★ 经典用法：PARTITION BY 分组 + ROW_NUMBER 排序 + 外层筛 rn=1")

    show(conn, "6-4 SUM OVER：按时间累计金额（累计求和）",
         "SELECT account_no, create_time, amount, "
         "SUM(amount) OVER (PARTITION BY account_no ORDER BY create_time) AS 累计金额 "
         "FROM trans WHERE account_no='1001'",
         "窗口函数不折叠行，每行都保留并附带聚合值")

    show(conn, "6-5 LAG：查上一笔交易金额（环比）",
         "SELECT account_no, create_time, amount, "
         "LAG(amount, 1) OVER (PARTITION BY account_no ORDER BY create_time) AS 上一笔, "
         "amount - LAG(amount, 1) OVER (PARTITION BY account_no ORDER BY create_time) AS 差额 "
         "FROM trans WHERE account_no='1001'",
         "LAG 取上一行，LEAD 取下一行")

    show(conn, "6-6 AVG OVER：每笔金额与该账户平均值的对比",
         "SELECT id, account_no, amount, "
         "ROUND(AVG(amount) OVER (PARTITION BY account_no), 2) AS 账户均值 "
         "FROM trans",
         "窗口聚合 vs GROUP BY：窗口不减少行数")

    conn.close()

    print("\n" + "=" * 70)
    print("练习完成。建议：把上面每条 SQL 遮住，自己默写一遍。")
    print("重点掌握：LEFT JOIN + IS NULL、GROUP BY + HAVING、")
    print("         数据校验类查询（查重复/查孤儿/查异常）、")
    print("         ROW_NUMBER 分组取 TOP1")
    print("=" * 70)


if __name__ == "__main__":
    main()
