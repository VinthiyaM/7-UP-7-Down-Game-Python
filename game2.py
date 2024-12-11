import random
import time

def roll_dice():
    # Roll two dice
    return random.randint(1, 6), random.randint(1, 6)

def print_dice(dice_value):
    # Display each dice face using ASCII art
    dice_faces = {
        1: ("[-----]", "[     ]", "[  *  ]", "[     ]", "[-----]"),
        2: ("[-----]", "[*    ]", "[     ]", "[    *]", "[-----]"),
        3: ("[-----]", "[*    ]", "[  *  ]", "[    *]", "[-----]"),
        4: ("[-----]", "[*   ]", "[     ]", "[   *]", "[-----]"),
        5: ("[-----]", "[*   ]", "[  *  ]", "[   *]", "[-----]"),
        6: ("[-----]", "[*   ]", "[   ]", "[   *]", "[-----]")
    }
    for line in dice_faces[dice_value]:
        print(line)

def play_game():
    print("Welcome to the 7 Up, 7 Down game!")
    print("Guess if the sum of two dice will be:")
    print("1. 7 Down (less than 7)")
    print("2. 7 Up (greater than 7)")
    print("3. Exactly 7")

    # Get the player's guess
    guess = int(input("Enter your guess (1 for 7 Down, 2 for 7 Up, 3 for Exactly 7): "))

    # Roll the dice and display results
    dice1, dice2 = roll_dice()
    total = dice1 + dice2
    print("\nRolling the dice...\n")
    time.sleep(1)  # Adding delay for effect

    print("Dice 1:")
    print_dice(dice1)
    print("\nDice 2:")
    print_dice(dice2)

    print(f"\nThe total of the dice roll is: {total}")

    # Determine the outcome
    if total < 7:
        outcome = 1  # 7 Down
    elif total > 7:
        outcome = 2  # 7 Up
    else:
        outcome = 3  # Exactly 7

    # Check if the guess matches the outcome
    if guess == outcome:
        print("Congratulations! Your guess was correct.")
    else:
        print("Sorry, your guess was wrong. Better luck next time!")

# Run the game
play_game()
input("\nPress Enter to exit.")