import turtle
import random

stickmanTurtle = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("black")

numLetters = 0
numErrors = 0

boxTurtle = turtle.Turtle()
boxTurtle.ht()
boxTurtle.speed(0)
boxTurtle.color("white")
boxTurtle.penup()
boxTurtle.pensize(7)
boxTurtle.goto(-300, 300)
boxTurtle.pendown()

for i in range(4):
    boxTurtle.forward(600)
    boxTurtle.right(90)

boxTurtle.penup()
boxTurtle.color("gold")
boxTurtle.goto(-130, 200)
boxTurtle.write("STICKMAN", font=("Arial", 40, "normal"))
print("Welcome to Stickman!")
print("Guess the word!")

myTurtle = turtle.Turtle()
myTurtle.speed(0)
myTurtle.pensize(5)
myTurtle.color("white")
myTurtle.ht()

stickmanTurtle.penup()
stickmanTurtle.speed(0)
stickmanTurtle.goto(-225, -200)
stickmanTurtle.color("white")
stickmanTurtle.pensize(5)
stickmanTurtle.ht()
stickmanTurtle.pendown()

word = "hello"
for i in range(len(word)):
    stickmanTurtle.forward(50)
    stickmanTurtle.penup()
    stickmanTurtle.forward(50)
    stickmanTurtle.pendown()


def drawStickHead(myTurtle):
    myTurtle.penup()
    myTurtle.goto(0, 100)
    myTurtle.pendown()
    for i in range(36):
        myTurtle.forward(5)
        myTurtle.right(10)

def drawStickBody(myTurtle):
    myTurtle.penup()
    myTurtle.goto(0, 40)
    myTurtle.pendown()
    myTurtle.right(90)
    myTurtle.forward(70)

def drawStickLegs(myTurtle, length):
    myTurtle.left(30)
    myTurtle.forward(length)
    myTurtle.backward(length)
    myTurtle.right(60)
    myTurtle.forward(length)
    myTurtle.backward(length)
    myTurtle.left(30)

def drawStickArms(myTurtle, length):
    myTurtle.backward(45)
    drawStickLegs(myTurtle, length)
    
def drawStick(number, myTurtle):
    if(number == 1):
        drawStickHead(myTurtle)
    elif(number == 2):
        drawStickBody(myTurtle)
    elif(number == 3):
        drawStickLegs(myTurtle, 60)
    elif(number == 4):
        drawStickArms(myTurtle, 50)


while True:
    userGuess = input("Guess a letter and determine stickman's fate: ")
    for i in range(len(word)):
        if(userGuess == word[i]):
            #draw letter on blank line
            numLetters += 1
    if(numLetters == 0):
        numErrors += 1
        drawStick(numErrors, myTurtle)
    numLetters = 0
    if numErrors >= 4:
        input("Game over. Stickman died. Try again next time! Press enter to quit: ")
        break