# file: app.py
import streamlit as st
import requests
import hashlib
import os
from dotenv import load_dotenv
import cv2
import mediapipe as mp

load_dotenv()

st.title("YouTube & TikTok CMS for @mylocyrus")

# -- Get bios from GitHub and TikTok (publicly available only) --
def get_github_bio(username):
    url = f"https://api.github.com/users/{username}"
    r = requests.get(url)
    if r.status_code == 200:
        return r.json().get("bio", "No bio found.")
    return "GitHub bio not available."

def get_tiktok_bio(username):
    # TikTok API is private, so demo string instead
    return "Tiktok bio not available via API. (Demo placeholder)"

github_bio = get_github_bio("mylocyrus")
tiktok_bio = get_tiktok_bio("mylocyrus")

st.subheader("GitHub Bio")
st.write(github_bio)
st.subheader("TikTok Bio")
st.write(tiktok_bio)

# -- Embed TikTok & YouTube --
st.subheader("TikTok Embed")
st.components.v1.iframe("https://www.tiktok.com/@mylocyrus", height=600)
st.subheader("YouTube Embed")
st.video("https://www.youtube.com/@mylocyrus")  # replace with actual video/channel if needed

# -- Memory mechanism (store user session in a file) --
def save_memory(data):
    with open("memory.nv", "w") as f:
        f.write(data)

def load_memory():
    if os.path.exists("memory.nv"):
        with open("memory.nv", "r") as f:
            return f.read()
    return ""

memory_val = load_memory()
st.text_area("Session Memory", value=memory_val, key="memory")
if st.button("Save Memory"):
    save_memory(st.session_state.memory)
    st.success("Memory saved!")

# -- SHA-256 Hashing Example --
to_hash = st.text_input("Input for SHA-256 hashing", value="example")
if st.button("Hash Input"):
    hashed = hashlib.sha256(to_hash.encode()).hexdigest()
    st.code(hashed)

# -- Hand Recognition (using webcam and mediapipe) --
st.subheader("Hand Recognition Demo (Webcam)")

run_handrec = st.checkbox("Enable Hand Recognition (Webcam)")

if run_handrec:
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands()
    mp_draw = mp.solutions.drawing_utils

    cap = cv2.VideoCapture(0)
    stframe = st.empty()
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        # Flip for selfie-view
        frame = cv2.flip(frame, 1)
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb)
        if results.multi_hand_landmarks:
            for handlms in results.multi_hand_landmarks:
                mp_draw.draw_landmarks(frame, handlms, mp_hands.HAND_CONNECTIONS)
        stframe.image(frame, channels="BGR")
        if st.button("Stop Hand Recognition"):
            break
    cap.release()

st.write("Powered by Streamlit, Mediapipe, OpenCV, and SHA-256 hashing.")

# -- .env Example --
st.write("Loaded .env variables (for demo):")
for key in os.environ:
    if key.startswith("MYLOCYRUS_"):
        st.write(f"{key}: {os.environ[key]}")
