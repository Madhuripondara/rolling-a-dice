#rolling a dice
import random
def roll_dice():
    dice_value=random.randint(1,6)
    print("you rolled",dice_value)
roll_dice()
while True:
    choice=input("roll_again?(yes/no)")
    if choice=="yes":
        roll_dice()
    else:
        print("thankyou")
        break
