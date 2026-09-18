"""独立探测脚本：把接口原始返回写入文件，用于排除终端显示干扰。

用法（在项目根目录执行）：
    D:\\work\\python\\python310\\python.exe probe_raw_output.py

输出：
    reports/raw_01.txt ... reports/raw_10.txt
    reports/raw_summary.txt  （汇总，方便一眼对比）
"""
import json
import sys
from pathlib import Path

# 让脚本能 import 到项目里的模块
sys.path.insert(0, str(Path(__file__).resolve().parent))

from api.chat_api import ChatApi  # noqa: E402
from config.config import config  # noqa: E402
import requests  # noqa: E402

INPUT_TEXT = "你好，how are you?"
RUNS = 10
REPORT_DIR = Path(__file__).resolve().parent / "reports"


def main():
    REPORT_DIR.mkdir(exist_ok=True)

    session = requests.Session()
    session.headers.update({
        "Content-Type": "application/json",
        "Authorization": f"Bearer {config.API_KEY}",
    })
    api = ChatApi(session)

    summary = []
    for i in range(1, RUNS + 1):
        resp = api.chat(INPUT_TEXT)
        if resp.status_code != 200:
            print(f"[{i:02d}] 状态码 {resp.status_code}，跳过：{resp.text[:100]}")
            continue

        content = api.get_content(resp)

        # 每次单独写一个文件，UTF-8，不经过终端
        out_file = REPORT_DIR / f"raw_{i:02d}.txt"
        out_file.write_text(content, encoding="utf-8")

        has_chinese = any("\u4e00" <= ch <= "\u9fa5" for ch in content)
        summary.append({"run": i, "has_chinese": has_chinese, "content": content})

        print(f"[{i:02d}] 已写入 {out_file.name}  "
              f"含中文={has_chinese}  长度={len(content)}")

    # 汇总文件，方便一次性对比
    summary_file = REPORT_DIR / "raw_summary.txt"
    with summary_file.open("w", encoding="utf-8") as f:
        f.write(f"输入：{INPUT_TEXT}\n")
        f.write(f"轮次：{RUNS}\n\n")
        for item in summary:
            f.write(f"===== 第 {item['run']:02d} 次 | 含中文={item['has_chinese']} =====\n")
            f.write(item["content"] + "\n\n")

    chinese_count = sum(1 for s in summary if s["has_chinese"])
    print("\n" + "=" * 50)
    print(f"完成：{len(summary)} 次有效返回")
    print(f"含中文：{chinese_count} 次")
    print(f"不含中文（疑似语言漂移）：{len(summary) - chinese_count} 次")
    print(f"汇总文件：{summary_file}")
    print("=" * 50)
    print("\n下一步：打开 reports\\raw_summary.txt 逐条核对，")
    print("确认接口原始返回里到底有没有漏字。")


if __name__ == "__main__":
    main()
