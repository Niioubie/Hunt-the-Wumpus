#actions.py

import game
import rules

def move():
	print "* \n* Vous etes dans la "+str( game.get_player_position() )+"eme salle, dans quelle salle voulez vous aller ?"
				
	for i in range ( len( ( game.get_lanes( game.get_player_position() ) ) ) ) :
		print "* "+str(i+1)+". Salle "+str(game.get_lanes( game.get_player_position() )[i])
	print "*\n* 4. Annuler"

	room_selected = input("* $> ")
	while (room_selected != 1 and room_selected != 2 and room_selected != 3 and room_selected != 4):
		print "Ce choix n'est pas valide."
		room_selected = input("* $> ")

	if(room_selected != 4):
		game.set_player_position( ( ( game.get_lanes( game.get_player_position() ) ) )[room_selected-1] )

		#On met a jour l etat du jeu en fonction du contenu de la nouvelle salle dans lequel le joueur arrive (+messages info)
		rules.check_player_position()

def shoot():
	print "* \n* Ou voulez vous tirer ?"
				
	for i in range ( len( ( game.get_lanes( game.get_player_position() ) ) ) ) :
		print "* "+str(i+1)+". Salle "+str(game.get_lanes( game.get_player_position() )[i])
	print "*\n* 4. Annuler"

	room_selected = input("* $> ")
	while (room_selected != 1 and room_selected != 2 and room_selected != 3 and room_selected != 4):
		print "Ce choix n'est pas valide."
		room_selected = input("* $> ")

	if(room_selected != 4):
		game.decrease_arrows()
		rules.shooting_result(game.get_lanes( game.get_player_position() )[room_selected-1])
		game.toString()