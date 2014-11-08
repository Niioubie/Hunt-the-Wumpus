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

#game_status="ENCOURS"
#room_content=[None]*12
#lanes={0:[1,5,10], 1:[0,2,11], 2:[1,3,6], 3:[2,4,7], 4:[3,5,8], 5:[0,4,9], 6:[2,7,11], 7:[3,6,8], 8:[4,7,9], 9:[5,8,10], 10:[0,9,11], 11:[1,6,10]}
#player_position=-1

def random_empty_room(player_position, room_content):
	"""Fonction qui prend en parametre la position du joueur et une liste avec le contenu des salles.
	Elle renvoie une position aleatoire parmi les salles vides disponibles.
	"""
	new_position = random.randint(0,11)
	while room_content[new_position] != "None" or new_position == player_position:
		new_position = randomp.randint(0,11)
	return new_position
	
def check_adjacent_rooms(player_position, room_content, lanes):
	"""Fonction qui prend en parametre la position du joueur, une liste avec le contenu des salles et un dictionnaire affectant les salles adjacentes a l index de la salle.
	Elle affiche, en fonction du contenu de la salle, la phrase correspondante.
	"""
	for i in range(len(lanes[palyer_position])):
		if room_content[lanes[i]] == "bat" :
			print "Vous entendez un battement d'aile. \n"
		elif room_content[lanes[i]] == "puit" :
			print "Vous sentez un courant d'air. \n"
		elif room_content[lanes[i]] == "wumpus" :
			print "Vous entendez un ronflement de wumpus endormi \n"
			
def check_player_position(player_position, room_content):
	"""Fonction qui prend en parametre la position du joueur et une liste avec le contenu des salles.
	Elle renvoie 2 valeurs : un etat du jeu et une position du joueur.
	Elle verifie les interactions entre le joueur et le contenu de sa salle, et affiche un message d information pour le joueur :
	- Si bat : on deplace le joueur vers une salle aleatoire et on reverifie les interactions dans cette nouvelle salle (par recursivite) puis on retourne un etat ENCOURS et la position du joueur mise a jour.
	On de palce la chauve souris vers une case vide aleatoire.
	- Si puit : renvoie un etat du jeu DEFAITE et la position du joueur mise a jour.
	- Si wumpus: renvoie un etat du jeu DEFAITE et la position du joueur mise a jour.
	- Si rien : renvoie un etat du jeu ENCOURS et la position du joueur mise a jour.
	"""
	if room_content[player_position] == "bat" :
		room_content[player_position] = "None"
		room_content[random_empty_room(player_position, room_content)] = "bat"
		player_position = random.randint(0,11)
		print "Une chauve souris vous emporte en case ", player_position, ". \n"
		return check_player_position(player_position, room_content)
	elif room_content[player_position] == "puit" :
		print "Vous êtes tombé dans un puit. \n"
		return "DEFAITE", player_position
	elif room_content[player_position] == "wumpus" :
		print "Miom Miom Miom... Le wumpus vous a dévoré. \n"
		return "DEFAITE", player_position
	return "ENCOURS", player_position

def init_game(player_position):
	return random.randint(0,12)
	#init tableau contenu
	#init liaison cases
	#position du joueur
	#nombre de fleche
	#retourne le premier resultat de recherche des adjacents
	#calcul_machin_autour()

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
	jouer_quitter = input("* $> ");
	if(jouer_quitter == 1):
		print "*\n* Jouons !"
		print "*\n* Histoire blah blah\n* Vous etes cet aventurier et vous vous retrouvez dans ce dedale ou habite un monstre sans pitie..."
		print "*\n* "
		#init
		#status partie
		game_status = "ENCOURS"
		#position joueur
		player_position = -1
		#player_position = init_game(player_position)
		player_position = 3
		#nombre de fleche
		arrow = 3
		#remplissage des salles
		room_content = [None]*12
		#couloirs
		lanes = {0:[1,5,10], 1:[0,2,11], 2:[1,3,6], 3:[2,4,7], 4:[3,5,8], 5:[0,4,9], 6:[2,7,11], 7:[3,6,8], 8:[4,7,9], 9:[5,8,10], 10:[0,9,11], 11:[1,6,10]}

		#debut partie
		while(game_status == "ENCOURS"):
			print "DEBUG: positionJoueur:"+str(player_position)
			#On verifie les salles adjacentes et on affiche les messages d info.
			check_adjacent_rooms(player_position, room_content, lanes)
			print "* 1.Se Deplacer\n* 2.Tirer une fleche"
			move_shoot = input("* $> ")
			if(move_shoot == 1):
				print "* \n* Vous etes dans la "+str(player_position)+"eme salle, dans quelle salle voulez vous aller ?"
				salles = lanes[player_position]
				for i in range (len(salles)):
					print "* "+str(i+1)+".Salle "+str(salles[i])
				choix_salle = input("* $> ")
				player_position = salles[choix_salle-1]
				#On met a jour l etat du jeu en fonction du contenu de la nouvelle salle dans lequel le joueur arrive (+messages info)
				game_status, player_position = check_player_position(player_position, room_content)




	else:
		print "* GRAOAR ! A bientot !"






run()




