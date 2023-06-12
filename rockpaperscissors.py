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
    "2 Player",
    "Computer",
    ]

choices1 = [
    [1, "Rock"],
    [2, "Paper"],
    [3, "Scissors"],
    ]

choices2 = [
    [1, "Rock"],
    [2, "Paper"],
    [3, "Scissors"],
    [4, "Lizard"],
    [5, "Spock"],
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
    modes = [item for item in game_type]
    mode = modes[selectedMode-1]

print(selectedMode)
print(modes)
print(mode)

view_rules = input("\nDo you need the rules for the " + mode + " version? (y/n) ")
while view_rules != 'y' or view_rules != 'n':
    if view_rules == 'y':
        print("\nThe rules for the " + mode + " version:")
        rule = rules[selectedMode-1]
        print(rule)
        break
    elif view_rules == 'n':
        break

print("\n")
for index, opponent_type in enumerate(opponent_type):
  opponent = opponent_type[0]
  print(str(int(index + 1)) + " - " + opponent_type)


selectedVS = int(input("\nWho are you against?: "))

print("\nSelect who your opponent: ")
for index, opponent_type in enumerate(opponent_type):
  opponent = opponent_type[0]
  print(str(int(index + 1)) + " - " + opponent_type)


selectedVS = int(input("\nWho are you against?: "))