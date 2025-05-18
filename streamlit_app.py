import streamlit as st
import random
import time
from PIL import Image

# --- Cài đặt giao diện ---
st.set_page_config(page_title="Game Kéo Búa Bao Trung Hoa", layout="wide")
st.markdown("""
    <style>
    .title {
        font-size:50px !important;
        color: red;
        text-align: center;
        font-weight: bold;
    }
    .subtitle {
        font-size:24px !important;
        text-align: center;
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">Game Kéo Búa Bao - Phong Cách Trung Hoa</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Hãy chọn chiêu thức của bạn!</div>', unsafe_allow_html=True)

# --- Khởi tạo trạng thái ---
if 'player_score' not in st.session_state:
    st.session_state.player_score = 0
if 'bot_score' not in st.session_state:
    st.session_state.bot_score = 0
if 'result' not in st.session_state:
    st.session_state.result = ""

# --- Chiêu thức ---
choices = ["Kéo", "Búa", "Bao"]
images = {
    "Kéo": "https://i.imgur.com/4f4JZTZ.png",
    "Búa": "https://i.imgur.com/1RuKZaN.png",
    "Bao": "https://i.imgur.com/eG7q5fT.png"
}

# --- Âm nhạc nền (Free Fire style) ---
st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3", format="audio/mp3")

# --- Hàm xử lý kết quả ---
def play(player_choice):
    st.subheader("Máy đang chọn chiêu thức...")
    for i in range(10):
        roll = random.choice(choices)
        st.image(images[roll], width=150)
        time.sleep(0.15)

    bot_choice = random.choice(choices)
    st.image(images[bot_choice], width=150, caption=f"Máy chọn: {bot_choice}")

    # --- Tính kết quả ---
    if player_choice == bot_choice:
        result = "Hòa!"
    elif (player_choice == "Kéo" and bot_choice == "Bao") or \
         (player_choice == "Búa" and bot_choice == "Kéo") or \
         (player_choice == "Bao" and bot_choice == "Búa"):
        result = "Bạn thắng!"
        st.session_state.player_score += 1
    else:
        result = "Bạn thua!"
        st.session_state.bot_score += 1

    st.session_state.result = result

# --- Nút chọn chiêu thức ---
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("🖖 Kéo"):
        play("Kéo")
with col2:
    if st.button("✊ Búa"):
        play("Búa")
with col3:
    if st.button("🫲 Bao"):
        play("Bao")

# --- Hiển thị kết quả ---
st.markdown("## Kết Quả")
st.success(st.session_state.result)
st.write(f"### Điểm của bạn: {st.session_state.player_score}")
st.write(f"### Điểm của máy: {st.session_state.bot_score}")

# --- Nút reset và kết thúc ---
col4, col5 = st.columns(2)
with col4:
    if st.button("🔁 Reset điểm"):
        st.session_state.player_score = 0
        st.session_state.bot_score = 0
        st.session_state.result = ""
        st.experimental_rerun()

with col5:
    if st.button("❌ Kết thúc"):
        st.balloons()
        st.markdown("### Cảm ơn bạn đã chơi game!")
