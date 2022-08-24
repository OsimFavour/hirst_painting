import turtle as turtle_module
import random

turtle_module.colormode(255)
screen = turtle_module.Screen()
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
screen.setup(width=660, height=600)

color_list = [(253, 251, 249), (253, 250, 253), (249, 250, 252), (236, 248, 243), (36, 95, 183), (236, 165, 79),
        (244, 223, 87), (215, 69, 105), (98, 197, 234), (250, 51, 22), (203, 70, 21), (240, 106, 143),
        (185, 47, 90), (143, 233, 216), (252, 136, 166), (165, 175, 233), (66, 45, 13), (72, 205, 170),
        (83, 187, 100), (20, 156, 51), (24, 36, 86), (252, 220, 0), (164, 28, 8), (105, 39, 44), (250, 152, 2),
        (22, 151, 229), (108, 213, 249), (254, 12, 3), (38, 48, 98), (98, 96, 186)]

tim.setheading(221)
tim.forward(430)
tim.setheading(0)
number_of_dots = 6150

for dot_count in range(1, number_of_dots + 1):
	tim.dot(6, random.choice(color_list))
	tim.forward(8)

	if dot_count % 82 == 0:
		tim.setheading(90)
		tim.forward(8)
		tim.setheading(180)
		tim.forward(656)
		tim.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()
