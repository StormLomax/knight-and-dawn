# Knight and Dawn
# Python Multiple Choice Text Adventure Game
# Created By Storm Lomax
# Created On 21/04/2025

def intro():
    print("Welcome to Knight and Dawn!")
    player = input("What's your name, Knight?: ")
    print("Hello " + player + ", welcome to the game!")
    print("""You are an honourable knight, under the service of the King for many years.
    You have fought many battles and won many wars. But now, the King has sent you on a quest to find his daughter - 
    the kidnapped Princess, guarded by a fierce dragon in a dangerous forest.
    The King has promised a generous reward if you can find her and bring her safely back home.
    But be careful, for the forest is full of dangers and traps, and the dragon is known to be very powerful.""")

    quest = get_valid_input("Do you accept the quest? (yes/no): ", ['yes', 'no'])
    if quest == 'yes':
        print("The King is pleased.")
        print("You start your journey into the forest, armed with your sword and shield.")
        print("As you walk deeper into the forest, you come across a fork in the road.")
        print("To your left, you see a dark and narrow path that leads deeper into the forest.")
        print("To your right, you see a wider path that seems to be well-trodden.")
        path = get_valid_input("Which path do you choose? (left/right): ", ['left', 'right'])

        if path == 'left':
            print("You take the left path and soon find yourself in a dark and eerie part of the forest.")
            print("Suddenly, you hear a rustling sound behind you.")
            print("You turn around to see a pack of wolves approaching you.")
            print("You draw your sword and prepare to fight.")
            action = get_valid_input("Do you fight or run? (fight/run): ", ['fight', 'run'])

            if action == 'fight':
               print("You bravely fight the wolves and manage to defeat them.")
               print("But you are injured in the process.")
               print("You continue on your journey, but you are now weaker than before.")
               print("You find a small cave to rest in and tend to your wounds.")
               print("The cave has some mushrooms that you think are edible.")
               print("Your memory is hazy but you think they're healing mushrooms.")
               food = get_valid_input("Do you eat the mushrooms? (yes/no): ", ['yes', 'no'])

               if food == 'yes':
                    print("You eat the mushrooms and feel your strength returning.")
                    print("You continue on your journey, feeling stronger than before.")
                    print("You find yourself in a clearing with a beautiful fountain.")
                    drink = get_valid_input("Do you drink from the fountain? (yes/no): ", ['yes', 'no'])

                    if drink == 'yes':
                        print("You drink from the fountain and feel rejuvenated.")
                        print("You continue on your journey, feeling invincible.")
                        print("Soon, you hear a beautiful singing voice.")
                        song = get_valid_input("Do you follow the voice? (yes/no): ", ['yes', 'no'])

                        if song == 'yes':
                            print("You follow the voice, and soon find yourself in the midst of ancient ruins.")
                            print("In the ruins sits a huge dragon, and you realise it's the dragon that's singing.")
                            print("The dragon doesn't seem to have noticed you yet.")
                            sneak = get_valid_input("Do you attack or compliment the dragon's singing? (attack/compliment): ", ['attack', 'compliment'])

                            if sneak == 'attack':
                                print("You attack the dragon.")
                                print("Thanks to the mushrooms and fountain water, you are now invincible.")
                                print("You strike a devastating blow, and the dragon falls to the ground.")
                                print("The dragon cries out 'No!' but it's too late.")
                                print("You have slain the dragon... but where is the princess?")
                                print("As you're about to search the ruins, the dragon's body starts to glow.")
                                print("The glow gets brighter and brighter, and you shield your eyes.")
                                print("When you open your eyes again, you find yourself looking down at the body of the princess.")
                                print("You've done it now. You killed the damn princess.")
                                print("Rather than face the King's wrath, you decide to run away.")
                                print("You spend the rest of your life in hiding as a wanted criminal. Bummer.")
                                return

                            elif sneak == 'compliment':
                                print("You compliment the dragon.")
                                print("It turns to you in surprise.")
                                print("There's an awkward pause, where you're just kind of staring at each other.")
                                print("You ask if they can do 'Wonderwall'.")
                                print("The dragon looks at you like you're stupid. You didn't know dragons were expressive enough for that.")
                                print("'I don't have a guitar,' the dragon says.")
                                print("'You can speak?' you ask.")
                                print("Again, the dragon gives you a look.")
                                print("'Well, I am the princess,' it says, as though that should be obvious.")
                                print("You stare in awe as the dragon glows.")
                                print("It glows so bright you have to shield your eyes. It's only when you open them again, you find yourself looking at the form of the princess.")
                                print("Oh.")
                                print("So, the dragon is the princess.")
                                print("You hide your sword. That could have been awkward.")
                                print("You and the princess have an amiable chat. She agrees to return to the King before sunrise.")
                                print("Congratulations! You have... well, you didn't save the princess, but at least you didn't kill her. Well done!")
                                return

                        elif song == 'no':
                            print("You decide not to follow the voice.")
                            print("You get lost in the forest and wander around aimlessly.")
                            print("The night grows deeper, and you hear growls from the dark.")
                            print("It's the family of the wolves you killed. And they look pissed.")
                            print("You try to fight back but the healing mushrooms have worn out.")
                            print("The wolves quickly overwhelm you.")
                            print("The wolves get their revenge, like a reverse John Wick. You are dead.")
                            return

                    elif drink == 'no':
                        print("You decide not to drink from the fountain.")
                        print("You continue on your journey.")
                        print("Soon, you hear a beautiful singing voice.")
                        song = get_valid_input("Do you follow the voice? (yes/no): ", ['yes', 'no'])
                        
                        if song == 'yes':
                           print("You follow the voice, and soon find yourself in the the midst of ancient ruins.")
                           print("In the ruins sits a huge dragon, and you realise it's the dragon that's singing.")
                           print("The dragon doesn't seem to have noticed you yet.")
                           sneak = get_valid_input("Do you attack or compliment the dragon's singing? (attack/compliment): ", ['attack', 'compliment'])
                           
                           if sneak == 'attack':
                              print("You attack the dragon")
                              print("Thanks to the fountain water, you feel strong, but not invincible.")
                              print("You strike a blow, but the dragon retaliates.")
                              print("It knocks you sideways, and you fall to the ground, winded.")
                              print("Before you can recover, the dragon opens its maw.")
                              print("You're quickly turned into knight bbq.")
                              print("You are dead.")
                              return
                           
                           if sneak == 'compliment':
                              print("You compliment the dragon.")
                              print("It turns to you in surprise.")
                              print("There's an awkward pause, where you're just kind of staring at each other")
                              print("You ask if they can do 'Wonderwall'")
                              print("The dragon looks at you like you're stupid. You didn't know dragons were expressive enough for that.")
                              print("'I don't have a guitar', the dragon says.")
                              print("'You can speak?' you ask.")
                              print("Again, the dragon gives you a look.")
                              print("'Well, I am the princess,' it says, as though that should be obvious")
                              print("You stare in awe as the dragon glows.")
                              print("It glows so bright you have to shield your eyes. It's only when you open them again, you find yourself looking at the form of the princess.")
                              print("Oh.")
                              print("So the dragon is the princess.")
                              print("You hide your sword. That could have been awkward.")
                              print("You and the princess have an amiable chat. She agrees to return to the King before sunrise.")
                              print("Congratulations! You have... well, you didn't save the princess, but at least you didn't kill her. Well done!")
                              return
                           
                        if song == 'no':
                           print("You decide not to follow the song.")
                           print("You are now lost in the forest.")
                           print("By the time the sun rises, you find yourself back at the start of the forest path.")
                           print("The King is waiting for you.")
                           print("When he sees you don't have the princess, he demands an explanation.")
                           print("You tell him you got lost.")
                           print("The King looks at you like you're an idiot.")
                           print("'How does someone miss a giant dragon in the forest?' he asks.")
                           print("Yeah, he's got a point. Maybe you should have followed that voice.")
                           print("The King orders your immediate execution for failing your quest.")
                           print("You are dead.")
                           return

               if food == 'no':
                  print("You decide not to eat the mushrooms.")
                  print("You continue on your journey, but you are still injured.")
                  print("You find yourself in a clearing with a beautiful fountain.")
                  drink = get_valid_input("Do you drink from the fountain? (yes/no): ", ['yes', 'no'])
                  
                  if drink == 'yes':
                     print("You drink from the fountain and feel rejuvenated.")
                     print("You continue on your journey, feeling invincible.")
                     print("Soon, you hear a beautiful singing voice.")
                     song = get_valid_input("Do you follow the voice? (yes/no): ", ['yes', 'no'])
                     
                     if song == 'yes':
                        print("You follow the voice, and soon find yourself in the the midst of ancient ruins.")
                        print("In the ruins sits a huge dragon, and you realise it's the dragon that's singing.")
                        print("The dragon doesn't seem to have noticed you yet.")
                        sneak = get_valid_input("Do you attack or compliment the dragon's singing? (attack/compliment): ", ['yes', 'no'])
                        
                        if sneak == 'attack':
                           print("You attack the dragon.")
                           print("Thanks to the fountain, you feel strong, but not invincible.")
                           print("You strike a blow, but the dragon retaliates.")
                           print("It knocks you sideways, and you fall to the ground, winded.")
                           print("Before you can recover, the dragon opens its maw.")
                           print("You're quickly turned into knight bbq.")
                           print("You are dead.")
                           return
                        
                        if sneak == 'compliment':
                           print("You compliment the dragon.")
                           print("It turns to you in surprise.")
                           print("There's an awkward pause, where you're just kind of staring at each other.")
                           print("You ask if they can do 'Wonderwall'.")
                           print("The dragon looks at you like you're stupid. You didn't know dragons were expressive enough for that.")
                           print("'I don't have a guitar,' the dragon says.")
                           print("'You can speak?' you ask.")
                           print("Again, the dragon gives you a look.")
                           print("'Well, I am the princess,' it says, as though that should be obvious.")
                           print("You stare in awe as the dragon glows.")
                           print("It glows so bright you have to shield your eyes. It's only when you open them again, you find yourself looking at the form of the princess.")
                           print("Oh.")
                           print("So, the dragon is the princess.")
                           print("You hide your sword. That could have been awkward.")
                           print("You and the princess have an amiable chat. She agrees to return to the King before sunrise.")
                           print("Congratulations! You have... well, you didn't save the princess, but at least you didn't kill her. Well done!")
                           return
                        
                     if song == 'no':
                        print("You decide not to follow the voice.")
                        print("You are now lost in the forest.")
                        print("The night grows deeper, and you hear growls from the dark.")
                        print("It's the family of the wolves you killed. And they look pissed.")
                        print("You try to fight back but the healing mushrooms have worn out.") 
                        print("The wolves quickly overwhelm you.") 
                        print("The wolves get their revenge, like a reverse John Wick. You are dead.")
                        return
                  
                  if drink == 'no':
                     print("You decide not to drink from the fountain.")
                     print("Not only are you still injured, but you're parched as well.")
                     print("It's not going well.")
                     print("Soon, you hear a beautiful singing voice.")
                     song = get_valid_input("Do you follow the voice? (yes/no) ", ['yes', 'no'])
                     
                     if song == 'yes':
                        print("You follow the voice, and soon find yourself in the the midst of ancient ruins.")
                        print("In the ruins sits a huge dragon, and you realise it's the dragon that's singing.")
                        print("The dragon doesn't seem to have noticed you yet.")
                        sneak = get_valid_input("Do you attack or compliment the dragon's singing? (attack/compliment): ", ['yes', 'no'])
                        
                        if sneak == 'attack':
                           print("You attack the dragon.")
                           print("Again, you're injured and parched, and pretty tired as well.")
                           print("The dragon barely has to swipe at you before you're in a crumpled heap.")
                           print("With one fiery breath, you're quickly turned into knight bbq.")
                           print("You are dead.")
                           return
                        
                        if sneak == 'compliment':
                           print("You compliment the dragon.")
                           print("It turns to you in surprise.")
                           print("There's an awkward pause, where you're just kind of staring at each other")
                           print("You ask if they can do 'Wonderwall'")
                           print("The dragon looks at you like you're stupid. You didn't know dragons were expressive enough for that.")
                           print("'I don't have a guitar', the dragon says.")
                           print("'You can speak?' you ask.")
                           print("Again, the dragon gives you a look.")
                           print("'Well, I am the princess,' it says, as though that should be obvious")
                           print("You stare in awe as the dragon glows.")
                           print("It glows so bright you have to shield your eyes. It's only when you open them again, you find yourself looking at the form of the princess.")
                           print("Oh.")
                           print("So, the dragon is the princess.")
                           print("You hide your sword. That could have been awkward.")
                           print("You and the princess have an amiable chat. She agrees to return to the King before sunrise.")
                           print("Congratulations! You have... well, you didn't save the princess, but at least you didn't kill her. Well done!")
                           return
                        
                     if song == 'no':
                        print("You decide not to follow the voice.")
                        print("You are now lost in the forest.")
                        print("The night grows deeper, and you hear growls from the dark.")
                        print("It's the family of the wolves you killed. And they look pissed.")
                        print("You try to fight back but the healing mushrooms have worn out.") 
                        print("The wolves quickly overwhelm you.") 
                        print("The wolves get their revenge, like a reverse John Wick. You are dead.")
                        return
                     
            if action == 'run':
               print("You run away from the wolves and manage to escape.")
               print("But you are now lost in the forest.")
               print("You wander around for hours, trying to find your way back.")
               print("You end up at the start of the forest as the sun rises.")
               print("The King is waiting for you.")
               print("When he sees you without the princess, his disappointment is immeasurable.")
               print("You try to explain about the wolves, but he gives you a look that could wither grass.")
               print("'My finest Knight, winner of wars, running away from wolves?'")
               print("Okay, yeah, when he says it like that, it sounds bad.")
               print("He orders your immediate execution, and really, you don't blame him.")
               print("You are dead.")
               return

        elif path == 'right':
            print("You take the right path and soon find yourself in a clearing.")
            print("In the clearing, you see a beautiful fountain with crystal clear water.")
            drink = get_valid_input("Do you drink from the fountain? (yes/no): ", ['yes', 'no'])
            
            if drink == 'yes':
               print("You drink from the fountain and feel rejuvenated.")
               print("You continue on your journey, feeling stronger than before.")
               print("Soon, you hear a beautiful singing voice.")
               song = get_valid_input("Do you follow the voice? (yes/no) ", ['yes', 'no'])
               
               if song == 'yes':
                  print("You decide to follow the voice.")
                  print("You follow the voice, and soon find yourself in the the midst of ancient ruins.")
                  print("In the ruins sits a huge dragon, and you realise it's the dragon that's singing.")
                  print("The dragon doesn't seem to have noticed you yet.")
                  sneak = get_valid_input("Do you attack or compliment the dragon's singing? (attack/compliment): ", ['yes', 'no'])
                  
                  if sneak == 'attack':
                     print("You attack the dragon")
                     print("Thanks to the fountain water, you feel strong, but not invincible.")
                     print("You strike a blow, but the dragon retaliates.")
                     print("It knocks you sideways, and you fall to the ground, winded.")
                     print("Before you can recover, the dragon opens its maw.")
                     print("You're quickly turned into knight bbq.")
                     print("You are dead.")
                     return
                  
                  if sneak =='compliment':
                     print("You compliment the dragon.")
                     print("It turns to you in surprise.")
                     print("There's an awkward pause, where you're just kind of staring at each other")
                     print("You ask if they can do 'Wonderwall'")
                     print("The dragon looks at you like you're stupid. You didn't know dragons were expressive enough for that.")
                     print("'I don't have a guitar', the dragon says.")
                     print("'You can speak?' you ask.")
                     print("Again, the dragon gives you a look.")
                     print("'Well, I am the princess,' it says, as though that should be obvious")
                     print("You stare in awe as the dragon glows.")
                     print("It glows so bright you have to shield your eyes. It's only when you open them again, you find yourself looking at the form of the princess.")
                     print("Oh.")
                     print("So the dragon is the princess.")
                     print("You hide your sword. That could have been awkward.")
                     print("You and the princess have an amiable chat. She agrees to return to the King before sunrise.")
                     print("Congratulations! You have... well, you didn't save the princess, but at least you didn't kill her. Well done!")
                     return
                  
               if song == 'no':
                  print("You decide not to follow the song.")
                  print("You are now lost in the forest.")
                  print("By the time the sun rises, you find yourself back at the start of the forest path.")
                  print("The King is waiting for you.")
                  print("When he sees you don't have the princess, he demands an explanation.")
                  print("You tell him you got lost.")
                  print("The King looks at you like you're an idiot.")
                  print("'How does someone miss a giant dragon in the forest?' he asks.")
                  print("Yeah, he's got a point. Maybe you should have followed that voice.")
                  print("The King orders your immediate execution for failing your quest.")
                  print("You are dead.")
                  return

            if drink == 'no':
               print("You decide not to drink from the fountain.")
               print("You continue on your journey, but you are now thirsty.")
               print("Soon, you hear a beautiful singing voice.")
               song = get_valid_input("Do you follow the voice? (yes/no) ")
               
               if song == 'yes':
                  print("You decide to follow the voice.")
                  print("You follow the voice, and soon find yourself in the the midst of ancient ruins.")
                  print("In the ruins sits a huge dragon, and you realise it's the dragon that's singing.")
                  print("The dragon doesn't seem to have noticed you yet.")
                  sneak = get_valid_input("Do you attack or compliment the dragon's singing? (attack/compliment): ", ['yes', 'no'])
                  
                  if sneak == 'attack':
                     print("You attack the dragon.")
                     print("Kind of a crazy decision, since it's a dragon and you're just some guy.")
                     print("You strike what you thought would be a devastating blow, but it barely glances off the dragon's hide.")
                     print("Because obviously.")
                     print("The dragon sideswipes you, sending you flying into the ruins.")
                     print("Before you can recover, it opens its maw and sends out a fiery breath.")
                     print("You are knight BBQ.")
                     print("You are dead.")
                     return
                  
                  if sneak == 'compliment':
                     print("You compliment the dragon.")
                     print("It turns to you in surprise.")
                     print("There's an awkward pause, where you're just kind of staring at each other")
                     print("You ask if they can do 'Wonderwall'")
                     print("The dragon looks at you like you're stupid. You didn't know dragons were expressive enough for that.")
                     print("'I don't have a guitar', the dragon says.")
                     print("'You can speak?' you ask.")
                     print("Again, the dragon gives you a look.")
                     print("'Well, I am the princess,' it says, as though that should be obvious")
                     print("You stare in awe as the dragon glows.")
                     print("It glows so bright you have to shield your eyes. It's only when you open them again, you find yourself looking at the form of the princess.")
                     print("Oh.")
                     print("So the dragon is the princess.")
                     print("You hide your sword. That could have been awkward.")
                     print("You and the princess have an amiable chat. She agrees to return to the King before sunrise.")
                     print("Congratulations! You have... well, you didn't save the princess, but at least you didn't kill her. Well done!")
                     return
               
               if song == 'no':
                  print("You decide not to follow the voice.")
                  print("You are now lost in the forest.")
                  print("By the time the sun rises, you find yourself back at the start of the forest path.")
                  print("The King is waiting for you.")
                  print("When he sees you don't have the princess, he demands an explanation.")
                  print("You tell him you got lost.")
                  print("The King looks at you like you're an idiot.")
                  print("'How does someone miss a giant dragon in the forest?' he asks.")
                  print("Yeah, he's got a point. Maybe you should have followed that voice.")
                  print("The King orders your immediate execution for failing your quest.")
                  print("You are dead.")
                  return
               
    elif quest == 'no':
        print("The King is displeased, and orders for your immediate execution.")
        return

def play_game():
    while True:
        intro()
        again = get_valid_input("\nWould you like to play again? (yes/no): ", ['yes', 'no'])
        if again != 'yes':
            break  
 
def get_valid_input(prompt, valid_options):
    while True:
        user_input = input(prompt).strip().lower()
        if user_input in valid_options:
            return user_input
        print(f"Invalid choice. Please choose from {', '.join(valid_options)}.")           
   
# Start the game
play_game()