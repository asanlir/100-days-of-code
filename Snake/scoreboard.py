from turtle import Turtle
from pathlib import Path

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.data_file = Path(__file__).with_name("data.txt")
        if self.data_file.exists():
            with open(self.data_file, encoding="utf-8") as data:
                self.highscore = int(data.read() or 0)
        else:
            self.highscore = 0
            with open(self.data_file, "w", encoding="utf-8") as data:
                data.write("0")
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(
            f"Score: {self.score}  High Score: {self.highscore}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open(self.data_file, "w", encoding="utf-8") as data:
                data.write(f"{self.highscore}")
        self.score = 0
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
