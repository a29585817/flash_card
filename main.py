import tkinter

import pandas
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"

window = tkinter.Tk()
window.title("Flash Card")
window.configure(bg=BACKGROUND_COLOR, padx=50, pady=50)

# ---------------------Open File--------------------------- --
try:
    df = pd.read_csv('words_to_learns.csv')
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    data_dict = {y["French"]: y["English"] for (x, y) in original_data.iterrows()}
else:
    data_dict = {y["French"]: y["English"] for (x, y) in df.iterrows()}
question = list(data_dict.keys())
choice_question = random.choice(question)


# # ---------------------word to learn--------------------------- --
def word_to_learn():
    with open("word_to_learn.csv", mode="a", encoding="utf-8") as file:
        file.write(choice_question + "|" + data_dict[choice_question] + "\n")
    next_card()


def is_know():
    question.remove(choice_question)
    print(len(question))
    next_card()
    data = pandas.DataFrame(question)
    data.to_csv("words_to_learns.csv", index=False)
# ---------------------choice--------------------------- --
def next_card():
    global choice_question, flip_timer
    window.after_cancel(flip_timer)
    choice_question = random.choice(question)
    canvas.itemconfig(title_text, text="French", fill='black')
    canvas.itemconfig(word_text, text=choice_question, fill="black")
    canvas.itemconfig(card_background, image=card_front)
    #         time.sleep(1)
    flip_timer = window.after(3000, func=change)


# # ---------------------cound down--------------------------- --
def change():
    canvas.itemconfig(title_text, text="English", fill='white')
    canvas.itemconfig(word_text, text=data_dict[choice_question], fill='white')
    canvas.itemconfig(card_background, image=card_back)


flip_timer = window.after(3000, func=change)

# ---------------------Canvas--------------------------- --
canvas = tkinter.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = tkinter.PhotoImage(file="images/card_front.png")
card_background = canvas.create_image(400, 263, image=card_front)
card_back = tkinter.PhotoImage(file="images/card_back.png")
title_text = canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text=choice_question, font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# ---------------------Botton-----------------------------

right = tkinter.PhotoImage(file="images/right.png")
wrong = tkinter.PhotoImage(file="images/wrong.png")

known_button = tkinter.Button(image=right, highlightthickness=0, command=is_know)
known_button.grid(column=1, row=1, )
unknown_button = tkinter.Button(image=wrong, highlightthickness=0, command=word_to_learn)
unknown_button.grid(column=0, row=1, )

# ---------------------word-----------------------------


window.mainloop()
