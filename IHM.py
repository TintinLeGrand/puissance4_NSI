import pygame
from pygame.locals import *

def chargement_jeu():
    ''' Cette fonction affiche l'interface graphique du jeu de puissance 4. '''
    global fenetre
    global pionr
    global pionj
    # Création de la fenêtre
    pygame.init()
    fenetre = pygame.display.set_mode((700,700))
    # Chargement des visuels des pions
    pionr = pygame.image.load("images/PionRouge.png").convert_alpha()
    pionj = pygame.image.load("images/PionJaune.png").convert_alpha()
    # Ajout des boutons "Nouvelle partie" et "Quitter"
    bouton_jouer = pygame.image.load("images/bouton jouer.png")
    bouton_sortie = pygame.image.load("images/bouton sortie.png")
    fenetre.blit(bouton_jouer, (0,600))
    fenetre.blit(bouton_sortie, (350,600))
    # Affichage de la fenêtre
    pygame.display.flip()

def affichage_plateau_vide():
    ''' Cette fonction affiche le plateau vide.
        La fonction chargement_jeu() doit avoir été appelée avant. '''
    global fond
    fond = pygame.image.load("images/grille.png")
    fenetre.blit(fond, (0,0))
    pygame.display.flip()

def recuperation_case(pion_x, pion_y):
    ''' Cette fonction renvoie le numéro de ligne et le numéro de colonne de la
        case contenant le pixel (pion_x, pion_y) de l'interface graphique  '''
    return int(pion_y/100), int(pion_x/100)

def collage_du_pion(joueur, num_ligne, num_colonne):
    ''' Cette fonction dessine le pion du joueur donné à la position donnée.
        Le paramètre joueur doit avoir la valeur 1 pour les pions rouges.    '''
    if joueur == 1 : pion = pionr
    else : pion = pionj
    fond.blit(pion, (num_colonne*100,num_ligne*100) )
    fenetre.blit(fond, (0,0))
    pygame.display.flip()

def victoire(joueur):
    ''' Cette fonction affiche le message de victoire pour le joueur donné.
        Le paramètre joueur doit avoir la valeur 1 pour les pions rouges.    '''
    if joueur == 1 : vic = pygame.image.load("images/Rougegagne.png").convert_alpha()
    else : vic = pygame.image.load("images/Jaunegagne.png").convert_alpha()
    fond.blit(vic, (125,140))
    fenetre.blit(fond, (0,0))
    pygame.display.flip()