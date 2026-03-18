import tkinter as tk
from chatbot_logic import get_response


def send_message():
    user_text = entry.get().strip()

    if user_text == "":
        return

    add_message(user_text, "user")
    entry.delete(0, tk.END)

    reply = get_response(user_text)
    root.after(400, lambda: add_message(reply, "bot"))


def add_message(message, sender):

    frame = tk.Frame(chat_frame, bg="#121826")

    if sender == "user":

        msg = tk.Label(
            frame,
            text="🧑 " + message,
            bg="#4F46E5",
            fg="white",
            padx=12,
            pady=8,
            wraplength=320,
            font=("Segoe UI", 11)
        )

        frame.pack(anchor="e", pady=6, padx=12)

    else:

        msg = tk.Label(
            frame,
            text="🤖 " + message,
            bg="#1F2937",
            fg="#E5E7EB",
            padx=12,
            pady=8,
            wraplength=320,
            font=("Segoe UI", 11)
        )

        frame.pack(anchor="w", pady=6, padx=12)

    msg.pack()

    chat_canvas.update_idletasks()
    chat_canvas.yview_moveto(1)


# Main Window
root = tk.Tk()
root.title("AI Chatbot")
root.geometry("520x620")
root.configure(bg="#0f172a")


# Header
header = tk.Label(
    root,
    text="🤖 AI Chatbot Assistant 💬",
    bg="#1e293b",
    fg="#38BDF8",
    font=("Segoe UI", 18, "bold"),
    pady=12
)

header.pack(fill="x")


# Chat Area
chat_canvas = tk.Canvas(
    root,
    bg="#0f172a",
    highlightthickness=0
)

chat_canvas.pack(fill="both", expand=True)

chat_frame = tk.Frame(chat_canvas, bg="#0f172a")
chat_canvas.create_window((0, 0), window=chat_frame, anchor="nw")


def configure_scroll(event):
    chat_canvas.configure(scrollregion=chat_canvas.bbox("all"))


chat_frame.bind("<Configure>", configure_scroll)


# Bottom Input Area
bottom = tk.Frame(root, bg="#1e293b")
bottom.pack(fill="x")


entry = tk.Entry(
    bottom,
    font=("Segoe UI", 12),
    bg="#334155",
    fg="white",
    insertbackground="white",
    relief="flat"
)

entry.pack(side="left", fill="x", expand=True, padx=12, pady=12)


send_btn = tk.Button(
    bottom,
    text="🚀 Send",
    bg="#22C55E",
    fg="white",
    font=("Segoe UI", 11, "bold"),
    padx=16,
    pady=6,
    relief="flat",
    command=send_message
)

send_btn.pack(side="right", padx=12)


root.mainloop()