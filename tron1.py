from turtle import Turtle, Screen

screen = Screen()
screen.bgcolor('black')

def up(who):
    global previousMove

    turtle, path = players[who]
    turtle.setheading(90)

    if previousMove != 'up':
        path.append(turtle.position())
    previousMove = 'up'

    turtle.fd(15)

    if checkCollision(turtle.position(), path, players[1 - who][PATH]):
        collision(turtle)

def right(who):
    global previousMove

    turtle, path = players[who]
    turtle.setheading(0)

    if previousMove != 'right':
        path.append(turtle.position())
    previousMove = 'right'

    turtle.fd(15)

    if checkCollision(turtle.position(), path, players[1 - who][PATH]):
        collision(turtle)

def left(who):
    global previousMove

    turtle, path = players[who]
    turtle.setheading(180)

    if previousMove != 'left':
        path.append(turtle.position())
    previousMove = 'left'

    turtle.fd(15)

    if checkCollision(turtle.position(), path, players[1 - who][PATH]):
        collision(turtle)

def down(who):
    global previousMove

    turtle, path = players[who]
    turtle.setheading(270)

    if previousMove != 'down':
        path.append(turtle.position())
    previousMove = 'down'

    turtle.fd(15)

    if checkCollision(turtle.position(), path, players[1 - who][PATH]):
        collision(turtle)

def collision(turtle):
    for key in ('Up', 'Left', 'Right', 'Down', 'w', 'a', 'd', 'x'):
        screen.onkey(None, key)  # disable game
    turtle.clear()  # remove the loser from the board!

def checkCollision(position, path1, path2):
    if len(path1) > 1:

        A, B = position, path1[-1]  # only check most recent line segment

        if len(path1) > 3:  # check for self intersection
            for i in range(len(path1) - 3):
                C, D = path1[i:i + 2]

                if intersect(A, B, C, D):
                    return True

        if len(path2) > 1:  # check for intersection with other turtle's path
            for i in range(len(path2) - 1):
                C, D = path2[i:i + 2]

                if intersect(A, B, C, D):
                    return True
    return False

X, Y = 0, 1

def ccw(A, B, C):
    """ https://stackoverflow.com/a/9997374/5771269 """
    return (C[Y] - A[Y]) * (B[X] - A[X]) > (B[Y] - A[Y]) * (C[X] - A[X])

def intersect(A, B, C, D):
    """ Return true if line segments AB and CD intersect """
    return ccw(A, C, D) != ccw(B, C, D) and ccw(A, B, C) != ccw(A, B, D)

player = Turtle('circle')
player.shapesize(6 / 20)
player.color('red')
player.pensize(6)
player.speed('fastest')
player.penup()
player.setposition(100, 100)
player.pendown()

enemy = Turtle('circle')
enemy.shapesize(6 / 20)
enemy.color('blue')
enemy.pensize(6)
enemy.speed('fastest')
enemy.penup()
enemy.setposition(-300, -300)
enemy.pendown()

players = [[player, [player.position()]], [enemy, [enemy.position()]]]
PLAYER, ENEMY = 0, 1
TURTLE, PATH = 0, 1

previousMove = None  # consolidate moves in same direction into single line segment

screen.onkey(lambda: up(PLAYER), 'Up')
screen.onkey(lambda: left(PLAYER), 'Left')
screen.onkey(lambda: right(PLAYER), 'Right')
screen.onkey(lambda: down(PLAYER), 'Down')

screen.onkey(lambda: up(ENEMY), 'w')
screen.onkey(lambda: left(ENEMY), 'a')
screen.onkey(lambda: right(ENEMY), 'd')
screen.onkey(lambda: down(ENEMY), 'x')

screen.listen()

screen.mainloop()
