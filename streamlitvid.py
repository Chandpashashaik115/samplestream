import cv2
import numpy as np
import streamlit as st
from streamlit_webrtc import VideoTransformerBase, webrtc_streamer

# Define a VideoTransformer class to process the video frames
class VideoTransformer(VideoTransformerBase):
    def transform(self, frame):
        # Convert the frame from BGR (OpenCV) to RGB
        img = frame.to_ndarray(format="bgr")
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        return img

def main():
    st.title("Webcam Stream using WebRTC")

    # WebRTC streamer to handle video streaming
    webrtc_streamer(key="example", video_transformer_factory=VideoTransformer)

if __name__ == "__main__":
    main()
