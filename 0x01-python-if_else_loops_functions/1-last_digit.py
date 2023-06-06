#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
last_d = abs(number) % 10

if number > 0 or number == 0:
    if last_d > 5:
        print(f"Last digit of {number} is {last_d} and is greater than 5")
    elif last_d == 0:
        print(f"Last digit of {number} is {last_d} and is 0")
    elif last_d < 6 and last_d != 0:
        print(f"Last digit of {number} is {last_d} and is less than 6 "
              f"and not 0")
else:
    print(f"Last digit of {number} is {-last_d} and is less than 6 "
          f"and not 0")

