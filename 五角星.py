import turtle as t
t.hideturtle()
t.pu()
t.goto(-100,-100)
t.pd()
t.seth(72)
t.fd(250)
t.bgcolor("red")
t.fillcolor("yellow")
t.begin_fill()
for i in range(4):
    t.right(144)
    t.fd(250)

t.end_fill()
t.done()
