from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]


def set_up_turtles():
    racers = []
    for color in colors:
        new_turtle = Turtle(shape="turtle")
        new_turtle.color(color)
        new_turtle.penup()
        new_turtle.goto(x=-230, y=-125 + colors.index(color) * 50)
        racers.append(new_turtle)
    return racers


def run_race(racers):
    is_race_on = True
    while is_race_on:
        for racer in racers:
            racer.forward(random.randint(0, 10))
            if racer.xcor() > 220:
                is_race_on = False
                return racer.pencolor()


def ask_play_again(message_title, message_prompt):
    answer = screen.textinput(title=message_title, prompt=message_prompt)
    return (answer or "").strip().lower() == "y"


def race():
    play_again = True

    while play_again:
        screen.clearscreen()
        racers = set_up_turtles()

        user_bet = screen.textinput(
            title="Make your bet",
            prompt="Which turtle will win the race? Enter a color: "
        )

        if not user_bet:
            break

        user_bet = user_bet.strip().lower()
        winning_color = run_race(racers)
        if not winning_color:
            break

        screen.title(f"{winning_color.upper()} WINS!")

        if winning_color == user_bet:
            play_again = ask_play_again(
                "You won!",
                f"You've won! The {winning_color} turtle is the winner! Do you want to play again? (y/n)"
            )
        else:
            play_again = ask_play_again(
                "You lost!",
                f"You've lost! The {winning_color} turtle is the winner! Do you want to play again? (y/n)"
            )

        if not play_again:
            screen.bye()
            return True

    return False


window_closed = race()

if not window_closed:
    screen.exitonclick()
