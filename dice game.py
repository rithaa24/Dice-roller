import random

def roll_dice(num_dice):
    dice_rolls = [random.randint(1, 6) for _ in range(num_dice)]
    return dice_rolls

def get_num_dice():
    return int(input("Enter the number of dice to roll: "))

def display_result(dice_rolls):
    print(f"Result: {dice_rolls}")

def main():
    while True:
        num_dice = get_num_dice()
        dice_rolls = roll_dice(num_dice)
        display_result(dice_rolls)

        play_again = input("Roll again? (y/n): ").lower()
        if play_again != 'y':
            break

if __name__ == "__main__":
    main()
