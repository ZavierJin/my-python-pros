# Number Guessing Game

import random

key = random.randint(1, 100)
total_count = 7
counter = 0
success = False

print("------- Number Guessing -------")

while counter < total_count:
    counter += 1
    answer = int(input("\nPlease input a number: (1-100)\n"))
    if key < answer:
        print("Too big!")
    elif key > answer:
        print("Too small!")
    elif key == answer:
        print("Congratulations on your correct answer!!!")
        success = True
        break

if not success:
    print("\nSorry, you lose.")
else:
    if counter == 1:
        mess = "Wow! You guessed it only once!!!"
    elif counter <= 3:
        mess = "Great! You guessed it only " + str(counter) \
            + " times!"
    else:
        mess = "You guessed it " + str(counter) + " times."
    print(mess)

print("\n----------- Game End -----------")
