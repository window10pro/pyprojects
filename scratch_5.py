import turtle as t
t.bgcolor('black')
t.setup(1537,865)
t.tracer(10)
t.pencolor('black')
t.width(2)
color=('red','orange','purple')
for i in range(2000):
    t.fillcolor(color[i%3])
    t.begin_fill()
    t.fd(i)
    t.rt(270)
    t.fd(i)
    t.fd(i)
    t.rt(270)
    t.circle(111,90)
    t.fd(i)
    t.rt(90)
    t.end_fill()
t.done()
