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
        print(f"Rolling for Player #{i+1}...")
        while not done_rolling:
            roll_values = [random.randint(1,6),random.randint(1,6),random.randint(1,6)]
            string = ""
            for z in range(len(dice_values)):
                if not dice_values[z][1]:
                    string += f"Die #{z+1}: value: {roll_values[z]}\n"
                    dice_values[z][0] = roll_values[z]
            print(string)
            if dice_values[0][0] == dice_values[1][0]:
                if dice_values[0][1] != True and dice_values[1][1] != True:
                    print("Dice 1 and 2 are now fixed!")
                dice_values[0][1] = True
                dice_values[1][1] = True
            if dice_values[0][0] == dice_values[2][0]:
                if dice_values[0][1] != True and dice_values[2][1] != True:
                    print("Dice 1 and 3 are now fixed!")
                dice_values[0][1] = True
                dice_values[2][1] = True
            if dice_values[1][0] == dice_values[2][0]:
                if dice_values[1][1] != True and dice_values[2][1] != True:
                    print("Dice 2 and 3 are now fixed!")
                dice_values[1][1] = True
                dice_values[2][1] = True
            print("---")
            print("Current dice values: ")
            total = 0
            for z in range(len(dice_values)):
                if dice_values[z][1]:
                    fixed = "yes"
                else:
                    fixed = "no"
                print(f"Dice #{z+1}: {dice_values[z][0]} - Fixed: {fixed}")
                total += dice_values[z][0]
            print(f"Total score: {total}")
            if dice_values[0][1] and dice_values[1][1] and dice_values[2][1]:
                print("All dice are fixed! Turn is over.")
                done_rolling = True
            else:
                cont = input("Would you like to roll again? (y/n): ").lower()
                if cont != 'y':
                    done_rolling = True
        
        for z in range(len(dice_values)):
            scores[i] += dice_values[z][0]
    for i in range(players):
        print(f"Player #{i+1}: Score: {dice_values[i]}")

main()