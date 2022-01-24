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


# Create Score Writer
score = trtl.Turtle()
sc = 0
def scoreboard():
    score.penup()
    score.goto(350, 350)
    score.write("Score: " + str(sc), font=fontSetup)


# Setting up plus movement
plus.speed(100)


def up():
    plus.penup()
    plus.setheading(90)
    plus.forward(200)
    blue_pick()
    red_pick()
    yellow_pick()
    pink_pick()
    green_pick()
    cyan_pick()
    grey_pick()
    orange_pick()
    maroon_pick()



def down():
    plus.penup()
    plus.setheading(90)
    plus.backward(200)
    blue_pick()
    red_pick()
    yellow_pick()
    pink_pick()
    green_pick()
    cyan_pick()
    grey_pick()
    orange_pick()
    maroon_pick()


def left():
    plus.penup()
    plus.setheading(0)
    plus.backward(200)
    blue_pick()
    red_pick()
    yellow_pick()
    pink_pick()
    green_pick()
    cyan_pick()
    grey_pick()
    orange_pick()
    maroon_pick()


def right():
    plus.penup()
    plus.setheading(0)
    plus.forward(200)
    blue_pick()
    red_pick()
    yellow_pick()
    pink_pick()
    green_pick()
    cyan_pick()
    grey_pick()
    orange_pick()
    maroon_pick()


wn.onkeypress(up, "w")
wn.onkeypress(down, "s")
wn.onkeypress(right, "d")
wn.onkeypress(left, "a")
wn.listen()


rand_color = ""
# Create color generator
colors = ["Blue", "red", "orange" , "cyan", "green", "pink", "grey", "yellow", "Maroon"]
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
    scoreboard()
    sc = 0
    if rand_color == "blue":
        if plus.xcor() < -199 and plus.ycor() > 199:
            plus.pendown()
def red_pick():
    global rand_color
    scoreboard()
    sc = 0
    if rand_color == "red":
        if plus.xcor() > 199 and plus.ycor() > 199:
            plus.pendown()
def orange_pick():
    global rand_color
    scoreboard()
    sc = 0
    if rand_color == "orange":
        if 199 > plus.xcor() > -199 and -199 > plus.ycor():
            sc = sc + 1
def cyan_pick():
    sc = 0
    global rand_color
    scoreboard()
    if rand_color == "cyan":
        if plus.xcor() > 199 and 199 > plus.ycor() > -199:
            sc = sc + 1
def green_pick():
    global rand_color
    scoreboard()
    sc = 0
    if rand_color == "green":
        if -199 < plus.xcor() < 199 and -199 < plus.ycor() < 199:
            sc = sc + 1
def pink_pick():
    global rand_color
    scoreboard()
    sc = 0
    if rand_color == "pink":
        if -400 < plus.xcor() < -199 and -199 < plus.ycor() < 199:
            sc = sc + 1
def grey_pick():
    global rand_color
    scoreboard()
    sc = 0
    if rand_color == "grey":
        if -400 < plus.xcor() < -199 and -199 > plus.ycor():
            sc = sc + 1
def yellow_pick():
    global rand_color
    scoreboard()
    sc = 0
    if rand_color == "yellow":
        if -199 < plus.xcor() < 199 and plus.ycor() > 199:
            sc = sc + 1
def maroon_pick():
    global rand_color
    scoreboard()
    sc = 0
    if rand_color == "maroon":
        if plus.xcor() > 199 and -199 > plus.ycor():
            sc = sc + 1


#Main Code
wn.ontimer(countdown, counterInterval)
scoreboard()
random_color()



wn.mainloop()