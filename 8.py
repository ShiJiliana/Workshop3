import turtle as t
t.setup(500, 500)
t.speed(10)

#корзинка
t.up()
t.setposition(-40, 65)
t.down()
t.pensize(7)
t.color('skyblue')
t.right(78)
t.forward(78)
t.up()
t.setposition(5, 65)
t.down()
t.right(12)
t.forward(75)
t.up()
t.setposition(50, 65)
t.down()
t.right(12)
t.forward(78)
t.left(102)

t.up()
t.setposition(-65, 40)
t.down()
t.forward(142)
t.up()
t.setposition(-62, 15)
t.down()
t.forward(132)

#тележка
t.up()
t.setposition(-100, 80)
t.down()
t.color('blue')
t.forward(20)
t.right(75)
t.forward(80)
t.up()
t.setposition(-75, 65)
t.left(75)
t.down()
t.forward(160)
t.right(105)
t.forward(80)
t.right(75)
t.forward(119)
t.left(105)
t.forward(15)
t.left(75)
t.forward(110)

t.up()
t.setposition(-30, -50)
t.down()
t.dot(25)
t.up()
t.setposition(38, -50)
t.down()
t.dot(25)

t.done()