# Case-study #1
# Developers: Komissarov P., Shevchenko A., Greshnova S., Tropin T.
#

import turtle as t

def red_triangle(x, y, a):
    t.fillcolor("red")
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    t.right(45)
    t.forward(a)
    t.left(90)
    t.forward(a)
    t.goto(x, y)
    t.setheading(90)
    t.end_fill()

def yellow_triangle(x, y, a):
    t.fillcolor("yellow")
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    t.right(45)
    t.forward(a)
    t.right(90)
    t.forward(a)
    t.goto(x, y)
    t.setheading(90)
    t.end_fill()

def green_rhomb(x, y, a):
    t.fillcolor("green")
    t.penup()
    t.goto(x, y)
    t.pendown()  
    t.begin_fill() 
    t.left(45)  
    for _ in range(4): 
       t.forward(a)
       t.left(90)
    t.setheading(90)
    t.end_fill()
    
def purple_parallelogram(x, y, a):
    t.fillcolor("purple")
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    for i in range(2):
        t.forward(2*a)
        t.left(60)
        t.forward(a)
        t.left(120)
    t.goto(x,y)
    t.end_fill()

def pink_triangle(x, y, a):
    t.fillcolor("pink")
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    t.left(45)
    t.forward(a)
    t.right(90)
    t.forward(a)
    t.goto(x, y)
    t.setheading(0)
    t.end_fill()

def blue_triangle(x, y, a):
    t.fillcolor("blue")
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    t.left(135)
    t.forward(a)
    t.right(90)
    t.forward(a)
    t.goto(x, y)
    t.setheading(0)
    t.end_fill()

def orange_triangle(x, y, a):
    t.fillcolor("orange")
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    t.forward(a)
    t.left(90)
    t.forward(a)
    t.goto(x, y)
    t.setheading(0)
    t.end_fill()

def main():
    t.speed(3)
    t.pensize(5)
    t.pencolor("white")

# Вместо этого текста вписывайте название функции которую создаёте типа redtriangle(200, 200, 100) вместе со значениями координат и прочего чтобы запустить

    t.done()

main()
