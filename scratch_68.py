import turtle
t=turtle.Turtle()
t.speed(0)
turtle.bgcolor("black")
t.color("red")
t.goto(-120,0)
for i in range(100):
    for j in range(2):
        t.fd(i)
        t.rt(20)
        t.lt(50)
        t.circle(120,180)
    t.rt(120)
turtle.done()
