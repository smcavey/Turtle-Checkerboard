import turtle

def main():
    color = "red" # initial color to black
    color_change = 1 # counter to change between black and white
    X_INCREMENT = 50 # x coord constant change
    Y_INCREMENT = 50 # y coord constant change
    x = 0 # initial x
    y = 0 # initial y
    WIDTH = 50 # constant width
    for j in range (5): # make a 5x5 checkerboard
        for k in range(5):
            if color_change % 2 == 0: # color check
                color = "green"
            else:
                color = "red"
            square(x, y, WIDTH, color)
            x += X_INCREMENT # increment x
            color_change += 1 # increment color counter to alternate black and white
        x = 0 # reset x
        y += Y_INCREMENT # increment y
    turtle.done()
def square(x, y, WIDTH, color):
    turtle.penup() # raise pen
    turtle.goto(x, y) # move to (x,y)
    turtle.fillcolor(color) # set fill color
    turtle.pendown() # lower pen
    turtle.begin_fill() # start filling
    for count in range(4): # draw a square
        turtle.forward(WIDTH)
        turtle.left(90)
    turtle.end_fill() # end fill
main()
