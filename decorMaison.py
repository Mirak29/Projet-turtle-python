import dessinMSDA as d
def pelouse():
    d.turtle.speed(11)
    d.turtle.color("#22780F")
    d.se_positionner(0, -685, -155)
    d.rectangle(400,1360, "#22780F")

def herbe():
    d.turtle.color("#22780F")
    d.turtle.fillcolor("#22780F")
    d.se_positionner(0, -685, -155)
    d.turtle.begin_fill()
    while d.turtle.xcor() < 677:
        d.turtle.left(60)
        d.turtle.forward(5)
        d.turtle.right(120)
        d.turtle.forward(5)
        d.turtle.left(60)
    d.turtle.end_fill()

def ciel():
    d.turtle.speed(11)
    d.turtle.color("#77B5FE")
    d.se_positionner(0, -685, 370)
    d.rectangle( 550,1360, "#77B5FE")

def soleil():
    d.turtle.speed(11)
    d.turtle.color("yellow")
    d.se_positionner(0, -550, 300)
    d.turtle.fillcolor("yellow")
    d.turtle.begin_fill()
    for i in range(12):
        d.turtle.left(45)
        d.turtle.forward(12)
        d.turtle.right(75)
        d.turtle.forward(20)
    d.turtle.end_fill()


