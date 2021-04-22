import random
import sys


def diceNumber():
    random.randint
    roll = input("press enter to roll the dice: ")

    die1 = random.randrange(1, 7)
    die2 = random.randrange(1, 7)

    return (die1, die2)


def roll_dice(dices):
    die1, die2 = dices
    print("player- the sum of numbers you have got in die 1 and die 2 are {} + {} = {}".format(die1, die2, sum(dices)))


value = diceNumber()
roll_dice(value)


sum_of_dices = sum(value)


if sum_of_dices in (7, 11):
    result = "congratulations you won"

elif sum_of_dices in (2, 3, 12):
    result = "you lost, try again next time"

else:
    result = "continue your game please"
    currentpoint = sum_of_dices
    print("good game, your current point is", currentpoint)

while result == "continue your game please":
    value = diceNumber()
    roll_dice(value)
    sum_of_dices = sum(value)

    if sum_of_dices == currentpoint:
        result = "congratulations you won"

    elif sum_of_dices == 7:
        result = "you lost, try again next time"


if result == "congratulations you won":
    print("congratulations,you won")

else:
    print("you lost, try again next time")
