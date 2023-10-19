import streamlit as st
import whisper
st.title("Whisper app")

audio_file = st.file_uploader("Upload Audio", type=['wav', 'mp3', 'mp4'])

model = whisper.load_model("base")
st.text("Whisper Model Loaded")

if st.sidebar.button("Transcribe Audio"):
  if audio_file is not None:
    st.sidebar.success("Transcribing Audio")
    transcription = model.transcribe(audio_file.name)
    st.sidebar.success("Transcription Complete")
    st.markdown(transcription["text"])
  else:
    st.sidebar.error("Please upload an audio file")

st.sidebar.header("Play Original Audio File")
st.sidebar.audio(audio_file)

import subprocess

cmd = "your_subprocess_command_here"
print("Executing command:", cmd)
try:
    output = subprocess.check_output(cmd, shell=True)
    print("Output:", output)
except subprocess.CalledProcessError as e:
    print("Error:", e)