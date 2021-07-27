import random

top_no = input('Type a number: ')

if top_no.isdigit():
    top_no = int(top_no)

    if top_no <= 0:
        print('Type a number greater than 0 next time: ')
        quit()

else:
    print('please a type a number time')
    quit()


random_number = random.randint(0, top_no)

guesses = 0

while True:
    guesses += 1
    user_guess = input('Make a guess: ')
    if user_guess.isdigit():
        user_guess = int(user_guess)

    else:
        print('Please type a number next time')
        continue

    if user_guess == random_number:
        print('You got it')
        break
    elif user_guess > random_number:
        print('you were above the number')
    else:
        print('You were below the number')

print(f"you got it in {guesses} guesses")