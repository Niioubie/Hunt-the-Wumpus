# Jeu wum pus

# 1. construction du jeu : faire 12 pieces reunies par des couloirs

# Un tableau qui contiendra le contenu de chaque salle
# L'indice du tableau correspond au numero de la salle, sa valeur a son contenu
# exemple : [null, null, puit, null, bat, null, wumpus, bat, null, null, puit, null]

# Un dictionnaire qui associe une case a ses voisins
# exemple : {1: [2,3,4], 2:[5,6,7], ...}

# La position du joueur est retenue dans une variable globale

# Le nombre de fleche aussi

# 2. Etape de jeu, Gameplay

# INIT
# Initialisation du plateau
# Randomisation de la creation de la liste/tableau de contenu de chaque salle
# Randomisation de la position du joueur 
# init du nombre de fleche
# > Cas ou la position du joueur contiendrait deja un element
# Re-Random du calcul de sa position jusqu'a ce qu'il tombe sur une case vide
# Calculer la presence d'elements adjacents : messages console
# On propose au joueur les differentes cases auxquelles il a acces (ie. la liste du dico)
# On propose au joueur de tirer une fleche

# ACTIONS
# Mouvements
# Le joueur decide de se deplacer
# Proposition des cases accessibles
# > Il tape dans la console le numero de la salle
# Calcul de ce qu'il se passe dans la salle
# Si rien, Calcul des voisins et de leurs contenu > message associe
# Proposition cases disponibles + proposition tirer une fleche
# Si il y a quelque chose sur la case > comportement du quelque chose

# Tirer une fleche
# Le joueur choisit de tirer une fleche
# Proposition des cases accessibles
# Calcul du comportement de la fleche avec le contenu de la salle concernee
# Si y'a le wumpus > Victoire
# Sinon si Wumpus a cote > il se reveille et se deplace d'une case random
# Si deplacement sur le joueur > DEFAITE OM NOM NOM NOM
# Sinon rien fleche = fleche -1

# Etat/Effet PVE
# Rien
# Joueur : Rien
# FLeche : Si wmpus a cote de la case du joueur > deplacement wumpus

# Chauve souris
# Joueur : Deplacement random du joueur (+ chauve souris ?)
# FLeche : Si wmpus a cote de la case du joueur > deplacement wumpus

# Puit
# Joueur : PLOUF
# FLeche : Si wmpus a cote de la case du joueur > deplacement wumpus

# Wumpus
# Joueur : DEFAITE
# FLeche : VICTOIRE

# CONDITIONS DE VICTOIRE / DEFAITE
# cf. 

import random
import game
import rules
import actions
import os
	
def run():
	print "*****************************************************************************************************************************"
	print "*  __   __  __   __  __    _  _______    _______  __   __  _______    _     _  __   __  __   __  _______  __   __  _______  *"
	print "* |  | |  ||  | |  ||  |  | ||       |  |       ||  | |  ||       |  | | _ | ||  | |  ||  |_|  ||       ||  | |  ||       | *"
	print "* |  |_|  ||  | |  ||   |_| ||_     _|  |_     _||  |_|  ||    ___|  | || || ||  | |  ||       ||    _  ||  | |  ||  _____| *"
	print "* |       ||  |_|  ||       |  |   |      |   |  |       ||   |___   |       ||  |_|  ||       ||   |_| ||  |_|  || |_____  *"
	print "* |       ||       ||  _    |  |   |      |   |  |       ||    ___|  |       ||       ||       ||    ___||       ||_____  | *"
	print "* |   _   ||       || | |   |  |   |      |   |  |   _   ||   |___   |   _   ||       || ||_|| ||   |    |       | _____| | *"
	print "* |__| |__||_______||_|  |__|  |___|      |___|  |__| |__||_______|  |__| |__||_______||_|   |_||___|    |_______||_______| *"
	print "*                                                                                                                           *"
	print "*****************************************************************************************************************************"
	print "* Bienvenu dans le jeu HUNT THE WUMPUS !"
	print "* Que voulez-vous faire ? : \n* 1.Jouer\t2.Quitter"

	option_selected = input("* $> ")
	while (option_selected != 1 and option_selected != 2):
		print "* Ce choix n'est pas valide."
		option_selected = input("* $> ")

	while(option_selected == 1):
		print "*\n* Jouons !"
		print "*\n* Histoire blah blah\n* Vous etes cet aventurier et vous vous retrouvez dans ce dedale ou habite un monstre sans pitie..."
		print "*\n* "

		#INIT
		game.destroy_previous_game()
		game.init_game()
		game.toString()
		os.system("xterm")

		while(game.get_game_status() == "RUNNING"):

			print "* Vous etes dans la salle ",game.get_player_position(),"."
			print "* Il vous reste ",game.get_arrows()," fleche(s)."

			print "*       0      "
  			print "*     / | \    "
  			print "*   /   6   \  "
  			print "* 5 _  / \  _ 1"
  			print "* |   11  7   |"
  			print "* |   |   |   |"
  			print "* | _ 10  8 _ |"
			print "* 4    \ /    2"
  			print "*   \   9   /  "
  			print "*     \ | /    "
  			print "*       3      "


			rules.check_adjacent_rooms()

			print "* 1.Se Deplacer\n* 2.Tirer une fleche"

			action_selected = input("* $> ")
			while (action_selected != 1 and action_selected != 2):
				print "* Ce choix n'est pas valide."
				action_selected = input("* $> ")

			if(action_selected == 1):
				actions.move()

			elif(action_selected == 2):
				actions.shoot()

		print "* Fin de partie.\n* Voulez-vous rejouer ?\n* 1. Oui\t2. Non"
		option_selected = input("* $> ")
		while (option_selected != 1 and option_selected != 2):
			print "* Ce choix n'est pas valide."
			option_selected = input("* $> ")

	print "* GRAOAR ! A bientot !"






run()




