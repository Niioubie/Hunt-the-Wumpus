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

"""Cette fonction affiche une phrase indicative au joueur pour chaque salle non vide adjacente a sa position"""
def check_adjacent_rooms():
	print "*"
	for i in range ( len( game.get_lanes( game.get_player_position() ) ) ) :
		if   game.get_room_content( game.get_lanes( game.get_player_position() )[i] ) == "bat" :
			print "* Vous entendez un battement d'aile."

		elif game.get_room_content( game.get_lanes( game.get_player_position() )[i] ) == "cave" :
			print "* Vous sentez un courant d'air."

		elif game.get_room_content( game.get_lanes( game.get_player_position() )[i] ) == "wumpus" :
			print "* Vous entendez le ronflement du wumpus endormi."
	print "*"

"""Cette fonction verifie les interactions entre le joueur et le contenu de sa salle"""
def check_player_position():
	#Si la salle contient une chauve souris
	if   game.get_room_content( game.get_player_position() ) == "bat" :
		#On vide le contenu de la salle sur laquelle on se trouve
		game.set_room_content (None, game.get_player_position() )
		#On choisit ensuite une nouvelle position aleatoire pour le joueur (vide ou pas)
		new_player_position()
		#et pour la chauve souris (nouvelle salle vide)
		new_bat_position()
		print "* Une chauve souris vous emporte en case ",game.get_player_position(),"."
		#On reverifie ensuite l'interaction entre joueur et le contenu de la nouvelle salle
		check_player_position()

	#Sinon si c'est un puit
	elif game.get_room_content( game.get_player_position() ) == "cave" :
		#Le joueur a perdu
		print "* Vous etes tombe dans un puit..."
		game.you_lose()

	#Sinon si c'est le Wumpus
	elif game.get_room_content( game.get_player_position() ) == "wumpus" :
		#Le joueur a perdu
		print "* Miom miom miom... Vous avez ete devore par le terrible Wumpus!"
		game.you_lose()

def shooting_result(room_selected):
	#Booleen indiquant si le Wumpus est dans une salle adjacente
	adjacent_wumpus = False

	#Pour toutes les salles adjacentes
	for i in range( len( ( game.get_lanes( game.get_player_position() ) ) ) ) :
		#Si on trouve le wumpus, on passe le booleen a vrai
		if game.get_room_content( game.get_lanes( game.get_player_position() )[i] ) == "wumpus" :
			adjacent_wumpus = True
			wumpus_position = game.get_lanes( game.get_player_position() )[i]
			break

	#Si le Wumpus est dans une salle adjacente on verifie si le joueur tire dans sa salle ou non
	if adjacent_wumpus:
		if game.get_room_content( room_selected ) == "wumpus":
			game.you_win()
		else :
			game.set_room_content(None, wumpus_position)
			new_wumpus_position(wumpus_position)
			check_player_position()
	#Sinon rien
	else :
		print "* Rien ne se passe..."

	# Si le joueur n'a plus de fleche alors qu'il n'a pas tue le wumpus, il a perdu
	if(game.get_game_status() == "RUNNING" and game.get_arrows() == 0):
		print "* Vous n'avez plus de fleche."
		game.you_lose()
