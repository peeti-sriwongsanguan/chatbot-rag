import streamlit as st
from src.chatbot import RAGChatbot
import yaml

# Load configuration
with open('configs/config.yml', 'r') as f:
    config = yaml.safe_load(f)

# Initialize chatbot
@st.cache_resource
def get_chatbot():
    return RAGChatbot()

chatbot = get_chatbot()

# Streamlit UI
st.title(config['streamlit_title'])

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("What is your question?"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Get chatbot response
    response = chatbot.get_response(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})