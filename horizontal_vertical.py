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

def alignement_horizontal(grille):
    ''' Cette fonction renvoie True si 4 pions de même couleur sont alignés
        horizontalement. Elle renvoie False sinon.   '''
    c = 0
    l = 5
    compt = 0
    compt1 = 0
    def ligne():
        while compt1 < 4 :
            if grille[l][c] == 0 :
                compt1 = 5
                
            if grille[l][c] == grille[l][c+1] == grille[l][c+2] == grille[l][c+3]:
                compt1 = 5
                return True
            else :
                compt1 = compt1 + 1
                c = c + 1
                
                
    while compt <= 6 :
        if ligne() == True:
            compt = 7
            return True
        else :
            compt = compt + 1
            l = l - 1
            c = 0
    
    pass     # permet d'exécuter une fonction vide

def alignement_vertical(grille):
    ''' Cette fonction renvoie True si 4 pions de même couleur sont alignés
        verticalement. Elle renvoie False sinon.   '''
    c = 0
    l = 0
    compt = 0
    compt1 = 0
    def ligne():
        while compt1 < 4 :
            if grille[l][c] == 0 :
                compt1 = 5
                
            if grille[l][c] == grille[l+1][c] == grille[l+2][c] == grille[l+3][c]:
                compt1 = 5
                return True
            else :
                compt1 = compt1 + 1
                l = l + 1
                
                
    while compt <= 6 :
        if ligne() == True:
            compt = 7
            return True
        else :
            compt = compt + 1
            c = c + 1
            l = 0
    pass     # permet d'exécuter une fonction vide

def alignement_quadrillage(grille):
    ''' Cette fonction renvoie True si la grille contient un alignement
        horizontal ou vertical de 4 pions de même couleur.
        Sinon elle renvoie False. '''
    
    if alignement_horizontal(grille) or alignement_vertical(grille) == True:
        return True
    else :
        return False
    pass     # permet d'exécuter une fonction vide
