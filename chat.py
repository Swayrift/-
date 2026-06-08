import os
from openai import OpenAI
from config import BASE_URL, MODEL

_client = None

def _get_client():
    global _client
    if _client is None:
        api_key = os.environ.get("DEEPSEEK_API_KEY")
        if not api_key:
            raise RuntimeError(
                "未找到 API Key，请设置环境变量 DEEPSEEK_API_KEY"
            )
        _client = OpenAI(api_key=api_key, base_url=BASE_URL)
    return _client

# 调用接口发送消息并获取回复
def chat(messages: list) -> str:
    response = _get_client().chat.completions.create(
        model=MODEL,
        messages=messages,
        stream=False,
    )
    return response.choices[0].message.content