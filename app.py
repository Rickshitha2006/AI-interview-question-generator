import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

# ----------------------------
# Load API Key
# ----------------------------
load_dotenv()

if "GEMINI_API_KEY" in st.secrets:
    api_key = st.secrets["GEMINI_API_KEY"]
else:
    api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("❌ Gemini API Key not found!")
    st.info("For local use, create a .env file.\nFor Streamlit Cloud, add GEMINI_API_KEY in Secrets.")
    st.stop()

# ----------------------------
# Configure Gemini
# ----------------------------
genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.5-flash")

# ----------------------------
# Streamlit Page
# ----------------------------
st.set_page_config(
    page_title="AI Interview Question Generator",
    page_icon="🤖"
)

st.title("🤖 AI Interview Question Generator")
st.write("Generate AI-powered interview questions with answers.")

# ----------------------------
# User Inputs
# ----------------------------
domain = st.selectbox(
    "📚 Select Domain",
    [
        "Python",
        "Java",
        "C++",
        "Machine Learning",
        "Artificial Intelligence",
        "Data Science",
        "DBMS",
        "HTML",
        "CSS",
        "JavaScript",
        "React",
        "SQL"
    ]
)

difficulty = st.selectbox(
    "🎯 Difficulty Level",
    [
        "Beginner",
        "Intermediate",
        "Advanced"
    ]
)

num_questions = st.slider(
    "📄 Number of Questions",
    min_value=5,
    max_value=20,
    value=5
)

# ----------------------------
# Generate Questions
# ----------------------------
if st.button("🚀 Generate Questions"):

    prompt = f"""
Generate {num_questions} {difficulty} interview questions for {domain}.

For every question provide:

Question:
Answer:

Keep the answers simple, short and suitable for college students.

Format properly using headings and bullet points.
"""

    with st.spinner("Generating Interview Questions..."):

        try:
            response = model.generate_content(prompt)

            st.success("✅ Questions Generated Successfully!")

            st.markdown(response.text)

        except Exception as e:
            st.error(f"Error: {e}")
