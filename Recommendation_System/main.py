import tkinter as tk
from tkinter import ttk
from recommender import get_recommendations

def recommend():
    selected_type = type_var.get()
    selected_genre = genre_var.get()

    result_box.delete(1.0, tk.END)

    if not selected_type or not selected_genre:
        result_box.insert(tk.END, "⚠️ Please select both type and genre")
        return

    results = get_recommendations(selected_type, selected_genre)

    if results:
        result_box.insert(tk.END, "🎯 Recommendations:\n\n")
        for r in results:
            result_box.insert(tk.END, f"• {r}\n")
    else:
        result_box.insert(tk.END, "No recommendations found.")

# WINDOW
root = tk.Tk()
root.title("AI Recommendation System")
root.geometry("500x500")
root.configure(bg="#0f172a")

# TITLE
title = tk.Label(root, text="🎯 Recommendation System",
                 font=("Helvetica", 18, "bold"),
                 bg="#0f172a", fg="#38bdf8")
title.pack(pady=10)

# TYPE SELECTION
tk.Label(root, text="Select Type",
         bg="#0f172a", fg="white").pack()

type_var = tk.StringVar()
type_menu = ttk.Combobox(root, textvariable=type_var,
                         values=["movie", "book", "music"])
type_menu.pack(pady=5)

# GENRE SELECTION
tk.Label(root, text="Select Genre",
         bg="#0f172a", fg="white").pack()

genre_var = tk.StringVar()
genre_menu = ttk.Combobox(root, textvariable=genre_var,
                          values=["action", "comedy", "romance", "fantasy", "pop"])
genre_menu.pack(pady=5)

# BUTTON
btn = tk.Button(root, text="Recommend 🚀",
                command=recommend,
                bg="#22c55e", fg="black",
                font=("Helvetica", 12, "bold"))
btn.pack(pady=15)

# RESULT BOX
result_box = tk.Text(root, height=10,
                     bg="#020617", fg="white",
                     font=("Consolas", 12))
result_box.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)


root.mainloop()