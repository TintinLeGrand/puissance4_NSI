################################################################################
# Votre travail consiste à compléter les fonctions suivantes afin de pouvoir   #
# afficher la grille dans la console et de rétablir la gravité pour les pions  #
################################################################################
# Il s'agit bien sûr de respecter scrupuleusement les specifications.
# Un commentaire pour les lignes de code non triviales est exigé.
# Pour tester votre script, il suffit d'exécuter le programme JeuPuissance4.
# Le jeu se joue avec la souris uniquement, les joueurs se la passe à tour de role.
# Si vos fonctions sont justes alors le jeu fonctionnera !
# Bon courage.


def affichage_console(grille):
    ''' Cette fonction affiche la grille dans la console.
        Chaque ligne de la grille est affichée sur une ligne différente dans le console.
        Un séparateur est affiché après la grille.
    '''
    affichage=''
    for ligne in range(6):
        for colonne in range(7):
            affichage=affichage+str(grille[ligne][colonne])
        affichage=affichage+'\n'
    affichage=affichage+'\n'+'-------------------------'
    print (affichage)

def case_libre_la_plus_basse(grille,num_colonne):
    '''Cette fonction renvoie la case libre la plus basse de la colonne donnée.
    Si la colonne est pleine, cette fonction renverra None.
    entrée:
    -grille: tableau de 6 lignes et 7 colonnes représentant le plateau du jeu
    -num_colonne: numéro de la colonne à analyser
    retour:
    -(num_ligne,num_colonne) correspondant au numéro de ligne et au numéro de colonne de la case vide la plus basse dans la colonne donnée.
    '''
    y=0
    for test in range(6):
        '''Cette boucle permet de vérifier de la case la plus basse à la case la plus haute de la colonne s'il y en a une qui est vide. Si une est vide, la boucle s'arrête grâce à la ligne 35 et cela renvoie le numéro de la ligne où la case est vide'''
        if grille[5-test][num_colonne]==0:
            y=1
            num_ligne=int(5-test)
            break
        else:
            None
    if y==0:
        '''Si ici y vaut 0, soit si aucune des 6 lignes de la colonne est égal à 0, alors la ligne est complète et aucun pion ne sera placé : la fonction ne renvoie rien et le joueur doit choisir une autre case.'''
        return None
    return (num_ligne,num_colonne)
