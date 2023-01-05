from tkinter import *
import random

window = Tk()
window.title("I am don")
window.resizable(0, 0)

Label(window, text='I am don', font='arial 20 bold').pack(side=BOTTOM)  # footer

score = 0
direction = 'right'

GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED = 180
SPACE_SIZE = 50
BODY_PARTS = 2
SNAKE_COLOR = '#00FF00'
FOOD_COLOR = '#FF0000'
BACKGROUND_COLOR = '#000000'

label = Label(window, text="Score:{}".format(score), font=('consolas', 40))
label.pack()

canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()


class Snake:
    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []

        for i in range(0, BODY_PARTS):
            self.coordinates.append([0, 0])

        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag="snake")
            self.squares.append(square)


class Food:
    def __init__(self):
        x = random.randint(0, (GAME_WIDTH / SPACE_SIZE) - 1) * SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT / SPACE_SIZE) - 1) * SPACE_SIZE

        self.coordinates = [x, y]
        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag='food')


def next_turn(snake, food):
    x, y = snake.coordinates[0]

    if direction == 'up' or direction == 'w':
        y -= SPACE_SIZE
    elif direction == 'down' or direction == 's':
        y += SPACE_SIZE
    elif direction == 'left' or direction == 'a':
        x -= SPACE_SIZE
    elif direction == 'right' or direction == 'd':
        x += SPACE_SIZE

    snake.coordinates.insert(0, (x, y))
    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)
    snake.squares.insert(0, square)

    if x == food.coordinates[0] and y == food.coordinates[1]:
        global score

        score += 1

        label.config(text='Score:{}'.format(score))
        canvas.delete("food")
        food = Food()
    else:
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]

    if check_collision(snake):
        game_over()
    else:
        window.after(SPEED, next_turn, snake, food)


def change_direction(new_direction):
    global direction

    if new_direction == 'left' or new_direction == 'a':
        if direction != 'right' or new_direction != 'd':
            direction = new_direction
    elif new_direction == 'right' or new_direction == 'd':
        if direction != 'left' or new_direction != 'a':
            direction = new_direction
    elif new_direction == 'up' or new_direction == 'w':
        if direction != 'down' or direction != 's':
            direction = new_direction
    elif new_direction == 'down' or new_direction == 's':
        if direction != 'up' or new_direction != 'w':
            direction = new_direction


def check_collision(snake):
    x, y = snake.coordinates[0]
    if x < 0 or x >= GAME_WIDTH:
        return True
    elif y < 0 or y >= GAME_HEIGHT:
        return True

    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            return True

    return False


def game_over():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width() / 2,
                       canvas.winfo_height() / 2,
                       font=('consolas', 70),
                       text='GAME_OVER',
                       fill='red',
                       tag="gameover")


window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")

window.bind('<Left>', lambda event: change_direction('left'))
window.bind('<a>', lambda event: change_direction('a'))
window.bind('<Right>', lambda event: change_direction('right'))
window.bind('<d>', lambda event: change_direction('d'))
window.bind('<Up>', lambda event: change_direction('up'))
window.bind('<w>', lambda event: change_direction('w'))
window.bind('<Down>', lambda event: change_direction('down'))
window.bind('<s>', lambda event: change_direction('s'))

snake = Snake()
food = Food()

next_turn(snake, food)

window.mainloop()
