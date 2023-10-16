# This file was created by: Owen Pence
''' 
Goals:

Create it so that when a player choses between rock, paper, or scissors, the opponent (AKA computer) makes a reandomized selection of either rock, paper, or scissors.

Based on those two choices, either a Win, Lose, or Draw result is displayed

'''


import turtle

from turtle import *

import os

print("The current working directory is (getcwd): " + os.getcwd())

print("The current working directory is (path.dirname): " + os.path.dirname(__file__))

 
 

game_folder = os.path.dirname(__file__)

# folder location of images that are imported
images_folder = os.path.join(game_folder, 'images') 

 

# Graphic display region in terminal

WIDTH, HEIGHT = 1000, 400  

 
# Rock position in the terminal

rock_w, rock_h = 256, 280 

 
# Paper position in the terminal 

paper_w, paper_h = 256, 204 
 
# Scissors position in the terminal 

scissors_w, scissors_h = 256, 170

 

 

 

screen = turtle.Screen()

screen.setup(WIDTH + 4, HEIGHT + 8)  

screen.setworldcoordinates(0, 0, WIDTH, HEIGHT)

screen.screensize(canvwidth=WIDTH, canvheight=HEIGHT, bg="darkblue")


cv = screen.getcanvas()

cv._rootwindow.resizable(False, False)

 

# File imports for rock, paper, and scissor images through turtle

rock_image = os.path.join(images_folder, 'rock.gif')

 

rock_instance = turtle.Turtle()

 

paper_image = os.path.join(images_folder, 'paper.gif')

 

paper_instance = turtle.Turtle()

 

scissors_image = os.path.join(images_folder, 'scissors.gif')

 

scissors_instance = turtle.Turtle()

 

 

def show_rock(x,y): #Rock displays in terminal 

    screen.addshape(rock_image)

    rock_instance.shape(rock_image)

    rock_instance.penup()

    rock_instance.setpos(x,y)

 


def show_paper(x,y): #Paper displays in terminal 

    screen.addshape(paper_image)  

    paper_instance.shape(paper_image)

    paper_instance.penup()  

    paper_instance.setpos(x,y)

 
def show_scissors(x,y): #Scissors displays in terminal 

    screen.addshape(scissors_image)

    scissors_instance.shape(scissors_image)

    scissors_instance.penup()

    scissors_instance.setpos(x,y)

 

 
# Add color of text in the termanal

t = turtle.Turtle()

text = turtle.Turtle()

text.color('white') 

t.penup()

text.hideturtle()

 

t.hideturtle()

# Computer shows images of rock, paper, and scissors 

show_rock(-300, 0)

show_paper(0,0)

show_scissors (300,0)

 

text.penup()

text.hideturtle()

text.setpos(-300,150)

text.write("Make your pick... either rock, paper, or scissors", False, "left", ("Times New Roman", 28, "normal"))

 

def collide(x,y,obj,w,h):

    if x < obj.pos()[0] + w/2 and x > obj.pos()[0] - w/2 and y < obj.pos()[1] + h/2 and y > obj.pos()[1] - h/2:

        return True

    else:

        return False

    t.penup()

 
 
  
   # Computer outputs player's choice of either rock, paper, or scissors
def player(x, y):

    global text

 
    if (collide(x,y,rock_instance, rock_w, rock_h)): # player choise of rock 

        user_choice = "rock"

    elif(collide(x,y,paper_instance,rock_w,rock_h)): # player choise of paper 

        user_choice = "paper"

    elif(collide(x,y,scissors_instance,scissors_w,scissors_h)): # player choise of scissors 

        user_choice = "scissors"

   

    text.penup()

    text.clear()  

    text.goto(-105, 150)

    text.write(f"You selected... {user_choice}!", align="left", font=("Times New Roman", 24, "normal"))

 

    from random import randint

 
    # Opponent chooses either rock, paper or scissors

    choices = ["rock", "paper", "scissors"]

    computer = choices[randint(0, 2)] 

    
    # Computer outputs text following opponent's choice

    message = f"Opponent chooses... {computer}!"

    x, y = -200, -200

    target_x, target_y = -200, -200

    text.penup()

    text.goto(x, y)

    text.write(message, align="left", font=("Times New Roman", 24, "normal"))

    text.goto(target_x, target_y)

 

 

    import time

    # How long it takes for the computor to project result
    time.sleep(2) 

 
    # Coputer projects result based on player choice

    if user_choice == computer:

        result = "DRAW!"

    elif (user_choice == "rock" and computer == "scissors") or \
         (user_choice == "paper" and computer == "rock") or \
         (user_choice == "scissors" and computer == "paper"):

        result = "Winner Winner Chicken Dinner!"

    else:

        result = "Better luck next time!"

 
    # The font, position, and size of the reult text
    text.clear()

    text.goto(-150, 151)

    text.write(result, align="left", font=("Times New Roman", 28, "normal"))

   

 

playerchoice = screen.onclick(player)

 

playerchoice = screen.mainloop()