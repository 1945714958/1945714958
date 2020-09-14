import turtle as t
t.pensize(3)
t.bgcolor("black")
colors = ["red","yellow","blue","green","orange","purple"]
t.tracer(6)
for i in range(240):
    t.forward(i)
    t.pencolor(colors[i % 6])
    t.right(59)
t.done()
    
