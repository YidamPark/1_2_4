import turtle as trtl

t = trtl.Turtle()
#length
length = 40
#pathwidth
path_width = 10

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
  t.forward(path_width*2)
  t.pendown()
  t.forward(length-10)
  length = length + 20
  t.hideturtle()




wn = trtl.Screen()
wn.mainloop()