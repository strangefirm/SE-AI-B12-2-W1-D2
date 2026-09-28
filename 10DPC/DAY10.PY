import tkinter as tk
import random

CELL_SIZE = 20
COLUMNS = 30
ROWS = 20
WIDTH = CELL_SIZE * COLUMNS
HEIGHT = CELL_SIZE * ROWS

window = tk.Tk()
window.title("Snake Game")
window.resizable(False, False)

score = 0
snake = []
direction = (1, 0)
food = None
running = True

score_label = tk.Label(window, text="Score: 0", font=("Arial", 16))
score_label.pack(pady=5)

canvas = tk.Canvas(window, width=WIDTH, height=HEIGHT, bg="black")
canvas.pack()

message_label = tk.Label(window, text="Use the arrow keys to move.", font=("Arial", 12))
message_label.pack(pady=5)


def place_food():
    empty_cells = [
        (x, y)
        for x in range(COLUMNS)
        for y in range(ROWS)
        if (x, y) not in snake
    ]
    return random.choice(empty_cells) if empty_cells else None


def draw():
    canvas.delete("all")

    if food:
        x, y = food
        canvas.create_rectangle(
            x * CELL_SIZE, y * CELL_SIZE,
            (x + 1) * CELL_SIZE, (y + 1) * CELL_SIZE,
            fill="red", outline="red"
        )

    for x, y in snake:
        canvas.create_rectangle(
            x * CELL_SIZE, y * CELL_SIZE,
            (x + 1) * CELL_SIZE, (y + 1) * CELL_SIZE,
            fill="lime green", outline="black"
        )


def change_direction(event):
    global direction

    new_direction = {
        "Up": (0, -1),
        "Down": (0, 1),
        "Left": (-1, 0),
        "Right": (1, 0),
    }.get(event.keysym)

    if new_direction and new_direction != (-direction[0], -direction[1]):
        direction = new_direction


def move_snake():
    global food, score, running

    if not running:
        return

    head_x, head_y = snake[0]
    new_head = (head_x + direction[0], head_y + direction[1])

    if (
        new_head[0] < 0 or new_head[0] >= COLUMNS
        or new_head[1] < 0 or new_head[1] >= ROWS
        or new_head in snake
    ):
        running = False
        message_label.config(text="Game over! Click Restart to play again.")
        return

    snake.insert(0, new_head)

    if new_head == food:
        score += 1
        score_label.config(text=f"Score: {score}")
        food = place_food()

        if food is None:
            running = False
            message_label.config(text="You win! Click Restart to play again.")
    else:
        snake.pop()

    draw()

    if running:
        window.after(120, move_snake)


def restart_game():
    global score, snake, direction, food, running

    score = 0
    snake = [(10, 10), (9, 10), (8, 10)]
    direction = (1, 0)
    food = place_food()
    running = True

    score_label.config(text="Score: 0")
    message_label.config(text="Use the arrow keys to move.")
    draw()
    window.after(120, move_snake)


window.bind_all("<Key>", change_direction)

restart_button = tk.Button(window, text="Restart", command=restart_game)
restart_button.pack(pady=5)

restart_game()
window.mainloop()