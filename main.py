import random


def int_input(msg=''):
    while True:
        try:
            return int(input(msg))
        except Exception:
            print('Invalid input. Please try again')


n = random.randint(10, 100)
term = 9

print('Welcome to guess the number game!\nFollow  the given hint to find the number')
print('Rule : You Have only 9 chance to guess mystery number. ')

num = int_input('Enter any number to guess : ')
win = False

for i in range(1, term):
    if num < n:
        print('Your number is lesser than mystery number.')
    elif num > n:
        print('Your number is greater than mystery number.')
    else:
        print(f'Congratulation You win this game in {i} term')
        win = True
        break

    num = int_input(f'Try Again, No. of guesses left {term - i}.\n')

if not win:
    print('You loose')
