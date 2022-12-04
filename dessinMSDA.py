#   Importation du module <<TURTLE>>
import turtle

def se_positionner(o,x,y,z=0):
    '''
        OBJECTIF : Cette fonction permet de positionner la tortue, sans tracer, à un point de coordonnees(x et y) connus dans le repère
        METHODE : utilisation des méthodes "penup()", "goto()" "right()" et "pendown()"
        BESOIN : "o" comme position actuelle du curseur, "x" comme abcisse du point et "y" comme ordonnee, "z" comme angle départ 
        CONNUS : /
        ENTREE : o,x,y,z
        SORTIE : /
        RESULTAT : /
        HYPOTHESE : les paramètres sont tous des nombres réels
    '''
    turtle.penup()
    turtle.goto(o+x,y)
    turtle.rt(z)
    turtle.pendown()
    return [x,y]

def se_deplacer(x,y,z=0,o=0):
    '''
        OBJECTIF : Cette fonction permet à la tortue de se déplacer jusqu'à à un point de coordonnees(x et y) connus dans le repère
        METHODE : utilisation des méthodes "goto()" "right()"
        BESOIN : "o" comme position actuelle du curseur, "x" comme abcisse du point et "y" comme ordonnee, "z" comme angle départ 
        CONNUS : /
        ENTREE : o,x,y,z
        SORTIE : /
        RESULTAT : /
        HYPOTHESE : les paramètres sont tous des nombres réels
    '''
    turtle.goto(o+x,y)
    turtle.rt(z)

def cercle(rayon,couleur=""):
    '''
        OBJECTIF : Tracer un cercle dans le repère
        METHODE : utilisation de la méthode "circle"
        BESOIN : "rayon" qui représente le rayon du cercle "couleur"
        CONNUS : /
        ENTREE : rayon
        SORTIE : /
        RESULTAT : /
        HYPOTHESE : "rayon" est un nombre réel; couleur est une chaîne de caractères qui désigne la couleur de remplissage des figures(c'est un paramètre facultatif)
    '''
    turtle.fillcolor(couleur)
    turtle.begin_fill()
    turtle.circle(rayon)
    turtle.end_fill()

def demi_cercle(rayon,couleur=""):
    '''
        OBJECTIF : Tracer un demi cercle
        METHODE : utilisation de la méthode "circle" en précisant un angle de 180 degrés
        BESOIN :"rayon" qui represente le rayon du demi cercle "couleur"
        CONNUS :/
        ENTREE :rayon
        SORTIE : /
        RESULTAT : /
        HYPOTHESE : "rayon" est un nombre reel; couleur est une chaîne de caractères qui désigne la couleur de remplissage des figures(c'est un paramètre facultatif)
    '''
    turtle.fillcolor(couleur)
    turtle.begin_fill()
    turtle.lt(90)
    turtle.circle(rayon,180)
    turtle.setheading(0)
    turtle.end_fill()

def carree(cote,couleur="",i=0):
    '''
        OBJECTIF : tracer un carre 
        METHODE : utilisation de boucle et des methode "forward" et "right"
        BESOIN : "cote" et "i" "couleur"
        CONNUS : /
        ENTREE : cote
        SORTIE : /
        RESULTAT : /
        HYPOTHESE : "cote" est un nombre reel, si i!=0 alors le carrée sera tracé dans le sens inverse; couleur est une chaîne de caractères qui désigne la couleur de remplissage des figures(c'est un paramètre facultatif)
    '''
    turtle.fillcolor(couleur)
    turtle.begin_fill()
    if i == 0 :
        for i in range(4):
            turtle.fd(cote)
            turtle.rt(90)
    else :
        for i in range(4):
            turtle.fd(cote)
            turtle.lt(90)
    turtle.end_fill()

def triangle_equilaterale(cote,couleur=""):
    '''
        OBJECTIF : tracer un triangle equilateral
        METHODE : utilisation de boucle ainsi les methodes "left"et "forward "
        BESOIN : "cote" et "i" "couleur"
        CONNUS : /
        ENTREE : cote
        SORTIE : /
        RESULTAT : /
        HYPOTHESE : cote est un nombre reel; couleur est une chaîne de caractères qui désigne la couleur de remplissage des figures(c'est un paramètre facultatif)
    '''
    turtle.fillcolor(couleur)
    turtle.begin_fill()
    for i in range(3):
        turtle.fd(cote)
        turtle.lt(120)
    turtle.end_fill()

def triangle_isocele(base,hauteur,couleur=""):
    '''
        OBJECTIF :tracer un triagle isocele
        METHODE : utilisation de boucle ainsi les methodes "left" et "forward"
        BESOIN : "cote" et "i" "couleur"
        CONNUS : /
        ENTREE : cote 
        SORTIE : origine
        RESULTAT : /
        HYPOTHESE : cote est un nombre reel; couleur est une chaîne de caractères qui désigne la couleur de remplissage des figures(c'est un paramètre facultatif)
    '''
    turtle.fillcolor(couleur)
    turtle.begin_fill()
    origine = turtle.pos()
    turtle.fd(base)
    turtle.goto(origine[0]+base/2,origine[1]+hauteur)
    turtle.goto(origine[0],origine[1])
    turtle.end_fill()
    return origine

def triangle_rectangle(base,hauteur,F=0,couleur=""):
    '''
        OBJECTIF : tracer un triangle rectangle 
        METHODE : utilisation des methodes "forward" et "goto"
        BESOIN : "base" , "hauteur" et "F" (qui prend une valeur différente de "0" pour inverser la figure) "couleur"
        CONNUS : /
        ENTREE : "base" et "hauteur"
        SORTIE : origine 
        RESULTAT : /
        HYPOTHESE : "base" et "hauteur" sont des nombres reels; couleur est une chaîne de caractères qui désigne la couleur de remplissage des figures(c'est un paramètre facultatif)
    '''
    turtle.fillcolor(couleur)
    turtle.begin_fill()
    origine = turtle.pos()
    if F == 0 :
        turtle.fd(base)
        turtle.goto(origine[0]+base,origine[1]+hauteur)
        turtle.goto(origine[0],origine[1])
    else:
        turtle.lt(90)
        turtle.fd(hauteur)
        turtle.goto(origine[0]+base,origine[1])
        turtle.goto(origine[0],origine[1])
    turtle.end_fill()
    return origine

def rectangle(longueur,largeur,couleur=""):
    '''
        OBJECTIF : tracer un rectangle 
        METHODE : utilisation de boucle ainsi les methodes "forward" et "goto"
        BESOIN : "longueur" et "largeur" "couleur"
        CONNUS : /
        ENTREE : longueur et largueur 
        SORTIE : origine
        RESULTAT : /
        HYPOTHESE : longueur et largeur sont des nombres reels; couleur est une chaîne de caractères qui désigne la couleur de remplissage des figures(c'est un paramètre facultatif)
    '''
    turtle.fillcolor(couleur)
    turtle.begin_fill()
    origine = turtle.pos()
    turtle.fd(largeur)
    turtle.goto(origine[0]+largeur,origine[1] - longueur)
    turtle.goto(origine[0],origine[1] - longueur)
    turtle.goto(origine[0],origine[1])
    turtle.end_fill()
    return origine

def losange(cote,couleur=""):
    '''
        OBJECTIF : tracer un losange
        METHODE : utisation de boucle ainsi les methodes "forward" et "goto"
        BESOIN : "cote" "couleur"
        CONNUS : /
        ENTREE : cote 
        SORTIE : / 
        RESULTAT : /
        HYPOTHESE : cote est un nombre reel ; couleur est une chaîne de caractères qui désigne la couleur de remplissage des figures(c'est un paramètre facultatif)
    '''
    turtle.fillcolor(couleur)
    turtle.begin_fill()
    turtle.lt(45)
    for i in range(4):
        turtle.fd(cote)
        turtle.rt(90)
    turtle.end_fill()

def trapeze(gbase,pbase,hauteur,couleur=""):
    '''
        OBJECTIF : tracer un trapeze
        METHODE :utilisation de boucle ainsi les methodes 
        BESOIN : "gbase" "pbase" et "hauteur" "couleur"
        CONNUS : /
        ENTREE : "gbase", "pbase", et "hauteur"
        SORTIE : x coordonnee x du débit de la petite base de la figure
        RESULTAT : / "gbase" "pbase" et "hauteur" sont des nombres reels
        HYPOTHESE :tous les paramtères sont des réels sauf couleur qui est une chaîne de caractères qui désigne la couleur de remplissage des figures(c'est un paramètre facultatif)
    '''
    turtle.fillcolor(couleur)
    turtle.begin_fill()
    o = turtle.pos()
    turtle.fd(gbase)
    turtle.goto(o[0]+gbase*3/4,o[1]+hauteur)
    turtle.goto(o[0]+gbase*1/4,o[1]+hauteur)
    x=turtle.pos()
    turtle.goto(o[0],o[1])
    turtle.heading()
    
    turtle.end_fill()
    return x

def parallelogramme(long, hauteur,angle,couleur=""):
    '''
        OBJECTIF :tracer un parrelogramme
        METHODE : utilisation d'affectations de boucle ainsi que les methodes "forward", "left", "penup", et "position"
        BESOIN : "long" "hauteur" et "angle" "couleur"
        CONNUS : /
        ENTREE : long hauteur et angle
        SORTIE : x : coordonnees de x en hauteur de la figure
        RESULTAT : /
        HYPOTHESE : "long" "hauteur" et "angle" sont des nombres des reels; couleur est une chaîne de caractères qui désigne la couleur de remplissage des figures(c'est un paramètre facultatif)
    '''
    turtle.fillcolor(couleur)
    turtle.begin_fill()
    origine = turtle.pos()
    y=turtle.ycor()
    turtle.fd(long)
    turtle.lt(angle)
    turtle.penup()
    while (y < origine[1] + hauteur) :
        turtle.fd(1)
        y=turtle.ycor()
    turtle.pendown()
    x=turtle.xcor()
    turtle.goto(origine[0]+long,origine[1])
    turtle.goto(+x,origine[1]+hauteur)
    turtle.lt(-angle)
    turtle.bk(long)
    turtle.goto(origine[0],origine[1])
    turtle.end_fill()
    return x

def polygone(long,nombre_cotes,couleur=""):
    '''
        OBJECTIF : Tracer un polygone à n côtés
        METHODE : utilisation de boucle et des méthodes "forward" et "left"
        BESOIN : "long" et"nombre_cotes"  "couleur"
        CONNUS : /
        ENTREE : "long" et "nombre_cotes"
        SORTIE : /
        RESULTAT : /
        HYPOTHESE : "long" et "nombre_cotes" sont des nombres reels; couleur est une chaîne de caractères qui désigne la couleur de remplissage des figures(c'est un paramètre facultatif)
    '''
    turtle.fillcolor(couleur)
    turtle.begin_fill()
    for i in range(nombre_cotes):
        turtle.fd(long)
        turtle.lt(360/nombre_cotes)
    turtle.end_fill()
    
def ellipse(r,couleur="",disposition = 0):
    '''
        OBJECTIF : Tracer une ellipse de
        METHODE : utilisation de boucle et des méthodes "circle" et "right"
        BESOIN : "r" et "disposition" (ce dernier est facultatif et indique si la figure est verticale ou horizontale)  "couleur"
        CONNUS : /
        ENTREE : "r" et "disposition"
        SORTIE : /
        RESULTAT : /
        HYPOTHESE : "r" et "disposition" sont des nombres reels; on obtient une ellipse horizontale si "disposition" = 0 et verticale dans les autres cas; couleur est une chaîne de caractères qui désigne la couleur de remplissage des figures(c'est un paramètre facultatif)
    '''
    turtle.fillcolor(couleur)
    turtle.begin_fill()
    if disposition == 0:
        turtle.right(45)
    else:
        turtle.left(45)

    for i in range(2):
        turtle.circle(r, 90)
        turtle.circle(r / 2, 90)
    turtle.end_fill()

def aile_gauche(couleur=""):
    '''
        OBJECTIF : Permet de tracer l'aile gauche de l'avion
        METHODE : utilisation des méthodes suivantes du modules "turtle": "fd", "rt" et "seteading"
        BESOINS : /
        CONNUS : /
        ENTREES : /
        SORTIES : /
        RESULTAT : /
        HYPOTHESE : ceci est une procedure avec des mesures prédéfinies
    '''
    turtle.fillcolor(couleur)
    turtle.begin_fill()
    turtle.rt(25)
    turtle.fd(300)
    turtle.rt(45)
    turtle.fd(25)
    turtle.rt(120)
    turtle.fd(285)
    turtle.setheading(0)
    turtle.end_fill()

def aile_droite(couleur=""):
    '''
        OBJECTIF : Permet de tracer l'aile droites de l'avion
        METHODE : utilisation des méthodes suivantes du modules "turtle": "fd", "rt" et "seteading"
        BESOINS : /
        CONNUS : /
        ENTREES : /
        SORTIES : /
        RESULTAT : /
        HYPOTHESE : ceci est une procedure avec des mesures prédéfinies
'''    
    turtle.fillcolor(couleur)
    turtle.begin_fill()
    turtle.lt(25)
    turtle.fd(300)
    turtle.lt(45)
    turtle.fd(25)
    turtle.lt(120)
    turtle.fd(285)
    turtle.setheading(0)
    turtle.end_fill()

def aileron_gauche(couleur=""):
    '''
        OBJECTIF : Permet de tracer l'aileron(queue) gauche de l'avion
        METHODE : utilisation des méthodes suivantes du modules "turtle": "fd", "rt" et "seteading"
        BESOINS : /
        CONNUS : /
        ENTREES : /
        SORTIES : /
        RESULTAT : /
        HYPOTHESE : ceci est une procedure avec des mesures prédéfinies
    '''
    turtle.fillcolor(couleur)
    turtle.begin_fill()
    turtle.rt(160)
    turtle.fd(80)
    turtle.lt(65)
    turtle.fd(50)
    turtle.lt(115)
    turtle.fd(129)
    turtle.setheading(0)
    turtle.end_fill()

def aileron_droite(couleur=""):
    '''
        OBJECTIF : Permet de tracer l'aileron(queue) droite de l'avion
        METHODE : utilisation des méthodes suivantes du modules "turtle": "fd", "rt" et "seteading"
        BESOINS : /
        CONNUS : /
        ENTREES : /
        SORTIES : /
        RESULTAT : /
        HYPOTHESE : ceci est une procedure avec des mesures prédéfinies
    '''
    turtle.fillcolor(couleur)
    turtle.begin_fill()
    turtle.rt(20)
    turtle.fd(80)
    turtle.rt(65)
    turtle.fd(50)
    turtle.rt(115)
    turtle.fd(129)
    turtle.setheading(0)
    turtle.end_fill()

