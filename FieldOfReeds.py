# Start of code for FieldOfReeds

# Declare variables
atk = 10
dmg = 10
heroHP = 100
BGHP = 100
correctAnswers = 0

#The space where all the methods will be place

key = input("Press any key to enter")
print("\n")
playerName = input print("Welcome! Press enter a name before playing: ") 
print("\n")
print("You have awoken to discover that you are in a poorly lit room by yourself with vermin. You have no recollection of what happened before this. As you see mounds of sand around you, you believe you are stranded somewhere random in Egypt. The door infront of you looks ancient. You turn the handle of the door and enter through.") 
print("\n")
print("As you enter the room, it appears there is a giant Sphinx infront of you. The room begins to shake and you hear a voice.")
print("\n")
print("I am the Sphinx, answer these riddles to determine your reward mortal!.")
print("\n")

#Sphinx mehtod

def sphinx():
	
# Declarations
	riddleAnswer1 = "Lettuce"
	riddleAnswer2 = "Rain"
	riddleAnswer3 = "Darkness"
	userAnswer1 = input("What has a head, but no brain?")
	userAnswer2 = input("What comes down, but never goes up?")
	userAnswer3 = input("The more of this there is, the less you see… What is it?")

	if userAnswer1 == riddleAnswer1:
		print("That is correct. Onto the next riddle.")
		correctAnswers += 1
	else: 
		print("That is incorrect. Onto the next riddle.")

	if userAnswer2 == riddleAnswer2:
		print("That is correct. Onto the next riddle.")
		correctAnswers += 1
	else: 
		print("That is incorrect. Onto the next riddle.")

	if userAnswer3 == riddleAnswer3:
		print("That is correct. You have heard all my riddles, claim your reward.")
		correctAnswers += 1


# TreasureChest method
def treasureChest():
	weapon = [None, “Dagger, Sword, Battle Axe]

	attackup = [0, 1, 2, 3]

	i = 0

	while correctAnswers < 4 :
	
		if correctAnswers == 1 :
			print(“Your weapon is ” + weapon[i] + “ and plus damage up is ” + attackup[i])
			atk += attackup[i]

		elif correctAnswers == 2 :
			print(“Your weapon is ” + weapon[i+1] + “ and plus damage up is ” + attackup[i+1])
			atk += attackup[i+1]

		elif correctAnswers == 3 :
			print(“Your weapon is ” + weapon[i+2] + “ and plus damage up is ” + attackup[2])
			atk += attackup[i+2]

		elif correctAnswers == 4 :
			print(“Your weapon is ” + weapon[i+3] + “ and plus damage up is ” + attackup[i+3])
			atk += attackup[i+3]
		else:
			print("Somthing went wrong")


print("Narrator 4: After you finish the Sphinx riddles, the Sphinx moves to the side. Depending on what you got correct previously, the greater reward you yield.")

	# Enter the treasure chest room
print("Narrator 3: You've just entered a room to find an armory of weapons that are at your disposal. You see a Sword, Axe, and Dagger. Although they appear to be old and rusted, they're still usable in combat. These will be useful for any deadly foes that you encounter along the way.")


 	#Exit the treasure chest room


   	#Enter the boss room



	#End of the program
