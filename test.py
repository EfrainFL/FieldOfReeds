
# BBEG()

# Declarations:
TurnCount = 0							#Turn Counter for BadGuy Turn
heroAct = "X"							#Default Value for Hero Action
Exit = False							#Exit becomes True when Hero or BadGuy HP drops to 0

heroHP = 100                            # Starting HP for Hero
BGHP = 100                              # Starting HP for BadGuy                           # Hero's attack damage
BGATK = 10  
dmg = 10
atk =10

# Monologue
print("Welcome, mortal. I see that you have bested the Sphinx and found your way to my chamber. I am not your enemy, I am simply here to test your resolve one last time. You may have one chance of returning to the land of the living. Best me in combat and I will free your soul, returning you to the life you left behind. Fail, and your soul is mine. Prepare yourself, mortal!")

# User Input
heroAct = input(" [Fight! Choose A to Attack, B to Block, or D to Dodge.]")
	
while Exit == False:							#Repeat Hero Turn, BadGuy Turn, and HP Calculation until either HP reaches 0

	if BGHP > 0:								#While BadGuy HP is greater than 0, Exit value remains False
		
		retry = True							#Retry if Invalid Input

		while retry:					#Loop to determine Hero Action 

			if heroAct == "A":
				dmg = BGATK
				atk = atk			#Attack: Take and Deal Full Damage
				retry = False			#Valid Input, Do not retry
			
	
			elif heroAct == "D":					#Dodge:
					dmg = 0							#Take 0 Damage
					atk = 0							#Deal 0 Damage
					retry = False					#Valid Input, Do not retry

			elif heroAct == "B":				#Block:
						dmg = BGATK / 2				#Take Half Damage
						atk = atk / 2				#Deal Half Damage
						retry = False				#Valid Input, Do not retry
			else:
						heroAct = input("Invalid Input. Please Enter 'A' to Attack, 'B' to Block, or 'D' to Dodge:")
												#If No Valid Input, Return Error Message and Ask Again. Retry remains True

		if TurnCount < 2:						#BadGuy Attacks twice, then Blocks on every 3rd Turn	
			TurnCount += 1						#Increment the Turn Count variable

		else:									#When Turn Count reaches 3, BadGuy Blocks
			atk = heroATK / 2						#BadGuy takes half damage from Hero's Attack
			dmg = 0								#BadGuy deals no damage when blocking
			TurnCount = 0						#Resets the Turn Counter to 0 

			
		heroHP -= dmg							#Reduce Hero HP by damage done by BGTurn() (dmg)

		BGHP -= atk								#Reduce BadGuy HP by damage done by heroTurn() (atk)
	
												#If Either HP Total reaches 0, Exit = True and the fight is over

		
				
												#Display the results of each round of Combat
		print(f"You did {atk} damage. You took {dmg} damage. Your remaining HP is {heroHP}.")
		
												#End of Round
		
		if heroHP > 0:							#While Hero HP is greater than 0, Exit value remains False
			heroAct = input("Choose 'A' to Attack, 'B' to Block, or 'D' to Dodge:" )
			
		else:						#If Hero HP drops to 0, player loses and Exit value becomes True
			print("You have failed. Your soul belongs to me! The shadows surround and consume you. Welcome to Oblivion.")
			Exit = True
			
	else:							#If BadGuy HP drops to 0, player wins and Exit Value becomes True
		print("You Win! The light swells around you as your soul returns to its earthly vessel. Congratulations!")
		Exit = True

	
