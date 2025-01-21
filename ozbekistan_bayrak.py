import turtle

window = turtle.Screen()
window.setup(1000, 600)
window.bgcolor("white")

turtle.speed(4)
turtle.penup()
turtle.goto(-500, 300)  
turtle.pendown()

hight_main = 195
width_main = 1000

def draw_rectangle(color, height):
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(width_main)
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)
    turtle.end_fill()
    turtle.right(90)
    turtle.forward(height)
    turtle.left(90)

draw_rectangle("#0099B5", hight_main)  
draw_rectangle("#CE1126", 10)         
draw_rectangle("white", hight_main)   
draw_rectangle("#CE1126", 10)         
draw_rectangle("#1EB53A", hight_main) 


def hilal(size):
    turtle.color("white")
    turtle.right(90)
    turtle.penup()
    turtle.goto(-435, 202.5)
    turtle.pendown()
    turtle.fillcolor("white")
    turtle.begin_fill()
    turtle.circle(size)
    turtle.end_fill()

    turtle.penup()
    turtle.goto(-410, 202.5)
    turtle.fillcolor("#0099B5")
    turtle.begin_fill()
    turtle.circle(size-8)
    turtle.end_fill()
    turtle.left(90)

hilal(70)

def yildiz(size):
    turtle.penup()
    turtle.goto(-180,255)
    turtle.pendown()
    for j in range(12):
        if j == 3:
            turtle.penup()
            turtle.goto(-240, 205)
            turtle.pendown()
        elif j == 7:
            turtle.penup()
            turtle.goto(-300, 155)
            turtle.pendown()
        turtle.fillcolor('white')
        turtle.begin_fill()
        turtle.begin_fill()  
        turtle.forward(size)  
        turtle.left(72)  
        turtle.forward(size)  
        turtle.right(144)
        turtle.forward(size)
        turtle.left(72)
        turtle.forward(size)
        turtle.right(144)
        turtle.forward(size)
        turtle.left(72)
        turtle.forward(size)
        turtle.right(144)
        turtle.forward(size)
        turtle.left(72)
        turtle.forward(size)
        turtle.right(144)
        turtle.forward(size)
        turtle.left(72)
        turtle.forward(size)
        turtle.right(144)

        turtle.end_fill()
        turtle.penup()
        turtle.forward(60)
        turtle.pendown()

yildiz(10)


turtle.hideturtle()
turtle.done()
