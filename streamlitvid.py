import streamlit as st
from streamlit_webrtc import VideoTransformerBase, webrtc_streamer

# Define a VideoTransformer class to process the video frames
class VideoTransformer(VideoTransformerBase):
    def transform(self, frame):
        img = frame.to_ndarray(format="bgr")
        return img  # Directly return the frame for now

def main():
    st.title("Webcam Stream using WebRTC")

    # WebRTC streamer to handle video streaming
    webrtc_streamer(key="example", video_transformer_factory=VideoTransformer)

if __name__ == "__main__":
    main()
