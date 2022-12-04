from dessinMSDA import *
turtle.bgcolor("#AE642D")
turtle.speed(11)
def route():
    '''
        OBJECTIF : Dessine la route qui sert de passsage à la voiture
        METHODE : utilisation de tests, de boucle, ainsi que des méthodes "se_positionner" et "rectangle",
        BESOINS : / 
        CONNUS : /
        ENTREES : /
        SORTIES : /
        RESULTAT : /
        HYPOTHESE : /
    '''
    se_positionner(0,-680,200)
    rectangle(450, 1500,"black")
    se_positionner(0,-670,-5)
    x = -670
    while True:
        rectangle(5,25,"white")
        x += 60
        se_positionner(0,x,-5)
        if x >= 670:
            break

    se_positionner(0,-680,250)
    rectangle(50,1500,"grey")
    se_positionner(0,-670,250)
    x = -670
    while True:
        rectangle(50,80,"white")
        x += 200
        se_positionner(0,x,250)
        if x >= 670:
            break
        
    se_positionner(0,-680,-250)
    rectangle(50,1500,"grey")
    se_positionner(0,-670,-250)
    x = -670
    while True:
        rectangle(50,80,"white")
        x += 200
        se_positionner(0,x,-250)
        if x >= 670:
            break
    se_positionner(0,0,0)
