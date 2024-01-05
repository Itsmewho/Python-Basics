from turtle import Turtle, Screen
import random

t = Turtle()
screen = Screen()
screen.title("Welcome to my turtle run")
t.screen.bgcolor("black")
t.color("red")

# Draw some shapes:

# def draw_shapes(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         t.forward(100)
#         t.right(angle)


# for shape_side_n in range(3,11):
#     t.color(random.choice(colours))
#     draw_shapes(shape_side_n)


# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     random_color = (r, g, b)
#     return random_color


# def do_the_walk():
#     directions = [0, 90, 180, 270]
#     for _ in range(200):
#         t.pensize(2)
#         t.color(random_color)
#         t.forward(50)
#         t.setheading(random.choice(directions))


# do_the_walk()

import turtle as t


tim = t.Turtle()
t.colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

draw_spirograph(5)