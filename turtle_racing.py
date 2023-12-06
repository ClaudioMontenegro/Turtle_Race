from turtle import Turtle, Screen
import random
screen = Screen()
screen.setup(width=500, height=400)

rainbow_colors = ["red", "orange", "yellow", "green", "blue", "purple"]


def turtle_factory():
    turtle_list = []
    for n in range(0, len(rainbow_colors)):
        tim = Turtle(shape="turtle")
        tim.color(rainbow_colors[n])
        turtle_list.append(tim)
    return turtle_list


def turtle_run(turtle_list, bet):
    y = -150
    x = -230
    is_on = True
    for t in turtle_list:
        t.penup()
        t.goto(x=x, y=y)
        y += 50
    while is_on:
        for t in turtle_list:
            if t.xcor() >= 220:
                is_on = False
                result = t.pencolor()
                if result == bet:
                    print(f"You've won! The {result} turtle is the winner!")
                else:
                    print(f"You've lost. The {result} turtle is the winner!")
            else:
                t.forward(random.randint(0, 10))


def turtle_racing():
    screen = Screen()
    screen.setup(width=500, height=400)
    user_bet = screen.textinput(title="Make your bet",
                                prompt='Which turtle will win the race? Enter a color: ').lower()
    turtle_run(turtle_factory(), user_bet)
    screen.exitonclick()
