#!/usr/bin/env python 3
from apps.tower_of_hanoi.NamedStack import NamedStack

print("\n === Towers of Hanoi ===")

# Set up "Board"
left = NamedStack("Left")
middle = NamedStack("Middle")
right = NamedStack("Right")

towers = [left, middle, right]

# Set Up Game
num_rings = int(input("\nHow many rings do you want to play with?\n"))

while num_rings < 3:
    num_rings = int(input("Enter a number greater than equal to 3\n"))

for ring in range(num_rings, 0, -1):
    left.push(ring)

optimal_moves = (2**num_rings) - 1
print(f"\nThe best solution to this game is {optimal_moves} moves.")


## Helper Method
def get_input():
    choices = [tower.name[0] for tower in towers]

    while True:
        for i in range(len(towers)):
            name = towers[i].name
            letter = choices[i]
            print(f"Enter {letter} for {name}")

        user_input = input("")

        if user_input.capitalize() in choices:
            for i in range(len(towers)):
                if user_input is choices[i]:
                    return towers[i]

### Play The Game ###
moves = 0

while right._size != num_rings:
    print("\n\n\n=== Current Towers ===")

    for tower in towers:
        tower.display()

    while True:
        print("\nWhich tower do you want to move from?\n")
        from_tower = get_input()

        print("\nWhich tower do you want to move to?\n")
        to_tower = get_input()

        if from_tower.is_empty():
            print("\n\nInvalid Move. Try Again")
        elif to_tower.is_empty() or from_tower.peek < to_tower.peek:
            disk = from_tower.pop()
            to_tower.push(disk)
            moves += 1
            break
        else:
            print("\n\nInvalid Move. Try Again")

    print(
        f"\n\nYou completed the game in {moves} moves, and the optimal number of moves is {optimal_moves}")

