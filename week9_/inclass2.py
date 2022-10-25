# Using Python Turtle create a program to draw a traffic light using user defined 
# Python functions.
from time import time
from turtle import *
from random import *
# The functions required are:

# DrawCircle - This function takes the values required to 
# draw a circle at the indicated coordinates and radius 
def DrawCircle(x,y,radius,color):
    #move down the amount of the radius to draw circle
    penup()
    fillcolor(color)
    begin_fill()
    goto(x,-radius + y)
    pendown()
    circle(radius)
    end_fill()




# DrawRectangle - This function takes the values required to 
# draw a rectangle at the indicated coordinates and length and width 
def DrawRectangle(x,y,width,height,color="#e6a102"):
    penup()
    fillcolor(color)
    begin_fill()
    #point A bottom right corner
    goto(width/2+x,-height/2+y)
    pendown()
    #point B top right corner
    goto(width/2+x,height/2+y)
    #point C top left corner
    goto(-width/2+x,height/2+y)
    #point D bottom left corner
    goto(-width/2+x,-height/2+y)
    #point A to complete the rtectangle
    goto(width/2+x,-height/2+y)
    end_fill()



# DrawTrafficLight - This is a glue function that connects the other 
# functions and variables together
def DrawTrafficLight(x,y):
    RECT_WIDTH = 100
    RECT_HEIGHT = 250
    LIGHT_RADIUS = 25
    DrawRectangle(x,y,RECT_WIDTH,RECT_HEIGHT)
    #yellow light
    DrawCircle(x,RECT_HEIGHT-RECT_HEIGHT+y,LIGHT_RADIUS,"yellow")
    #red light
    DrawCircle(x,RECT_HEIGHT/3+y,LIGHT_RADIUS,"red")
    #green light
    DrawCircle(x,-RECT_HEIGHT/3+y,LIGHT_RADIUS,"green")

# main - This function will call the DrawTrafficLight function 
# at 3 different locations and therefore draw 3 traffic lights
def main():
    speed(0)
    hideturtle()


    # DrawRectangle(0,0,100,250)
    # DrawCircle(0,0,25,"yellow")
    # DrawCircle(0,75,25,"red")
    # DrawCircle(0,-75,25,"green")
    while True:
        x = random.randrange(-200,200)
        y = random.randrange(-200,200)



        DrawTrafficLight(0,0)
        DrawTrafficLight(100,0)
        DrawTrafficLight(-100,0)
        time.sleep(1)
        clear()
    

# kick off the program
main()

exitonclick()
print("End of program")



# Note: When designing the program, think about the percentage 
# of sizes instead of absolute sizes.
















