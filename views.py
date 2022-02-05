import random

flag = True
while flag:
    # takes in random number that user inputs stores in num variable
    num = input('Type a number for an upper bound: ')
    # makes sure user input is valid non negative integer
    if num.isdigit():
        print("Let's play!")
        num = int(num)
        # exits while loop
        flag = False
    else:
        print('Invalid input! Try again')

## stores random number in var secret between 1 and number input from user
secret = random.randint(1, num)
# set to none because we havent guessed yet
guess = None
# count = 1 because we want to tell user amount of tries
count = 1

# keep guessing until guess = secret
while guess != secret:
    # cannot use , for user input
    guess = input('Please type a number between 1 and ' + str(num) + ": ")
    # checks to make sure input is an integer
    if guess.isdigit():
        guess = int(guess)

    if guess == secret:
        print('You got it!')
    else:
        print('Please try again!')
        count += 1
print('It took you', count, 'guesses!')