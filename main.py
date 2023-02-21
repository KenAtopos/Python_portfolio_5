import random
import time
import tkinter as tk


class TypingSpeedTest:
    def __init__(self, master):
        self.master = master
        self.master.title("Typing Speed Test")

        self.word_list = ["apple", "banana", "cherry", "date", "elderberry",
                  "fig", "grape", "honeydew", "kiwi", "lemon",
                  "orange", "peach", "pear", "quince", "raspberry",
                  "strawberry", "tangerine", "watermelon", "blueberry", "blackberry"]


        self.current_word = ""
        self.typed_word = ""
        self.correct_words = 0
        self.total_words = 0
        self.accuracy = 0
        self.start_time = 0
        self.end_time = 0
        self.elapsed_time = 0

        self.instructions = tk.Label(self.master, text="Type the word below and press enter:")
        self.instructions.pack()

        self.word_label = tk.Label(self.master, text="")
        self.word_label.pack()

        self.entry = tk.Entry(self.master)
        self.entry.bind("<Return>", self.check_word)
        self.entry.pack()

        self.stats_label = tk.Label(self.master, text="")
        self.stats_label.pack()

        self.new_word()

    def new_word(self):
        self.current_word = random.choice(self.word_list)
        self.word_label.config(text=self.current_word)

    def check_word(self, event):
        self.typed_word = self.entry.get()
        self.total_words += 1
        if self.typed_word == self.current_word:
            self.correct_words += 1
        self.accuracy = round((self.correct_words / self.total_words) * 100, 2)

        if self.total_words == 1:
            self.start_time = time.time()

        if self.correct_words == 10:
            self.end_time = time.time()
            self.elapsed_time = round(self.end_time - self.start_time, 2)
            self.show_results()
            return

        self.stats_label.config(text=f"Accuracy: {self.accuracy}%")

        self.entry.delete(0, tk.END)
        self.new_word()

    def show_results(self):
        self.word_label.config(text="")
        self.entry.destroy()
        self.instructions.config(text="Test complete!")
        self.stats_label.config(text=f"Accuracy: {self.accuracy}%\n"
                                      f"Elapsed time: {self.elapsed_time} seconds")


if __name__ == "__main__":
    root = tk.Tk()
    app = TypingSpeedTest(root)
    root.mainloop()
