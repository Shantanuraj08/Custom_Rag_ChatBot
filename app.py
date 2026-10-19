import streamlit as st

from custom_assistant.pipeline import ask, build_custom_agent



st.set_page_config(page_title="Employee Policy Assistant", page_icon="🤖")
st.title("Employee Policy Assistant")
st.caption("Ask me anything about the company Employee policy document.")


@st.cache_resource(show_spinner="Setting up the assistant (only happens once)...")
def get_agent():
    return build_custom_agent()


agent = get_agent()

if "messages" not in st.session_state:
    st.session_state.messages = []

# Show the past conversation
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Get a new question from the user
question = st.chat_input("Ask a question about HR policy...")

if question:
    
    st.session_state.messages.append({"role": "user", "content": question})
    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            answer = ask(agent, question)
        st.markdown(answer)
    st.session_state.messages.append({"role": "assistant", "content": answer})