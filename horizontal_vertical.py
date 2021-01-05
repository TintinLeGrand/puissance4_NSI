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
    l = 5
    c = 0
    for ligne in range (6):
        for colonne in range (4):
            if grille[l][c] == grille[l][c+1] == grille[l][c+2] == grille[l][c+3]: 
                if grille[l][c] == 0 :   #Permet d'empécher la victoire en cas de ligne vide
                    None
                else :
                    return True
                    break
            else :
                c = c + 1
        l = l - 1    #Permet de tester la ligne du dessus
        c = 0    #Réinitialise c

def alignement_vertical(grille):
    ''' Cette fonction renvoie True si 4 pions de même couleur sont alignés
        verticalement. Elle renvoie False sinon.   '''
    lv = 0
    cv = 0
    for ligne in range (7):
        for colonne in range (3):
            if grille[lv][cv] == grille[lv+1][cv] == grille[lv+2][cv] == grille[lv+3][cv]:
                if grille[lv][cv] == 0 :    #Permet d'empécher la victoire en cas de colonne vide
                    None
                else :
                    return True
                    break
            else :
                lv = lv + 1
        cv = cv + 1    #Permet de tester la colonne suivante
        lv = 0    #Réinitialise lv

def alignement_quadrillage(grille):
    ''' Cette fonction renvoie True si la grille contient un alignement
        horizontal ou vertical de 4 pions de même couleur.
        Sinon elle renvoie False.'''
    
    if alignement_horizontal(grille) or alignement_vertical(grille) == True:
        return True
    else :
        return False