import streamlit as st
import groq_ai


st.set_page_config(page_title="CodeCopilot", page_icon=":robot_face:")
st.title("CodeCopilot: Your AI Coding Assistant")
st.write("Welcome to CodeCopilot, your AI-powered coding assistant! Ask me anything about programming, and I'll do my best to help you out.")

if st.sidebar.button("🔁Clear Chat"):
    st.session_state.messages = []
    st.session_state.response = ""
    st.session_state.user_input = ""
    st.rerun()
    
if "messages" not in st.session_state:
    st.session_state.messages = []

if "response" not in st.session_state:
    st.session_state.response = ""
    
if "user_input" not in st.session_state:
    st.session_state.user_input = ""
    
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
        
user_input=st.chat_input('Type your message here...')

if user_input:
    st.session_state.messages.append({'role':'user','content':user_input})
    
        
    bot_reply=groq_ai.get_reponse(user_input)
    st.session_state.messages.append({'role':'assistant','content':bot_reply})
    
        
    if len(st.session_state.messages) > 1:
        with st.chat_message('user'):
            st.markdown(user_input)
        with st.chat_message('assistant'):
            st.markdown(bot_reply)
    else:
        st.write("Please enter a message to start the conversation.")
        
