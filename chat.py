import logging
import ollama


def generate_response(messages, logger, st):
    try:
        response = ollama.chat(
            model="llama3", stream=True, messages=st.session_state.messages
        )
        for partial_resp in response:
            token = partial_resp["message"]["content"]
            st.session_state["full_message"] += token
            yield token
    except Exception as e:
        logger.error(f"Error generating response: {e}", exc_info=True)
        raise e
