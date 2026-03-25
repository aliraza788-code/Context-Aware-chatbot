import streamlit as st
import os
from utils import load_data, create_chain

# ✅ API KEY
os.environ["GROQ_API_KEY"] = "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"

st.set_page_config(page_title="Context Aware  Chatbot", layout="wide")

st.title("🤖 Context Aware Chatbot")

with st.sidebar:
    st.title("⚙ Settings")

    if st.button("Clear Chat"):
        st.session_state.messages = []

    # ✅ Download Chat
    if st.session_state.get("messages"):
        chat_text = ""
        for msg in st.session_state.messages:
            role = msg["role"]
            content = msg["content"]
            chat_text += f"{role.upper()}: {content}\n\n"

        st.download_button(
            label="📥 Download Chat",
            data=chat_text,
            file_name="chat_history.txt",
            mime="text/plain"
        )

# ✅ Load data once
if "qa_chain" not in st.session_state:
    docs = load_data()
    st.session_state.qa_chain = create_chain(docs)

# ✅ Chat history store
if "messages" not in st.session_state:
    st.session_state.messages = []

# ✅ Display previous messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ✅ Input box
user_input = st.chat_input("Ask something...")

if user_input:
    # Show user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Get response
    response = st.session_state.qa_chain({"query": user_input})
    answer = response["result"]

    # Show bot message
    st.session_state.messages.append({"role": "assistant", "content": answer})
    with st.chat_message("assistant"):
        st.markdown(answer)





    ##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