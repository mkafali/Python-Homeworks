#Basic turtle game. If you click the circle middle on the screen it asks to you to enter an angle. If you entered correct angle and hit the target you won game.and
#Also, there is a restart button at the top-right corner of the screen. 
import turtle
import random
def game():
    wn = turtle.Screen()
    wn.setup(width=800, height=600)
    wn.bgcolor("black")

    turtle.hideturtle()
    turtle.penup()
    turtle.speed(0)
    turtle.goto(370,270)
    turtle.fillcolor("red")
    turtle.begin_fill()
    turtle.forward(10)
    for _ in range(3):
        turtle.left(90)
        turtle.forward(10)
    turtle.end_fill()
    turtle.setheading(0)


    striker = turtle.Turtle()
    striker.speed(0)
    #striker.shape("circle")
    #striker.color("white")
    striker.hideturtle()
    striker.fillcolor("white")
    striker.begin_fill()
    striker.circle(10)
    striker.end_fill()
    striker.penup()
    striker.goto(0,0)


    strike_x = random.randrange(-300,300)
    strike_y = random.randrange(-300,300)
    turtle.pencolor("red")
    turtle.hideturtle()
    turtle.penup()
    turtle.speed(0)
    turtle.goto(strike_x, strike_y)
    turtle.fillcolor("blue")
    turtle.begin_fill()
    turtle.forward(50)
    for _ in range(3):
        turtle.left(90)
        turtle.forward(50)
    turtle.end_fill()
    turtle.goto(0,0)
    turtle.pendown()
    turtle.speed(20)
    click_occured = False
    click_out = False

    def on_click(x, y):
        nonlocal click_occured, click_out, strike_x, strike_y
        if not click_occured:
            if(-20 <= x <= 20 and -20 <= y <= 20):
                font_size = 24
                click_occured = True
                angle = int(wn.textinput("angle", "enter angle"))
                wn.update()
                #angle = int(input("enter angle to hit the target: "))
                turtle.showturtle()
                turtle.setheading(angle)
                turtle.penup()
                while True:
                    turtle.forward(2)
                        

                    if((strike_x <= turtle.xcor() <= (strike_x + 50)) and (strike_y <= turtle.ycor() <= strike_y + 50)):
                        turtle.hideturtle()
                        turtle.goto(-10,50)
                        turtle.pencolor("white")
                        turtle.write("win", align = "center", font = ("Arial", font_size, "normal"))
                        turtle.pencolor("red")
                        break
                    
                    if((turtle.xcor() >= 390 or turtle.xcor() <= -390) or (turtle.ycor() >= 290 or turtle.ycor() <= -290)):
                        turtle.hideturtle()
                        turtle.goto(-10,50)
                        turtle.pencolor("white")
                        turtle.write("game over", align = "center", font = ("Arial", font_size, "normal"))
                        turtle.pencolor("red")
                        break

        if not click_out:
            if(370 <= x <= 380 and 270 <= y <= 280):
                wn.clearscreen()
                game()



            
    wn.onclick(on_click)


    turtle.done()

game()