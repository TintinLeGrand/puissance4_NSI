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
    t = grille
    joueur_pion_rouge = 1
    joueur_pion_jaune = 3
    if (t[y+1, x] == 1) and (t[y+2, x] == 1) and (t[y+3, x] == 1) :
        return True #retourne Vrai si la condition est respecté c'est à dire si les quatres pions de la même couleur sont alignés en l'occurance les pions de couleur rouge.
    if (t[y+1, x] == 3) and (t[y+2, x] == 3) and (t[y+1, x] == 3):
        return True #retourne Vrai si la condition est respecté c'est à dire si les quatres pions de la même couleur sont alignés en l'occurance les pions de couleur jaune.
    else :
        return False #retourne Faux si la condition n'est pas respecté.
    exit() #change de programme

def alignement_oblique_montant(grille):
     ''' Cette fonction renvoie True si 4 pions de même couleur sont alignés
        horizontalement. Elle renvoie False sinon.   '''
     resultat=0
     for ligne in range(6):
        for colonne in range(7):
            if grille[ligne][colonne] == joueur and grille[ligne+1][colonne]== joueur and grille[ligne+2][colonne] == joueur and grille[ligne+3][colonne]== joueur:
                return True
            else:
                return False
            while grille[0][0] == joueur :
                grille[0][0] = grille[0][0] +1
                if (grille[0][0] == joueur) and (grille[1][0]== joueur) and (grille[2][0]== joueur) and (grille[3][0]== joueur) :
                    return True
                exit()
        
def alignement_oblique(grille):
    ''' Cette fonction renvoie True si la grille contient un alignement oblique de 4 pions de même couleur (que ce soit en descendant ou en montant. Sinon elle renvoie False.'''# permet d'exécuter une fonction vide 
    grille_a = alignement_oblique_descendant
    grille_b= alignement_oblique_montant
    if grille_a == True or grille_b == True :
        # si la condition alignement_oblique_descendant et alignement_oblique_montant revoie true s'il y a un alignement de pions de même couleur.
        return True
    else:
        return False

def alignement_oblique_diagonale(grille):
    """Cette fonction permet de vérifier s'il y a un gagnant en vérifiant si 4 jetons sont alignés en diagonale"""
    
    #On vérifie les alignements des diagonales vers le bas
    for i in range(3):
        for j in range(3,7):
            if a[i][j] == 1 and a[i][j] == t[i+1][j-1] and a[i][j] == t[i+2][j-2] and a[i][j] == tab[i+3][j-3]:
                resultat=1
                if a[i][j] == 2 and a[i][j] == tab[i+1][j-1] and a[i][j] == tab[i+2][j-2] and a[i][j] == tab[i+3][j-3]:
                    resultat=2

    #On vérifie les alignements des diagonales vers le haut
                    for i in range(3):
                        for j in range(3,7):
                            if a[i][j] == 1 and a[i][j] == tab[i+1][j+1] and a[i][j] == tab[i+2][j+2] and a[i][j] == tab[i+3][j+3]:
                                resultat=1
                                if a[i][j] == 1 and a[i][j] == tab[i+1][j+1] and a[i][j] == tab[i+2][j+2] and a[i][j] == tab[i+3][j+3]:
                                    resultat=2
                                    return resultat
                                
def alignement_oblique_horizontal(grille):
    resultat=0
    #alignement_oblique_horizontal
    for i in range(6):
        for j in range(4):
            if t[y][x] == 1 and t[x][y] == t[y][x+1] and t[x][y] == t[y][x+2] and t[x][y] == t[y][x+3]:
                resultat=1
                if t[y][x] == 1 and t[x][y] == t[y][x+1] and t[x][y] == t[y][x+2] and t[x][y] == t[y][x+3]:
                    resultat=2

    #alignement_oblique_horizontal vertical
                    for j in range(7):
                        for i in range(3):
                            if a[i][j] == 1 and a[i][j] == a[i+1][j] and a[i][j] == a[i+2][j]and a[i][j] == a[i+3][j]:
                                resultat=1
                                if a[i][j] == 2 and a[i][j] == a[i+1][j] and a[i][j] == a[i+2][j]and a[i][j] == a[i+3][j]:
                                    resultat=2
                                
def victoire_alignement(grille):
    ''' Cette fonction renvoie la vitoire si il y a un alignement oblique de 4 pions de même couleur (que ce soit en descendant ou en montant. Sinon elle renvoie False.'''# permet d'exécuter une fonction vide 
    grille_a = alignement_oblique_descendant
    grille_b= alignement_oblique_montant
    grille_c= alignement_oblique_diagonale
    grille_d= alignement_oblique_horizontal
    if grille_a == True or grille_b == True or grille_c == True or grille_d == True:
        # si la condition alignement_oblique_descendant, alignement_oblique_montant ou alignement_oblique_diagonale ou alignement_oblique_horizontal revoie true s'il y a un alignement de pions de même couleur.
        return True
    else:
        return False
