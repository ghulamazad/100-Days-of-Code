from tkinter import *
from tkinter import messagebox
from timeit import default_timer as timer
from difflib import SequenceMatcher
import random

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
BLACK = "#000000"
YELLOW = "#f7f5dd"
FONT_NAME = "Times Roman"


# ---------------------------- GENERATE SENTENCE ------------------------------- #
def get_sentance():
    sentences = ''
    with open('sentences.txt') as file:
        sentences = file.readlines()
    return random.choice(sentences).rstrip()


# ---------------------------- Initial UI ------------------------------- #
class TypingSpeedTest(Tk):
    def __init__(self):
        super(TypingSpeedTest, self).__init__()
        self.title('Typing Speed Test')
        self.config(padx=26, pady=26, bg=YELLOW)

        # TITLE
        title_lbl = Label(self, text="Typing Speed Test", fg=RED,
                          bg=YELLOW, font=(FONT_NAME, 46, "bold"))
        title_lbl.grid(row=0, column=0)


# ---------------------------- RESTART TEST ------------------------------- #
def restart(main_window):
    main_window.destroy()
    start_test()


# ---------------------------- MAIN WINDOW UI ------------------------------- #
def start_test():
    try:
        start_window.destroy()
    except Exception:
        pass
    # get sentence
    sentence = get_sentance()

    def check_result():
        end_time = timer()
        total_time = end_time - start_time
        accuracy = SequenceMatcher(None, sentence, entry.get()).ratio() * 100
        wpm = len(entry.get()) * 60/(5*total_time)
        result = f'Time: {str(round(total_time))} secs Accuracy: {str(round(accuracy))}% Wpm: {str(round(wpm))}'
        messagebox.showinfo(title="Typing Speed Test", message=result)
        try_again_btn = Button(main_window, text="Try Again.",
                               fg=YELLOW, bg=RED, font=(FONT_NAME, 16, "normal"), command=lambda: restart(main_window))
        try_again_btn.grid(row=4, column=0, pady=(10, 0))
        entry['state'] = DISABLED
        check_result_btn["state"] = DISABLED

    # START TIMER
    start_time = timer()
    # CREATE NEW WINDOW FOR TEST
    main_window = TypingSpeedTest()
    sentance_lbl = Label(main_window, text=sentence,
                         fg=BLACK, bg=YELLOW, font=(FONT_NAME, 36, "normal"), wraplength=1000, justify="center")
    sentance_lbl.grid(row=1, column=0, pady=(50, 20))
    entry = Entry(main_window, width=36, font=(FONT_NAME, 36, "normal"))
    entry.grid(row=2, column=0)

    check_result_btn = Button(main_window, text="Check Result",
                              fg=YELLOW, bg=RED, font=(FONT_NAME, 16, "normal"), command=check_result)
    check_result_btn.grid(row=3, column=0, pady=(46, 0))
    main_window.mainloop()


# ---------------------------- START WINDOW UI ------------------------------- #
if __name__ == "__main__":
    start_window = TypingSpeedTest()
    start_test_btn = Button(start_window, text="Start Typing Test",
                            fg=YELLOW, bg=RED, font=(FONT_NAME, 16, "normal"), command=start_test)
    start_test_btn.grid(row=2, column=0, padx=10, pady=100)
    start_window.mainloop()
