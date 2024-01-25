import tkinter as tk
from tkinter import Entry, Label, Button, StringVar
import random
import string

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")

        self.password_var = StringVar()

        self.create_gui()

    def create_gui(self):
        Label(self.root, text="Specify Password Length:").pack(pady=10)

        self.length_entry = Entry(self.root)
        self.length_entry.pack(pady=5)

        Button(self.root, text="Generate Password", command=self.generate_password).pack(pady=10)

        Label(self.root, text="Generated Password:").pack()
        Label(self.root, textvariable=self.password_var, font=("Courier", 12)).pack()

    def generate_password(self):
        try:
            password_length = int(self.length_entry.get())
            if password_length <= 0:
                raise ValueError("Length should be a positive integer.")

            characters = string.ascii_letters + string.digits + string.punctuation
            generated_password = ''.join(random.choice(characters) for _ in range(password_length))

            self.password_var.set(generated_password)
        except ValueError as e:
            self.password_var.set("Invalid input. Please enter a positive integer.")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
