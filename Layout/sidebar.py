import uuid
import streamlit as st
from JsonDB.conversations import list_conversations, select_conversation_by_id, delete_conversation_by_id


# -- 回调：开始新对话 --
def new_chat():
    st.session_state.conv_id = str(uuid.uuid4())
    st.title("A Easy ChatBot")
    st.session_state.messages = []


# -- 回调：加载历史对话 --
def load_chat(conv_id: str):
    conv = select_conversation_by_id(conv_id)
    if conv:
        st.session_state.conv_id = conv["id"]
        st.session_state.messages = conv["messages"]


# -- 回调：删除历史对话 --
def delete_chat(conv_id: str):
    delete_conversation_by_id(conv_id)
    if st.session_state.conv_id == conv_id:
        new_chat()


# -- 渲染侧边栏 --
def render():
    if "conv_id" not in st.session_state:
        st.session_state.conv_id = str(uuid.uuid4())

    with st.sidebar:
        st.button("＋ 新对话", on_click=new_chat, use_container_width=True)

        st.divider()

        conversations = list_conversations()
        if not conversations:
            st.caption("暂无历史记录")
        else:
            for conv in conversations:
                col1, col2 = st.columns([4, 1])
                with col1:
                    is_active = conv["id"] == st.session_state.conv_id
                    label = f"{'● ' if is_active else ''}{conv['title']}"
                    st.button(
                        label,
                        key=f"load_{conv['id']}",
                        on_click=load_chat,
                        args=(conv["id"],),
                        use_container_width=True,
                    )
                with col2:
                    st.button(
                        "🗑",
                        key=f"del_{conv['id']}",
                        on_click=delete_chat,
                        args=(conv["id"],),
                    )
