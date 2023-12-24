from dotenv import load_dotenv
load_dotenv() ##loading all the envrionment variables from the .env file

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## function to load Gemimi pro model and get responses
model = genai.GenerativeModel("gemini-pro")

def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text

st.set_page_config(page_title="Gemini Chatbot", page_icon=":robot:")
st.header("Gemini LLM Chatbot")
input=st.text_input("Enter your question here:", key="input")
submit = st.button("ask the questions")

## when submit is clicked
if submit:
    response=get_gemini_response(input)
    st.subheader("The response is")
    st.write(response)