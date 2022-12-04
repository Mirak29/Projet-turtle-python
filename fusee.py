import turtle
import dessinMSDA as d
import decorFusee as de

de.planete()
d.se_positionner(0,5,200)
de.astre()
de.feu()

# montage de la base de la fusée
d.se_positionner(0,0,-250/2)
d.rectangle(100/2,25/2,"#CECECE")
d.se_positionner(0,-50/2,(-100-250)/2)
d.triangle_rectangle(50/2,100/2,0,"#AFAFAF")
d.se_positionner(0,25/2,(-100-250)/2)
d.triangle_rectangle(50/2,100/2,1,"#AFAFAF")

d.se_positionner(0,(-25)/2,(0-250)/2)
d.cercle(6.25/2,"#AFAFAF")
d.se_positionner(0,56.25/2,(0-250)/2)
d.cercle(6.25/2,"#AFAFAF")

# Assemblage de l'axe de la fusée
d.se_positionner(0,0,(0-250)/2)
d.carree(25/2,"#CECECE")

d.se_positionner(0,-50/2,(75-250)/2,90)
d.rectangle(50/2,125/2,"#CECECE")

d.se_positionner(0,(-41.66+12)/2,(155-250)/2)
d.carree(80/2,"#CECECE")

d.se_positionner(0,(-72+12.5)/2,(96-250)/2)
d.cercle(20/2,"#AFAFAF")

d.se_positionner(0,(75+12.5)/2,(96-250)/2)
d.cercle(20/2,'#AFAFAF')

d.se_positionner(0,-90/2,(155+100-250)/2)
d.rectangle(100/2,200/2,"#CECECE")

d.se_positionner(0,(-90-50)/2,(155+60-250)/2)
d.rectangle(60/2,300/2,"#CECECE")
d.triangle_rectangle(25,20,0,"#AFAFAF")

d.se_positionner(0,(-90+200)/2,(155+60-250)/2)
d.triangle_rectangle(25,20,1,"#AFAFAF")
d.turtle.setheading(0)

d.se_positionner(0,(-90+250)/2,(155-250)/2)
d.triangle_isocele(-50/2,(90-250+50)/2,"#AFAFAF")

d.se_positionner(0,-90/2,(155-250)/2)
d.triangle_isocele(-50/2,(90-250+50)/2,"#AFAFAF")

#Assemblage et finition de la tête de la fusée
d.se_positionner(0,-90/2,(155+100-250)/2)
d.triangle_rectangle(30/2,100/2,0,"#AFAFAF")
d.se_positionner(0,15-90/2,(155+100-250+100)/2)
d.rectangle(50,70,"#CECECE")

d.se_positionner(0,(-90+200-30)/2,(155+100-250)/2)
d.triangle_rectangle(30/2,100/2,1,"#AFAFAF")

d.se_positionner(0,-78/2,(155+100+100-250)/2,90)
d.triangle_equilaterale(180/2,"#AFAFAF")

d.se_positionner(0,(-78+49)/2,40+(155+100+100-250)/2)
d.rectangle(40,40,"#CECECE")

turtle.hideturtle()

d.turtle.done()