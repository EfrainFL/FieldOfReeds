#beggning of code for FieldOfReeds

#Declare variables
atk = 10
dmg = 10
heroHP = 100
BGHP = 100


playerName = input print("Welcome! Press Enter a name before playing: ") 
#Narrator 1
print("You have awoken to discover that you are in a poorly lit room by yourself with vermin. You have no recollection of what happened before this. As you see mounds of sand around you, you believe you are stranded somewhere random in Egypt. The door infront of you looks like a possible exit if you can find a way to unlock it. Find a means of opening the door.")


#Enter the Sphinax Room

print("Sphinx: Halt! You must solve my riddles in order to proceed.")













print("Narrator 2: Great job! You successfully passed my riddles! You may now proceed to the next rooom.")


print("Narrator 4: After you finish the Sphinx riddles, the Sphinx moves to the side. Depending on what you got correct previously, the greater reward you yield.")

#Enter the treasure chest room
print("Narrator 3: You've just entered a room to find an armory of weapons that are at your disposal. You see a Sword, Axe, and Dagger. Although they appear to be old and rusted, they're still usable in combat. These will be useful for any deadly foes that you encounter along the way.")


weapon = [“None”, “Dagger”, “Sword”, “Battle Axe”]

attackup = [0, 1, 2, 3]

Match correctAnswers:
	case 1:
		print(“Your weapon is ” + weapon[0] + “ and plus damage up is ” + attackup[0])
		atk += attackup[0]

	case 2:
		print(“Your weapon is ” + weapon[1] + “ and plus damage up is ” + attackup[1])
		atk += attackup[1]

	case 3:
		print(“Your weapon is ” + weapon[2] + “ and plus damage up is ” + attackup[2])
		atk += attackup[2]

	case 4:
		print(“Your weapon is ” + weapon[3] + “ and plus damage up is ” + attackup[3])
		atk += attackup[3]

Return








#Enter the Boss Room
#Big Bad Evil Guy Dialog 
print("Welcome to the final room ", playerName " . You have made it very far, but this will be where you will die")

print("Why does the Egypt god Anubis want to fight me!?")

print("Shut Up!!!")

#BBEG()
#Declarations:
TurnCount = 0
heroAct = "X"
Exit = False


def heroTurn():
	if heroAct == "D":
		dmg = 0
		atk = 0
	else:
		if heroAct == "B":
			dmg = dmg / 2
			atk = atk / 2
		else:
			if heroAct != "A":
				heroAct = input("Invalid Input. Please Enter 'A' to Attack, 'B' to Block, or 'D' to Dodge:")
heroTurn()

def BGTurn():
	if TurnCount < 2:
		TurnCount += 1
	if TurnCount >= 4:
		TurnCount = 0
BGTurn()

def calcHP():
	heroHP -= dmg
	BGHP -= atk
calcHP()
 
#Monologue
print("Welcome, mortal. I see that you have bested the Sphinx and found your way to my chamber. I am not your enemy, I am simply here to test your resolve one last time. You may have one chance of returning to the land of the living. Best me in combat and I will free your soul, returning you to the life you left behind. Fail, and your soul is mine. Prepare yourself, mortal!")

#User Input
heroAct = input(" [Fight! Choose A to Attack, B to Block, or D to Dodge.]")
	
while Exit == False:

	if BGHP > 0:
		heroTurn()   #Execute the player choice
		
		BGTurn()     #Bad Guy gets a turn. Blocks every 3rd turn
		
		calcHP() 	 #Calculate final hit points for Hero and BadGuy
		
		print(f"You did {atk} damage. You took {dmg} damage. Your remaining HP is {heroHP}.")
		#endRound
		
		if heroHP > 0:
			heroAct = input("Choose 'A' to Attack, 'B' to Block, or 'D' to Dodge:" )
			
		else:
			print("You have Failed. Your soul belongs to me! The shadows surround and consume you. Welcome to Oblivion.")
			Exit = True
			
	else:
		print("You Win! The light swells around you as your soul returns to its earthly vessel.Congratulations!")
		Exit = True




print("What? How could've I possibly been defeated by a weakling like you? This isn't over, you haven't seen the last of me!")


print("Thank you for playing our game! We hope you had as much fun playing it as we did creating the story!")
