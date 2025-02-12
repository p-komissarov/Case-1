# Case-study #1
# Developers: Komissarov P., Shevchenko A., Greshnova S., Tropin T.
#

import turtle as t

def redtriangle(x, y):
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
    t.right(45)
    t.end_fill()

def yellowtriangle(x, y, a):
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
    t.right(90)
    t.right(135)
    t.end_fill()

def main():
    t.speed(3)
    t.pensize(5)
    t.pencolor("white")

# Вместо этого текста вписывайте название функции которую создаёте типа redtriangle(200, 200, 100) вместе со значениями координат и прочего чтобы запустить

    t.done()

main()