import turtle as trtl
import random as rand

bt = trtl.Turtle()
plus = trtl.Turtle()
plus_image = "plus.gif"

wn = trtl.Screen()
wn.addshape(plus_image)

#Set turtle speed
bt.speed("fastest")
#Making the Big Box
bt.penup()
bt.goto(300,300)
bt.pensize(5)
bt.pendown()
bt.goto(300,-300)
bt.goto(-300,-300)
bt.goto(-300,300)
bt.goto(300,300)
#Making the top right box
bt.fillcolor("red")
bt.begin_fill()
bt.goto(300,100)
bt.goto(100,100)
bt.goto(100,300)
bt.end_fill()
#Making the top box
bt.fillcolor("yellow")
bt.begin_fill()
bt.goto(100,100)
bt.goto(-100,100)
bt.goto(-100,300)
bt.goto(100,300)
bt.end_fill()
#Making the top left box
bt.fillcolor("blue")
bt.begin_fill()
bt.goto(-300,300)
bt.goto(-300,100)
bt.goto(-100,100)
bt.goto(-100,300)
bt.end_fill()
#Making the left box
bt.fillcolor("magenta")
bt.begin_fill()
bt.goto(-100,-100)
bt.goto(-300,-100)
bt.goto(-300,100)
bt.goto(-100,100)
bt.end_fill()
#Making the middle box
bt.fillcolor("green")
bt.begin_fill()
bt.goto(100,100)
bt.goto(100,-100)
bt.goto(100,-100)
bt.goto(-100,-100)
bt.goto(-100,100)
bt.end_fill()
#Making the right box
bt.fillcolor("cyan")
bt.begin_fill()
bt.goto(300,100)
bt.goto(300,-100)
bt.goto(100,-100)
bt.goto(100,100)
bt.end_fill()
#Making bottom right box
bt.fillcolor("maroon")
bt.begin_fill()
bt.goto(100,-300)
bt.goto(300,-300)
bt.goto(300,-100)
bt.goto(100,-100)
bt.end_fill()
#Making bottom box
bt.fillcolor("orange")
bt.begin_fill()
bt.goto(100,-300)
bt.goto(-100,-300)
bt.goto(-100,-100)
bt.goto(100,-100)
bt.end_fill()
#Making bottom left box
bt.fillcolor("gray")
bt.begin_fill()
bt.goto(-300,-100)
bt.goto(-300,-300)
bt.goto(-100,-300)
bt.goto(-100,-100)
bt.end_fill()
#Fix perimeter
bt.goto(-100,300)
bt.goto(300,300)
#Hide Turtle
bt.hideturtle()

#Drawing the plus turtle
def draw_plus(active_plus):
    active_plus.shape(plus_image)
    wn.update()
draw_plus(plus)



#Create timer
counter = trtl.Turtle()
counter.penup()
counter.speed(100)
counter.goto(-450, 350)
timer = 30

fontSetup = ("Arial", 20, "normal")
counterInterval = 1000

def countdown():
    global timer, timerUp
    counter.clear()
    if timer <=0:
        counter.write("TIME IS UP", font=fontSetup)
        timerUp = True
    else:
        counter.write("Timer: " + str(timer), font=fontSetup)
        timer -= 1
        counter.getscreen().ontimer(countdown, counterInterval)






# Setting up plus movement
plus.speed(100)


def up():
    plus.penup()
    plus.setheading(90)
    plus.forward(200)


def down():
    plus.penup()
    plus.setheading(90)
    plus.backward(200)


def left():
    plus.penup()
    plus.setheading(0)
    plus.backward(200)


def right():
    plus.penup()
    plus.setheading(0)
    plus.forward(200)


wn.onkeypress(up, "w")
wn.onkeypress(down, "s")
wn.onkeypress(right, "d")
wn.onkeypress(left, "a")
wn.listen()


rand_color = ""
# Create color generator
colors = ["Blue" , "Maroon"]
def random_color():
    global rand_color
    color_write = trtl.Turtle()
    color_write.penup()
    color_write.speed(100)
    color_write.goto(-100, 350)
    rand_color = rand.choice(colors)
    color_write.write(str(rand_color), font=fontSetup)



#Pair the generated color with the square
def blue_pick():
    global rand_color
    if rand_color == "blue":
        if plus.xcor() < -199 and plus.ycor() > 199:
            print("hi")

#Main Code
wn.ontimer(countdown, counterInterval)
random_color()
blue_pick()



















wn.mainloop()