def intro():
    print("Welcome to Knight and Dawn!")
    player = input("What's your name, Knight?: ")
    print("Hello " + player + ", welcome to the game!")
    
    print("""\nYou are an honourable knight, under the service of the King for many years.
You have fought many battles and won many wars. But now, the King has sent you on a quest to find his daughter – 
the kidnapped Princess, guarded by a fierce dragon in a dangerous forest.
The King has promised a generous reward if you can find her and bring her safely back home.
But be careful, for the forest is full of dangers and traps, and the dragon is known to be very powerful.\n""")

    quest = input("Do you accept the quest? (yes/no): ").lower()

    if quest == 'yes':
        print("\nThe King is pleased.")
        print("You start your journey into the forest, armed with your sword and shield.")
        print("As you walk deeper into the forest, you come across a fork in the road.")
        print("To your left, you see a dark and narrow path that leads deeper into the forest.")
        print("To your right, you see a wider path that seems to be well-trodden.")
        # Add the rest of the game here
    else:
        print("\nThe King is displeased, and orders for your immediate execution. You are dead.")
        return

def play_game():
    while True:
        intro()
        again = input("\nWould you like to play again? (yes/no): ").lower()
        if again != 'yes':
            print("Farewell, brave knight!")
            break

# Start the game
play_game()
