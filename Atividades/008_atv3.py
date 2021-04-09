import random
from time import sleep

number1 = int(input("Write a number here: "))

if number1 % 2 == 1:
    print("The number is odd.")
else:
    print("The number is pair.")

sleep(1)
print("Now let's see the computer.")
sleep(2)
number2 = random.randint(1, 100)

if number2 % 2 == 1:
    print(f"The computer chose a number {number2} it is odd.")
else:
    print(f"The computer chose a number {number2} it is pair.")
