"""接口层：只负责"怎么调接口"，不写业务断言。"""
import requests

from config.config import config


class ChatApi:
    """大模型对话接口封装（OpenAI 兼容协议）。"""

    def __init__(self, session: requests.Session):
        self.session = session
        self.url = f"{config.BASE_URL}{config.CHAT_PATH}"

    def chat(self, content: str, model: str = None, **extra) -> requests.Response:
        """发送单轮对话请求。

        :param content: 用户输入内容
        :param model: 模型名，默认取配置
        :param extra: 其他需要透传的请求体字段
        """
        payload = {
            "model": model or config.MODEL,
            "messages": [{"role": "user", "content": content}],
            **extra,
        }
        return self.session.post(self.url, json=payload, timeout=config.TIMEOUT)

    def chat_raw(self, payload: dict) -> requests.Response:
        """发送原始 payload，用于构造异常/畸形请求体。"""
        return self.session.post(self.url, json=payload, timeout=config.TIMEOUT)

    @staticmethod
    def get_content(resp: requests.Response) -> str:
        """从响应中取出模型回复文本。"""
        data = resp.json()
        return data["choices"][0]["message"]["content"]
