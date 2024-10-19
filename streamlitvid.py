import streamlit as st

if 'camera_enabled' not in st.session_state:
    st.session_state.camera_enabled = False

# Checkbox to enable camera
enable_camera = st.checkbox("Enable camera")

# Start and Stop buttons
if st.button("Start"):
    st.session_state.camera_enabled = True

if st.button("Stop"):
    st.session_state.camera_enabled = False

# Simulate live streaming
if enable_camera and st.session_state.camera_enabled:
    st.info("Streaming live camera feed...")
    st.camera_input("Live camera feed", key="camera")

# Display camera status
if st.session_state.camera_enabled:
    st.success("Camera is active and streaming.")
else:
    st.warning("Camera is not active. Click 'Start' to enable.")




