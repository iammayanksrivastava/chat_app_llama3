import streamlit as st
import ollama
import logging
import logging_config
import chat

logging_config.configure_logging()

# Use the standard logging.getLogger() to get logger instances
logger = logging.getLogger(__name__)

st.title("Llama3 Chatbot")

if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "assistant", "content": "How can I help you?"}
    ]

for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.chat_message(msg["role"], avatar="🧑‍💻").write(msg["content"])
    else:
        st.chat_message(msg["role"], avatar="🤖").write(msg["content"])

if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user", avatar="🧑‍💻").write(prompt)
    st.session_state["full_message"] = ""
    try:
        st.chat_message("assistant", avatar="🤖").write_stream(
            chat.generate_response(st.session_state.messages, logger, st)
        )
    except Exception as e:
        logger.error(f"Error processing user input: {e}", exc_info=True)
    st.session_state.messages.append(
        {"role": "assistant", "content": st.session_state["full_message"]}
    )
