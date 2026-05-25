import streamlit as st
from streamlit_webrtc import webrtc_streamer
import numpy as np

st.set_page_config(page_title="Live Attendance by Suhana")

st.title("Live Attendance System 📸")
st.write("Made by Suhana Parveen 💚")

def video_frame_callback(frame):
    img = frame.to_ndarray(format="bgr24")
    return frame

webrtc_streamer(
    key="attendance", 
    video_frame_callback=video_frame_callback,
    media_stream_constraints={"video": True, "audio": False},
    async_processing=True,
)

st.success("Camera is Live! Attendance System Ready ✅")
st.balloons()
st.info("6 ghante 45 minute ki mehnat safal hui 🎉")
