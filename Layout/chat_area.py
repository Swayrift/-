import streamlit as st
from chat import chat
from JsonDB.conversations import insert_conversation


def render():
    """渲染对话区域"""
    
    if "messages" not in st.session_state:
        st.title("聊天机器人")
        st.session_state.messages = []

    # 显示对话消息
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # 读取用户输入
    if prompt := st.chat_input("请输入你的消息..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.spinner("正在生成回复..."):
            # 调用机器人
            response = chat(st.session_state.messages)
            st.session_state.messages.append({"role": "assistant", "content": response})
            with st.chat_message("assistant"):
                st.markdown(response)

        # 自动保存到 JSON
        insert_conversation(st.session_state.conv_id, st.session_state.messages)
