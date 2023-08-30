import tkinter as tk
from tkinter import ttk
import random
import string

class PasswordGenerator(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Password Generator")
        self.geometry("300x150")

        # Label
        self.label = ttk.Label(self, text="Password Length:")
        self.label.pack(pady=10)

        # Combobox for length selection
        self.length_var = tk.IntVar()
        self.length_var.set(8)  # default value
        self.combobox = ttk.Combobox(self, textvariable=self.length_var, values=[i for i in range(6, 21)], width=15)
        self.combobox.pack(pady=10)

        # Button to generate password
        self.generate_button = ttk.Button(self, text="Generate Password", command=self.generate_password)
        self.generate_button.pack(pady=10)

        # Entry to display generated password
        self.password_var = tk.StringVar()
        self.password_entry = ttk.Entry(self, textvariable=self.password_var, width=30)
        self.password_entry.pack(pady=10)

    def generate_password(self):
        length = self.length_var.get()
        chars = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(chars) for i in range(length))
        self.password_var.set(password)

if __name__ == '__main__':
    app = PasswordGenerator()
    app.mainloop()
