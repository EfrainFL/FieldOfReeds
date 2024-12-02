import os                   #Import OS to use clear screen command

atk = 10
dmg = 15
heroHP = 100
BGHP = 100
correctAnswers = 0
Sword = "Sword"
Dagger = "Dagger"
Axe = "Axe"
Nothing = "Nothing"
i = 0
playerName = ""
weaponName = ""

def prRed(skk): print("\033[91m {}\033[00m".format(skk))  # Red
def prGreen(skk): print("\033[92m {}\033[00m".format(skk))  # Green
def prYellow(skk): print("\033[93m {}\033[00m".format(skk))  # Yellow
def prBlue(skk): print("\033[94m {}\033[00m".format(skk))  # Blue
def prMagenta(skk): print("\033[95m {}\033[00m".format(skk))  # Magenta
def prCyan(skk): print("\033[96m {}\033[00m".format(skk))  # Cyan

def EyeOfRa():
    os.system('clear')
    prYellow("                              ..,,,,,,,,,,,,,,,.                                ")
    prYellow("                      ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,.                      ")
    prYellow("              ,,,,,,,,,,,,,,,,,,.                ,,,,,,,,,,,,,,,,,              ")
    prYellow("  .,,,,,,,,,,,,,,,,,,,,             ,,,,,,,,,              .,,,,,,,,,,,,,,,,,,,,")
    prYellow("  ,,,,,,,,,,,,,.        .,,,,,,,,,,,,,,,,,,,,,,,,,,,,,.            .,,,,,,,,,,,,")
    prYellow("  ,,,.         .,,,,,,,,,,,,,,. ,,,,,,,,,,,,,,   .,,,,,,,,,,,,                  ")
    prYellow("      .,,,,,,,,,,,,.            ,,,,,,,,,,,,,,,            ,,,,,,,,,,,,,,,,,,,,,")
    prYellow(" .,,,,,,,,,,.                   ,,,,,,,,,,,,,,                  ,,,,,,,,,,,,,,,,")
    prYellow(" .,,,,,,,,,,,,.                  .,,,,,,,,,,,                  .,,,,,,,,,.      ")
    prYellow("        .,,,,,,,,,,,,.                ...                  ,,,,,,,,,            ")
    prYellow("                .,,,,,,,,,,,,,,,,,,,,         ,,,,,,,,,,,,,,,,,,,               ")
    prYellow("                        .,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,                ")
    prYellow("                                               .,,,,,,,,   ,,,,                 ")
    prYellow("     .,,,,.                                  .,,,,,,,,     ,,,,                 ")
    prYellow("  ,,.   ,,,,,.                             ,,,,,,,,.      ,,,,,,,               ")
    prYellow(" ,.     ,,,,,.                          ,,,,,,,,,        .,,,,,,,,              ")
    prYellow(",,                                   ,,,,,,,,,           ,,,,,,                 ")
    prYellow(" ,                                ,,,,,,,,,.            .,,,,                   ")
    prYellow(" ,,                            ,,,,,,,,,                .,,.                    ")
    prYellow("  .,,                      ,,,,,,,,,,                   .,.                     ")
    prYellow("    .,,,             .,,,,,,,,,,,                        ,                      ")
    prYellow("        ,,,,,,,,,,,,,,,,,,,.                             ,                      ")
    prYellow("              .. .                                                              ")


def main_intro():
    global playerName
    
    name = "\n\n{:^80}".format("Please Enter Your Name: " )
    playerName = input(name + "\n") 
    
    os.system('clear')            #clear screen
    
    darkness = "\n\n{:^80}".format("Darkness Surrounds You")
    
    prCyan(darkness)
    
    key = input("...\n") 
    
    os.system('clear')            #clear screen
    
    prCyan(" Hey, You! You're finally Awake... \n\nAs your awareness returns to you, you find yourself walking up the shifting slope of a sand dune. \nA sickle of a moon shines down on you, illuminating the seemingly endless sea of sand that surrounds you. \nYou feel as though you have been walking for days, possibly weeks. Time has long since lost all meaning to you. \nYour eyes and throat are parched and dry, your skin caked with sand. You can't remember ever being this thirsty \nbefore in your entire Life. The cool caress of water against your lips feels like nothing more than a distant memory. \nYou have no idea where you are or how you got here, all you can remember is the endless sand. \n\nIt's Coarse, and Rough, and Irritating... and it is Everywhere.\n") 
    
    key = input("...\n")

    prCyan("\n You stumble forward, nearly blind, moving through the sheer force of Will, alone. As the last of your resolve threatens to leave you, \nyour hands come into contact with rough-hewn wood, bound with metal. \n\nA Door.") 
    
    key = input("\nPress Enter to Open the Door.")
    
    os.system('clear')            #clear screen 
   
    prCyan(f" Desperate for shelter, you pull at the handles with all your remaining strength. For a moment, the door does not budge. \nThen, with a sound no louder than a whisper, it swings effortlessly open, revealing a long corridor of smooth stone, \nexpertly fitted together so that the seams between the massive blocks are almost imperceptible. \n\n You wander the dimly lit halls and stone corridors of the labyrinth, passing frescoes and carvings of strange creatures; \nbirds with the heads of women and men, human bodies with the heads of various animals... \nThe image of a giant set of scales adorns one wall. \nYou walk down endless corridors, dimly lit by an unseen source; unlit torches occupy sconces every few meters \nyet produce no smoke, nor flame, nor light. \n\n After some time, a faint noise reaches your ears. At first you think they are playing tricks on you, \nbut as you get closer to the source of the sound, you realize that it is, in fact, the sound of falling water. \nDesperate for moisture, your tongue feels like sandpaper as it tries, in vain, to wet your cracked and bleeding lips. \nThe prospect of quenching your agonizing thirst pulls you forward toward the sound of water. \n\n As you turn a corner, you step into a vast chamber, the ceiling and far walls shrouded in darkness. The sounds of water \ncome from a trickle of a waterfall that descends from the darkness above you as it splashes into a seemingly endless expanse of \ndark water that extends into the distance of the cavelike room. \n\n Before the deathly still pool sits a massive Sphinx, its paws crossed in front of itself, eyes closed. At first you think \nit is a statue until it opens one great, golden eye and looks down at you with a sharp-toothed smile. \nThe voice of the massive beast rumbles through the cavernous space:")

    prYellow(f"\n Come in {playerName}. I have been expecting you. Come have a drink and sit with me.")
    
    key = input("...\n")
    
    prCyan("Despite his massive size, the Sphinx is a gracious host. He provides you with cool water to drink and gives you a few minutes \nto rest on the soft sand by the endless underground sea, making occasional polite conversation. \nAfter a time, the guardian speaks once more:")
    
    prYellow("\n Now that you have found a moment of respite, I regret that I must send you on your way. \n Who would cross the Lake of Death must Answer Me these Riddles Three, ere the other side ye see...\n When you are ready, proceed to determine your reward.")
    
    key = input("\n\nPress Enter to hear the First Riddle.")
    os.system('clear')


# Sphinx method
def sphinx():
    global correctAnswers
    global playerName
    wrongAnswers = 0
    riddleAnswer1 = "Lettuce"
    riddleAnswerA = "lettuce"
    riddleAnswer2 = "Rain"
    riddleAnswerB = "rain"
    riddleAnswer3 = "Darkness"
    riddleAnswerC = "darkness"
    #riddleAnswer3 = "Aces"             #Alternate Riddle Answer

    userAnswer1 = input("\n\n I am one of many on the field with no body, nor eyes, nor mouth, or nose. I am a head with no brain. What am I?  ")

    if userAnswer1 == riddleAnswer1 or  userAnswer1 == riddleAnswerA:
        correctAnswers += 1
        prCyan("\nThe Sphinx nods solemnly, then smirks.")
        prYellow(f"\n Well done, human. You have answered {correctAnswers} correctly. You are smarter than you look.\n")
        key = input("\nPress Enter to proceed.")
        
    else: 
        wrongAnswers += 1
        prCyan("\nThe Sphinx shakes his great head sadly.")
        prYellow(f"\n That is incorrect. You have answered {correctAnswers} correctly and have gotten {wrongAnswers} wrong. A pity.\n")
        key = input("\nPress Enter to move on to the next riddle.")

    userAnswer2 = input("\n It is said that that which goes up must come down. But what comes down, yet never goes up? ")
    
    if userAnswer2 == riddleAnswer2 or userAnswer2 == riddleAnswerB:
        correctAnswers += 1
        prCyan("\nThe Sphinx nods sagely.")
        prYellow(f"\n Well done, {playerName}. You have answered {correctAnswers} correctly. Only one riddle remains.\n")
        key = input("\nPress Enter to proceed.")
    else: 
        wrongAnswers += 1
        prYellow(f"\n That is incorrect. You have answered {correctAnswers} correctly and have gotten {wrongAnswers} wrong. Only one riddle remains.\n Onto the final riddle.\n\n My last riddle is a simple one, yet more difficult than it may appear..." )
    userAnswer3 = input("\n The more of this there is, the less you see. What is it? ")
    #userAnswer3 = input("\n We are the youngest children of Four Royal Houses. Even or Odd whether we stand Before the King or After him. What are We?")    #Alternate Riddle
    
    if userAnswer3 == riddleAnswer3 or userAnswer3 == riddleAnswerC:
        correctAnswers += 1
        prCyan(f"\nThe Sphinx nods enthusiastically.")
        prYellow(f"\n Well done {playerName}. You have heard the last of my riddles. You answered {correctAnswers} riddles correctly and got {wrongAnswers} wrong.\n")
    else: 
        wrongAnswers += 1
        prCyan("\nThe guardian shakes his head.")
        prYellow(f"\n I'm sorry, but that is incorrect. You answered {correctAnswers} riddles correctly and got {wrongAnswers} wrong.\n")

# TreasureChest method
def treasureChest():
    global atk
    global playerName
    global weaponName 
    global correctAnswers
    weapon = [Nothing, Dagger, Sword, Axe]
    attackup = [0, 2, 5, 10]
 
    key = input("\n...\n")
    os.system('clear')
    
    if correctAnswers == 0:
        weaponName = "Bare Fists"
        prCyan("The Sphinx looks down at you with sympathy.")
        prYellow(f"\n I am sorry, {playerName} but you did not answer any of my riddles correctly.\nI truly wish I could aid you in the next step of your journey, alas I am bound by higher laws.")
        prRed(f"\nYou get {weapon[i]} to help you as you move forward.")
        atk += attackup[i]
        key = input("\nPress Enter to Continue")
        os.system('clear')
        
    
    elif correctAnswers == 1:
        answerStr = "one"
        atk += attackup[i+1]
        weaponName = weapon[i+1]
        prCyan("The Sphinx moves one massive paw revealing an ornate chest of gold, set with precious stones and carved with \nthe likeness of a jackal's head.") 
        prYellow(f"\n Come forward, {playerName}, and receive your reward for answering {answerStr} of my riddles correctly. Within this chest \nis a weapon that will aid you in your final challenge.")
        key = input("\n Press Enter to Open the Chest")
        os.system('clear')
        prRed(f"\nInside the chest you find an ornate " + weapon[i+1] + " that will add " + str(attackup[i+1]) + " to your attacks")
        
        
    elif correctAnswers == 2:
        answerStr = "two"
        atk += attackup[i+2]
        weaponName = weapon[i+2]
        prCyan("The Sphinx moves one massive paw revealing an ornate chest of gold, set with precious stones and carved with \nthe likeness of a jackal's head.") 
        prYellow(f"\n Come forward, Hero known as {playerName}, and receive your reward for answering {answerStr} of my riddles correctly. Within this chest \nis a weapon that will aid you in your final challenge.")
        key = input("\n Press Enter to Open the Chest")
        os.system('clear')
        prRed(f"\nInside the chest you find an ornate " + weapon[i+2] + " that will add " + str(attackup[i+2]) + " to your attacks")
     
        
    elif correctAnswers == 3:
        answerStr = "all"
        atk += attackup[i+3]
        weaponName = weapon[i+3]
        prCyan("The Sphinx moves one massive paw revealing an ornate chest of gold, set with precious stones and carved with \nthe likeness of a jackal's head.") 
        prYellow(f"\n Come forward, Mighty {playerName}, and receive your reward for answering {answerStr} of my riddles correctly. Within this chest \nis a weapon that will aid you in your final challenge.")
        key = input("\n Press Enter to Open the Chest")
        os.system('clear')
        prRed(f"\nInside the chest you find an ornate " + weapon[i+3] + " that will add " + str(attackup[i+3]) + " to your attacks")
     
        
    else:
        prRed("\n Something went wrong.")
    
    prCyan("\nOnce you have collected your reward from the chest, the great Sphinx speaks again.")
    
    prYellow("\n Behind me you will find a coracle made of reeds. Step into it and it will carry you to your final task and the end of your journey.")
    
    prCyan("\nThe Sphinx pauses briefly, considering you with large, golden eyes before speaking one last time.")
    
    prYellow(f"\n Good Luck to you, {playerName}. May Maat watch over you and guide you safely to the Field of Reeds.")
    
    key = input("\nPress Enter to step into the Coracle\n")
    os.system('clear')
    
# BBEG Method - Renamed to combat() 
def combat():
    #Temporary Declarations for Testing Purposes 
    global heroHP                           	# Starting HP for Hero
    global BGHP                             	# Starting HP for BadGuy                          
    global dmg							        # BadGuy Attack damage. Can be increased for higher difficulty
    global atk  							    # Hero Attack damage
    global playerName
    global weaponName
    
    # Declarations:
    TurnCount = 0							    # Turn Counter for BadGuy Turn
    heroAct = "X"							    # Default Value for Hero Action
    Exit = False							    # Exit becomes True when Hero or BadGuy HP drops to 0
    atkReset = atk                              # Preserve atk value with modifier included
    BGatk = dmg                                 # Redefine dmg as BGatk
    BGatkReset = BGatk

    prCyan("\n\nYou bid farewell to the Sphinx as you step into the diminuitive vessel. Once you are settled, the coracle drifts away \nfrom the shore of its own accord and carries you into the darkness, hardly making a sound as its hull breaks the still water. \nAfter some time, you begin to see tiny pinpricks of light far above you. \nThe stars twinkle and shine in the darkness, illuminating nothing.\n\n Soon, between the gentle rocking of the tiny boat and the swishing sounds of water against the reed hull, you find yourself \ndrifting in and out of consciousness. You dream briefly of your family members that you have lost.\n For a time, a favored pet walks beside you; a feeling of security envelops you and restful sleep descends upon you.")
    
    key = input("\n...")
    
    os.system('clear')
    
    prCyan("You wake abruptly as the coracle makes landfall, bumping against a sandy shore. Clearing the sleep from your eyes, \nyou find yourself on the bank of a vast river, the fields surrounding it covered in tall reeds that sway in an unseen wind. \nThe sound of the reeds as they rattle against one another is eerily reminiscent of hollow bone against hollow bone.\n\n You step out of the boat and onto the shore, and as you glance behind you the coracle is nowhere to be seen.\n\n With no other recourse available, you step forward into the Field of Reeds.")
    
    key = input("\n...")
    os.system('clear')

    prCyan("\n Soon you come to a clearing.\n\n Before you stands the imposing figure of a powerfully built man, his chest and arms bare, yet adorned with gold and precious stones. \nHe wears a large, ornate headdress atop his Jackal's head and bares long, viciously sharp teeth in a rictus of a grin as he \nmeets your gaze.\nHis voice is deep, like the rolling of thunder, as he speaks.")
    
    # Monologue
    prYellow(f"\n Welcome, {playerName}. Allow me to introduce myself properly. I am Anubis. \n\n I see that you have bested the Sphinx and found your way to my demesne. \n\n Despite what you may think, I am not your enemy, I am simply here to test your resolve one last time and to weigh the guilt \nin your heart against... this.")
    
    prCyan("\nAnubis holds up a single, large, white feather and gestures behind himself to a large set of scales.")
    
    prYellow("\n Sadly for you, before it can be weighed, it must be... removed.")
    
    prCyan("\nA dread chill moves down your spine as the old deity smiles savagely.")
    
    prYellow("\n However... Of late I have grown bored of this monotony, therefore I propose to you a challenge: I will give you one opportunity \nto avoid my judgement. Defeat me in combat and I will guide you to the Field of Reeds myself where you may spend eternity \nin Peace, with all the food and drink you desire. Fail, and your soul will be forfeit. \n\n Prepare yourself, human! Your fate is at hand!")

    # User Input
    heroAct = input("\n Fight! [Choose A to Attack, B to Block, or D to Dodge.]: ")
	
    while not Exit:					#Repeat Hero Turn, BadGuy Turn, and HP Calculation until either HP reaches 0

        if BGHP > 0:						#While BadGuy HP is greater than 0, Exit value remains False
            
            #for i in range(BGHP):          #Attempt at making a Health Bar for BadGuy
            #    prRed("♥", end="")                  #Comment out if not working
		
            retry = True					#Retry if Invalid Input

            while retry:					#Loop to determine Hero Action 

                if heroAct == "A" or  heroAct == "a":			#Attack: Take and Deal Full Damage
                    prCyan(f"\nYou attack with your {weaponName}!")
                    dmg = BGatk
                    atk = atk			
                    retry = False			#Valid Input, Do not retry
	
                elif heroAct == "D" or heroAct == "d":		#Dodge:
                    prCyan(f"\nYou roll out of the way of the incoming attack!")
                    dmg = 0				#Take 0 Damage
                    atk = 0				#Deal 0 Damage
                    retry = False		#Valid Input, Do not retry

                elif heroAct == "B" or heroAct == "b":		#Block:
                    prCyan(f"\nYou parry the incoming attack before delivering your riposte!")
                    dmg = BGatk / 2		#Take Half Damage
                    atk = atk / 2		#Deal Half Damage
                    retry = False		#Valid Input, Do not retry
                else:
                    heroAct = input("Invalid Input. Please Enter 'A' to Attack, 'B' to Block, or 'D' to Dodge:")
										#If No Valid Input, Return Error Message and Ask Again. Retry remains True

            if TurnCount < 2:				#BadGuy Attacks twice, then Blocks on every 3rd Turn
                prRed("\nAnubis attacks you fiercely with his kopesh!")							
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

            #prRed(f"Anubis has {BGHP} HP left.\n") 		# For testing/debugging purposes
		
            if BGHP < 5:
                prRed("The ancient god falls to his knees before you, defeated. Finish Him!\n")
             
            atk = atkReset						#Reset Hero Attack to initial value with modifier
            BGatk = BGatkReset						#Reset BadGuy Attack to initial value
		
												#End of Round
		
            if heroHP > 0:							#While Hero HP is greater than 0, Exit value remains False
                heroAct = input("Choose 'A' to Attack, 'B' to Block, or 'D' to Dodge: " )
			
            else:						#If Hero HP drops to 0, player loses and Exit value becomes True
                prRed("\n\n You have Failed. You look on in horror as Ammut, a great beast with the head of a Crocodile, \nthe body of a Hippopotamus, and the hindquarters of a Lion, pounces upon you from the shadows behind the Ancient God.\n You feel no pain as it begins to devour your heart and darkness consumes you once again.")
                key = input("...")
                os.system('clear')
                Exit = True
			
        else:							#If BadGuy HP drops to 0, player wins and Exit Value becomes True
            prBlue("\n\n You are Victorious! The ancient god falls to the ground at your feet, bloodied and beaten.")
            key = input("...\n")
            os.system('clear')
            
            prCyan(f"\nAs you watch, Anubis rises gracefully to his feet, his many wounds closing within the span of a single breath. \nThe scarlet blood scattered across your private battlefield is swallowed hungrily by the sandy ground beneath your feet. \nHe takes a deep, almost satisfied breath.")
            prYellow(f"\n Congratulations, {playerName}. You have fought well and defeated me fairly. I will keep my word and guide you to your eternal rest.")
            prCyan("\nAnubis reaches out a hand that seems to grow immense as it gets closer and closer, \nblotting out the sun and sky as it engulfs you.")
            prYellow("\n Rest well, Human. You have earned it.")
            key = input("\n\nPress any Key")
            os.system('clear')
            Exit = True

# Thank You message - Include Dev info/credits, course info, date submitted, instructor, etc 
def main_end():
    prMagenta("\nThank you for playing 'Field of Reeds: An Egyptian Underworld Adventure'. We hope you have enjoyed your journey.")
    prMagenta("\nBrought to you by Efrain, Sean, Ian, and Jamie")
    prMagenta("\nMade for CSC1019, Front Range Community College, Fall 2024")
    prMagenta("\nSpecial Thanks to our Instructor: Dr. Jim Irwin.\n\n\n")
    
# Order of method execution
def main():
    EyeOfRa()       #Display splash screen
    main_intro()    #Set the scene, narrate setting
    sphinx()        #Puzzles to determine reward
    treasureChest() #Reward to boost attack during combat
    combat()        #Final Boss combat 
    main_end()      #Thank You/Credits

# Call the Main function to run the program
if __name__ == '__main__':
    main()
