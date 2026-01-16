import streamlit as st
from google import genai

# ---------------- CONFIG ----------------
API_KEY = "AIzaSyBYJG779_rrBjNAJVtX2_680-wapgEH05w"  # 🔴 your key
MODEL_NAME = "models/gemini-flash-lite-latest"

client = genai.Client(api_key=API_KEY)

# ---------------- PAGE SETUP ----------------
st.set_page_config(
    page_title="AI Study Helper",
    page_icon="🎓",
    layout="centered"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
.main {
    background-color: #f5f7fb;
}
.card {
    background-color: white;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    margin-top: 20px;
}
.title {
    text-align: center;
    font-size: 40px;
    font-weight: bold;
    color: #2c3e50;
}
.subtitle {
    text-align: center;
    color: #555;
    margin-bottom: 30px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown('<div class="title">🎓 AI Study Helper</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Learn any topic easily (Class 6–10)</div>', unsafe_allow_html=True)

# ---------------- INPUT CARD ----------------
st.markdown('<div class="card">', unsafe_allow_html=True)

class_level = st.selectbox("📘 Select Class", ["6", "7", "8", "9", "10"])
subject = st.selectbox("📚 Select Subject", ["Science", "Maths", "Social Science", "English"])
topic = st.text_input("✏️ Enter Topic (Example: Magnets)")

explain = st.button("✨ Explain Simply")

st.markdown('</div>', unsafe_allow_html=True)

# ---------------- OUTPUT ----------------
if explain and topic.strip():
    prompt = f"""
    Explain the topic '{topic}' for Class {class_level} {subject}.
    Use very simple language.
    Use bullet points.
    Give one real-life example.
    """

    try:
        with st.spinner("🧠 Thinking..."):
            response = client.models.generate_content(
                model=MODEL_NAME,
                contents=prompt
            )

        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("### ✅ Explanation")
        st.write(response.text)
        st.markdown('</div>', unsafe_allow_html=True)

    except Exception as e:
        st.error("⚠️ Something went wrong")
        st.code(str(e))

elif explain:
    st.warning("Please enter a topic first.")

# ---------------- FOOTER ----------------
st.markdown("""
<hr>
<p style="text-align:center; color:gray;">
Made with ❤️ using Gemini AI
</p>
""", unsafe_allow_html=True)
