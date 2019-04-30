import turtle as t 
def DegreeCurve(n, r, d = 1):
    for i in range(n):
        t.left(d)
        t.circle(r, abs(d))

s = 0.2 
t.setup(450 * 5 * s, 750 * 5 * s)
t.pencolor("black")
t.fillcolor("red")
t.speed(100) 
t.penup()
t.goto(0, 900 * s)
t.pendown()

t.begin_fill()
t.circle(200 * s, 30)
