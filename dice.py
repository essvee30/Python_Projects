import random

n = int(input("How many times do you want to throw the dice = "))
sum = 0
for i in range(1, n+1):
    dice = random.randrange(1, 7)
    print(f"Number = {dice} after {i} roll of the die");
    sum += dice
print(f"The sum of all the numbers that appear on the die is = {sum}")