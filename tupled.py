import random
import matplotlib.pyplot as plt
import time
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
    time.sleep(0.5)
    for i in range(players):
        scores.append(0)
        dice_values = [[0, False], [0, False], [0, False]]
        done_rolling = False
        print(f"\n\nRolling for Player #{i+1}...")
        time.sleep(0.5)
        print('...')
        time.sleep(0.3)
        print('...')
        time.sleep(0.3)
        print('...')
        time.sleep(0.5)
        while not done_rolling:
            roll_values = [random.randint(1,6),random.randint(1,6),random.randint(1,6)]
            string = "\n"
            for z in range(len(dice_values)):
                if not dice_values[z][1]:
                    string += f"Die #{z+1}: value: {roll_values[z]}\n"
                    dice_values[z][0] = roll_values[z]
            print(string)
            if dice_values[0][0] == dice_values[1][0] and dice_values[1][0] == dice_values[2][0]:
                print("Tupled out!")
                tupled_out = True
                done_rolling = True
                scores[i] = 0
                time.sleep(1.5)
                
            else:
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
                time.sleep(0.8)
                print("---")
                print(f"Current dice values (player {i+1}): ")
                total = 0
                for z in range(len(dice_values)):
                    fixed = "yes" if dice_values[z][1] else "no"
                    print(f"Dice #{z+1}: {dice_values[z][0]} - Fixed: {fixed}")
                    total += dice_values[z][0]
                print(f"Total score: {total}")
                cont = input("Would you like to roll again? (y/n): ").lower()
                if cont != 'y':
                    for z in range(len(dice_values)):
                        scores[i] += dice_values[z][0]
                    done_rolling = True
                else:
                    print("Re-rolling...")      
                    time.sleep(0.7)
  
    x = []
    for i in range(players):
        print(f"Player #{i+1}: Score: {scores[i]}")
        x.append(f"Player {i+1}")
    bar = plt.bar(x, scores, color="red")
    bar[scores.index(max(scores))].set_color('gold')
    plt.title("Tupled Out Final Scores")
    print("Displaying final scores (close program when done)")
    plt.show()
    return

main()