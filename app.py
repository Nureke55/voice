import streamlit as st
import speech_recognition as sr
from gtts import gTTS
import tempfile
import os

st.set_page_config(page_title="Voice Access System", page_icon="🎙", layout="centered")
st.title("🎙 Система голосового доступа")
st.write("🎧 Загрузите голосовую команду (например, 'Открыть дверь')")

audio_file = st.file_uploader("Загрузите аудиофайл (.wav или .mp3)", type=["wav", "mp3"])

if audio_file is not None:
    st.audio(audio_file)
    recognizer = sr.Recognizer()

    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(audio_file.read())
        tmp_path = tmp.name

    with sr.AudioFile(tmp_path) as source:
        audio = recognizer.record(source)

    try:
        text = recognizer.recognize_google(audio, language="ru-RU")
        st.write(f"🔎 Распознано: **{text}**")

        if "открыть дверь" in text.lower():
            st.success("✅ Доступ разрешён")
            st.markdown("<div style='background-color:green;color:white;padding:10px;border-radius:10px;text-align:center;'>Дверь открыта</div>", unsafe_allow_html=True)
            tts = gTTS("Доступ разрешён", lang="ru")
        else:
            st.error("⛔ Доступ запрещён")
            st.markdown("<div style='background-color:red;color:white;padding:10px;border-radius:10px;text-align:center;'>Дверь закрыта</div>", unsafe_allow_html=True)
            tts = gTTS("Доступ запрещён", lang="ru")

        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as audio_out:
            tts.save(audio_out.name)
            st.audio(audio_out.name, format="audio/mp3")

    except sr.UnknownValueError:
        st.warning("Не удалось распознать речь.")
    except Exception as e:
        st.error(f"Ошибка: {e}")

