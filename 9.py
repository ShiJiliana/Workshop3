import turtle

colors = ['red', 'skyblue', 'blue', 'green', 'orange', 'red']
percent = [15, 33, 7, 15, 20, 10]  # Процентное соотношение данных

total = sum(percent)
angle_sum = 0

turtle.speed(100)
turtle.up()
turtle.setposition(0, -200)
turtle.down()

for i in range(len(percent)):
    angle = percent[i] / total * 360
    turtle.color(colors[i], colors[i])
    turtle.begin_fill()
    turtle.circle(200, angle)
    position = turtle.position()
    angle_sum += angle
    turtle.setposition(0, 0)
    turtle.end_fill()
    turtle.setposition(position)

turtle.up()
turtle.color('black')
turtle.setposition(0, -220)
turtle.down()
turtle.write('B', False)

turtle.up()
turtle.color('black')
turtle.setposition(180, 100)
turtle.down()
turtle.write('A', False)

turtle.up()
turtle.color('black')
turtle.setposition(-20, 200)
turtle.down()
turtle.write('E', False)

turtle.up()
turtle.color('black')
turtle.setposition(-150, 140)
turtle.down()
turtle.write('D', False)

turtle.up()
turtle.color('black')
turtle.setposition(-210, -40)
turtle.down()
turtle.write('C', False)

turtle.hideturtle()
turtle.done()
