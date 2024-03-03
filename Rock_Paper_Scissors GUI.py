#importing libraries 
from tkinter import *
import random
#a dictionary to randomly select for computer
Comp_dict={
    "0":"Rock",
    "1":"Paper",
    "2":"Scissor"
    }
#defining Global Variables
your_choice=""
Comp_choice=""
computer_score=0
your_score=0

#function to clear the text area where choices are displayed 
def Playagain():
    text_to_display.delete("1.0","end")

#function to update points after every game 
def points():
    text_to_scores.delete("1.0","end")
    text_to_scores.insert(END,f"  {your_score}                   {computer_score}")
    

#function to define what happens when user select Rock 
def rock():
    global computer_score
    global your_score
    your_choice="Rock"
#choosing random variable from the above defined dictionary 
    Comp_choice=Comp_dict[str(random.randint(0,2))]
#to display choices 
    text_to_display.insert(END,f"Your Choice:          {your_choice}\nComputer's Choice:    {Comp_choice}"
                           
)
#to increase the scores accordingly 
    if Comp_choice=="Paper":
        computer_score+=1
    if Comp_choice=="Scissor":
        your_score+=1
    points()

#same as the above function   
def paper():
    global computer_score
    global your_score
    your_choice="Paper"
    Comp_choice=Comp_dict[str(random.randint(0,2))]
    text_to_display.insert(END,f"Your Choice:          {your_choice}\nComputer's Choice:    {Comp_choice}"
)
    if Comp_choice=="Scissor":
        computer_score+=1
    if Comp_choice=="Rock":
        your_score+=1
    points()
def scissor():
    global computer_score
    global your_score
    your_choice="Scissor"
    Comp_choice=Comp_dict[str(random.randint(0,2))]
    text_to_display.insert(END,f"Your Choice:          {your_choice}\nComputer's Choice:    {Comp_choice}"
)
    if Comp_choice=="Rock":
        computer_score+=1
    if Comp_choice=="Paper":
        your_score+=1
    points()
#Defining main window and all it's widgets 
root=Tk()
root.title("ProjectGurukul Rock Paper Scissor")
root.geometry('270x200')
root.config(bg="sky blue")
#text widget to display choices 
text_to_display=Text(root,height=3,width=30)
text_to_display.grid(row=0,columnspan=5,pady=10)
#buttons defined accordingly 
bttn_rock=Button(root,text="Rock",width=6,command=rock)
bttn_rock.grid(row=2,column=0,padx=10)

bttn_paper=Button(root,text="Paper",width=6,command=paper)
bttn_paper.grid(row=2,column=1,padx=5)

bttn_Scissor=Button(root,text="Scissor",width=6,command=scissor)
bttn_Scissor.grid(row=2,column=2,padx=10)

#Widget to add label specified by text
label_scores=Label(root,text="Your score         vs        Computer's score")
label_scores.grid(row=3,columnspan=5,pady=8)



text_to_scores=Text(root,height=1,width=30)
text_to_scores.grid(row=4,columnspan=5,pady=5)

#play again button to start the game again 
Play_again=Button(root,text="Play Again",command=Playagain)
Play_again.grid(row=5,columnspan=3)



mainloop()
