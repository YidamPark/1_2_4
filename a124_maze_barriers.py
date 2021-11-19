import turtle as trtl

t = trtl.Turtle()
#length
length = 40
#pathwidth
path_width = 20

#square
t.pensize(5)
t.speed(0)
t.penup()
t.forward(length)
t.pendown()

#maze
for i in range(25):
  t.left(90)

  #doors
  t.forward(10)
  t.penup()
  t.forward(path_width)
  t.pendown()

  #barriers
  t.forward(40)
  t.right(90)
  t.forward(path_width*2)
  t.back(path_width*2)
  t.left(90)
  t.forward(length-40)
  length = length + 20
t.hideturtle()




wn = trtl.Screen()
wn.mainloop()