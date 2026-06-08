import json
import os
from datetime import datetime
from typing import Optional

# 设置文件路径
HISTORY_FILE = os.path.join(os.path.dirname(__file__), "data.json")


def _load_all() -> dict:
    """读取全部历史记录"""
    if not os.path.exists(HISTORY_FILE):
        return {"conversations": []}
    with open(HISTORY_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def _save_all(conversations: dict):
    """写入全部历史记录"""
    with open(HISTORY_FILE, "w", encoding="utf-8") as f:
        json.dump(conversations, f, ensure_ascii=False, indent=2)



def list_conversations() -> list[dict]:
    """列出所有对话（不含消息内容），按时间倒序"""
    data = _load_all()
    convs = data.get("conversations", [])
    result = []
    for c in convs:
        result.append({
            "id": c["id"],
            "title": c.get("title", "新对话"),
            "created_at": c.get("created_at", ""),
            "message_count": len(c.get("messages", [])),
        })
    # 按 created_at 倒序
    result.sort(key=lambda x: x["created_at"], reverse=True)
    return result


def select_conversation_by_id(conv_id: str) -> Optional[dict]:
    """根据 ID 获取对话详情（含消息内容）"""
    data = _load_all()
    for c in data.get("conversations", []):
        if c["id"] == conv_id:
            return c
    return None


def insert_conversation(conv_id: str, messages: list):
    """保存或更新对话"""
    data = _load_all()
    conversations = data.get("conversations", [])

    # 自动生成标题：取第一条用户消息的前30个字符
    title = "新对话"
    for m in messages:
        if m.get("role") == "user":
            title = m["content"][:30]
            break

    for c in conversations:
        if c["id"] == conv_id:
            c["messages"] = messages
            c["title"] = title
            break
    else:
        conversations.append({
            "id": conv_id,
            "title": title,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "messages": messages,
        })

    data["conversations"] = conversations
    _save_all(data)


def delete_conversation_by_id(conv_id: str):
    """删除指定对话"""
    data = _load_all()
    data["conversations"] = [c for c in data.get("conversations", []) if c["id"] != conv_id]
    _save_all(data)
