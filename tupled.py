import random
def main():
    print("Welcome to the tupled out game")
    players = 0
    try:
        players = int(input("How many players?: "))
    except:
        print("That is not a valid number. Please try again.")
        return
    if players < 1:
        print("1 or more players required. Please try again.")
        return
    scores = []
    for i in range(players):
        scores.append(0)
        dice_values = [[0, False], [0, False], [0, False]]
        done_rolling = False
        while not done_rolling:
            roll_values = [random.randint(1,6),random.randint(1,6),random.randint(1,6)]
            string = ""
            for z in range(len(dice_values)):
                if not dice_values[z][1]:
                    string += f"Die #{z+1}, new value: {roll_values[z]}\n"
                    dice_values[z][0] = roll_values[z]
            print("---")
            print("Current dice values: ")
            for z in range(len(dice_values)):
                print(f"Dice #{z+1}: {dice_values[z][0]} - Fixed:")
            cont = input("Would you like to roll again? (y/n): ").lower()
            if cont != 'y':
                done_rolling = False
        
        for z in range(len(dice_values)):
            scores[i] += dice_values[z]
    for i in range(players):
        print(f"Player #{i+1}: ")
main()