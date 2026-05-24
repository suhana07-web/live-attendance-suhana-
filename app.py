import streamlit as st
import cv2
import pandas as pd
from datetime import datetime
import os

st.set_page_config(page_title="Attendance System", layout="centered")
st.title("📸 Live Attendance System")

CSV_FILE = "attendance.csv"

if not os.path.exists(CSV_FILE):
    df = pd.DataFrame(columns=["Name", "Time"])
    df.to_csv(CSV_FILE, index=False)

run = st.checkbox("Start Camera")
FRAME_WINDOW = st.image([])
camera = cv2.VideoCapture(0)

name = st.text_input("Enter your Name:")

if st.button("Mark Attendance"):
    if name:
        time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        new_data = pd.DataFrame([[name, time_now]], columns=["Name", "Time"])
        new_data.to_csv(CSV_FILE, mode='a', header=False, index=False)
        st.success(f"{name}'s attendance marked at {time_now}!")
    else:
        st.error("Please enter your name first!")

while run:
    ret, frame = camera.read()
    if not ret:
        st.error("camera is not working")
        break
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    FRAME_WINDOW.image(frame)
else:
    camera.release()

st.subheader(f"{name}'s attendance")
df = pd.read_csv(CSV_FILE)
st.dataframe(df)