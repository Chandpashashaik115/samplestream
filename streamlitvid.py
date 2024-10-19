import streamlit as st

st.title("Webcam Stream Example")

# HTML and JavaScript code to access the webcam
st.markdown(
    """
    <video autoplay playsinline id="videoElement"></video>
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
            window.parent.document.getElementById('image-data').value = dataURL; // Set the data URL in a hidden input
            window.parent.document.getElementById('upload-button').click(); // Trigger upload
        });
    </script>
    """,
    unsafe_allow_html=True,
)

# Hidden input field to store image data
st.markdown('<input type="hidden" id="image-data">', unsafe_allow_html=True)

# Button to upload the captured frame
if st.button("Upload Frame"):
    # Get the base64 image data from the input field
    image_data = st.session_state.get('image_data', None)
    if image_data:
        # Display the captured image
        st.image(image_data, caption="Captured Frame", use_column_width=True)

# Use Session State to store captured image data
if 'image_data' not in st.session_state:
    st.session_state.image_data = None

# Capture image data from JavaScript
st.write(
    """
    <script>
        document.getElementById("image-data").addEventListener("change", function() {
            window.parent.streamlit.setComponentValue("image_data", this.value);
        });
    </script>
    """,
    unsafe_allow_html=True,
)
