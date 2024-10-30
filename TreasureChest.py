# Start
def treasureChest():
	weapon = [“None”, “Dagger”, “Sword”, “Battle Axe”]

	attackup = [0, 1, 2, 3]

	i = 0

	Match correctAnswers :
	
		case 1 :
			print(“Your weapon is ” + weapon[i] + “ and plus damage up is ” + attackup[i])
			atk += attackup[i]

		case 2 :
			print(“Your weapon is ” + weapon[i+1] + “ and plus damage up is ” + attackup[i+1])
			atk += attackup[i+1]

		case 3 :
			print(“Your weapon is ” + weapon[i+2] + “ and plus damage up is ” + attackup[2])
			atk += attackup[i+2]

		case 4 :
			print(“Your weapon is ” + weapon[3] + “ and plus damage up is ” + attackup[3])
			atk += attackup[3]

# Return
