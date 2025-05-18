import streamlit as st
import random
import time

# list chiêu thức và biểu tượng
choices = ["Song kiếm trảm", "Long quyền chưởng", "Ngũ đao phi vũ"]
icons = {"Song kiếm trảm": "✌", "Long quyền chưởng": "✊", "Ngũ đao phi vũ": "🖐"}

# điểm số (sử dụng st.session_state để duy trì trạng thái)
if 'score' not in st.session_state:
    st.session_state['score'] = {"win": 0, "lose": 0, "draw": 0}
if 'player_choice' not in st.session_state:
    st.session_state['player_choice'] = ""
if 'computer_choice' not in st.session_state:
    st.session_state['computer_choice'] = "❓" # Bắt đầu với dấu hỏi
if 'result_text' not in st.session_state:
    st.session_state['result_text'] = "🤖 Xuất chiêu đi, ta chưa ngán ai bao giờ hahahahaha"
if 'outcome' not in st.session_state:
    st.session_state['outcome'] = ""
if 'rolling' not in st.session_state:
    st.session_state['rolling'] = False

# Hàm tính kết quả trận đấu (GIỮ NGUYÊN)
def get_result(player, computer):
    if player == computer:
        st.session_state['score']['draw'] += 1
        return "⚖️ Chiêu này ngang tài ngang sức!", "draw"
    elif (player == "Song kiếm trảm" and computer == "Ngũ đao phi vũ") or \
         (player == "Long quyền chưởng" and computer == "Song kiếm trảm") or \
         (player == "Ngũ đao phi vũ" and computer == "Long quyền chưởng"):
        st.session_state['score']['win'] += 1
        return "🏆 Không thể nào... Sao ngươi có thể học chiêu thức đó?", "win"
    else:
        st.session_state['score']['lose'] += 1
        return "❌ Còn quá non kém. Ngươi đã bại dưới chiêu thức của ta!", "lose"

# Hàm hiển thị kết quả trận đấu (THAY ĐỔI CHO STREAMLIT)
def show_result_screen_streamlit(player_choice, computer_choice, result, outcome):
    st.subheader("⚔️ Kết quả tỉ thí...")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"**Ngươi xuất chiêu:** {icons[player_choice]} ({player_choice})")
    with col2:
        st.markdown(f"**Bổn tọa chọn chiêu:** {icons[computer_choice]} ({computer_choice})")
    st.markdown(f"### {result}")
    if outcome == "win":
        st.success("Ngươi đã thắng!")
    elif outcome == "lose":
        st.error("Ngươi đã thua!")
    else:
        st.info("Hòa rồi!")

# Hàm thực hiện hiệu ứng roll
def roll():
    for _ in range(30):  # Số lần "roll"
        st.session_state['computer_choice'] = random.choice(choices)
        time.sleep(0.05)  # Tốc độ "roll"
        st.rerun() # Chạy lại script để cập nhật giao diện
    # Sau khi "roll" xong, tính toán kết quả thật
    computer_choice_final = random.choice(choices)
    result, outcome = get_result(st.session_state['player_choice'], computer_choice_final)
    st.session_state['computer_choice'] = computer_choice_final
    st.session_state['result_text'] = result
    st.session_state['outcome'] = outcome
    st.session_state['rolling'] = False
    st.rerun() # Chạy lại lần cuối để hiển thị kết quả cuối cùng

# Xử lý khi người chơi chọn chiêu (THAY ĐỔI CHO STREAMLIT)
def play_streamlit(choice):
    st.session_state['player_choice'] = choice
    st.session_state['computer_choice'] = "❓" # Reset hiển thị của máy
    st.session_state['result_text'] = "🤖 Bổn tọa đang chọn chiêu..."
    st.session_state['outcome'] = ""
    st.session_state['rolling'] = True
    roll()

# Hàm đặt lại điểm số (GIỮ NGUYÊN)
def reset_score():
    st.session_state['score'] = {"win": 0, "lose": 0, "draw": 0}
    st.session_state['player_choice'] = ""
    st.session_state['computer_choice'] = "❓"
    st.session_state['result_text'] = "🤖 Xuất chiêu đi, ta chưa ngán ai bao giờ hahahahaha"
    st.session_state['outcome'] = ""
    st.session_state['rolling'] = False

# Hàm hiển thị tổng kết (THAY ĐỔI CHO STREAMLIT)
def show_summary_streamlit():
    st.subheader("📜 Kết quả tỉ thí võ công")
    st.markdown(f"**✅ Thắng:** {st.session_state['score']['win']} | **❌ Bại:** {st.session_state['score']['lose']} | **⚖️ Hòa:** {st.session_state['score']['draw']}")

    if st.session_state['score']['win'] > st.session_state['score']['lose']:
        comment = "🔥 Không thể nào...ta đã thua. Ngươi quả là cao thủ, bổn tọa bái phục!"
    elif st.session_state['score']['win'] < st.session_state['score']['lose']:
        comment = "🌪 Võ công của ngươi chưa đủ wow, ta tha mạng cho nhà ngươi!"
    else:
        comment = "⚖️ Thế cục ngang tài ngang sức, tái đấu mới rõ anh hùng!"
    st.info(comment)

# Giao diện Streamlit
st.title("⚔️ Võ Lâm Tranh Đấu")

st.markdown("---")

st.markdown(f"**Điểm số:** ✅ {st.session_state['score']['win']} | ❌ {st.session_state['score']['lose']} | ⚖️ {st.session_state['score']['draw']}")

st.markdown("---")

col_player, col_vs, col_comp = st.columns(3)

with col_player:
    if st.session_state['player_choice']:
        st.markdown(f"👤 Ngươi ra chiêu: **{st.session_state['player_choice']}** {icons[st.session_state['player_choice']]}")
    else:
        st.markdown("👤 Ngươi:")

with col_vs:
    st.markdown("## VS")

with col_comp:
    st.markdown(f"🤖 Bổn tọa chọn: **{st.session_state['computer_choice']}** {icons.get(st.session_state['computer_choice'], '')}")

st.markdown("---")

col_buttons = st.columns(3)
if not st.session_state['rolling']:
    if col_buttons[0].button(f"✌ {choices[0]}"):
        play_streamlit(choices[0])
    if col_buttons[1].button(f"✊ {choices[1]}"):
        play_streamlit(choices[1])
    if col_buttons[2].button(f"🖐 {choices[2]}"):
        play_streamlit(choices[2])
else:
    st.info("🤖 Bổn tọa đang thi triển chiêu thức...")

st.markdown("---")

if 'result_text' in st.session_state and st.session_state['result_text']:
    st.info(st.session_state['result_text'])

st.markdown("---")

col_reset_summary = st.columns(2)
if col_reset_summary[0].button("🔄 Đặt lại điểm"):
    reset_score()
if col_reset_summary[1].button("📊 Xem tổng kết"):
    show_summary_streamlit()

if 'outcome' in st.session_state:
    if st.session_state['outcome'] == "win":
        st.balloons()
    elif st.session_state['outcome'] == "lose":
        st.warning("Cố gắng lên ở trận sau nhé!")
    elif st.session_state['outcome'] == "draw":
        st.info("Một trận hòa cân sức!")
