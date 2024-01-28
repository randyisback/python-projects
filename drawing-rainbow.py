import turtle as t
import colorsys
t.bgcolor('black')
t.speed(0)
hue=0.0




for i in range(390):
	col = colorsys.hsv_to_rgb(hue,1,1)
	t.pencolor(col)
	hue += 0.005
	
	
	
	
	
	
	
	
	
	
	for j in range(2):
		t.forward(i)
		t.right(120)
		t.forward(10)
		t.right(60)
		t.circle(70)
	t.right(181)
	t.tracer(10)
t.hideturtle()
t.done()