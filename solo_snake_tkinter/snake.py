from tkinter import *
from random import (choice)

SIZE = 30
KEY = str("")
EX, EY = 0, 0
DELAY = 100
SNAKE = []
COORD = []
score = 0


class Game:
    def __init__(self):

        self.window = Tk()
        self.window.wm_title("I am don")
        self.window.geometry("600x600+400+100")
        self.window.bind("<KeyPress>", self.keypress)
        self.frame = Frame(self.window)
        self.highScore = 0
        self.frame.pack(side="top", fill="x")
        self.right_score_label = Label(self.frame, text=f"High Score: {self.highScore}", font=("Arial", 20, "bold"))
        self.right_score_label.pack(side="right")
        self.left_score_label = Label(self.frame, text=f"Score: {score}", font=("Arial", 20, "bold"))
        self.left_score_label.pack(side="left")

        Label(self.window, text='Press arrows key or WASD to move', font='arial 20 bold').pack(side=BOTTOM)
        self.map()

    def map(self):
        self.mapa = Frame(
            self.window, width=500, height=500, bg="#47C65E"
        )
        self.mapa.pack(expand=True, padx=10, pady=10)
        self.snake()
        self.place()
        self.food()
        self.loop()

    def keypress(self, key):
        global KEY
        KEY = key.keysym

    def move(self):
        global EX, EY
        if KEY == "Right" or KEY == "d":
            EX = EX + SIZE
        elif KEY == "Left" or KEY == "a":
            EX = EX - SIZE
        elif KEY == "Up" or KEY == "w":
            EY = EY - SIZE
        elif KEY == "Down" or KEY == "s":
            EY = EY + SIZE
        self.cobra.place(x=EX, y=EY)

    def snake(self):
        self.cobra = Frame(
            self.mapa, width=SIZE, height=SIZE, bg="purple"
        )
        self.cobra.place(x=0, y=0)

    def place(self):
        lis = []
        for k in range(0, 500 - SIZE, SIZE):
            lis.append(k)
        self.x = choice(lis)
        self.y = choice(lis)

    def food(self):
        color = [
            "white", "gray", "black",
            "pink", "blue", "purple",
            "red", "violet", "yellow",
            "yellow", "orange", "pink",
            "#9900ff", "#cccc00", "#33bbff",
            "#4d4d00", "#ff80b3", "#77b300"
        ]
        self.fruit = Frame(
            self.mapa, width=SIZE, height=SIZE, bg=choice(color)
        )
        self.fruit.place(x=self.x, y=self.y)

    def collision(self):
        global score
        if EX < 0 or EX > 500 - SIZE:
            return "outOfBound"
        if EY < 0 or EY > 500 - SIZE:
            return "outOfBound"
        if EX == self.x and EY == self.y:
            score += 5
            if score > self.highScore:
                self.highScore += 5
            self.left_score_label.configure(text=f"Score: {score}")
            self.right_score_label.configure(text=f"High Score: {self.highScore}")
            return "foodEaten"
        tup = tuple((EX, EY))
        if tup in COORD:
            return "selfDamage"

    def game_over(self):
        self.text = Label(
            self.mapa, fg="#A62205", text="Game Over",
            font=("Arial", 50, "bold"), bg="#47C65E"
        )
        self.points = Label(
            self.mapa, fg="black", text="Points: " +
                                       str(len(SNAKE) * 5) + "\nSize: " + str(len(SNAKE)),
            font=("Arial", 30, "bold"), bg="#47C65E",
        )
        self.bt = Button(
            self.mapa, text="Play again", relief="flat",
            cursor="exchange", font=("Arial", 20, "bold"),
            fg="black", bg="#CE571C", command=self.clear
        )

        self.text.place(relx=0.15, rely=0.1)
        self.points.place(relx=0.35, rely=0.3)
        self.bt.place(relx=0.35, rely=0.5)

    def clear(self):
        global EX, EY, SNAKE, COORD, KEY, score
        EX, EY, KEY, score = 0, 0, "", 0
        SNAKE, COORD = [], []
        for k in [
            self.mapa, self.fruit,
            self.text, self.points,
            self.cobra
        ]:
            k.destroy()
        self.left_score_label.configure(text=f"Score: {score}")
        self.map()
        return

    def loop(self):
        global SNAKE, COORD
        collision = self.collision()
        if collision == "outOfBound":
            self.game_over()
            return
        if collision == "foodEaten":
            self.fruit.destroy()
            self.place()
            self.food()
            SNAKE.append(Frame(self.mapa, width=SIZE, height=SIZE, bg=str(self.fruit['bg'])))
        if collision == "selfDamage":
            self.game_over()
            return

        COORD.append((EX, EY))
        if len(COORD) > len(SNAKE):
            del (COORD[0])

        length = len(SNAKE)
        for self.k in SNAKE:
            self.k.place(x=COORD[-length][0], y=COORD[-length][1])
            length = length - 1

        self.move()
        self.window.after(DELAY, self.loop)

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    snake = Game()
    snake.run()
