import turtle as t
t.bgcolor('black')
color = ('teal','crimson')

for i in range(180):
    t.speed(0)
    t.pencolor(color[i%2])
    t.fillcolor(color[i%2])
    t.begin_fill()
    t.forward(i)
    t.right(12)
    t.circle(50,20)
    t.forward(i)
    t.right(30)
    t.left(30)
    t.circle(20,30)
    t.right(30)
    t.backward(i)
    t.left(400)
    
    
    for j in range(170):
        t.speed(0)
        t.pencolor(color[j%2])
        t.fillcolor(color[j%2])
        t.begin_fill()
        t.forward(j)
        t.right(22)
        t.circle(50,20)
        t.forward(j)
        t.right(40)
        t.left(30) 
        t.circle(20,30)
        t.right(40)
        t.backward(j)
        t.left(500)
t.end_fill()
t.done()