#PythonDraw.py
import turtle      # import ...   from ... import ...  from ... import *   import ... as ...
turtle.setup(650, 350, 200, 200)  # (width, height, startx, starty)    goto()   
turtle.penup()
turtle.fd(-250)     # forward(d) +/- fd(d) 
turtle.pendown()     # penup() pendown() pu() pd()
turtle.pensize(25)    # pensize(width)
turtle.pencolor("purple")     # colormode(1.0/255)  pencolor(color) pencolor(0.63, 0.13, 0.94)
turtle.seth(-40)     # seth(angle)   absolute    left(angle)  right(angle)  relative
for i in range(4):   # range(N) 0 ~ N - 1   range(M, N) M ~ N -1
    turtle.circle(40, 80)     # circle(r, angle = 360)
    turtle.circle(-40, 80)
turtle.circle(40, 80/2)
turtle.fd(40)
turtle.circle(16, 180)
turtle.fd(40 * 2/3)
turtle.done()