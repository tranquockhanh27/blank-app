import streamlit as st
import random
import time
from streamlit_extras.audio import audio_player

# --- Cấu hình ---
st.set_page_config(page_title="Võ Lâm Tranh Đấu", page_icon="⚔️", layout="centered")

# --- Nhạc nền ---
audio_player("assets/bgm.mp3", autoplay=True, loop=True)

# --- Các chiêu thức ---
moves = {
    "✌️ Song kiếm trảm": {
        "code": "scissors",
        "img": "assets/song_kiem.gif"
    },
    "✊ Long quyền chưởng": {
        "code": "rock",
        "img": "assets/long_quyen.gif"
    },
    "🖐 Ngũ đao phi vũ": {
        "code": "paper",
        "img": "assets/ngu_dao.gif"
    }
}

# --- Session State ---
if "score" not in st.session_state:
    st.session_state.score = {"win": 0, "lose": 0, "draw": 0}

# --- Tiêu đề ---
st.markdown("<h2 style='text-align: center;'>🧙‍♂️ Võ Lâm Tranh Đấu</h2>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>Lên chiêu đi, hảo hán!</h4>", unsafe_allow_html=True)

# --- Nút chọn chiêu ---
cols = st.columns(3)
player_move = None
for idx, (label, move) in enumerate(moves.items()):
    with cols[idx]:
        if st.button(label):
            player_move = move["code"]
            st.image(move["img"], caption=label, use_column_width=True)

# --- Xử lý kết quả ---
if player_move:
    st.markdown("### 🤖 Đối thủ đang ra chiêu...")
    time.sleep(1.2)
    bot_choice = random.choice(list(moves.values()))
    bot_move = bot_choice["code"]
    
    st.image(bot_choice["img"], caption="Chiêu của đối thủ", use_column_width=True)
    
    # Kết quả trận đấu
    result = ""
    if player_move == bot_move:
        result = "🤝 Hòa rồi!"
        st.session_state.score["draw"] += 1
    elif (player_move == "rock" and bot_move == "scissors") or \
         (player_move == "scissors" and bot_move == "paper") or \
         (player_move == "paper" and bot_move == "rock"):
        result = "🏆 Bạn đã thắng!"
        st.session_state.score["win"] += 1
    else:
        result = "💥 Bạn thua rồi!"
        st.session_state.score["lose"] += 1

    st.success(f"🎯 {result}")

# --- Bảng điểm ---
st.markdown("### 📊 Kết quả hiện tại:")
st.info(f"""✅ Thắng: {st.session_state.score["win"]}  
❌ Thua: {st.session_state.score["lose"]}  
🤝 Hòa: {st.session_state.score["draw"]}""")

# --- Các nút điều khiển ---
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("🔁 Reset điểm"):
        st.session_state.score = {"win": 0, "lose": 0, "draw": 0}
        st.experimental_rerun()

with col2:
    if st.button("📜 Tổng kết"):
        st.toast(f"🎯 Tổng kết sau trận: {st.session_state.score}")

with col3:
    if st.button("❌ Kết thúc"):
        st.stop()
