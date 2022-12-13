import turtle
import random

tim = turtle.Turtle()
my_sreen = turtle.Screen()
turtle.colormode(255)



colors_list = [(212, 154, 97), (239, 246, 243), (52, 108, 132), (178, 78, 33), (198, 143, 34), (123, 80, 97), (235, 240, 244),
 (116, 155, 171), (124, 175, 158), (228, 197, 129), (194, 85, 105), (54, 38, 20), (12, 51, 65), (189, 123, 142), (54, 120, 115),
  (41, 169, 126), (167, 21, 31), (225, 94, 78), (4, 30, 28), (39, 32, 34), (243, 163, 159), (81, 148, 168), (164, 27, 22),
   (239, 163, 167), (104, 123, 159), (164, 209, 193), (21, 81, 93), (29, 85, 81), (162, 206, 212), (53, 62, 81), (183, 190, 206), 
   (85, 74, 35)]

tim.speed('fastest')
tim.setheading(225)
tim.penup()
tim.forward(250)
tim.pendown()
tim.setheading(0)


for j in range(10):
    for i in range(10):
        tim.pendown()
        tim.dot(20, random.choice(colors_list))
        tim.penup()
        tim.forward(50)
    tim.setheading(90)
    tim.forward(50)
    tim.setheading(180)
    tim.forward(500)
    tim.setheading(0)











my_sreen.exitonclick()