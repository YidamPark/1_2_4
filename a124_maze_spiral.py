import turtle as trtl

t = trtl.Turtle()
#width
length = 30

#square
t.pensize(5)
t.speed(0)
t.penup()
t.forward(length)
t.pendown()

#maze
for i in range(25):
  t.left(90)
  t.forward(length)
  length = length + 15
t.hideturtle()



wn = trtl.Screen()
wn.mainloop()