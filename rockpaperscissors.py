"Rock Paper Scissors"

import random
from enum import IntEnum

game_type = [
    "Normal",
    "Sheldon",
    ]

rules = [
    """1. Scissors cuts Paper
2. Paper covers Rock
3. Rock crushes Scissors""",
    """1. Scissors cuts Paper
2. Paper covers Pock
3. Pock crushes Lizard
4. Lizard poisons Spock
5. Spock smashes Scissors
6. Scissors decapitates Lizard
7. Lizard eats Paper
8. Paper disproves Spock
9. Spock vaporizes Rock
10. Rock crushes Scissors""",
    ]

opponent_type = [
    "Computer",
    "Player 2"
    ]

choices = [
    "Rock",
    "Paper",
    "Scissors",
    "Lizard",
    "Spock",
    ]

play = True

print("\033[1m Welcome to Rock Paper Scissors!\033[0m")
print("================================")

print("\nSelect a game mode: ")  
for index, game in enumerate(game_type):
        games = game_type[index]
        print(str(int(index + 1)) + " - " + game)

selectedMode = 0
while selectedMode <= 0 or selectedMode >= 3: 
    selectedMode = int(input("\nGame Mode: "))
    if selectedMode > 0 and selectedMode <= 3:
        modes = [item for item in game_type]
        mode = modes[selectedMode-1]
        break
    else:
        print("Invalid option! Please type either 1 or 2")

print(selectedMode)
print(modes)
print(mode)


view_rules = ""
while view_rules != 'y' or view_rules != 'n':
    view_rules = input("\nDo you need the rules for the " + mode + " version? (y/n) ")
    if view_rules == 'y':
        print("\nThe rules for the " + mode + " version:")
        rule = rules[selectedMode-1]
        print(rule)
        break
    elif view_rules == 'n':
        break
    else:
        print("Invalid option! Please type either y or n")



print("\n")
for index, type in enumerate(opponent_type):
  print(str(int(index + 1)) + " - " + type)


selectedVS = "0"
while selectedVS != "1" or selectedVS != "2":
    selectedVS = input("\nWho are you against?: ")
    if selectedVS in ("1", "2"):
        if selectedVS == "1":
            opponent = opponent_type[0]
            print("\nThe " + opponent + " is your opponent!")
            break
        elif selectedVS == "2":
            opponent = opponent_type[1]
            print("\n" + opponent + " is your opponent!")
            break
    else:
        print("Invalid Option!, you needed to type a 1, or 2")

while play:

    if mode == game_type[0]:
        game_options = choices[0:3]
        print("Your options: " + str(game_options))
    elif mode == game_type[1]:
        game_options = choices[0:5]
        print("Your options: " + str(game_options))
    else:
        print("An error has occured")

    # Player Selection of options
    player_selection = input("Player 1 select your choice: ") 
    player_choice = game_options[int(player_selection) - 1]
    print(player_choice)

    # If statement on if it is 2 player or vs computer
    if selectedVS == "1":
        # Computers Selection of options
        max_choices = int(len(game_options))
        cpu_choice = random.randint(0,max_choices)
        opponent_choice = game_options[int(cpu_choice) - 1]
        print("The computer chose: " + opponent_choice)
    elif selectedVS == "2":
        # Player
        opponent_selection = input("Player 2 select your choice: ")
        opponent_choice = game_options[int(opponent_selection) - 1]
        print(opponent_choice)


    # Which options beat which
    # Displaying Outcome of options (Win/Loss/Draw)

    if player_choice == opponent_choice:
        print(f"Both players selected {player_choice}. It's a tie!")
    elif player_choice == "Rock":
        if opponent_choice == "Scissors":
            print("Rock crushes scissors! Player 1 wins!")
        elif opponent_choice == "Lizard":
            print("Rock crushes lizard! Player 1 wins!")
        elif opponent_choice == "Spock":
            print(f"Spock vaporizes rock! {opponent} wins!")
        else:
            print(f"Paper covers rock! {opponent} wins!")
    elif player_choice == "Paper":
        if opponent_choice == "Rock":
            print("Paper covers rock! Player 1 wins!")
        elif opponent_choice == "Spock":
            print("Spock disproves paper! Player 1 wins!")
        elif opponent_choice == "Lizard":
            print(f"Lizard eats paper! {opponent} wins!")
        else:
            print(f"Scissors cuts paper! {opponent} wins!")
    elif player_choice == "Scissors":
        if opponent_choice == "Paper":
            print("Scissors cuts paper! Player 1 wins!")
        elif opponent_choice == "Lizard":
            print("Scissors decapitates lizard! Player 1 wins!")
        elif opponent_choice == "Spock":
            print(f"Spock smashes scissors! {opponent} wins!")
        else:
            print(f"Rock smashes scissors! {opponent} wins!") 
    elif player_choice == "Lizard":
        if opponent_choice == "Paper":
            print("Lizard eats paper! Player 1 wins!")
        elif opponent_choice == "Spock":
            print("Lizard poisons Spock! Player 1 wins!")
        elif opponent_choice == "Scissors":
            print(f"Scissors decapitates lizard! {opponent} wins!.")
        else:
            print(f"Rock crushes lizard! {opponent} wins!")
    elif player_choice == "Spock":
        if opponent_choice == "Rock":
            print("Spock vaporizes rock! Player 1 wins!")
        elif opponent_choice == "Scissors":
            print("Spock smashes scissors! Player 1 wins!")
        elif opponent_choice == "Lizard":
            print(f"Lizard poisons Spock! {opponent} wins!.")
        else:
            print(f"Spock disproves paper! {opponent} wins!")   

    # Play again feature
    again=str(input("Do you want to play again, type yes or no? "))
    if again == "no":
      play = False

# Display Score