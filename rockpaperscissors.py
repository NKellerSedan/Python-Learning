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
    "Human"
    ]

choices = [
    ["Rock"],
    ["Paper"],
    ["Scissors"],
    ["Lizard"],
    ["Spock"],
    ]

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
            print("\nThe " + opponent + " is your opponent!")
            break
    else:
        print("Invalid Option!, you needed to type a 1, or 2")

if mode == game_type[0]:
    game_options = choices[0:3]
    print("Your options: " + str(game_options))
elif mode == game_type[1]:
    game_options = choices[0:5]
    print("Your options: " + str(game_options))
else:
    print("An error has occured")

# Player Selection of options

player_choice = input("Player 1 select your choice: ") 
print(game_options[int(player_choice) - 1])


# If statement on if it is 2 player or vs computer
if selectedVS == "1":
    # Computers Selection of options
    max_choices = int(len(game_options))
    cpu_choice = random.randint(0,max_choices)
    print("The computer chose: " + str(game_options[int(cpu_choice) - 1]))
elif selectedVS == "2":
    # Player
    opponent_choice = input("Player 2 select your choice: ")
    print(game_options[int(opponent_choice) - 1])


# Which options beat which


# Displaying Outcome of options (Win/Loss/Draw)


# Features to add
# Ask how many rounds are being played
# Display Score
# Play again feature