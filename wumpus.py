# wumpus.py

import random
import game
import rules
import actions
	
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
	print "* Que voulez-vous faire ? \n* 1. Jouer\t2. Quitter"

	#Recuperation du choix du joueur
	option_selected = 0
	while (option_selected != 1 and option_selected != 2):
		try:
			option_selected = int(raw_input("* $> "))
			if(option_selected != 1 and option_selected != 2):
				print "* Ce choix n'est pas valide."

		except ValueError:
			print "* Ce choix n'est pas valide."

	#Debut partie
	while(option_selected == 1):
		print "*\n* Jouons !"
		print "*\n* Histoire blah blah\n* Vous etes cet aventurier et vous vous retrouvez dans ce dedale ou habite un monstre sans pitie..."
		print "* "

		#Initialisation du jeu
		game.destroy_previous_game()
		game.init_game()

		#Boucle principale du jeu
		while(game.get_game_status() == "RUNNING"):

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

			print "* Vous etes dans la salle ",game.get_player_position(),"."
			print "* Il vous reste ",game.get_arrows()," fleche(s)."

			#Verification du contenu des salles adjacentes
			rules.check_adjacent_rooms()

			print "* Que voulez-vous faire ? \n* 1. Se Deplacer\n* 2. Tirer une fleche"

			#Recuperation du choix du joueur
			action_selected = 0
			while (action_selected != 1 and action_selected != 2):
				try:
					action_selected = int(raw_input("* $> "))
					if(action_selected != 1 and action_selected != 2):
						print "* Ce choix n'est pas valide."

				except ValueError:
					print "* Ce choix n'est pas valide."

			#Deplacement
			if(action_selected == 1):
				actions.move()

			#Tire
			elif(action_selected == 2):
				actions.shoot()

		print "* Fin de partie.\n* Voulez-vous rejouer ?\n* 1. Oui\t2. Non"
		#Recuperation du choix du joueur
		option_selected = 0
		while (option_selected != 1 and option_selected != 2):
			try:
				option_selected = int(raw_input("* $> "))
				if(option_selected != 1 and option_selected != 2):
					print "* Ce choix n'est pas valide."

			except ValueError:
				print "* Ce choix n'est pas valide."

	#Fin du jeu
	print "* GRAOAR ! A bientot !"





#Lancement du jeu
run()




