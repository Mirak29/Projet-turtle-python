from dessinMSDA import *
from decorMaison import *
ciel()
soleil()
pelouse()
herbe()

turtle.color("black")
se_positionner(0, -100, -145)
rectangle(10, 50, "#8B6C42")
rectangle(10, 200, "#8B6C42")
rectangle(10, 350, "#8B6C42")


turtle.color("white")
se_positionner(0, -100, 120)
rectangle(265, 350, "#B67823")


turtle.color("white")
se_positionner(0, -20, -15)
rectangle(130, 100, "#FFE4C4")

turtle.color("black")
se_positionner(0, 130, -12)
carree(45,"white")
se_positionner(0, 175, -12)
carree(45, "white")
se_positionner(0, 130, -57)
carree(45, "white")
se_positionner(0, 175, -57)
carree(45, "white")

turtle.color("white")
se_positionner(0, 200, 300)
rectangle(100, 50,"#8B6C42")


turtle.color("white")
se_positionner(0, -225, 120)
triangle_isocele(600, 235,"#E8D630")

turtle.hideturtle()
turtle.done()
