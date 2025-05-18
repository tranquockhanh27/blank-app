import streamlit as st
import random
import time

# --- Cài đặt nhạc nền (cần file nhạc nền) ---
# Lưu ý: Streamlit không hỗ trợ phát nhạc trực tiếp.
# Bạn có thể cung cấp link đến một nguồn nhạc trực tuyến hoặc
# hướng dẫn người dùng tự mở nhạc nền.
st.sidebar.title("Âm nhạc")
st.sidebar.write("Bạn có thể mở nhạc nền Free Fire yêu thích của mình trong trình duyệt khác.")

# --- Tiêu đề và giao diện chính ---
st.title("Kéo Búa Bao Phong Cách Trung Hoa")
st.write("Chào mừng đến với trò chơi!")

# --- Khởi tạo trạng thái trò chơi ---
if 'player_score' not in st.session_state:
    st.session_state['player_score'] = 0
if 'bot_score' not in st.session_state:
    st.session_state['bot_score'] = 0
if 'game_over' not in st.session_state:
    st.session_state['game_over'] = False
if 'round_result' not in st.session_state:
    st.session_state['round_result'] = ""
if 'player_choice' not in st.session_state:
    st.session_state['player_choice'] = None
if 'bot_choice' not in st.session_state:
    st.session_state['bot_choice'] = None

# --- Các lựa chọn của người chơi và bot ---
choices = ["Kéo", "Búa", "Bao"]
chinese_choices = {"Kéo": "剪刀", "Búa": "石头", "Bao": "布"}

def determine_winner(player, bot):
    if player == bot:
        return "Hòa!"
    elif (player == "Kéo" and bot == "Bao") or \
         (player == "Búa" and bot == "Kéo") or \
         (player == "Bao" and bot == "Búa"):
        return "Bạn thắng!"
    else:
        return "Bot thắng!"

def play_round(player_choice):
    st.session_state['player_choice'] = player_choice
    st.session_state['bot_choice'] = random.choice(choices)
    st.session_state['game_over'] = True # Chuyển sang giao diện hiệu ứng

# --- Giao diện lựa chọn chiêu thức ---
st.subheader("Chọn chiêu thức của bạn:")
col1, col2, col3 = st.columns(3)
if not st.session_state['game_over']:
    if col1.button("Kéo"):
        play_round("Kéo")
    if col2.button("Búa"):
        play_round("Búa")
    if col3.button("Bao"):
        play_round("Bao")

# --- Giao diện hiệu ứng roll chiêu thức ---
if st.session_state['game_over']:
    st.subheader("Hiệu ứng...")
    placeholder = st.empty()
    bot_roll_placeholder = st.empty()

    roll_symbols = ["⚔️", "🔨", "🛡️", "🐉", "🐅", "🐼"]
    roll_text_player = "Bạn đã chọn: "
    roll_text_bot = "Bot đang chọn: "

    for i in range(5):
        placeholder.write(f"{roll_text_player} {random.choice(roll_symbols)}")
        bot_roll_placeholder.write(f"{roll_text_bot} {random.choice(roll_symbols)}")
        time.sleep(0.3)

    placeholder.write(f"{roll_text_player} **{chinese_choices[st.session_state['player_choice']]} ({st.session_state['player_choice']})**")
    bot_roll_placeholder.write(f"{roll_text_bot} **{chinese_choices[st.session_state['bot_choice']]} ({st.session_state['bot_choice']})**")

    result = determine_winner(st.session_state['player_choice'], st.session_state['bot_choice'])
    st.session_state['round_result'] = result
    st.subheader(f"Kết quả: {result}")

    if result == "Bạn thắng!":
        st.session_state['player_score'] += 1
    elif result == "Bot thắng!":
        st.session_state['bot_score'] += 1

    # Nút để quay lại giao diện chọn chiêu thức
    if st.button("Chơi tiếp"):
        st.session_state['game_over'] = False

# --- Hiển thị điểm số ---
st.sidebar.subheader("Điểm số")
st.sidebar.write(f"Bạn: {st.session_state['player_score']}")
st.sidebar.write(f"Bot: {st.session_state['bot_score']}")

# --- Nút tổng kết kết quả ---
if st.sidebar.button("Tổng kết kết quả"):
    st.sidebar.subheader("Kết quả cuối cùng")
    if st.session_state['player_score'] > st.session_state['bot_score']:
        st.sidebar.write("Chúc mừng! Bạn đã chiến thắng chung cuộc!")
    elif st.session_state['player_score'] < st.session_state['bot_score']:
        st.sidebar.write("Bot đã chiến thắng chung cuộc. Chúc bạn may mắn lần sau!")
    else:
        st.sidebar.write("Trận đấu hòa!")

# --- Nút reset điểm ---
if st.sidebar.button("Reset điểm"):
    st.session_state['player_score'] = 0
    st.session_state['bot_score'] = 0
    st.session_state['game_over'] = False
    st.session_state['round_result'] = ""
    st.session_state['player_choice'] = None
    st.session_state['bot_choice'] = None
    st.rerun()

# --- Nút kết thúc ---
if st.sidebar.button("Kết thúc trò chơi"):
    st.sidebar.write("Cảm ơn bạn đã chơi!")
