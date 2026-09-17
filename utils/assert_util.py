"""工具层：统一断言封装，失败时输出可读信息。"""


def assert_status(resp, expected: int = 200, desc: str = ""):
    """校验 HTTP 状态码。"""
    assert resp.status_code == expected, (
        f"[{desc}] 状态码不符，期望 {expected}，实际 {resp.status_code}，"
        f"响应: {resp.text[:200]}"
    )


def assert_not_auth_error(resp, desc: str = ""):
    """前置守卫：拦截鉴权失败，避免用例「假通过」。

    背景：缺少字段、字段类型错误等用例期望 4xx，
    但鉴权失败同样返回 401，会让用例错误地变绿。
    因此所有期望 4xx 的用例必须先过这一关。
    """
    assert resp.status_code != 401, (
        f"[{desc}] 鉴权失败(401)，本用例未真正验证目标场景。"
        f"请检查 .env 中的 API_KEY。响应: {resp.text[:200]}"
    )
    assert resp.status_code != 403, (
        f"[{desc}] 权限不足(403)，本用例未真正验证目标场景。响应: {resp.text[:200]}"
    )


def assert_not_empty(text: str, desc: str = ""):
    """校验返回内容非空。"""
    assert text and text.strip(), f"[{desc}] 返回内容为空"


def assert_contains(text: str, keyword: str, desc: str = ""):
    """校验返回内容包含关键字。"""
    assert keyword in text, f"[{desc}] 返回内容未包含 '{keyword}'，实际: {text[:200]}"


def assert_json_field(data: dict, field: str, desc: str = ""):
    """校验响应 JSON 中存在指定字段。"""
    assert field in data, f"[{desc}] 响应中缺少字段 '{field}'，实际字段: {list(data.keys())}"
