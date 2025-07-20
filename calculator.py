import tkinter as tk

BG = "#22223B"
BTN_BG = "#393e53"
BTN_FG = "#fff"
ENTRY_BG = "#352F44"
ENTRY_FG = "#fff"
ACCENT = "#7dcfff"

class calc:
    def __init__(self, window):
        self.win = window
        self.win.title("Mini  Calculator ")
        self.win.configure(bg=BG)
        self.box = tk.Entry(window, font=("Arial", 18), bg=ENTRY_BG, fg=ENTRY_FG,
                            bd=0, relief=tk.FLAT, insertbackground=ENTRY_FG, highlightthickness=1,
                            highlightbackground=ACCENT, justify="right")
        self.box.grid(row=0, column=0, columnspan=4, padx=12, pady=14, ipady=7)
        self.box.insert(0, "0")
        btns = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("C", 4, 2), ("+", 4, 3),
        ]
        for (text, row, col) in btns:
            btn = tk.Button(window, text=text, width=4, height=2,
                            font=("Arial", 14),
                            bg=BTN_BG, fg=BTN_FG, activebackground=ACCENT,
                            relief=tk.FLAT,
                            command=lambda t=text: self.poke(t))
            btn.grid(row=row, column=col, padx=3, pady=3)
        eq_btn = tk.Button(window, text="=", width=18, height=2,
                           font=("Arial", 14, "bold"),
                           bg=ACCENT, fg=BG, activebackground=BTN_BG,
                           relief=tk.FLAT, command=self.equals)
        eq_btn.grid(row=5, column=0, columnspan=4, pady=7)

    def poke(self, char):
        if self.box.get() == "0" or self.box.get() == "Oops!":
            self.box.delete(0, tk.END)
        if char == "C":
            self.box.delete(0, tk.END)
            self.box.insert(0, "0")
        else:
            self.box.insert(tk.END, char)

    def equals(self):
        try:
            expr = self.box.get()
            result = str(eval(expr))
            self.box.delete(0, tk.END)
            self.box.insert(0, result)
        except Exception:
            self.box.delete(0, tk.END)
            self.box.insert(0, "Oops!")

if __name__ == "__main__":
    root = tk.Tk()
    app = calc(root)
    root.mainloop()