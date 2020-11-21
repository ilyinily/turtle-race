from turtle import Turtle, Screen
import random

screen = Screen()

# Let us create the contestants.
turtles = []
colors = ["red", "orange", "yellow", "green", "blue", "violet"]
for i in range(len(colors)):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    turtles.append(new_turtle)

# Now, placing the contestants.
for i in range(len(turtles)):
    turtles[i].penup()
    turtles[i].goto(-330, -(30 * (len(turtles) - 1) / 2) + i * 30)

# Now, let us ensure the contestants move.
finish_not_reached = True
winner = ""
while finish_not_reached:
    for i in range(len(turtles)):
        turtles[i].forward(random.randint(1, 10))
        if turtles[i].position()[0] >= 130:
            finish_not_reached = False
            winner = turtles[i].color()
            turtles[i].goto(-150, 150)
            turtles[i].write(f"And the winner is me, {winner[0]} turtle! Hooray!", font=("Verdana", 10, "bold"))


screen.exitonclick()
