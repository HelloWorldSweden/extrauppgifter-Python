''' Skriven av Jenny Böjeryd Maj 2023'''

from taskMaster import * 
from deltagare import *
import turtle

# Hallå!
# Kul att du hittade hit! Här ska du egentligen inte vara,
# snälla rör rör ingenting av koden 

def resetScreen(screen):
    screen.bgpic("rutnät.png")

def resetTurtle(turtle):
    turtle.clear()
    turtle.setheading(0)
    turtle.up()
    turtle.goto(-230,-210) #startpos på bilden.
    turtle.pensize(10)
    turtle.down()

# input: Inget
# output: 
# Turtle objekt pelle (facitturtle), 
# Turtle objekt deltagare 
# Turtle screen objekt screen #
def setUp():
    screen = turtle.Screen()
    screen.setup(500,500)

    pelle = turtle.Pen()
    pelle.color("red")
    pelle.shape("turtle")
    pelle.speed(1)

    deltagare = turtle.Pen()
    deltagare.color("blue")
    deltagare.shape("turtle")
    deltagare.speed(1)
    
    return pelle, deltagare, screen

def createMenu():
    antal = 13
    uppgifter = []
    for i in range(antal):
        uppgifter.append("Uppgift:" + str(i))
    return uppgifter

def printMenu(uppgifter):
    for i in uppgifter:
        print("#",i )
    
# Utvecklingsområde: Hitta ett sätt att inte behöva hårdkoda menyn.
def choiceHandler(master, deltagare, screen):
        valdUppgift = input("Uppgift: ")
        resetScreen(screen)
        resetTurtle(master)
        resetTurtle(deltagare)

        if valdUppgift == "1":
            task1(master)
            uppgift1(deltagare)
        elif valdUppgift == "0":
            task0(master)
            uppgift0(deltagare)
        elif valdUppgift == "2":
            task2(master)
            uppgift2(deltagare)
        elif valdUppgift == "3":
            task3(master)
            uppgift3(deltagare)
        elif valdUppgift == "4":
            task4(master)
            uppgift4(deltagare)
        elif valdUppgift == "5":
            task5(master)
            uppgift5(deltagare)
        elif valdUppgift == "6":
            task6(master)
            uppgift6(deltagare)
        elif valdUppgift == "7":
            task7(master)
            uppgift7(deltagare)
        elif valdUppgift == "8":
            task8(master)
            uppgift8(deltagare)
        elif valdUppgift == "9":
            task9(master)
            uppgift9(deltagare)
        elif valdUppgift == "10":
            task10(master)
            uppgift10(deltagare)
        elif valdUppgift == "11":
            task11(master)
            uppgift11(deltagare)
        elif valdUppgift == "12":
            egenUppgift(deltagare)
        elif valdUppgift == "q":
            print("Hejdå!")
            exit()
        else: 
            print("Du måste välja en siffra som finns listad.") 
        
# main 
# skapar turtle objekten som behövs för uppgifterna.
# Skriver ut meddelandet och menyn.
# Hanterar användarens val och exekverar rätt uppgift. 
# Skriv 'q' för att avsluta. #
def main():
    master, deltagare, screen = setUp()
    uppgifter = createMenu()
    print("Hello, World!")
    print("Välkommen till Python turtle! \n \
Det här programmet låter dig köra olika uppgifter. \n \
Du ska efterskapa den röda linjen som målas av datorn \
genom att skriva egen kod i 'deltagare.py' filen.")

    while True:
        print("Välj vilken uppgift du vill köra genom att skriva \
i motsvarande siffra och tryck enter. \
Skriv 'q' för att avsluta")
        
        printMenu(uppgifter)
        choiceHandler(master, deltagare, screen)

main()

