import streamlit as st
import tkinter as tk
import random
import threading

# list chiêu thức và biểu tượng
choices = ["Song kiếm trảm", "Long quyền chưởng", "Ngũ đao phi vũ"]
icons = {"Song kiếm trảm": "✌", "Long quyền chưởng": "✊", "Ngũ đao phi vũ": "🖐"}

# điểm số
score = {"win": 0, "lose": 0, "draw": 0}

# Hàm tính kết quả trận đấu
def get_result(player, computer):
    if player == computer:
        score["draw"] += 1
        return "⚖️ Chiêu này ngang tài ngang sức!", "draw"
    elif (player == "Song kiếm trảm" and computer == "Ngũ đao phi vũ") or \
         (player == "Long quyền chưởng" and computer == "Song kiếm trảm") or \
         (player == "Ngũ đao phi vũ" and computer == "Long quyền chưởng"):
        score["win"] += 1
        return "🏆 Không thể nào... Sao ngươi có thể học chiêu thức đó?", "win"
    else:
        score["lose"] += 1
        return "❌ Còn quá non kém. Ngươi đã bại dưới chiêu thức của ta!", "lose"

# Hàm hiển thị kết quả trận đấu, hiệu ứng đổi màu nền và âm thanh
def show_result_screen(player_choice, computer_choice, result, outcome):
    result_window = tk.Toplevel()
    result_window.title("⚔️ Tỉ thí võ công...")
    result_window.geometry("1000x1000")

    # Đổi màu nền cửa sổ kết quả theo outcome
    if outcome == "win":
        bg_color = "#d4edda"  # xanh nhạt
    elif outcome == "lose":
        bg_color = "#f8d7da"  # đỏ nhạt
    else:
        bg_color = "#fff3cd"  # vàng nhạt

    result_window.config(bg=bg_color)

    player_line = tk.Frame(result_window, bg=bg_color)
    player_line.pack(pady=10)
    tk.Label(player_line, text="Ngươi xuất chiêu:", font=("Arial", 14), bg=bg_color).pack(side="left", padx=(0, 10))
    tk.Label(player_line, text=icons[player_choice], font=("Arial", 50), bg=bg_color).pack(side="left")

    comp_line = tk.Frame(result_window, bg=bg_color)
    comp_line.pack(pady=10)
    tk.Label(comp_line, text="Bổn tọa chọn chiêu:", font=("Arial", 14), bg=bg_color).pack(side="left", padx=(0, 10))
    comp_icon = tk.Label(comp_line, text="❓", font=("Arial", 50), bg=bg_color)
    comp_icon.pack(side="left")

    result_label = tk.Label(result_window, text="", font=("Arial", 16, "bold"), bg=bg_color)
    result_label.pack(pady=20)

    button_container = tk.Frame(result_window, bg=bg_color)
    button_container.pack(pady=10)

    # Phát âm thanh theo kết quả trong thread riêng tránh gián đoạn GUI
    def play_sound_for_outcome():
        try:
            if outcome == "win":
                playsound('sounds/win_sound.mp3')
            elif outcome == "lose":
                playsound('sounds/lose_sound.mp3')
            else:
                playsound('sounds/draw_sound.mp3')
        except:
            pass

    def roll(count=0):
        if count < 30:
            comp_icon.config(text=icons[random.choice(choices)])
            result_window.after(50, lambda: roll(count + 1))
        else:
            comp_icon.config(text=icons[computer_choice])
            result_label.config(
                text=result,
                fg="green" if outcome == "win" else "red" if outcome == "lose" else "orange"
            )
            threading.Thread(target=play_sound_for_outcome).start()

            if outcome == "win":
                btn = tk.Button(button_container, text="💥 Đòn tiếp theo", bg="#198754", fg="white", command=result_window.destroy)
            elif outcome == "lose":
                btn = tk.Button(button_container, text="🌀 Phục thù!", bg="#dc3545", fg="white", command=result_window.destroy)
            else:
                btn = tk.Button(button_container, text="🧘 Tiếp chiêu đi", bg="#ffc107", fg="black", command=result_window.destroy)
            btn.pack(pady=10)

    result_window.after(200, roll)

# Xử lý khi người chơi chọn chiêu
def play(choice):
    computer_choice = random.choice(choices)
    result, outcome = get_result(choice, computer_choice)

    player_choice_label.config(text=f"👤 Ngươi ra chiêu: {choice}")
    result_label.config(text="🤖 Lên chiêu đi, hảo hán!", fg="#666")
    score_label.config(text=f"✅ Thắng: {score['win']} | ❌ Bại: {score['lose']} | ⚖️ Hòa: {score['draw']}")

    show_result_screen(choice, computer_choice, result, outcome)

# Đặt lại điểm số
def reset_score():
    score.update({"win": 0, "lose": 0, "draw": 0})
    score_label.config(text="✅ Thắng: 0 | ❌ Bại: 0 | ⚖️ Hòa: 0")
    result_label.config(text="🤖 Xuất chiêu đi, ta chưa ngán ai bao giờ hahahahaha", fg="#0077b6")
    player_choice_label.config(text="👤 Ngươi ra chiêu: ")

# Hiển thị tổng kết
def show_summary():
    summary_window = tk.Toplevel()
    summary_window.title("📜 Kết quả tỉ thí võ công")
    summary_window.geometry("1600x1000")
    summary_window.config(bg="#fff8dc")

    tk.Label(summary_window, text="📜 Kết quả tỉ thí:", font=("Arial", 16, "bold"), bg="#fff8dc").pack(pady=10)
    tk.Label(summary_window, text=f"✅ Thắng: {score['win']} | ❌ Bại: {score['lose']} | ⚖️ Hòa: {score['draw']}", font=("Arial", 14), bg="#fff8dc").pack(pady=10)

    if score["win"] > score["lose"]:
        comment = "🔥 Không thể nào...ta đã thua. Ngươi quả là cao thủ, bổn tọa bái phục!"
    elif score["win"] < score["lose"]:
        comment = "🌪 Võ công của ngươi chưa đủ wow, ta tha mạng cho nhà ngươi!"
    else:
        comment = "⚖️ Thế cục ngang tài ngang sức, tái đấu mới rõ anh hùng!"

    tk.Label(summary_window, text=comment, font=("Arial", 12, "italic"), bg="#fff8dc", fg="#8b4513").pack(pady=20)

# Giao diện chính
root = tk.Tk()
root.title("⚔️ Võ Lâm Tranh Đấu")
root.geometry("1600x900")
root.configure(bg="#f0f4f8")

tk.Label(root, text="🕹 Võ Lâm Tranh Đấu", font=("Arial", 20, "bold"), bg="#f0f4f8", fg="#333").pack(pady=20)

player_choice_label = tk.Label(root, text="👤 Ngươi ra chiêu: ", font=("Arial", 14), bg="#f0f4f8")
player_choice_label.pack(pady=10)

result_label = tk.Label(root, text="🤖 Xuất chiêu đi, ta chưa ngán ai bao giờ hahahahaha", font=("Arial", 14), bg="#f0f4f8", fg="#0077b6")
result_label.pack(pady=10)

score_label = tk.Label(root, text="✅ Thắng: 0 | ❌ Bại: 0 | ⚖️ Hòa: 0", font=("Arial", 13), bg="#f0f4f8", fg="#444")
score_label.pack(pady=10)

button_frame = tk.Frame(root, bg="#f0f4f8")
button_frame.pack(pady=20)

tk.Button(button_frame, text="✌ Song kiếm trảm", width=20, font=("Arial", 20), command=lambda: play("Song kiếm trảm")).grid(row=0, column=0, padx=10)
tk.Button(button_frame, text="✊ Long quyền chưởng", width=20, font=("Arial", 20), command=lambda: play("Long quyền chưởng")).grid(row=0, column=1, padx=10)
tk.Button(button_frame, text="🖐 Ngũ đao phi vũ", width=20, font=("Arial", 20), command=lambda: play("Ngũ đao phi vũ")).grid(row=0, column=2,)

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
