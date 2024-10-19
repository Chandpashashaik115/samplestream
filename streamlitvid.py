import cv2
import streamlit as st
import numpy as np

def main():
    st.title("Webcam Stream using OpenCV and Streamlit")

    # Initialize session state for start/stop control
    if 'run' not in st.session_state:
        st.session_state['run'] = False

    # "Start" button to toggle webcam streaming
    if st.button("Start"):
        st.session_state['run'] = True

    # "Stop" button to toggle off webcam streaming
    if st.button("Stop"):
        st.session_state['run'] = False

    # Placeholder for video stream
    frame_placeholder = st.empty()

    # If "Start" has been pressed, capture video from webcam
    if st.session_state['run']:
        cap = cv2.VideoCapture(0)

        # Check if webcam is opened correctly
        if not cap.isOpened():
            st.error("Cannot access the webcam!")
            return

        # Loop to read and display frames in the Streamlit app
        while st.session_state['run']:
            ret, frame = cap.read()
            if not ret:
                st.warning("Failed to grab frame")
                break

            # Convert the color from BGR (OpenCV format) to RGB (Streamlit format)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Update the image in the Streamlit app
            frame_placeholder.image(frame, channels="RGB")

            # Break the loop if the user clicks the "Stop" button
            if not st.session_state['run']:
                break

        # Release the webcam and close the stream
        cap.release()

if __name__ == "__main__":
    main()
