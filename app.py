import streamlit as st
import speech_recognition as sr
import pyttsx3

# Настройка синтезатора речи
engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('voice', 'ru')

st.set_page_config(page_title="Voice Access System", page_icon="🎙", layout="centered")
st.title("🎙 Система голосового доступа")
st.write("Скажите команду: **Открыть дверь**")

# Кнопка для активации микрофона
if st.button("🎧 Говорить"):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("Говорите...")
        audio = recognizer.listen(source, phrase_time_limit=5)
        st.success("Обработка...")

    try:
        text = recognizer.recognize_google(audio, language="ru-RU")
        st.write(f"🔎 Распознано: **{text}**")

        if "открыть дверь" in text.lower():
            st.success("✅ Доступ разрешён")
            st.markdown("<div style='background-color:green;color:white;padding:10px;border-radius:10px;text-align:center;'>Дверь открыта</div>", unsafe_allow_html=True)
            engine.say("Доступ разрешён")
            engine.runAndWait()
        else:
            st.error("⛔ Доступ запрещён")
            st.markdown("<div style='background-color:red;color:white;padding:10px;border-radius:10px;text-align:center;'>Дверь закрыта</div>", unsafe_allow_html=True)
            engine.say("Доступ запрещён")
            engine.runAndWait()
    except sr.UnknownValueError:
        st.warning("Не удалось распознать речь, повторите попытку.")
    except Exception as e:
        st.error(f"Ошибка: {e}")

st.caption("💡 Скажите «Открыть дверь» для разрешения доступа")


