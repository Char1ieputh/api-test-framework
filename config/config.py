"""环境配置：从 .env 读取 BaseURL、API Key、超时时间。"""
import os
from pathlib import Path

from dotenv import load_dotenv

# 项目根目录
ROOT_DIR = Path(__file__).resolve().parent.parent

# 加载 .env（不存在时不报错，便于 CI 环境用系统环境变量）
load_dotenv(ROOT_DIR / ".env")


class Config:
    """全局配置。"""

    BASE_URL: str = os.getenv("BASE_URL", "https://api.deepseek.com").rstrip("/")
    API_KEY: str = os.getenv("API_KEY", "")
    TIMEOUT: int = int(os.getenv("TIMEOUT", "30"))

    # 接口路径
    CHAT_PATH: str = "/v1/chat/completions"

    # 默认模型
    MODEL: str = os.getenv("MODEL", "deepseek-chat")


config = Config()
