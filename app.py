import streamlit as st
import pandas as pd
from streamlit_webrtc import webrtc_streamer
from datetime import datetime
import os

st.set_page_config(page_title="Live Attendance", page_icon="📸")

st.title("Live Attendance System 📸")
st.markdown("### Made by Suhana Parveen 💚")

# Camera Stream
webrtc_streamer(key="attendance")

st.success("Camera is Live! Attendance System Ready ✅")

# Attendance Feature
st.markdown("---")
st.subheader("Mark Your Attendance 👇")

name = st.text_input("Enter Your Name:")
roll = st.text_input("Enter Roll Number:")

if st.button("Mark Present ✅"):
    if name and roll:
        # Get current time
        now = datetime.now()
        date = now.strftime("%d-%m-%Y")
        time = now.strftime("%H:%M:%S")
        
        # Create data entry
        new_data = {"Name": name, "Roll_No": roll, "Date": date, "Time": time}
        
        # Save to CSV file
        if os.path.exists("attendance.csv"):
            df = pd.read_csv("attendance.csv")
            df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)
        else:
            df = pd.DataFrame([new_data])
        
        df.to_csv("attendance.csv", index=False)
        st.balloons()
        st.success(f"Done {name}! Your attendance is marked at {time} 🎉")
    else:
        st.error("Please enter both Name and Roll Number 😅")

# Display Table
st.markdown("---")
st.subheader("Today's Attendance List 📋")

if os.path.exists("attendance.csv"):
    df = pd.read_csv("attendance.csv")
    st.dataframe(df)
    
    # Download button
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button("Download Excel 📥", csv, "attendance.csv", "text/csv")
else:
    st.info("No attendance marked yet")

st.info("Built with 6 hours 45 minutes of hard work 🎉")
