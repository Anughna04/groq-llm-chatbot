import os
import streamlit as st
from groq import Groq

groq_api_key="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"

st.sidebar.title("Personalization")
prompt=st.sidebar.title("System prompt: ")
model=st.sidebar.selectbox('Choose a model',['Llama3-8b-8192','Llama3-70b-8192','Mixtral-8x7b-32768','Gemma-7b-It'])

client=Groq(api_key=groq_api_key)

st.title("Chat with Groq LLM")

if "history" not in st.session_state:
    st.session_state.history=[]

user_input=st.text_input("Enter your query: ","")
if st.button("Submit"):
    chat_completion=client.chat.completions.create(
        messages=[
            {
                "role":"user",
                "content":user_input,
            }
        ],
        model=model,
    )

    response=chat_completion.choices[0].message.content
    st.session_state.history.append({"query":user_input,"response":response})

    st.markdown(f'<div class="response-box">{response}</div',unsafe_allow_html=True)

st.sidebar.title("History")
for i,entry in enumerate(st.session_state.history):
    if st.sidebar.button(f'Query {i+1}: {entry["query"]}'):
        st.markdown(f'<div class="response-box">{entry["response"]}</div',unsafe_allow_html=True)

