import tkinter as tk
import random

class GuessingGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Guessing Game")

        self.target_number = random.randint(1, 100)
        self.attempts = 0

        self.label = tk.Label(master, text="Guess a number between 1 and 100:")
        self.label.pack()

        self.entry = tk.Entry(master)
        self.entry.pack()

        self.result_label = tk.Label(master, text="")
        self.result_label.pack()

        self.submit_button = tk.Button(master, text="Submit", command=self.check_guess)
        self.submit_button.pack()

    def check_guess(self):
        guess = int(self.entry.get())
        self.attempts += 1

        if guess < self.target_number:
            self.result_label.config(text="Too low! Try again.")
        elif guess > self.target_number:
            self.result_label.config(text="Too high! Try again.")
        else:
            self.result_label.config(text=f"Congratulations! You guessed the number {self.target_number} in {self.attempts} attempts.")
            self.submit_button.config(state=tk.DISABLED)
            self.entry.config(state=tk.DISABLED)

def main():
    root = tk.Tk()
    game = GuessingGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
