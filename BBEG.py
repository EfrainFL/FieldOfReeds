# BBEG()

# Declarations:
TurnCount = 0
heroAct = "X"
Exit = False

# Temporary Declarations of Global Variables for Testing Purposes
atk = 10
dmg = 10
heroHP = 100
BGHP = 100

def heroTurn():
	retry = True
	while retry == True
		if heroAct == "D":
			dmg = 0
			atk = 0
			retry = False
		else:
			if heroAct == "B":
				dmg = dmg / 2
				atk = atk / 2
				retry = False
			else:
				if heroAct == "A":
					retry = False
				else:
					heroAct = input("Invalid Input. Please Enter 'A' to Attack, 'B' to Block, or 'D' to Dodge:")
					
	return dmg
	return atk
	return heroAct

def BGTurn():
	if TurnCount < 2:
		TurnCount += 1
	else:
		atk = atk / 2
		dmg = 0
		TurnCount = 0
	return atk
	return dmg
	
def calcHP():
	heroHP -= dmg
	BGHP -= atk
	return heroHP
	return BGHP

 
# Monologue
print("Welcome, mortal. I see that you have bested the Sphinx and found your way to my chamber. I am not your enemy, I am simply here to test your resolve one last time. You may have one chance of returning to the land of the living. Best me in combat and I will free your soul, returning you to the life you left behind. Fail, and your soul is mine. Prepare yourself, mortal!")

# User Input
heroAct = input(" [Fight! Choose A to Attack, B to Block, or D to Dodge.]")
	
while Exit == False:

	if BGHP > 0:
		heroTurn()   # Execute the player choice
		
		BGTurn()     # Bad Guy gets a turn. Blocks every 3rd turn
		
		calcHP()     # Calculate final hit points for Hero and BadGuy
		
		print(f"You did {atk} damage. You took {dmg} damage. Your remaining HP is {heroHP}.")
		# endRound
		
		if heroHP > 0:
			heroAct = input("Choose 'A' to Attack, 'B' to Block, or 'D' to Dodge:" )
			
		else:
			print("You have failed. Your soul belongs to me! The shadows surround and consume you. Welcome to Oblivion.")
			Exit = True
			
	else:
		print("You Win! The light swells around you as your soul returns to its earthly vessel.Congratulations!")
		Exit = True

	
