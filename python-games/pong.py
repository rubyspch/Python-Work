import turtle #built in module for beginners games 

wn = turtle.Screen() #creates a window
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0) #stops windows from updating, have to manually update them

#Main game loop

#Paddle A
paddle_a=turtle.Turtle() #creates a turtle object from Turtle class
paddle_a.speed(0) #speed of animation for turtle, set to maximum
paddle_a.shape("square") #turtle has a few built in shapes default 20x20
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup() #turtles draw lines as they move so this stops the line from being drawn
paddle_a.goto(-350,0) #(x co-ord, y co-ord)

#Paddle B
paddle_b=turtle.Turtle() 
paddle_b.speed(0) 
paddle_b.shape("square") 
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup() 
paddle_b.goto(0,350)

#Ball

turtle.done()