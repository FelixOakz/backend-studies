import turtle


def sierpinski(length, level):
	if level == 0:
		for i in range(3):
			turtle.forward(length)
			turtle.left(120)
	else:
		sierpinski(length/2, level-1)
		turtle.forward(length/2)
		sierpinski(length/2, level-1)
		turtle.backward(length/2)
		turtle.left(60)
		turtle.forward(length/2)
		turtle.right(60)
		sierpinski(length/2, level-1)
		turtle.left(60)
		turtle.backward(length/2)
		turtle.right(60)


turtle.speed(0)
sierpinski(200, 4)
