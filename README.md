# 聊天机器人

基于 Streamlit 构建的本地聊天机器人，通过 OpenAI 兼容接口对接 DeepSeek 大模型，支持多轮对话与历史记录持久化。

## 功能特性

- **多轮对话**：保持完整上下文，支持 system prompt 角色预设
- **历史管理**：侧边栏新建 / 切换 / 删除历史对话
- **本地存储**：对话内容以 JSON 格式持久化到 `JsonDB/data.json`

## 项目结构

```
聊天机器人/
├── app.py                 # 入口文件
├── chat.py                 # AI 接口调用（OpenAI SDK）
├── config.py              # 配置（API 地址、模型）
├── JsonDB/
│   ├── conversations.py   # 对话 CRUD 操作
│   └── data.json          # 对话数据文件（自动生成）
├── Layout/
│   ├── sidebar.py         # 侧边栏 UI（新建/切换/删除对话）
│   └── chat_area.py       # 聊天区域 UI（消息展示与输入）
└── requirements.txt       # Python 依赖
```

## 环境要求

- Python 3.8+
- DeepSeek API Key（[申请地址](https://platform.deepseek.com)）

## 安装运行

```bash
# 1. 安装依赖
pip install -r requirements.txt

# 2. 设置 API Key
# Windows (CMD):
set DEEPSEEK_API_KEY=your-api-key-here

# Windows (PowerShell):
$env:DEEPSEEK_API_KEY="your-api-key-here"

# macOS / Linux:
export DEEPSEEK_API_KEY="your-api-key-here"

# 3. 启动应用
streamlit run app.py    # 或 python -m streamlit run app.py
```

## 配置说明

编辑 [config.py](config.py) 可修改以下参数：

| 参数 | 默认值 | 说明 |
|------|--------|------|
| `BASE_URL` | `https://api.deepseek.com` | API 服务地址（OpenAI 兼容接口均可） |
| `MODEL` | `deepseek-v4-pro` | 使用的模型名称 |

如需切换其他兼容 OpenAI 接口的服务（如 Ollama、vLLM），只需修改 `BASE_URL` 和 `MODEL` 即可。

## 使用说明

1. 启动后在浏览器中打开 Streamlit 提供的地址（默认 `http://localhost:8501`）
2. 点击左侧 **＋ 新对话** 创建新会话
3. 在底部输入框输入消息，按回车发送
4. 对话自动保存，可在侧边栏点击历史记录切换或点击 🗑 删除
