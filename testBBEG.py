# BBEG() ** WORKING **
#Print colors to identify errors/print statements and for aesthetics during final presentation
def prRed(skk): print("\033[91m {}\033[00m" .format(skk))			#Print Red
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))			#Print Green
def prCyan(skk): print("\033[96m {}\033[00m" .format(skk))			#Print Cyan

# Declarations:
TurnCount = 0							#Turn Counter for BadGuy Turn
heroAct = "X"							#Default Value for Hero Action
Exit = False							#Exit becomes True when Hero or BadGuy HP drops to 0

heroHP = 50                          	# Starting HP for Hero
BGHP = 50                             	# Starting HP for BadGuy                          
BGatk = 10  							# BadGuy Attack damage. Can be increased for higher difficulty
#dmg = 10								# Default damage taken by hero - reassigned to BGatk
atk = 10								# Hero Attack damage

# Monologue
prRed("Welcome, mortal. \n\nI see that you have bested the Sphinx and found your way to my chamber. \nI am not your enemy, I am simply here to test your resolve one last time. \nYou may have one final chance of returning to the land of the living. Best me in combat and I will free your soul, returning you to the life you left behind. \n\nFail, and your soul is mine. Prepare yourself, human! Your fate is at hand!")

# User Input
heroAct = input("\n Fight! [Choose A to Attack, B to Block, or D to Dodge.]: ")
	
while Exit == False:					#Repeat Hero Turn, BadGuy Turn, and HP Calculation until either HP reaches 0

	if BGHP > 0:						#While BadGuy HP is greater than 0, Exit value remains False
		
		retry = True					#Retry if Invalid Input

		while retry:					#Loop to determine Hero Action 

			if heroAct == "A":			#Attack: Take and Deal Full Damage
				prCyan(f"\nYou attack with your ______!")
				dmg = BGatk
				atk = atk			
				retry = False			#Valid Input, Do not retry
			
	
			elif heroAct == "D":		#Dodge:
					prCyan(f"\nYou roll out of the way of the incoming attack!")
					dmg = 0				#Take 0 Damage
					atk = 0				#Deal 0 Damage
					retry = False		#Valid Input, Do not retry

			elif heroAct == "B":		#Block:
					prCyan(f"\nYou parry with the back of your weapon before delivering your riposte!")
					dmg = BGatk / 2		#Take Half Damage
					atk = atk / 2		#Deal Half Damage
					retry = False		#Valid Input, Do not retry
			else:
					heroAct = input("Invalid Input. Please Enter 'A' to Attack, 'B' to Block, or 'D' to Dodge:")
										#If No Valid Input, Return Error Message and Ask Again. Retry remains True

		if TurnCount < 2:				#BadGuy Attacks twice, then Blocks on every 3rd Turn
			prRed("\nAnubis attacks you with his kopesh!")							
			TurnCount += 1				#Increment the Turn Count variable

		else:							#When Turn Count reaches 3, BadGuy Blocks
			prGreen("\nAnubis blocks your attack with his shield!")
			atk = atk / 2				#BadGuy takes half damage from Hero's Attack
			dmg = 0						#BadGuy deals no damage when blocking
			TurnCount = 0				#Resets the Turn Counter to 0 

			
		heroHP -= dmg					#Reduce Hero HP by damage done by BGTurn() (dmg)

		BGHP -= atk						#Reduce BadGuy HP by damage done by heroTurn() (atk)
	
										#If Either HP Total reaches 0, Exit = True and the fight is over

		
				
										#Display the results of each round of Combat
		prCyan(f"\n\nYou did {atk} points of damage to Anubis. You took {dmg} points of damage. Your remaining HP is {heroHP}.\n")

		prRed(f"Anubis has {BGHP} HP left.\n")
		if BGHP < 5:
			prRed("The ancient god falls to his knees before you, defeated. Finish Him!\n")

		atk = 10						#Reset Hero Attack to initial value
		BGatk = 10						#Reset BadGuy Attack to initial value
		
												#End of Round
		
		if heroHP > 0:							#While Hero HP is greater than 0, Exit value remains False
			heroAct = input("Choose 'A' to Attack, 'B' to Block, or 'D' to Dodge:" )
			
		else:						#If Hero HP drops to 0, player loses and Exit value becomes True
			print("You have failed. Your soul belongs to me! The shadows surround and consume you. Welcome to Oblivion.")
			Exit = True
			
	else:							#If BadGuy HP drops to 0, player wins and Exit Value becomes True
		print("You Win! The light swells around you as your soul returns to its earthly vessel. Congratulations!")
		Exit = True
