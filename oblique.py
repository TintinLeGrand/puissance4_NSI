################################################################################
# Votre travail consiste à compléter les fonctions ci-dessous afin de          #
#  contribuer à la détection d'une victoire                                    #
################################################################################
# Il s'agit bien sûr de respecter scrupuleusement les specifications.
# Un commentaire pour les lignes de code non triviales est exigé.
# Pour tester votre script, il suffit d'exécuter le programme JeuPuissance4.
# Le jeu se joue avec la souris uniquement, les joueurs se la passe à tour de role.
# Si vos fonctions sont justes alors le jeu fonctionnera !
# Bon courage.

#PREVEL Evan 103 oblique.py

def alignement_oblique_descendant(grille):
     ''' Cette fonction renvoie True si la grille contient un alignement oblique
        descendant de 4 pions de même couleur. Sinon elle renvoie False. '''
        
    pass     # permet d'exécuter une fonction vide
    t = grille #definit la variable grille
    #1 = pion rouge
    #3 = pion jaune
    if (t[y+1, x] == alignement_oblique_descendant) and (t[y+2, x] == alignement_oblique_descendant) and (t[y+1, x] == alignement_oblique_descendant) :
        return True #retourne Vrai si la condition est respecté c'est à dire si les quatres pions de la même couleur sont alignés.
    else :
        return False ##retourne Faux si la condition est respecté c'est à dire si les quatres pions de la même couleur sont alignés.
    exit()

#IHM = joueur pour le pion rouge = 1 et le pion jaune = 3

def alignement_oblique_descendant(grille):
    t = grille
    joueur_pion_rouge = 1
    joueur_pion_jaune = 3
    if (t[y+1, x] == 1) and (t[y+2, x] == 1) and (t[y+3, x] == 1) :
        return True #retourne Vrai si la condition est respecté c'est à dire si les quatres pions de la même couleur sont alignés en locurance ici les pions de couleurs rouge.
   if (t[y+1, x] == 3) and (t[y+2, x] == 3) and (t[y+1, x] == 3) :
       return True #retourne Vrai si la condition est respecté c'est à dire si les quatres pions de la même couleur sont alignés en locurance les pions de couleurs jaune.
    else :
        return False #retourne Faux si la condition n'est pas respecté.
    exit() #change de programme

def alignement_oblique_descendant(grille):
    pion rouge = 1 #defini le caractère du pion rouge
    pion jaune = 3 #defini le caractère du pion jaune
    if (grille[0][0] == 1) and (grille[0][1]== 1) and (grille[0][2]== 1) and (grille[0][3]== 1) :
        return True  #retourne Vrai si la condition est respecté c'est à dire si les pions de la même couleur sont aligné sur la même colonne.
   if (grille[0][0] == 3) and (grille[0][1] == 3) and (grille[0][2]== 3) and (grille[0][3]== 1)
       return True #retourne Vrai si la condition est respecté c'est à dire si les pions de la même couleur sont aligné sur la même ligne.
    else :
        return False # retourne Faux si la condition n'est pas validé.
    exit()

    #pass     # permet d'executer une fonction vide

def alignement_oblique_montant(grille):
     ''' Cette fonction renvoie True si 4 pions de même couleur sont alignés
        horizontalement. Elle renvoie False sinon.'''

    if (grille[0][0] == joueur) and (grille[1][0]== joueur) and (grille[2][0]== joueur) and (grille[3][0]== joueur) :
        return True
    else:
        return False
    exit()

    while grille[0][0] == joueur :
        grille[0][0] = grille[0][0] +1
        if (grille[0][0] == joueur) and (grille[1][0]== joueur) and (grille[2][0]== joueur) and (grille[3][0]== joueur) :
            return True
        exit()

def alignement_oblique_montant(grille):
     ''' Cette fonction renvoie True si 4 pions de mÃªme couleur sont alignÃ©s
        horizontalement. Elle renvoie False sinon.   '''
    pass     # permet d'exécuter une fonction vide
    #for x in grille: #on cherche la grille x
        #for y in grille: #on cherche la grille y
            if (t[y+1, x] == 1) and (t[y+2, x] == 1) and (t[y+3, x] == 1) :
                if (t[y , x+1] == 1) and (t[y, x]+2 == 1) and (t[y, x+3] == 1) :
                    return True #Retourne vrai si il ya un alignement de pion de même couleur dans la grille x ou la grille y
            else:
                return False #retourne Faux si la condition n'est pas respecter.

            if (t[y+1, x] == 3) and (t[y+2, x] == 3) and (t[y+3, x] == 3) :
                if (t[y , x+1] == 3) and (t[y, x]+2 == 3) and (t[y, x+3] == 3) :
                    return True
                else:
                    return False
    exit()

    while t[y+1, x] == 1 == joueur :
        x = x +1
        if (t[y+1, x] == 1 == joueur) and (t[y+1, x] == 1== joueur) and (t[y+1, x] == 1== joueur) and (t[y+1, x] == 1== joueur) :
            return True
        exit()


    #pass     # permet d'exÃ©cuter une fonction vide


def alignement_oblique(grille):
    ''' Cette fonction renvoie True si la grille contient un alignement oblique
        de 4 pions de même couleur (que ce soit en descendant ou en montant.
        Sinon elle renvoie False. '''
    pass     # permet d'exécuter une fonction vide 
    grille_a = alignement_oblique_descendant
    grille_b= alignement_oblique_montant
    if grille_a == True and grille_b = True : # si la condition alignement_oblique_descendant et alignement_oblique_montant revoie true s'il y a un alignement de pions de même couleur.
        return True
    else:
        return False
    pass     # permet d'exÃ©cuter une fonction vide
