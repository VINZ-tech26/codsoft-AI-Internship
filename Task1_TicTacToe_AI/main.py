import customtkinter as ctk
from game_logic import board, check_winner, is_draw
from ai import ai_move

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Tic Tac Toe AI")
app.geometry("400x500")

current_player = "X"
buttons = []

title = ctk.CTkLabel(app, text="Tic Tac Toe AI", font=("Arial", 28, "bold"))
title.pack(pady=20)

frame = ctk.CTkFrame(app)
frame.pack()

status = ctk.CTkLabel(app, text="Your Turn (X)", font=("Arial", 16))
status.pack(pady=10)


def button_click(index):
    global current_player

    if board[index] == " ":
        board[index] = "X"
        buttons[index].configure(text="X")

        if check_winner("X"):
            status.configure(text="You Win 🎉")
            disable_buttons()
            return

        if is_draw():
            status.configure(text="Draw Game 🤝")
            return

        ai_turn()


def ai_turn():
    move = ai_move(board)
    board[move] = "O"
    buttons[move].configure(text="O")

    if check_winner("O"):
        status.configure(text="AI Wins 🤖")
        disable_buttons()
        return

    if is_draw():
        status.configure(text="Draw Game 🤝")
        return


def disable_buttons():
    for b in buttons:
        b.configure(state="disabled")


def reset_game():
    for i in range(9):
        board[i] = " "
        buttons[i].configure(text="", state="normal")

    status.configure(text="Your Turn (X)")


grid_frame = ctk.CTkFrame(frame)
grid_frame.pack()

for i in range(9):
    btn = ctk.CTkButton(
        grid_frame,
        text="",
        width=80,
        height=80,
        font=("Arial", 30, "bold"),
        command=lambda i=i: button_click(i)
    )
    btn.grid(row=i // 3, column=i % 3, padx=5, pady=5)
    buttons.append(btn)


reset_btn = ctk.CTkButton(app, text="Restart Game", command=reset_game)
reset_btn.pack(pady=20)

app.mainloop()
