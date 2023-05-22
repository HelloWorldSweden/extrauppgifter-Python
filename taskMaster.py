''' Skriven av Jenny Böjeryd Maj 2023'''

import turtle 
import math

# Hallå!
# Kul att du hittade hit! Här ska du egentligen inte vara,
# snälla rör rör ingenting av koden :)) ##

def task0(pelle):
    pelle.forward(100)

def task1(pelle):
    pelle.left(90)
    pelle.forward(250)

def task2(pelle):
    pelle.left(90)
    pelle.forward(250)
    pelle.right(90)
    pelle.forward(250)
    pelle.right(90)
    pelle.forward(50)

def task3(pelle):
    pelle.forward(50)
    pelle.left(90)
    pelle.forward(100)
    pelle.right(90)
    pelle.forward(100)
    pelle.left(90)
    pelle.forward(200)

def task4(pelle):
    pelle.forward(50)
    pelle.left(45)
    pelle.forward(math.sqrt(5000))
    pelle.right(45)
    pelle.forward(100)
    pelle.left(135)
    pelle.forward(math.sqrt(5000)*3)

def task5(pelle):
    for j in range(4):
        for i in range(5):
            pelle.forward(50)
        pelle.left(90)


def task6(pelle):
    pelle.up()
    pelle.forward(200)
    pelle.left(90)
    pelle.forward(200)
    pelle.down()
    for i in range(4):
        pelle.right(90)
        pelle.forward(200)
    

def task7(pelle):
    for i in range(2):
        pelle.forward(400)
        pelle.left(90)
    pelle.setheading(-135)
    pelle.forward(math.sqrt(80000))
    pelle.setheading(180)
    pelle.forward(200)
    pelle.setheading(90)
    pelle.forward(200)

def task8(pelle):
    pelle.up()
    pelle.forward(200)
    pelle.left(90)
    pelle.forward(200)
    pelle.left(90)
    pelle.down()
    for j in range(9):
        for i in range(2):
            pelle.forward(50*j)
            pelle.right(90)
        pelle.speed(j)
    pelle.forward(400)

def task9(pelle):
    
    for i in range(8):
        pelle.setheading(i*180)
        pelle.forward(400)
        pelle.setheading(90)
        pelle.forward(50)
        pelle.speed(i+1)
    pelle.setheading(0)    
    pelle.forward(400)

def task10(pelle):
    pelle.up()
    pelle.forward(200)
    pelle.left(90)
    pelle.forward(400)
    pelle.setheading(0)
    pelle.down()
    pelle.speed(4)
    for i in range(360):
        pelle.forward(400/360 * math.pi)
        pelle.right(1)

def task11(pelle):
    pelle.up()
    pelle.forward(200)
    pelle.left(90)
    pelle.forward(400)
    pelle.setheading(0)
    pelle.right(360/5)
    pelle.down()
    for i in range(5):
        pelle.forward(-400/math.cos(360/5))
        pelle.left(3*360/5)