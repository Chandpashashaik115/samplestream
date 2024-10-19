import streamlit as st

st.title("Live Webcam Feed")

# HTML and JavaScript for accessing the webcam
st.markdown(
    """
    <video autoplay muted width="640" height="480" id="videoElement"></video>
    <script>
        var video = document.getElementById('videoElement');
        if (navigator.mediaDevices.getUserMedia) {
            navigator.mediaDevices.getUserMedia({ video: true })
            .then(function(stream) {
                video.srcObject = stream;
            })
            .catch(function(err) {
                console.error("Error accessing webcam: " + err);
            });
        }
    </script>
    """,
    unsafe_allow_html=True
)
