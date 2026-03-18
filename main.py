import tkinter as tk
from game_logic import check_winner, ai_move

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe - Unbeatable AI")
        self.window.config(bg="#1E1E2F")

        self.board = [" "] * 9
        self.buttons = []

        self.create_board()
        self.create_status()
        self.create_restart()

        self.window.mainloop()

    def create_board(self):
        frame = tk.Frame(self.window, bg="#1E1E2F")
        frame.pack(pady=10)

        for i in range(9):
            btn = tk.Button(frame, text=" ", font=("Arial", 24), width=5, height=2,
                            bg="#2E2E3F", fg="white",
                            command=lambda i=i: self.player_move(i))
            btn.grid(row=i//3, column=i%3, padx=5, pady=5)
            self.buttons.append(btn)

    def create_status(self):
        self.status = tk.Label(self.window, text="Your Turn (X)",
                               font=("Arial", 16),
                               bg="#1E1E2F", fg="white")
        self.status.pack(pady=10)

    def create_restart(self):
        btn = tk.Button(self.window, text="Restart",
                        font=("Arial", 14),
                        bg="#ED5C5C", fg="white",
                        command=self.reset_board)
        btn.pack(pady=10)

    def player_move(self, i):
        if self.board[i] == " ":
            self.board[i] = "X"
            self.buttons[i].config(text="X", bg="#5C9DED")

            if check_winner(self.board, "X"):
                self.status.config(text="You Win 🎉")
                self.disable()
                return

            if " " not in self.board:
                self.status.config(text="Draw 🤝")
                return

            self.status.config(text="AI Thinking...")
            self.window.after(500, self.ai_turn)

    def ai_turn(self):
        move = ai_move(self.board)

        if move is not None:
            self.board[move] = "O"
            self.buttons[move].config(text="O", bg="#ED5C5C")

            if check_winner(self.board, "O"):
                self.status.config(text="AI Wins 😈")
                self.disable()
                return

        if " " not in self.board:
            self.status.config(text="Draw 🤝")
            return

        self.status.config(text="Your Turn (X)")

    def disable(self):
        for b in self.buttons:
            b.config(state="disabled")

    def reset_board(self):
        self.board = [" "] * 9
        for b in self.buttons:
            b.config(text=" ", bg="#2E2E3F", state="normal")
        self.status.config(text="Your Turn (X)")


if __name__ == "__main__":
    TicTacToe()