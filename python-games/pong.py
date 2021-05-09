import turtle #built in module for beginners games 

turtle.setup(width=800, height=600)
wn = turtle.Screen() #creates paddle_a window
wn.title("Pong")
wn.bgcolor("black")
wn.tracer(0) #stops windows from updating, have to manually update them

#Paddle A
paddle_a=turtle.Turtle() #creates paddle_a turtle object from Turtle class
paddle_a.speed(0) #speed of animation for turtle, set to maximum
paddle_a.shape("square") #turtle has paddle_a few built in shapes default 20x20
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
paddle_b.goto(350,0)

#Ball
ball=turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)

#Function
def paddle_a_up():
    y= paddle_a.ycor() #ycor method is from turtle, it returns y co-ord
    y += 20
    paddle_a.sety(y) #set the y co ord of p_a to the new +20 value
def paddle_a_down():
    y= paddle_a.ycor() 
    y -= 20
    paddle_a.sety(y) 

def paddle_b_up():
    y= paddle_b.ycor() 
    y += 20
    paddle_b.sety(y) 
def paddle_b_down():
    y= paddle_b.ycor() 
    y -= 20
    paddle_b.sety(y) 

#Keyboard binding
wn.listen() #listen for keyboard input
wn.onkeypress(paddle_a_up, "w") #when user presses w, call paddle_a_up function
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

#Main game loop
while True:
    wn.update()