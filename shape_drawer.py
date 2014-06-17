import turtle

def draw_shapes():
	window = turtle.Screen()
	window.bgcolor("orange")
	
	laura = turtle.Turtle()
	laura.shape("turtle")
	laura.color("white")
	
	for i in range(4):
		laura.forward(100)
		laura.right(90)
		
	brian = turtle.Turtle()
	brian.shape("arrow")
	brian.color("tan")
	brian.circle(100)
	
	cj = turtle.Turtle()
	cj.shape("circle")
	cj.color("white")
	
	for i in range(3):
		cj.backward(100)
		cj.left(120)
	
	window.exitonclick()
	
def circle_from_square(n = 10, length = 100, speed = 2):
	#Defining how many squares you want to make-up your circle
	window = turtle.Screen()
	window.bgcolor("orange")
	
	squaw_birds = turtle.Turtle()
	squaw_birds.shape("turtle")
	squaw_birds.color("green")
	squaw_birds.speed(speed)
	
	degrees_turn = 360./n
	
	for i in range(n):
		for i in range(3):
			squaw_birds.forward(length)
			squaw_birds.right(90)
		squaw_birds.forward(length)
		squaw_birds.right(90 + degrees_turn)
	
	window.exitonclick()
	
circle_from_square(n=360, speed = 100)
	
	
	