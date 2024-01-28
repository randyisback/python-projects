from turtle import *
bgcolor('black')
speed(90)
hideturtle()
pensize(3)
a = 0
colors = ['green','red','yellow']
while a<180:
	pencolor(colors[a%3])
	left (245)
	forward(a*1)
	a = a+1
	forward(a*1)