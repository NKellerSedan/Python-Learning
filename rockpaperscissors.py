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

player_score = 0
opponent_score = 0

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
    player_selection = input("\nPlayer 1 select your choice: ") 
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
        print(f"\nBoth players selected {player_choice}. It's a tie!")
    elif player_choice == "Rock":
        if opponent_choice == "Scissors":
            print("\nRock crushes scissors! Player 1 wins!")
            player_score += 1
        elif opponent_choice == "Lizard":
            print("\nRock crushes lizard! Player 1 wins!")
            player_score += 1
        elif opponent_choice == "Spock":
            print(f"\nSpock vaporizes rock! {opponent} wins!")
            opponent_score += 1
        else:
            print(f"\nPaper covers rock! {opponent} wins!")
            opponent_score += 1
    elif player_choice == "Paper":
        if opponent_choice == "Rock":
            print("\nPaper covers rock! Player 1 wins!")
            player_score += 1
        elif opponent_choice == "Spock":
            print(f"\nPaper disproves Spock! Player 1 wins!")
            player_score += 1
        elif opponent_choice == "Lizard":
            print(f"\nLizard eats paper! {opponent} wins!")
            opponent_score += 1
        else:
            print(f"\nScissors cuts paper! {opponent} wins!")
            opponent_score += 1
    elif player_choice == "Scissors":
        if opponent_choice == "Paper":
            print("\nScissors cuts paper! Player 1 wins!")
            player_score += 1
        elif opponent_choice == "Lizard":
            print("\nScissors decapitates lizard! Player 1 wins!")
            player_score += 1
        elif opponent_choice == "Spock":
            print(f"\nSpock smashes scissors! {opponent} wins!")
            opponent_score += 1
        else:
            print(f"\nRock smashes scissors! {opponent} wins!") 
            opponent_score += 1
    elif player_choice == "Lizard":
        if opponent_choice == "Paper":
            print("\nLizard eats paper! Player 1 wins!")
            player_score += 1
        elif opponent_choice == "Spock":
            print("\nLizard poisons Spock! Player 1 wins!")
            player_score += 1
        elif opponent_choice == "Scissors":
            print(f"\nScissors decapitates lizard! {opponent} wins!")
            opponent_score += 1
        else:
            print(f"\nRock crushes lizard! {opponent} wins!")
            opponent_score += 1
    elif player_choice == "Spock":
        if opponent_choice == "Rock":
            print("\nSpock vaporizes rock! Player 1 wins!")
            player_score += 1
        elif opponent_choice == "Scissors":
            print("\nSpock smashes scissors! Player 1 wins!")
            player_score += 1
        elif opponent_choice == "Lizard":
            print(f"\nLizard poisons Spock! {opponent} wins!")
            opponent_score += 1
        else:
            print(f"\nSpock disproves paper! {opponent} wins!")
            opponent_score += 1   

    # Display Score
    if player_score > opponent_score:
        print("\nPlayer 1 is in the lead by " + str(player_score - opponent_score) + "!")
        print(str(player_score) + " - " + str(opponent_score))
    elif player_score < opponent_score:
        print(f"\n{opponent} is in the lead by " + str(opponent_score - player_score) + "!")
        print(str(opponent_score) + " - " + str(player_score))
    else:
        print("\nThe match is tied!")
        print(str(player_score) + " - " + str(opponent_score))
    

    # Play again feature
    again=str(input("\nDo you want to play again, type yes or no? "))
    if again == "no" or again == "n":
        play = False
        if player_score > opponent_score:
            print("\nPlayer 1 wins with a final score of " + str(player_score) + " - " + str(opponent_score) + "!")
        elif player_score < opponent_score:
            print(f"\n{opponent} wins with a final score of " + str(opponent_score) + " - " + str(player_score) + "!")
        else:
            print("\nThe match ended as a tie with a final score of " + str(player_score) + " - " + str(opponent_score) + "!")