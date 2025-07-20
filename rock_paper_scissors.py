import tkinter as tk
import random

def play(user):
    comp= random.choice(["Rock", "Paper", "Scissors"])
    result = "Tie" if user == comp else "Win" if (user == "Rock" and comp == "Scissors") or (user == "Paper" and comp == "Rock") or (user == "Scissors" and comp == "Paper") else "Lose"
    lbl.config(text=f"Computer: {comp}\nYou {result}!")

root = tk.Tk()
root.title("Rock paper scissors Game")

lbl = tk.Label(root, text="Choose Rock, Paper or Scissors", font=("Arial", 12))
lbl.pack(pady=20)

for choice in ["Rock", "Paper", "Scissors"]:
    tk.Button(root, text=choice, width=10, command=lambda c=choice: play(c)).pack(pady=5)

root.mainloop()