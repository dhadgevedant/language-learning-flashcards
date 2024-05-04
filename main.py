from tkinter import *
from random import randint
import time
import pyttsx3

root = Tk()
root.title('Codemy.com - Spanish Language Flashcards')
#root.iconbitmap('c:/gui/codemy.ico')
root.geometry("550x410")

engine = pyttsx3.init()

'''
words = [
    (("Hola"), ("Hello")),
    (("Adiós"), ("Goodbye")),
    (("Por favor"), ("Please")),
    (("Gracias"), ("Thank you")),
    (("Lo siento"), ("Sorry")),
    (("Salud"), ("Bless you")),
    (("Sí"), ("Yes")),
    (("No"), ("No")),
    (("¿Quién?"), ("Who")),
    (("¿Qué?"), ("What")),
    (("¿Por qué?"), ("Why")),
    (("¿Dónde?"), ("Where"))
]
'''



import csv
with open('English_to_learn.csv', 'r', errors="ignore") as read_obj: 
  
    # Return a reader object which will 
    # iterate over lines in the given csvfile 
    csv_reader = csv.reader(read_obj) 
  
    # convert string to list 
    words = list(csv_reader) 


def switch():

    global a
    global b
 
    if a:
        a = 0
    else:
        a = 1

    if b:
        b = 0
    else:
        b = 1       
    next()



#SWITCH VAR WHEN LEARNING AND TESTING

a = 0
b = 1




# get a count of our word list
count = len(words)

def next():
    global hinter, hint_count
    # Clear the screen
    answer_label.config(text="")
    my_entry.delete(0, END)
    hint_label.config(text="")
    # Reset Hint stuff
    hinter = ""
    hint_count = 0

    # Create random selection
    global random_word
    random_word = randint(0, count-1)
    # update label with Spanish Word
    spanish_word.config(text=words[random_word][b])

    
    
    


def answer():
    if my_entry.get().capitalize() == words[random_word][a]:
        answer_label.config(text=f"Correct! {words[random_word][b]} is {words[random_word][a]}")
    else:
        answer_label.config(text=f"Incorrect! {words[random_word][b]} is not {my_entry.get().capitalize()}")

# Keep Track Of the Hints
hinter = ""
hint_count = 0
def hint():
    global hint_count
    global hinter

    if hint_count < len(words[random_word][a]):
        hinter = hinter + words[random_word][a][hint_count]
        hint_label.config(text=hinter)
        hint_count +=1

def speak():
    
    engine.say(words[random_word][b])                             
    engine.runAndWait()




# Labels
spanish_word = Label(root, text="", font=("Helvetica", 36))
spanish_word.pack(pady=50)

answer_label = Label(root, text="")
answer_label.pack(pady=20)

my_entry = Entry(root, font=("Helvetica", 18))
my_entry.pack(pady=20)

# Create Buttons
button_frame = Frame(root)
button_frame.pack(pady=20)

answer_button = Button(button_frame, text="Answer", command=answer)
answer_button.grid(row=0, column=0, padx=20)

next_button = Button(button_frame, text="Next", command=next)
next_button.grid(row=0, column=1, padx = 20)

hint_button = Button(button_frame, text="Hint", command=hint)
hint_button.grid(row=0, column=2, padx=20)

speak_button = Button(button_frame, text="Speak", command=speak)
speak_button.grid(row=0, column=3, padx=20)

switch_button = Button(button_frame, text="Switch", command=switch)
switch_button.grid(row=0, column=4, padx=20)

# Create Hint Label
hint_label = Label(root, text="")
hint_label.pack(pady=20)

# Run next function when program starts
next()


root.mainloop()

