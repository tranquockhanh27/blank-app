import streamlit as st
import random
import time
from streamlit_extras.audio import audio_player

# Cấu hình trang
st.set_page_config(page_title="Võ Lâm Tranh Đấu", page_icon="⚔️", layout="centered")

# Nhạc nền (link file hoặc mp3 URL)
audio_url = "https://cdn.pixabay.com/download/audio/2022/03/15/audio_f58dfc7b37.mp3?filename=epic-cinematic-action-trailer-111062.mp3"
audio_player(audio_url, autoplay=True, loop=True)

# Ảnh động hiệu ứng chiêu thức
moves = {
    "✌️ Song kiếm trảm": "scissors",
    "✊ Long quyền chưởng": "rock",
    "🖐 Ngũ đao phi vũ": "paper"
}

# Session state
if "player_score" not in st.session_state:
    st.session_state.update({
        "player_score": 0,
        "bot_score": 0,
        "draw": 0
    })

# Giao diện chính
st.markdown("## 🧙‍♂️ Võ Lâm Tranh Đấu")
st.markdown("### 🤜 Lên chiêu đi, hảo hán!")

# Chọn chiêu
col1, col2, col3 = st.columns(3)
player_move = None
with col1:
    if st.button("✌️ Song kiếm trảm"):
        player_move = "scissors"
with col2:
    if st.button("✊ Long quyền chưởng"):
        player_move = "rock"
with col3:
    if st.button("🖐 Ngũ đao phi vũ"):
        player_move = "paper"

# Xử lý logic sau khi người chơi chọn
if player_move:
    with st.spinner("⏳ Đối thủ đang xuất chiêu..."):
        time.sleep(1.5)
        bot_move = random.choice(["rock", "paper", "scissors"])
    
    # Kết quả
    result = ""
    if player_move == bot_move:
        result = "🏵️ Hòa!"
        st.session_state.draw += 1
    elif (player_move == "rock" and bot_move == "scissors") or \
         (player_move == "scissors" and bot_move == "paper") or \
         (player_move == "paper" and bot_move == "rock"):
        result = "🏆 Bạn thắng!"
        st.session_state.player_score += 1
    else:
        result = "💥 Bạn thua!"
        st.session_state.bot_score += 1

    # Hiển thị kết quả
    move_display = {v: k for k, v in moves.items()}
    st.success(f"""
    🤖 Đối thủ ra chiêu: {move_display[bot_move]}  
    🧘‍♂️ Bạn chọn chiêu: {move_display[player_move]}  
    👉 Kết quả: {result}
    """)

# Tổng kết điểm
st.markdown("### 📊 Kết quả:")
st.write(f"✅ Thắng: {st.session_state.player_score} | ❌ Thua: {st.session_state.bot_score} | 🤝 Hòa: {st.session_state.draw}")

# Nút điều khiển
colA, colB, colC = st.columns(3)
with colA:
    if st.button("🔁 Reset điểm"):
        st.session_state.player_score = 0
        st.session_state.bot_score = 0
        st.session_state.draw = 0
with colB:
    if st.button("📜 Tổng kết"):
        st.info(f"🎯 Tổng kết: Thắng {st.session_state.player_score} - Thua {st.session_state.bot_score} - Hòa {st.session_state.draw}")
with colC:
    if st.button("❌ Kết thúc"):
        st.stop()
