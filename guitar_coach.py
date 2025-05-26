import streamlit as st
import librosa
import soundfile as sf
import os

st.title("Tu Maestro Virtual de Guitarra")
st.subheader("Géneros: Gypsy Jazz, Jazz y Blues")

st.markdown("### 1. Sube tu grabación de práctica (formato .wav o .mp3)")
audio_file = st.file_uploader("Sube un archivo de audio", type=["wav", "mp3"])

def evaluar_audio(file):
    y, sr = librosa.load(file, sr=None)
    duration = librosa.get_duration(y=y, sr=sr)
    tempo, _ = librosa.beat.beat_track(y=y, sr=sr)
    return f"- Duración: {duration:.2f} segundos\n- Tempo estimado: {tempo:.1f} BPM"

if audio_file is not None:
    st.audio(audio_file)
    with open("temp.wav", "wb") as f:
        f.write(audio_file.getbuffer())
    st.markdown("### 2. Evaluación de tu práctica")
    feedback = evaluar_audio("temp.wav")
    st.text(feedback)
    os.remove("temp.wav")

st.markdown("### 3. Lecciones de Ritmo y Escalas")
nivel = st.selectbox("Selecciona tu nivel actual:", ["Intermedio 1", "Intermedio 2", "Avanzado"])

if nivel == "Intermedio 1":
    st.markdown("""
    - **Ritmo sugerido para loops**: Compás 4/4, acentos en 2 y 4 (swing feel).
    - **Escalas para improvisar**: Escala menor armónica, escala pentatónica menor.
    """)
elif nivel == "Intermedio 2":
    st.markdown("""
    - **Ritmo**: Compás 6/8 con sincopas (usado en gypsy jazz).
    - **Escalas**: Dórico, Mixolidio, Arpegios de séptima.
    """)
else:
    st.markdown("""
    - **Ritmo**: Compases compuestos y desplazamiento rítmico (polirritmia ligera).
    - **Escalas**: Locrio, cromática, modos alterados.
    """)

st.info("Este agente está en desarrollo. Pronto podrás recibir feedback más detallado con análisis melódico.")