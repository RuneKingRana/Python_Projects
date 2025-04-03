# Importing libraries
from tkinter import *
import random

# Dictionary to randomly select for computer
Comp_dict = {
    "0": "Rock",
    "1": "Paper",
    "2": "Scissor"
}

# Defining Global Variables
your_choice = ""
Comp_choice = ""
computer_score = 0
your_score = 0

# Function to clear the text area where choices are displayed
def Playagain():
    text_to_display.delete("1.0", "end")

# Function to update points after every game
def points():
    your_score_label.config(text=f"Your Score: {your_score}")
    computer_score_label.config(text=f"Computer Score: {computer_score}")

# Function to define what happens when user selects Rock
def rock():
    global computer_score, your_score
    your_choice = "Rock"
    Comp_choice = Comp_dict[str(random.randint(0, 2))]
    text_to_display.insert(END, f"Your Choice:          {your_choice}\nComputer's Choice:    {Comp_choice}\n")

    if Comp_choice == "Paper":
        computer_score += 1
    if Comp_choice == "Scissor":
        your_score += 1
    points()

# Function to define what happens when user selects Paper
def paper():
    global computer_score, your_score
    your_choice = "Paper"
    Comp_choice = Comp_dict[str(random.randint(0, 2))]
    text_to_display.insert(END, f"Your Choice:          {your_choice}\nComputer's Choice:    {Comp_choice}\n")

    if Comp_choice == "Scissor":
        computer_score += 1
    if Comp_choice == "Rock":
        your_score += 1
    points()

# Function to define what happens when user selects Scissor
def scissor():
    global computer_score, your_score
    your_choice = "Scissor"
    Comp_choice = Comp_dict[str(random.randint(0, 2))]
    text_to_display.insert(END, f"Your Choice:          {your_choice}\nComputer's Choice:    {Comp_choice}\n")

    if Comp_choice == "Rock":
        computer_score += 1
    if Comp_choice == "Paper":
        your_score += 1
    points()

# Defining main window and all its widgets
root = Tk()
root.title("Rock Paper Scissor")
root.attributes('-fullscreen', True)  # Open in full-screen mode
root.config(bg="sky blue")

# Frame for choices display
text_to_display = Text(root, height=5, width=50, font=("Arial", 16))
text_to_display.pack(pady=20)

# Frame for buttons
button_frame = Frame(root, bg="sky blue")
button_frame.pack(pady=20)

# Buttons with larger size
bttn_rock = Button(button_frame, text="Rock", width=15, height=2, font=("Arial", 16), command=rock)
bttn_rock.grid(row=0, column=0, padx=20)

bttn_paper = Button(button_frame, text="Paper", width=15, height=2, font=("Arial", 16), command=paper)
bttn_paper.grid(row=0, column=1, padx=20)

bttn_Scissor = Button(button_frame, text="Scissor", width=15, height=2, font=("Arial", 16), command=scissor)
bttn_Scissor.grid(row=0, column=2, padx=20)

# Frame for scores
score_frame = Frame(root, bg="sky blue")
score_frame.pack(pady=20)

# Labels for scores
your_score_label = Label(score_frame, text="Your Score: 0", font=("Arial", 20), bg="sky blue")
your_score_label.grid(row=0, column=0, padx=50)

computer_score_label = Label(score_frame, text="Computer Score: 0", font=("Arial", 20), bg="sky blue")
computer_score_label.grid(row=0, column=1, padx=50)

# Play again button
Play_again = Button(root, text="Play Again", width=15, height=2, font=("Arial", 16), command=Playagain)
Play_again.pack(pady=20)

# Exit button
Exit_btn = Button(root, text="Exit", width=15, height=2, font=("Arial", 16), command=root.quit)
Exit_btn.pack(pady=10)

root.mainloop()
