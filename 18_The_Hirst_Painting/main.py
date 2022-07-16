import turtle

# import colorgram as cg
"""color extraction from an image"""
# colors = cg.extract('spotPainting.jpg', 20)
# print(colors)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     color_list.append(new_color)
#
# print(color_list)

from turtle import Turtle, Screen
import random
turtle.colormode(255)
color_list = [(212, 154, 97), (52, 108, 132), (178, 78, 33), (198, 143, 34), (123, 80, 97),
              (116, 155, 171), (124, 175, 158), (228, 197, 129), (194, 85, 105), (54, 38, 20),
              (12, 51, 65), (189, 123, 142), (54, 120, 115), (41, 169, 126), (167, 21, 31), (225, 94, 78)]
tim = Turtle()

tim.speed("fast")
tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100
for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        # tim.penup()
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

scr = Screen()
scr.exitonclick()
