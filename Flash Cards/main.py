from tkinter import Tk, Canvas, PhotoImage, Button
import pandas
import random


BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = []
flip_timer = None


# Load saved progress if it exists; otherwise start with the full deck.
try:
    data = pandas.read_csv("./Flash Cards/data/to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("./Flash Cards/data/french_words.csv")
    to_learn = data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer

    # Reset the flip countdown every time a new card is shown.
    if flip_timer is not None:
        window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=car_front_img)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=car_back_img)


def is_known():
    # Remove known words from the learning pool and persist the progress.
    to_learn.remove(current_card)
    updated_data = pandas.DataFrame(to_learn)
    updated_data.to_csv("./Flash Cards/data/to_learn.csv", index=False)
    next_card()


# UI setup

window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
car_front_img = PhotoImage(file="./Flash Cards/images/card_front.png")
car_back_img = PhotoImage(file="./Flash Cards/images/card_back.png")
card_background = canvas.create_image(400, 263, image=car_front_img)
card_title = canvas.create_text(
    400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

cross_img = PhotoImage(file="./Flash Cards/images/wrong.png")
unknown_button = Button(
    image=cross_img, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

check_img = PhotoImage(file="./Flash Cards/images/right.png")
known_button = Button(image=check_img, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)


next_card()


window.mainloop()
