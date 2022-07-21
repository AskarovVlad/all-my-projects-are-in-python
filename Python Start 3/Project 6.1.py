import turtle

t = turtle.Pen()
t.speed(5)
t.width(5)
t.color(0.9, 0.75, 0)
t.fillcolor('blue')
t.begin_fill()
for x in range(1, 19):
    t.forward(100)
    if x % 2 == 0:
        t.left(175)
    else:
        t.left(225)
t.end_fill()
t.up()
t.goto(-200, -200)
t.down()


def mysquare(size, filled):
    if filled == True:
        t.begin_fill()
    for x in range(0, 4):
        t.forward(size)
        t.lt(90)
    if filled == True:
        t.end_fill()

mysquare(500, False)
mysquare(150, True)

t.reset()


def draw_star(size, points):
    degree = 360 / points
    for x in range(0, points):
        t.forward(size)
        t.left(90 + degree)
        t.forward(size)
        t.right(90 + 2 * degree)


draw_star(50, 10)
turtle.done()
