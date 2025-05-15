import streamlit as st
import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

api_key=os.getenv("groq_api_key")

def get_reponse(message):
    """
    Sends a request to the Groq API and retrieves a response.

    This function uses the API key stored in the environment variables
    to authenticate the request. It is designed to interact with the
    Groq chatbot API and return the response received.

    Returns:
        str: The response from the Groq API as a string.
    """
    
    headers={
        "Authorization":f"bearer{api_key}",
        "Content-type":"appilication/json"
    }
    system_prompt="""You are a helpful and intelligent coding assistant named CodeCopilot. 
                    You help programmers by answering coding questions, explaining concepts clearly, 
                    generating code snippets, fixing errors, and improving code quality. 
                    You are concise, accurate, and provide code in clean, readable format. 

                    When given a prompt, respond in a helpful and encouraging tone. 
                    If clarification is needed, ask follow-up questions. 
                    When possible, provide examples and explain why your solution works.

                    You specialize in Python, JavaScript, C++, Java, and SQL, but can also assist with other languages. 
                    You are aware of best practices, algorithms, and libraries. 
                    If asked for help with debugging, you analyze the error and suggest fixes.

                    Always wrap code in markdown-style code blocks using the correct language tag."""
    payload={
        'model':"llama3-8b-8192",
        "messages":[
            {
                "role":"system",
                "content":system_prompt
            },
            {
                "role":"user",
                "content":message
            }
        ],
        "temperature": 0.7,
        "top_p": 0.9,
        "max_tokens": 8192,
    }
    
    try:
        client = Groq(api_key=api_key)
        response=client.chat.completions.create(**payload)
        return response.choices[0].message.content
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return None
