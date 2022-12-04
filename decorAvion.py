from dessinMSDA import *
turtle.bgcolor("#22780F")
turtle.speed(11)
def piste():
    '''
        OBJECTIF : présente le décor d'une piste d'attérissage pour l'avion en plein vol
        METHODE : utilisation de tests, de boucle, ainsi que des méthodes "se_positionner", "triangle_equilaterale"et "rectangle",
        BESOINS : / 
        CONNUS : /
        ENTREES : /
        SORTIES : /
        RESULTAT : /
        HYPOTHESE : /
    '''
    se_positionner(0,-675,-360)
    triangle_equilaterale(1350,"black")
    se_positionner(0,0,375)
    y = 380
    while True:
        rectangle(20,5,"white")
        y -= 60
        se_positionner(0,0,y)
        if y <= -380:
            break



