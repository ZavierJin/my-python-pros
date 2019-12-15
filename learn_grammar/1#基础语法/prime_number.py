
"""
input a number and determine
whether the number is prime or not
"""

from math import sqrt

print("\n----- Judging Prime Number -----")

while True:
    num = int(input("\nPlease enter a positive integer: \
(enter 0 to quit)\n"))
    if num == 0:    # quit
        break

    is_prime = True
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:    # not prime
            is_prime = False
            break
    if is_prime and num != 1:
        print("%d is a prime number." % num)
    else:
        print("%d is not a prime number." % num)

print("\n----- BYE -----\n")
