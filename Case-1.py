# Case-study #1
# Developers: Komissarov P., Tropin T., Shevchenko A., Greshnova S.
#

import turtle as t
import math as m

def red_triangle(x, y, a, angle): 

# x - x-coordinate 
# y - y-coordinate
# a - catheter length
# angle - slope angle

    t.fillcolor("red")
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    t.setheading(angle)
    t.right(45)
    t.forward(a)
    t.left(90)
    t.forward(a)
    t.goto(x, y)
    t.setheading(0)
    t.end_fill()

def yellow_triangle(x, y, a, angle):
    t.fillcolor("yellow")
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    t.setheading(angle)
    t.right(45)
    t.forward(a)
    t.right(90)
    t.forward(a)
    t.goto(x, y)
    t.setheading(0)
    t.end_fill()

def green_rhomb(x, y, a, angle):

# a - side lengths

    t.fillcolor("green")
    t.penup()
    t.goto(x, y)
    t.pendown()  
    t.begin_fill()
    t.setheading(angle) 
    t.left(45)  
    for _ in range(4): 
       t.forward(a)
       t.right(90)
    t.setheading(0)
    t.end_fill()
    
def purple_parallelogram(x, y, a, angle):

# a - length of the larger side

    t.fillcolor("purple")
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    t.setheading(angle)
    for i in range(2):
        t.forward(a)
        t.left(45)
        t.forward(a*(m.sqrt(2)/2))
        t.left(135)
    t.goto(x,y)
    t.setheading(0)
    t.end_fill()

def pink_triangle(x, y, a, angle):
    t.fillcolor("pink")
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    t.setheading(angle)
    t.left(45)
    t.forward(a)
    t.right(90)
    t.forward(a)
    t.goto(x, y)
    t.setheading(0)
    t.end_fill()

def blue_triangle(x, y, a, angle):
    t.fillcolor("blue")
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    t.setheading(angle)
    t.left(135)
    t.forward(a)
    t.right(90)
    t.forward(a)
    t.goto(x, y)
    t.setheading(0)
    t.end_fill()

def orange_triangle(x, y, a, angle):
    t.fillcolor("orange")
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    t.setheading(angle)
    t.forward(a)
    t.left(90)
    t.forward(a)
    t.goto(x, y)
    t.setheading(0)
    t.end_fill()

def main():
    t.pensize(3)
    t.pencolor("white")
    t.tracer(0)
    def square():
        red_triangle(-100, 100, m.sqrt(20000), 0)
        yellow_triangle(-100, 100, m.sqrt(20000), 0)
        orange_triangle(0, -100, 100, 0)
        blue_triangle(100, 0, m.sqrt(5000), 0)
        green_rhomb(0, 0, m.sqrt(5000), 0)
        pink_triangle(-50, -50, m.sqrt(5000), 0)
        purple_parallelogram(-100, -100, 100, 0)
    square()
    def helicopter():
        orange_triangle(30, -170, m.sqrt(3000), 135)
        purple_parallelogram(30, -170, 50, 0)
        yellow_triangle(30, -270, m.sqrt(5000), 180)
        red_triangle(30, -270, m.sqrt(5000), 90)
        blue_triangle(-45, -245, m.sqrt(1250), -90)
        pink_triangle(-20, -220, m.sqrt(1250), 180)
        green_rhomb(-53, -207, 37, 180)
    helicopter()
    def man_left():
        yellow_triangle(-190, 20, m.sqrt(5000), -45)
        red_triangle(-150, 60, m.sqrt(5000), -135)
        purple_parallelogram(-255.9, -10, 50, 45)
        green_rhomb(-225, 81, 30, 0)
        orange_triangle(-190, -90, 48, 45)
        blue_triangle(-190, -105, 30, 0)
        pink_triangle(-280, -70, 30, 45)
    man_left()
    def rabbit():
        blue_triangle(-150, 110, m.sqrt(1250), 45)
        orange_triangle(-232, 110, 48, 0)
        yellow_triangle(-232, 110, m.sqrt(5000), -225)
        red_triangle(-232, 180, m.sqrt(5000), 45)
        pink_triangle(-161, 200, m.sqrt(1250), -90)
        green_rhomb(-161, 235, m.sqrt(1250), 45)
        purple_parallelogram(-140, 270, 50, 135)
    rabbit()
    def boat():
       blue_triangle(-172, -145, 40, 45)
       yellow_triangle(-212, -160, m.sqrt(5000), -45)
       red_triangle(-212, -245, m.sqrt(5000), 90)
       pink_triangle(-212, -245, 35, 0)
       green_rhomb(-187, -220, 35, 0)
       orange_triangle(-237, -245, 55, -45)
       purple_parallelogram(-274, -245, 54, -45)
    boat()
    def cock():
        purple_parallelogram(167, 167, 40, 90)
        red_triangle(196, 171, 52, 135)
        blue_triangle(146, 223, 38, 270)
        yellow_triangle(196, 149, 45, 135)
        green_rhomb(212, 194, 25, 45)
        pink_triangle(211, 218, 26, 0)
        orange_triangle(226, 180, 27, 225)
    cock()
    def rocket():
        pink_triangle(164, -130, 30, 0)
        blue_triangle(165, -130, 40, -135)
        yellow_triangle(165, -130, 57, 0)
        red_triangle(205, -170, 57, -90)
        green_rhomb(148, -230, 26, 0)
        orange_triangle(148, -266, 26, 45)
        purple_parallelogram(224, -267, 38, 90)
    rocket()
    def man_right():
        green_rhomb(165, 81, 30, 0)
        red_triangle(184,-8, 67, 135)
        yellow_triangle(186,-8, 67, 135)
        blue_triangle(225,-43, 40, 45)
        purple_parallelogram(184, -5, 38, 225)
        pink_triangle(172,-44, 30, 225)
        orange_triangle(232, -73, 30, 90)
    man_right()
    def fish():
        blue_triangle(-35, 210, 40, 135)
        pink_triangle(-35, 168, 40, 45)
        purple_parallelogram(3, 208, 52, 135)
        green_rhomb(2, 206, 37, 0)
        yellow_triangle(54, 206, m.sqrt(5000), -45)
        red_triangle(54, 206, m.sqrt(5000), 135)
        orange_triangle(55, 160, m.sqrt(5000), 45)
    fish()
    t.hideturtle()
    t.done()
main()
