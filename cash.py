from cs50 import get_float

# get a positive input from user
dollars = get_float("Change owed: ")

if dollars <= 0.00:
    dollars = get_float("Change owed: ")

# convert dollars to cents
cents = round(dollars * 100)

# create a variable that will count number of coins
coins = 0

# can we use quarters? If positive, find the leftover and add 1 coin
while cents >= 25:
    cents = cents - 25
    coins += 1

# can we use dimes? If positive, find the leftover and add 1 coin
while cents >= 10:
    cents = cents - 10
    coins += 1

# can we use nickels? If positive, find the leftover and add 1 coin
while cents >= 5:
    cents = cents - 5
    coins += 1

# can we use pennies? If positive, find the leftover and add 1 coin
while cents >= 1:
    cents = cents - 1
    coins += 1

# print the number of coins
print(coins)
