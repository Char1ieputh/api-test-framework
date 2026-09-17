"""跨文件共享的 fixture。"""
import pytest
import requests

from api.chat_api import ChatApi
from config.config import config


@pytest.fixture(scope="session")
def session():
    """全局会话：统一 headers，复用连接。"""
    s = requests.Session()
    s.headers.update({
        "Content-Type": "application/json",
        "Authorization": f"Bearer {config.API_KEY}",
    })
    yield s
    s.close()


@pytest.fixture(scope="session")
def chat_api(session):
    """对话接口实例，全局复用。"""
    return ChatApi(session)
