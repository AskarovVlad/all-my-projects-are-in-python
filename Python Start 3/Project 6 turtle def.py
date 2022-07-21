import turtle
import time

t = turtle.Pen()
t.up()
t.goto(-50, -50)  # переместить в нужные координаты(х,у)
# t.home()           переместить в центр экрана
t.speed(10)  # скорость движения 1 медленно, 10 бістро, 0 без анимации
t.down()
t.left(36)
t.color('green')  # цвет
t.width(5)  # ширина следа
t.fillcolor("red")
t.begin_fill()
for x in range(1, 20):
    t.forward(200)
    t.left(95)
t.end_fill()
t.up()
t.goto(-200, -200)
t.down()

time.sleep(10)
t.write("Hello, World!", move=True, align='center',
        font=('Times New Roman', 20, 'italic'))  # название шрифта, размер шрифта и тип начертания текста
# align — служит для выравнивания надписи относительно Черепашки.
# Может принимать значения right, center и left. По умолчанию равен значению right.
t.up()
t.goto(-400, -400)
t.down()
text = turtle.textinput("Заголовок окна", "Текст в диалоговом окне")
turtle.done()

