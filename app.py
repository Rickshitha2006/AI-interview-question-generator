import streamlit as st
from groq import Groq
from dotenv import load_dotenv
import os

# ----------------------------
# Load API Key
# ----------------------------
load_dotenv()

if "GROQ_API_KEY" in st.secrets:
    api_key = st.secrets["GROQ_API_KEY"]
else:
    api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    st.error("❌ GROQ API Key not found!")
    st.info("Add your API key in .env (local) or Streamlit Secrets.")
    st.stop()

client = Groq(api_key=api_key)

# ----------------------------
# Streamlit Page
# ----------------------------
st.set_page_config(
    page_title="AI Interview Question Generator",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Interview Question Generator")
st.write("Generate AI-powered interview questions with answers using Groq AI.")

st.divider()

# ----------------------------
# User Inputs
# ----------------------------

col1, col2 = st.columns(2)

with col1:
    domain = st.selectbox(
        "📚 Select Domain",
        [
            "Python",
            "Java",
            "C++",
            "Artificial Intelligence",
            "Machine Learning",
            "Data Science",
            "DBMS",
            "SQL",
            "HTML",
            "CSS",
            "JavaScript",
            "React",
            "Node.js"
        ]
    )

with col2:
    difficulty = st.selectbox(
        "🎯 Difficulty",
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
# Generate
# ----------------------------

if st.button("🚀 Generate Questions", use_container_width=True):

    prompt = f"""
Generate {num_questions} {difficulty} interview questions for {domain}.

For each question provide:

Question:
Answer:

Rules:

1. Answers should be simple.
2. Suitable for college students.
3. Keep answers under 6 lines.
4. Use markdown formatting.
"""

    with st.spinner("Generating Interview Questions..."):

        try:

            response = client.chat.completions.create(

                model="llama-3.3-70b-versatile",

                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],

                temperature=0.7,

                max_tokens=2048

            )

            result = response.choices[0].message.content

            st.success("✅ Questions Generated Successfully!")

            st.markdown(result)

        except Exception as e:
            st.error(f"❌ Error : {e}")
