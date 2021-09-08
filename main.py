from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
try:
    words_frame = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    words_frame = pandas.read_csv("./data/words.csv")

words_dict = words_frame.to_dict(orient="records")
current_word = {}


def random_word():
    global current_word, flip_timer
    window.after_cancel(flip_timer)
    current_word = random.choice(words_dict)
    canvas.itemconfigure(en_text, text=current_word["English"], fill="black")
    canvas.itemconfigure(title, text="English", fill="black")
    canvas.itemconfigure(background_img, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfigure(en_text, text=current_word["Russian"], fill="white")
    canvas.itemconfigure(title, text="Russian", fill="white")
    canvas.itemconfigure(background_img, image=card_back_img)


def yes():
    words_dict.remove(current_word)
    new_words = pandas.DataFrame(words_dict)
    new_words.to_csv("data/words_to_learn.csv", index=False)
    random_word()


def no():
    random_word()


# ------------------------------------WINDOW---------------------------------------#
window = Tk()
window.title("Flash")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)
# ------------------------------------CANVAS---------------------------------------#
canvas = Canvas(height=526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")
background_img = canvas.create_image(400, 263, image=card_front_img)
title = canvas.create_text(400, 150, text="English", font=("Ariel", 40, "italic"))
en_text = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)
# ------------------------------------BUTTONS---------------------------------------#
yes_img = PhotoImage(file="./images/right.png")
no_img = PhotoImage(file="./images/wrong.png")
yes_button = Button(image=yes_img, highlightthickness=0, command=yes)
no_button = Button(image=no_img, highlightthickness=0, command=no)
yes_button.grid(column=0, row=1)
no_button.grid(column=1, row=1)

random_word()

window.mainloop()
