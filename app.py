import streamlit as st
from groq import Groq
from dotenv import load_dotenv
import os

# -----------------------------
# Load Environment
# -----------------------------
load_dotenv()

if "GROQ_API_KEY" in st.secrets:
    api_key = st.secrets["GROQ_API_KEY"]
else:
    api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    st.error("❌ GROQ API Key not found!")
    st.info("Add GROQ_API_KEY in .env (local) or Streamlit Secrets.")
    st.stop()

client = Groq(api_key=api_key)

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="AI Interview Question Generator",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------
# Custom CSS
# -----------------------------
st.markdown("""
<style>

.stApp{
    background:linear-gradient(135deg,#0f172a,#1e293b);
}

h1,h2,h3{
    color:white;
}

.main-title{
    text-align:center;
    font-size:48px;
    font-weight:700;
    color:#38bdf8;
}

.sub-title{
    text-align:center;
    color:#d1d5db;
    font-size:18px;
    margin-bottom:25px;
}

.card{
    background:#1e293b;
    padding:20px;
    border-radius:15px;
    border:1px solid #334155;
    box-shadow:0px 4px 15px rgba(0,0,0,.3);
}

.metric-card{
    background:#111827;
    border-radius:15px;
    padding:15px;
    text-align:center;
}

.stButton>button{
    background:#2563eb;
    color:white;
    border:none;
    border-radius:12px;
    padding:12px;
    font-size:18px;
    font-weight:bold;
    width:100%;
}

.stButton>button:hover{
    background:#1d4ed8;
}

.footer{
    text-align:center;
    color:#9ca3af;
    margin-top:40px;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# Sidebar
# -----------------------------
with st.sidebar:

    st.title("🤖 AI Interview")

    st.write("### Features")

    st.success("✔ AI Generated Questions")
    st.success("✔ AI Answers")
    st.success("✔ 12+ Domains")
    st.success("✔ Beginner to Advanced")
    st.success("✔ Powered by Groq")

    st.divider()

    st.info(
        """
This application helps students prepare for technical interviews using AI.
        """
    )

# -----------------------------
# Header
# -----------------------------
st.markdown(
    "<div class='main-title'>🤖 AI Interview Question Generator</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='sub-title'>Practice Technical Interviews using Groq AI</div>",
    unsafe_allow_html=True
)

# -----------------------------
# Dashboard
# -----------------------------
c1,c2,c3=st.columns(3)

with c1:
    st.metric("Domains","12+")

with c2:
    st.metric("Model","Llama 3.3")

with c3:
    st.metric("Questions","5-20")

st.write("")

# -----------------------------
# Input Card
# -----------------------------
st.markdown("<div class='card'>",unsafe_allow_html=True)

col1,col2=st.columns(2)

with col1:

    domain=st.selectbox(
        "📚 Domain",
        [
            "Python",
            "Java",
            "C++",
            "JavaScript",
            "React",
            "Node.js",
            "HTML",
            "CSS",
            "SQL",
            "DBMS",
            "Machine Learning",
            "Artificial Intelligence"
        ]
    )

with col2:

    difficulty=st.selectbox(
        "🎯 Difficulty",
        [
            "Beginner",
            "Intermediate",
            "Advanced"
        ]
    )

num_questions=st.slider(
    "📄 Number of Questions",
    5,
    20,
    5
)

generate=st.button("🚀 Generate Interview Questions")

st.markdown("</div>",unsafe_allow_html=True)

# -----------------------------
# Generate Questions
# -----------------------------
if generate:

    prompt = f"""
You are an expert technical interviewer.

Generate {num_questions} {difficulty} interview questions for {domain}.

For every question provide:

### Question X
Question

**Answer:**
Simple explanation suitable for college students.

Rules:
- Use Markdown formatting.
- Keep answers under 5-6 lines.
- Explain clearly.
- Use bullet points wherever possible.
"""

    with st.spinner("🤖 AI is generating interview questions..."):

        try:

            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {
                        "role": "system",
                        "content": "You are a professional technical interviewer."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=0.7,
                max_tokens=2500
            )

            result = response.choices[0].message.content

            st.success("✅ Interview Questions Generated Successfully!")

            st.balloons()

            with st.expander("📄 View Interview Questions", expanded=True):
                st.markdown(result)

            st.download_button(
                label="📥 Download Questions",
                data=result,
                file_name=f"{domain}_Interview_Questions.txt",
                mime="text/plain"
            )

            st.info("""
💡 **Interview Tips**

• Read the question carefully.

• Explain your answer with an example.

• Practice speaking confidently.

• Revise important concepts before interviews.

• Don't memorize—understand the concepts.
""")

        except Exception as e:

            st.error("❌ Failed to generate questions.")
            st.code(str(e))

# -----------------------------
# Footer
# -----------------------------
st.divider()

col1, col2, col3 = st.columns(3)

with col1:
    st.info("👨‍💻 Built with Python")

with col2:
    st.info("⚡ Powered by Groq AI")

with col3:
    st.info("🚀 Developed using Streamlit")

st.markdown(
    """
<div class="footer">

Made with ❤️ using Streamlit & Groq AI

</div>
""",
    unsafe_allow_html=True,
)
