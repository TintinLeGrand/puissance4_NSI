################################################################################
# Mini projet Puissance 4 à réaliser en équipe de 3
# Le plateau de jeu est modélisé par une liste de 6 éléments représentant les lignes du plateau
# Chaque ligne contient 6 éléments représentant les case du plateau
# La valeur de la case sera 0 pour une case vide ou 1 pour un pion rouge ou 3 pour un pion jaune
# Pour accéder à une case,il faut indiquer son numéro de ligne et son numéro de colonne
# sans oublier que les indices commencent à zéro.
# Ainsi pour la case en haut à gauche (1ère ligne,1ère colonne), on écrira grille[0][0]
#       pour la case en 4e ligne et 2e colonne :  grille[3][1]
################################################################################
# Chacun de vous sera responsable de l'un des modules suivants
# VOTRE travail sera de compléter VOTRE module afin de rendre le jeu fonctionnel.
from gravite import *
from horizontal_vertical import alignement_quadrillage
from oblique import alignement_oblique

####### Le code ci-dessous n'est pas à modifier ################################
import IHM

def nouvelle_partie():
    ''' Cette fonction renvoie une grille vide et le joueur de départ.
        Elle déclenche aussi l'affichage du plateau vide sur l'IHM.    '''
    IHM.affichage_plateau_vide()
    return [[0] * 7 for _ in range(6)], 1

def placement_pion(grille, joueur, num_ligne, num_colonne):
    ''' Cette fonction place le pion du joueur passé en paramètre dans la
        case dont le numéro de ligne et de colonne sont eux aussi passés en
        paramètre. La gravité et l'affichage de la grille dans la console sont
        appliqués si le module gravite a été complété.  '''
    cl = case_libre_la_plus_basse(grille, num_colonne)
    if cl is not None : num_ligne, num_colonne = cl
    grille[num_ligne][num_colonne]= joueur
    affichage_console(grille)
    IHM.collage_du_pion( joueur, num_ligne, num_colonne )

# On affiche la fenêtre d'interface graphique du jeu
IHM.chargement_jeu()
continuer_jeu = True
# On démarre une nouvelle partie
grille, joueur = nouvelle_partie()
# Tant que le jeu continue ...
while continuer_jeu == True :
    # Pour chaque évènement, sur la fenêtre d'interface graphiqe
    for event in IHM.pygame.event.get():
        # Si cet évènement est un clic sur la croix rouge, on stoppe le jeu
        if event.type == IHM.pygame.locals.QUIT:
            continuer_jeu = False
        # Si cet évènement est un clic gauche, on vérifie la zone cliquée
        if event.type == IHM.pygame.locals.MOUSEBUTTONDOWN and event.button == 1:
            pion_x, pion_y = event.pos[0], event.pos[1]
            # Si la zone cliquée est "Nouvelle partie", on démarre une partie partie
            if 0<=pion_x<=349 and 600<=pion_y<=700:
                grille, joueur = nouvelle_partie()
            # Sinon la zone cliquée est "Quitter", on stoppe le jeu
            elif 350<=pion_x<=700 and 600<=pion_y<=700:
                continuer_jeu = False
            # Sinon si la partie n'est pas finie, on identifie la case choisie
            elif not joueur == 0 :
                num_ligne, num_colonne = IHM.recuperation_case(pion_x, pion_y)
                # Si la case est libre, on place le pion du joueur actuel
                if grille[num_ligne][num_colonne] == 0:
                    placement_pion(grille, joueur, num_ligne, num_colonne)
                    # Si le joueur a gagné, on affiche la victoire
                    if alignement_quadrillage(grille) or alignement_oblique(grille) :
                        IHM.victoire(joueur)
                        joueur = 0
                    # Sinon on passe au joueur suivant
                    elif joueur == 1 : joueur = 3
                    else : joueur = 1
# On ferme la fenêtre d'interface graphique du jeu
IHM.pygame.quit()