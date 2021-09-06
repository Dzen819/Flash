from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"

words_frame = pandas.read_csv("./data/words.csv")


def random_word():
    r = random.randint(1, len(words_frame))
    ru_word = words_frame["Russian"][r]
    en_word = words_frame["English"][r]
    return [ru_word, en_word]
#------------------------------------WINDOW---------------------------------------#
window = Tk()
window.title("Flash")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
#------------------------------------CANVAS---------------------------------------#
canvas = Canvas(height=526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")
canvas.create_image(400, 263, image=card_front_img)
canvas.create_image(400, 263, image=card_back_img)
canvas.create_text(400, 150, text="English", font=("Ariel", 40, "italic"))
canvas.create_text(400, 263, text=random_word()[1], font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)
#------------------------------------BUTTONS---------------------------------------#
yes_img = PhotoImage(file="./images/right.png")
no_img = PhotoImage(file="./images/wrong.png")
yes_button = Button(image=yes_img, highlightthickness=0)
no_button = Button(image=no_img, highlightthickness=0)
yes_button.grid(column=0, row=1)
no_button.grid(column=1, row=1)






















window.mainloop()