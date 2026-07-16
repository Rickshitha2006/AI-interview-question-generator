import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load API Key
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Gemini Model
model = genai.GenerativeModel("gemini-2.5-flash")

st.set_page_config(page_title="AI Interview Question Generator")

st.title("🤖 AI Interview Question Generator")

# User Inputs
domain = st.selectbox(
    "Select Domain",
    ["Python", "Java", "C++", "AI", "Machine Learning", "DBMS", "HTML", "CSS", "JavaScript"]
)

difficulty = st.selectbox(
    "Difficulty",
    ["Beginner", "Intermediate", "Advanced"]
)

num_questions = st.slider(
    "Number of Questions",
    5,
    20,
    5
)

if st.button("Generate Questions"):

    prompt = f"""
Generate {num_questions} {difficulty} interview questions on {domain}.

For each question, provide:

Question:
Answer:

Keep answers simple and concise.
"""

    with st.spinner("Generating Questions..."):
        response = model.generate_content(prompt)

    st.success("Questions Generated Successfully!")

    st.markdown(response.text)
