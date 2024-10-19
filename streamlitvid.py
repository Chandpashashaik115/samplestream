import streamlit as st

st.title("Live Webcam Feed with Start/Stop Controls")

# HTML and JavaScript for accessing the webcam
st.markdown(
    """
    <video autoplay muted width="640" height="480" id="videoElement"></video>
    <br>
    <button id="startButton">Start</button>
    <button id="stopButton" disabled>Stop</button>
    
    <script>
        let stream;

        const video = document.getElementById('videoElement');
        const startButton = document.getElementById('startButton');
        const stopButton = document.getElementById('stopButton');

        startButton.addEventListener('click', async function() {
            // Request access to the webcam
            stream = await navigator.mediaDevices.getUserMedia({ video: true });
            video.srcObject = stream;
            startButton.disabled = true;
            stopButton.disabled = false;
        });

        stopButton.addEventListener('click', function() {
            // Stop the video stream
            if (stream) {
                const tracks = stream.getTracks();
                tracks.forEach(track => track.stop());
                video.srcObject = null;
                startButton.disabled = false;
                stopButton.disabled = true;
            }
        });
    </script>
    """,
    unsafe_allow_html=True
)
