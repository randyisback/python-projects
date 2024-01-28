from turtle import *
colors = ['pink','purple','red','white','gold','powderblue']
colors2 = ['pink','skyblue']
bgcolor('black')

for x in range (30):
		pencolor(colors[x%6])
		width (x/230+8)
		forward(270)
		left(150)
		speed(0)
		
for x in range (40):
		pencolor(colors2[x%2])
		width (x/180+65)
		forward(200)
		right(250)
		speed(0)