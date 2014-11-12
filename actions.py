#actions.py

import game
import rules

"""Fonction de deplacement du joueur"""
def move():
	print "* \n* Vous etes dans la "+str( game.get_player_position() )+"eme salle, dans quelle salle voulez vous aller ?"
	
	#Liste des salles accessibles
	for i in range ( len( ( game.get_lanes( game.get_player_position() ) ) ) ) :
		print "* "+str(i+1)+". Salle "+str(game.get_lanes( game.get_player_position() )[i])
	print "*\n* 4. Annuler"

	#Recuperation du choix du joueur
	room_selected = 0
	while (room_selected != 1 and room_selected != 2 and room_selected != 3 and room_selected != 4):
		try:
			room_selected = int(raw_input("* $> "))
			if(room_selected != 1 and room_selected != 2 and room_selected != 3 and room_selected != 4):
				print "* Ce choix n'est pas valide."

		except ValueError:
			print "* Ce choix n'est pas valide."

	#Deplacement du joueur et consequences
	if(room_selected != 4):
		game.set_player_position( ( ( game.get_lanes( game.get_player_position() ) ) )[room_selected-1] )
		rules.check_player_position()

"""Fonction de tire du joueur"""
def shoot():
	print "* \n* Ou voulez vous tirer ?"
				
	#Liste des salles accessibles
	for i in range ( len( ( game.get_lanes( game.get_player_position() ) ) ) ) :
		print "* "+str(i+1)+". Salle "+str(game.get_lanes( game.get_player_position() )[i])
	print "*\n* 4. Annuler"

	#Recuperation du choix du joueur
	room_selected = 0
	while (room_selected != 1 and room_selected != 2 and room_selected != 3 and room_selected != 4):
		try:
			room_selected = int(raw_input("* $> "))
			if(room_selected != 1 and room_selected != 2 and room_selected != 3 and room_selected != 4):
				print "* Ce choix n'est pas valide."

		except ValueError:
			print "* Ce choix n'est pas valide."

	#Tire et consequences
	if(room_selected != 4):
		game.decrease_arrows()
		rules.shooting_result(game.get_lanes( game.get_player_position() )[room_selected-1])