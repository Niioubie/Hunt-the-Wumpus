#TODO recommenter

import random

#CONSTANTES
BAT_NUMBER = 2
CAVE_NUMBER = 2
WUMPUS_NUMBER = 1
ROOM_NUMBER = 12

game = {'game_status':None, 'player_position':0, 'arrows':0, 'lanes':[], 'room_content':[]}

#ACCESSEURS
def get_game_status():
	return game['game_status']

def get_player_position():
	return game['player_position']

def get_arrows():
	return game['arrows']

def get_lanes(room):
	return (game['lanes'])[room]

def get_room_content(room):
	return (game['room_content'])[room]

def set_player_position(new_position):
	game['player_position'] = new_position

def set_room_content(entity, new_position):
	(game['room_content'])[new_position] = entity

def decrease_arrows():
	game['arrows'] -= 1

def you_win():
	game['game_status'] = "VICTORY"
	print "* Vous avez vaincu le Wumpus."

def you_lose():
	game['game_status'] = "DEFEATE"
	print "* Vous avez perdu."

#FONCTIONS
"""Cette fonction permet de trouver et de retourner une salle vide aleatoire dans le plateau"""
def random_empty_room():
	new_position = random.randint(0,11)

	while get_room_content(new_position) != None or new_position == get_player_position():
		new_position = random.randint(0,11)

	return new_position

"""Cette fonction permet de trouver et de retourner une salle vide aleatoire parmis celles adjacentes a la salle passee en parametre"""
def random_adjacent_empty_room(room):
	new_position = random.randint(0,2)

	while get_room_content( (get_lanes(room))[new_position] ) != None :
		new_position = random.randint(0,2)

	return (get_lanes(room))[new_position]

"""Fonction d'affichage du contenu du plateau"""
def toString():
	print "Room content : "
	for i in range ( len( game['room_content'] ) ):
		print "\t",i," : ", get_room_content(i)

#INIT GAME
def init_game_status():
	game['game_status'] = "RUNNING"

def init_player_position():
	game['player_position'] = random_empty_room()

def init_arrows():
	game['arrows'] = 3

def init_lanes():
	game['lanes'] = [[1,5,6],[0,2,7],[1,3,8],[2,4,9],[3,5,10],[0,4,11],[0,7,11],[1,6,8],[2,7,9],[3,8,10],[4,9,11],[5,6,10]]

def init_room_content():

	for i in range (ROOM_NUMBER):
		game['room_content'].append(None)

	for i in range (BAT_NUMBER):
		new_bat_position = random_empty_room()
		game['room_content'][new_bat_position] = "bat"

	for i in range (CAVE_NUMBER):
		new_cave_position = random_empty_room()
		game['room_content'][new_cave_position] = "cave"

	for i in range (WUMPUS_NUMBER):
		new_wumpus_position = random_empty_room()
		game['room_content'][new_wumpus_position] = "wumpus"
	
def init_game():
	init_game_status()
	init_room_content()
	init_player_position()
	init_arrows()
	init_lanes()

def destroy_previous_game():
	game['lanes'] = []
	game['room_content'] = []
