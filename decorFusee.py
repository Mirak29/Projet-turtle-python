from dessinMSDA import *
turtle.bgcolor("black")
def planete():
    '''
        OBJECTIF : présente la partie supérieure de la planete Terre qui sert de lieu de décollage pour la fusée
        METHODE : utilisation des méthodes "se_positionner", "cercle" et "ellipse",
        BESOINS : / 
        CONNUS : /
        ENTREES : /
        SORTIES : /
        RESULTAT : /
        HYPOTHESE : /
    '''
    turtle.speed(11)
    se_positionner(0, -780, -1060)
    turtle.left(90)
    cercle(-800, "skyblue")
    se_positionner(0, 0, -305, -190)
    ellipse(200,"#3AF24B")
    turtle.setheading(0)

def astre():
    '''
        OBJECTIF : dessine un astre qui sert de chemin de traverse pour la fuséee en plein vol vers une destination inconnue
        METHODE : utilisation de tests, de boucle, ainsi que de la méthodes "carrée"
        BESOINS : / 
        CONNUS : /
        ENTREES : /
        SORTIES : /
        RESULTAT : /
        HYPOTHESE : /
    '''
    turtle.speed(11)
    turtle.color("white")
    taille = 250
    arreter = 0
    ang = 5
    for i in range(5):
        while True:
            carree(taille)
            turtle.right(ang)
            arreter += 1
            if arreter == 24:
                break
        ang += 1
        taille -= 20
        arreter = 0
    turtle.color("black")
    turtle.setheading(0)

def feu():
    '''
        OBJECTIF : dessine les flammes que projette la fusée en plein décollage pour échapper à l'attraction terrestre
        METHODE : utilisation  de boucle, ainsi que des méthodes "se_positionner"
        BESOINS : / 
        CONNUS : /
        ENTREES : /
        SORTIES : /
        RESULTAT : /
        HYPOTHESE : /
    '''
    turtle.fillcolor("orange")
    turtle.begin_fill()
    se_positionner(0,3,-180, 170)
    ang = 15
    for i in range(15):
        turtle.fd(10)
        turtle.lt(ang)
        ang -=1
    turtle.setheading(0)

    se_positionner(0,3,-180, 10)
    ang = -15
    for i in range(15):
        turtle.fd(10)
        turtle.lt(ang)
        ang +=1
    turtle.setheading(0)
    turtle.end_fill()


