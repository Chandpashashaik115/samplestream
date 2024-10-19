import streamlit as st

# Initialize session state
if 'camera_enabled' not in st.session_state:
    st.session_state.camera_enabled = False

# Checkbox to enable camera
enable_camera = st.checkbox("Enable camera")

# Start and Stop buttons
if st.button("Start"):
    st.session_state.camera_enabled = True

if st.button("Stop"):
    st.session_state.camera_enabled = False

# Use camera input only if enabled
if enable_camera and st.session_state.camera_enabled:
    picture = st.camera_input("Take a picture")

    if picture:
        st.image(picture)

# Display camera status
if st.session_state.camera_enabled:
    st.success("Camera is active. Click 'Take a picture' to capture an image.")
else:
    st.warning("Camera is not active. Click 'Start' to enable.")
