import random


color = random.choice(1,100)

for i in range(1, 99):
    try:
        user = str(input("Guess the lucky color: "))
        if user == color:
            print("Hurray!!")
            print(f"You guessed the color right, it's {color}")
            break

    except(ValueError):
        user != color
        print(f"Your Guess is Incorrect, the color is {color}")


# import random


# num = random.choices(white, green, yellow)

# n = str(input("Guess a color:"))

# if (n == num):
# 	print("Great! You guessed the color in just 1 try! You're a Mastermind!")
# else:
# 	ctr = 0

# 	while (n != num):
# 		ctr += 1

# 		count = 0
		
# 		n = str(n)

		
# 		num = str(num)

		
# 		correct = ['X']*4

		
# 		for i in range(0, 4):

			
# 			if (n[i] == num[i]):
			
# 				count += 1

# 				correct[i] = n[i]
# 			else:
# 				continue

# 		if (count < 4) and (count != 0):
# 			print("Not quite the number. But you did get ", count, " digit(s) correct!")
# 			print("Also these numbers in your input were correct.")
# 			for k in correct:
# 				print(k, end=' ')
# 			print('\n')
# 			print('\n')
# 			n = str(input("Enter your next choice of numbers: "))

# 		elif (count == 0):
# 			print("None of the colors in your input match.")
# 			n = str(input("Enter your next choice of colors: "))

# 	if n == num:
# 		print("You've become a Mastermind!")
# 		print("It took you only", ctr, "tries.")

# these are what i have tried on this also
