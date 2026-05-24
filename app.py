import streamlit as st
import cv2
import mediapipe as mp
import numpy as np
import pandas as pd
from datetime import datetime
import os

st.set_page_config(page_title="Live Attendance", layout="wide")
st.title("Live Attendance System - Suhana")

mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils

if not os.path.exists('attendance.csv'):
    df = pd.DataFrame(columns=['Name', 'Time'])
    df.to_csv('attendance.csv', index=False)

name = st.text_input("Enter Your Name")
run = st.checkbox('Start Camera')

FRAME_WINDOW = st.image([])
camera = cv2.VideoCapture(0)

with mp_face_detection.FaceDetection(model_selection=0, min_detection_confidence=0.5) as face_detection:
    while run:
        ret, frame = camera.read()
        if not ret:
            st.error("Camera not found")
            break
            
        frame = cv2.flip(frame, 1)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = face_detection.process(rgb_frame)
        
        if results.detections:
            for detection in results.detections:
                mp_drawing.draw_detection(frame, detection)
                
                if name:
                    time_now = datetime.now().strftime("%H:%M:%S")
                    df = pd.read_csv('attendance.csv')
                    if name not in df['Name'].values:
                        new_data = {'Name': name, 'Time': time_now}
                        df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)
                        df.to_csv('attendance.csv', index=False)
                        st.success(f"Attendance marked for {name} at {time_now}")
        
        FRAME_WINDOW.image(frame, channels="BGR")
    
camera.release()

st.subheader("Attendance Sheet")
if os.path.exists('attendance.csv'):
    df = pd.read_csv('attendance.csv')
    st.dataframe(df)
