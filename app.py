import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("API_KEY")
genai.configure(api_key=api_key)


# Configure GenAI with API key
# genai.configure(api_key="API_KEY")

# Create the model
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="tunedModels/ind-as-115-revenue-recognition-3oontpmqc",
    generation_config=generation_config,
)

# Streamlit app interface
st.title("IND AS-115  AI")
st.write("By Shiv Bhushan Upadhyay")
# User input
user_input = st.text_input("Ask a question:", "")
if user_input:
    # Start chat session
    chat_session = model.start_chat(history=[])
    response = chat_session.send_message(user_input)
    
    # Display response
    st.subheader("Response:")
    st.write(response.text)