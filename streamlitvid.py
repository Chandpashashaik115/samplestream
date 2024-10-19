import streamlit as st

def main():
    st.title("Webcam Stream using HTML5 and Streamlit")

    # HTML and JavaScript code to access the webcam
    st.markdown(
        """
        <video autoplay playsinline id="videoElement" style="width: 100%;"></video>
        <button id="captureButton">Capture</button>
        <canvas id="canvas" style="display: none;"></canvas>
        <script>
            var video = document.querySelector("#videoElement");
            var canvas = document.querySelector("#canvas");
            var context = canvas.getContext('2d');
            var captureButton = document.querySelector("#captureButton");

            // Access the webcam
            if (navigator.mediaDevices.getUserMedia) {
                navigator.mediaDevices.getUserMedia({ video: true })
                    .then(function (stream) {
                        video.srcObject = stream;
                    })
                    .catch(function (error) {
                        console.log("Something went wrong!", error);
                    });
            }

            // Capture the video frame when the button is clicked
            captureButton.addEventListener('click', function() {
                canvas.width = video.videoWidth;
                canvas.height = video.videoHeight;
                context.drawImage(video, 0, 0);
                var dataURL = canvas.toDataURL('image/png');

                // Send the captured frame to Streamlit
                fetch('/capture', {
                    method: 'POST',
                    body: JSON.stringify({ image: dataURL }),
                    headers: {
                        'Content-Type': 'application/json'
                    }
                });
            });
        </script>
        """,
        unsafe_allow_html=True,
    )

    # Handle the captured frame from JavaScript
    if st.session_state.get('image_data') is not None:
        st.image(st.session_state.image_data, caption="Captured Frame", use_column_width=True)

if __name__ == "__main__":
    main()
