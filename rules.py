#rules.py

#TODO recommenter
#TODO switch case

import random
import game

######


def new_player_position():
	game.set_player_position( random.randint(0,11) )

def new_bat_position():
	game.set_room_content("bat", game.random_empty_room() )

def new_wumpus_position(wumpus_position):
	game.set_room_content("wumpus", game.random_adjacent_empty_room(wumpus_position))

######
def check_adjacent_rooms():
	"""Fonction qui prend en parametre la position du joueur, une liste avec le contenu des salles et un dictionnaire affectant les salles adjacentes a l index de la salle.
	Elle affiche, en fonction du contenu de la salle, la phrase correspondante.
	"""
	for i in range ( len( game.get_lanes( game.get_player_position() ) ) ) :

		if   game.get_room_content( game.get_lanes( game.get_player_position() )[i] ) == "bat" :
			print "Vous entendez un battement d'aile."

		elif game.get_room_content( game.get_lanes( game.get_player_position() )[i] ) == "cave" :
			print "Vous sentez un courant d'air."

		elif game.get_room_content( game.get_lanes( game.get_player_position() )[i] ) == "wumpus" :
			print "Vous entendez le ronflement du wumpus endormi."


def check_player_position():
	"""Fonction qui prend en parametre la position du joueur et une liste avec le contenu des salles.
	Elle renvoie 2 valeurs : un etat du jeu et une position du joueur.
	Elle verifie les interactions entre le joueur et le contenu de sa salle, et affiche un message d information pour le joueur :
	- Si bat : on deplace le joueur vers une salle aleatoire et on reverifie les interactions dans cette nouvelle salle (par recursivite) puis on retourne un etat ENCOURS et la position du joueur mise a jour.
	On de palce la chauve souris vers une case vide aleatoire.
	- Si puit : renvoie un etat du jeu DEFAITE et la position du joueur mise a jour.
	- Si wumpus: renvoie un etat du jeu DEFAITE et la position du joueur mise a jour.
	- Si rien : renvoie un etat du jeu ENCOURS et la position du joueur mise a jour.
	"""

	if   game.get_room_content( game.get_player_position() ) == "bat" :
		#
		game.set_room_content (None, game.get_player_position() )
		#
		new_player_position()
		new_bat_position()
		#
		print "Une chauve souris vous emporte en case ",game.get_player_position(),"."
		check_player_position()

	elif game.get_room_content( game.get_player_position() ) == "cave" :
		#
		print "Vous etes tombe dans un puit..."
		game.you_lose()

	elif game.get_room_content( game.get_player_position() ) == "wumpus" :
		#
		print "Miom miom miom... Vous avez ete devore par le terrible Wumpus!"
		game.you_lose()

def shooting_result(room_selected):
	#check si wumpus adjacent
	adjacent_wumpus = False

	for i in range( len( ( game.get_lanes( game.get_player_position() ) ) ) ) :
		if game.get_room_content( game.get_lanes( game.get_player_position() )[i] ) == "wumpus" :
			adjacent_wumpus = True
			wumpus_position = game.get_lanes( game.get_player_position() )[i]
			break

	if adjacent_wumpus:
		print "Room_select ", room_selected
		if game.get_room_content( room_selected ) == "wumpus":
			game.you_win()
		else :
			game.set_room_content(None, wumpus_position)
			new_wumpus_position(wumpus_position)
			check_player_position()
	else :
		print "Rien ne se passe..."

	# Si le joueur n'a plus de fleche alors qu'il n'a pas tue le wumpus, il a perdu
	if(game.get_game_status() == "RUNNING" and game.get_arrows() == 0):
		game.you_lose()
