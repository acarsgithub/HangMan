import turtle
import random

stickmanTurtle = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("black")

numLetters = 0
numErrors = 0
numCorrect = 0


# drawing the boundary box of the game
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
boxTurtle.color("white")
boxTurtle.goto(-150, 200)
boxTurtle.write("STICKMAN", font=("Times New Roman", 45, "normal"))
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

# reading through dictionary text file and choosing a random word from the file
with open('dictionary.txt') as fobj:
    data = fobj.read()
    lines = data.split('\n')

randNum = random.randint(0, len(lines))

while(len(lines[randNum]) != 5):
    randNum = random.randint(0, len(lines))

word = lines[randNum]
wordLength = len(word)

# drawing the empty lines for letters of the word
for i in range(len(word)):
    stickmanTurtle.forward(50)
    stickmanTurtle.penup()
    stickmanTurtle.forward(50)
    stickmanTurtle.pendown()

# functions to help draw stickman body parts
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
    myTurtle.backward(55)
    drawStickLegs(myTurtle, length)

def drawStickEyes(myTurtle, x, y):
    myTurtle.penup()
    myTurtle.color('red')
    myTurtle.pensize(3)
    myTurtle.goto(x, y)
    myTurtle.pendown()
    myTurtle.right(45)
    myTurtle.forward(7)
    myTurtle.backward(14)
    myTurtle.forward(7)
    myTurtle.left(90)
    myTurtle.forward(7)
    myTurtle.backward(14)
    myTurtle.forward(7)
    myTurtle.right(45)
    myTurtle.pensize(5)

# function that determines which part of stickman's body it should draw
def drawStick(number, myTurtle):
    if(number == 1):
        drawStickHead(myTurtle)
    elif(number == 2):
        drawStickBody(myTurtle)
    elif(number == 3):
        drawStickLegs(myTurtle, 60)
    elif(number == 4):
        drawStickArms(myTurtle, 50)
    elif(number == 5):
        drawStickEyes(myTurtle, -8, 75)
        drawStickEyes(myTurtle, 12, 75)

# turtle for final result display
resultTurtle = turtle.Turtle()
resultTurtle.ht()
resultTurtle.penup()
resultTurtle.goto(-87.5, 120)

# list to contain the letters already guessed
lettersList = []


while True:
    userGuess = input("Guess a letter and determine stickman's fate: ")

    # determining if the user guess has already been made
    guessedAlready = False
    for letter in lettersList:
        if(letter == userGuess):
            guessedAlready = True

    if(guessedAlready == False):
        # algorithm to determine if the user guess is correct
        for i in range(len(word)):
            if(userGuess == word[i]):
                letterTurtle = turtle.Turtle()
                letterTurtle.penup()
                letterTurtle.ht()
                letterTurtle.color('blue')
                letterTurtle.goto(-215 + (100 * i), -195)
                letterTurtle.write(word[i].upper(), font=("Times New Roman", 40, "normal"))
                numLetters += 1
                numCorrect += 1

        # appending to user guess list
        lettersList.append(userGuess)

        # the user guessed the wrong letter
        if(numLetters == 0):
            numErrors += 1
            drawStick(numErrors, myTurtle)
        numLetters = 0

        # determinig if the user won the game
        if(numCorrect == wordLength):
            resultTurtle.forward(25)
            resultTurtle.color('green')
            resultTurtle.write("NICE", font=("Times New Roman", 50, "normal"))
            input("Great job! You won the game. Press enter to quit: ")
            break

        # determining if the stickman died
        if numErrors >= 5:
            resultTurtle.color('red')
            resultTurtle.write("DEAD", font=("Times New Roman", 50, "normal"))

            # show the user what the correct word was
            for i in range(len(word)):
                letterTurtle = turtle.Turtle()
                letterTurtle.penup()
                letterTurtle.ht()
                letterTurtle.color('blue')
                letterTurtle.goto(-215 + (100 * i), -195)
                letterTurtle.write(word[i].upper(), font=("Times New Roman", 40, "normal"))
        
            input("Game over. Stickman died. Try again next time! Press enter to quit: ")
            break
    else:
        print("You have already guessed this letter. Guess voided!")