import streamlit as st
import openai
from dotenv import load_dotenv
import os

st.set_page_config(page_title="QuizAI", layout="centered")

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key

st.title("🧠 QuizAI - Otomatik Quiz Oluşturucu")
st.write("Yapay zeka ile otomatik çoktan seçmeli test soruları üretin!")

topic = st.text_input("Konu Başlığı Girin (örn. Osmanlı Tarihi, Python Değişkenler):")

def generate_quiz(topic):
    prompt = f"""
    Konu: {topic}
    Bu konuyla ilgili 5 adet çoktan seçmeli soru oluştur.
    Her soru için:
    - Soru metni
    - 4 şık (A, B, C, D)
    - Doğru cevabın harfi (yalnızca harf)
    Format:

    1. Soru: ...
       A) ...
       B) ...
       C) ...
       D) ...
       Cevap: B
    """
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

if st.button("Quiz Oluştur"):
    if topic.strip() == "":
        st.warning("Lütfen bir konu girin.")
    else:
        with st.spinner("Sorular oluşturuluyor..."):
            try:
                quiz_text = generate_quiz(topic)
                st.success("Quiz hazır!")
                st.text_area("Sorular", quiz_text, height=350)
            except openai.error.OpenAIError as e:
                st.error(f"API hatası: {e}")

st.markdown("---")
st.caption("Developed with ❤️ using Streamlit and OpenAI GPT-4")
