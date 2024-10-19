import streamlit as st
import cv2

def main():
    st.title("Live Webcam Stream with OpenCV")

    # Create a VideoCapture object
    video_capture = cv2.VideoCapture(0)

    # Check if the webcam is opened correctly
    if not video_capture.isOpened():
        st.error("Error: Could not access the webcam.")
        return

    # Create a placeholder for the video feed
    stframe = st.empty()

    while True:
        ret, frame = video_capture.read()
        if not ret:
            st.error("Error: Could not read the frame.")
            break

        # Convert the frame from BGR to RGB format
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Display the frame in the Streamlit app
        stframe.image(frame)

    # Release the webcam when done
    video_capture.release()

if __name__ == "__main__":
    main()
