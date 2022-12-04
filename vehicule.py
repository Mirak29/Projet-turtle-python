from dessinMSDA import *
from decorVehicule import *
route()

#
# Création de la forme de base (carosserie avant)
rectangle(75,400,"#2C75FF")
se_positionner(0,100,0)
B=trapeze(200,100,50,"#C0C0C0")

# Pose de la malle avant
se_positionner(0,0,0)
A=parallelogramme(100,100,120,"yellow")

# Pose de la face avant du véhicule
turtle.fillcolor("yellow")
turtle.begin_fill()
turtle.goto(A-100,100)
turtle.goto(A-100,100-75)
turtle.goto(0,-75)
turtle.end_fill()

# Pose de la forme de base (carosserie arrière)
se_positionner(0,A,100)
trapeze(200,100,50,"#C0C0C0")

# Pose de la malle arrière
se_positionner(0,400-100,0)
parallelogramme(100,100,120,"yellow")

# Pose de la vitre arrière
turtle.fillcolor("#C0C0C0")
turtle.begin_fill()
turtle.goto(B[0]+100,B[1])
turtle.goto(A+150,150)
turtle.goto(A+200,100)
turtle.goto(A+200,100)
turtle.end_fill()

# Pose de la toiture
se_positionner(0,B[0],B[1])
parallelogramme(100,100,120,"yellow")

# Pose de la vitre avant
turtle.fillcolor("#C0C0C0")
turtle.begin_fill()
turtle.goto(A+50,150)
turtle.goto(A,100)
turtle.goto(100,0)
turtle.end_fill()

# Montage de la roue avant
se_positionner(0,125,-75)
demi_cercle(25,"#C0C0C0")
se_positionner(0,100,-95)
cercle(20,"brown")
# Montage de la roue arrière
se_positionner(0,105+200,-75)
demi_cercle(25,"#C0C0C0")
se_positionner(0,100+180,-95)
cercle(20,"brown")

# fin de l'asemblage
turtle.hideturtle()
turtle.done()