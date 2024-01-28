from turtle import *
bgcolor('black')
pensize(4)
color = ('red','green','yellow','green','pink','powderblue')

for i in range(500):
    tracer(20)
    forward(i)
    left(50)
    pencolor(color[i%6])
    speed(0)
    i = 0
    i = i * 0.3
    i = i + 1