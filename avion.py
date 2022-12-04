from turtle import pencolor
from dessinMSDA import *
import decorAvion as a

a.piste()

pencolor("skyblue")
se_positionner(0, 0 , 250)
demi_cercle(40,"#AFAFAF")
rectangle(400, 80,"#AFAFAF")
se_positionner(0, 0 , 120)
aile_gauche("#9E9E9E")
se_positionner(0, -80 , 120, 180)
aile_droite("#9E9E9E")
se_positionner(0, -80 , -150)
se_positionner(0, -80 , -150)
triangle_isocele(80,-34,"#9E9E9E")
aileron_gauche("#9E9E9E")
se_positionner(0, 0 , -150)
aileron_droite("#9E9E9E")
se_positionner(0, 0 , -12)

turtle.hideturtle()
turtle.done()