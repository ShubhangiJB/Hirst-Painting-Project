import random
from turtle import Screen, Turtle

import colorgram

screen = Screen()
screen.colormode(255)

timmy = Turtle()

timmy.hideturtle()
timmy.up()
timmy.goto(-190, 140)

colors = colorgram.extract('hirst-spots.jpg', 30)
rgb = []
for n in range(len(colors)):
  rgb.append(colors[n].rgb)

n = 1
for n in range(1,10):
  for _ in range(10):
    timmy.dot(20, random.choice(rgb))
    timmy.forward(50)
  timmy.goto(-190, 140-50*n)

timmy.speed("fastest")
screen.exitonclick()
