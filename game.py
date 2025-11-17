# I acknowledge the use of ChatGPT (OpenAI, GPT-5.1) to co-create the code in this file.
# TODO: add difficulty levels later

import tkinter as tk
import random

class ClickGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Click the Target! v2")

        self.score = 0
        self.time_left = 20

        self.canvas = tk.Canvas(root, width=400, height=400, bg="white")
        self.canvas.pack()

        self.score_label = tk.Label(root, text=f"Score: {self.score}")
        self.score_label.pack()

        self.time_label = tk.Label(root, text=f"Time left: {self.time_left}")
        self.time_label.pack()

        self.target = self.canvas.create_oval(0, 0, 40, 40, fill="red")
        self.move_target()

        self.canvas.tag_bind(self.target, "<Button-1>", self.hit_target)

        self.update_timer()

    def move_target(self):
        x = random.randint(20, 380)
        y = random.randint(20, 380)
        self.canvas.coords(self.target, x-20, y-20, x+20, y+20)

    def hit_target(self, event):
        if self.time_left > 0:
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}")
            self.move_target()

    def update_timer(self):
        if self.time_left > 0:
            self.time_left -= 1
            self.time_label.config(text=f"Time left: {self.time_left}")
            self.root.after(1000, self.update_timer)
        else:
            self.time_label.config(text="Game Over!")

if __name__ == "__main__":
    root = tk.Tk()
    game = ClickGame(root)
    root.mainloop()
