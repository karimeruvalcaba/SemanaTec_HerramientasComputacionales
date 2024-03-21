from random import randrange, choice
from turtle import *
from freegames import square, vector

colors = ['blue', 'green', 'yellow', 'purple', 'orange']  # Available colors for snake and food
snake_color = choice(colors)  # Random color for the snake
food_color = choice([color for color in colors if color != snake_color and color != 'red'])  # Random color for the food, different from snake and not red

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)


def change(x, y):
    """Change snake direction."""
    aim.x = x
    aim.y = y


def inside(head):
    """Return True if head inside boundaries."""
    return -200 < head.x < 190 and -200 < head.y < 190


def move_food():
    """Move food randomly within boundaries."""
    food.x += randrange(-10, 11, 10)
    food.y += randrange(-10, 11, 10)

    # Ensure food stays within boundaries
    food.x = max(min(food.x, 190), -200)
    food.y = max(min(food.y, 190), -200)


def move():
    """Move snake forward one segment."""
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')  # Red color for collision
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        move_food()  # Move the food randomly
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, snake_color)  # Snake color
    square(food.x, food.y, 9, food_color)  # Food color
    update()
    ontimer(move, 100)


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
