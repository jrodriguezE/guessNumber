# Guess the number
number = 21
user = 0

while number != user:
    user = int(input('Enter a Number: '))
    if number > user:
        print('too low')
    elif number < user:
        print('too high')
    else:
        print('You guess right!')