import random

highest_number = input("Type a number: ") #using this name for variable because this will be the highest number that random.randint will go to.

if highest_number.isdigit():
    highest_number = int(highest_number)

    if highest_number <= 0:
        print('Please type a number larger than 0 next time.')
        quit()
else:
    print('Please type a number next time.')
    quit()

random_number = random.randint(0, highest_number)
guesses = 0 #we create a counter

while True:
    guesses += 1 #everytime user make a guess it will add +1 in guesses. 
    user_guess = input("Make a guess: ") #we ask user to make a guess and to type a number
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('Please type a number next time.')  # if user dont type a number program will tell him to print a number next time and send him back to "make a guess"
        continue

    if user_guess == random_number:   #if user types the same number as program, program will end (break).
        print("You got it!")
        break  
    elif user_guess > random_number:
        print("You were above the number!")
    else:
        print("You were below the number!")

print("You got it in", guesses, "guesses") #after break program will print out in how many guesses user got it!
