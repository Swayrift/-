import os

# 大模型配置
BASE_URL = "https://api.deepseek.com"
MODEL = "deepseek-v4-flash"
API_KEY = os.environ.get("DEEPSEEK_API_KEY", "")

# 数据库配置
DB_HOST = "localhost"
DB_PORT = 3306
DB_USER = "root"
DB_PASSWORD = "root"
DB_NAME = "chatbot"
