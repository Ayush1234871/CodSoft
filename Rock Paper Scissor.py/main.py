import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissorsGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock, Paper, Scissors Game")

        self.user_score = 0
        self.computer_score = 0

        self.create_gui()

    def create_gui(self):
        tk.Label(self.root, text="Choose Rock, Paper, or Scissors:").pack(pady=10)

        tk.Button(self.root, text="Rock", command=lambda: self.play("Rock")).pack(side=tk.LEFT, padx=10)
        tk.Button(self.root, text="Paper", command=lambda: self.play("Paper")).pack(side=tk.LEFT, padx=10)
        tk.Button(self.root, text="Scissors", command=lambda: self.play("Scissors")).pack(side=tk.LEFT, padx=10)

        self.result_label = tk.Label(self.root, text="")
        self.result_label.pack(pady=20)

        self.score_label = tk.Label(self.root, text="Score: User - 0, Computer - 0")
        self.score_label.pack()

    def play(self, user_choice):
        choices = ["Rock", "Paper", "Scissors"]
        computer_choice = random.choice(choices)

        if user_choice == computer_choice:
            result = "It's a Tie!"
        elif (
            (user_choice == "Rock" and computer_choice == "Scissors") or
            (user_choice == "Scissors" and computer_choice == "Paper") or
            (user_choice == "Paper" and computer_choice == "Rock")
        ):
            result = "You Win!"
            self.user_score += 1
        else:
            result = "Computer Wins!"
            self.computer_score += 1

        result_text = f"User: {user_choice}\nComputer: {computer_choice}\nResult: {result}"
        self.result_label.config(text=result_text)

        score_text = f"Score: User - {self.user_score}, Computer - {self.computer_score}"
        self.score_label.config(text=score_text)

        play_again = messagebox.askyesno("Play Again", "Do you want to play again?")
        if not play_again:
            self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    game = RockPaperScissorsGame(root)
    root.mainloop()
