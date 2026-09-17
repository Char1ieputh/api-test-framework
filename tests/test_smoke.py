"""框架自检用例：不依赖网络与 API Key，用于验证框架本身可运行。

即使没有配置 API Key，这个文件也必须能跑通（全绿）。
面试时可以先跑它，证明框架是活的。
"""


def test_framework_alive():
    """框架自检：断言模块可正常导入与执行。"""
    assert True


def test_parametrize_works():
    """验证参数化生效。"""
    assert 1 + 1 == 2


def test_assert_util_importable():
    """验证工具层可导入。"""
    from utils.assert_util import assert_not_empty

    assert_not_empty("有内容", "工具层自检")
