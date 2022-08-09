from email.mime import image
import tkinter
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient = "records")
else:
    to_learn = data.to_dict(orient = "records")

#------------------------CREATE NEW LIST--------------------------#
"""Of known words by the user"""
def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index  =  False)

    next_card()




#------------------------FLIP CARD--------------------------#
def flip_card():
    global current_card
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text = "English", fill = "white")
    canvas.itemconfig(card_word, text = current_card["English"], fill = "white")
    canvas.itemconfig(card_backround, image = card_back_png)
#------------------------CURRENT CARD--------------------------#
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer) #cancel timer after button is pressed
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text = "French", fill = "black")
    canvas.itemconfig(card_word, text = current_card["French"], fill = "black")
    canvas.itemconfig(card_backround, image = card_front_png)
    flip_timer = window.after(3000, func=flip_card) #creating new timer after button is pressed

#------------------------UI SETUP--------------------------#
"""window"""
window = tkinter.Tk()
window.title("Flash card app")  
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = tkinter.Canvas(width=800, height=526)
card_back_png = tkinter.PhotoImage(file = "images/card_back.png")
card_front_png = tkinter.PhotoImage(file = "images/card_front.png")
card_backround = canvas.create_image(400, 263, image = card_front_png)
card_title = canvas.create_text(400, 150, text = "", font = ("Ariel", 40, "italic"), fill= "black")
card_word = canvas.create_text(400, 263, text = "", font = ("Arial", 60, "bold"), fill = "black" )
canvas.config(bg = BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row = 0, column = 0, columnspan=2)


"""buttons"""
wrong_button_png = tkinter.PhotoImage(file = "images/wrong.png")
wrong_button = tkinter.Button(image = wrong_button_png, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

right_button_png = tkinter.PhotoImage(file = "images/right.png")
right_button = tkinter.Button(image = right_button_png, highlightthickness=0, command=is_known)
right_button.grid(row = 1, column = 1)

next_card()
window.mainloop()

