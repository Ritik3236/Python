# Python does not provide multiple ways to do the same thing .
import random

tricks = ['s', 'w', 'g']
rounds = 10
tie = 0
win = 0
loose = 0
invalid = 0


def wining_rule(c_bet, u_bet):
    if u_bet not in tricks:
        return -1
    print(f'Computer bet : {c_bet}')
    index_of_c_bet = tricks.index(c_bet)
    index_of_u_bet = tricks.index(u_bet)
    if index_of_u_bet == index_of_c_bet:
        return 0
    elif (index_of_c_bet + 1) % 3 != index_of_u_bet:
        return 1
    else:
        return 2


''' Rules '''

try:
    file = open('ruless.txt')
    for line in file:
        print(line.rstrip(), end='\n')
        # input()
    file.close()
except Exception:
    print("Snake : s, Water : w, Gun : g")

''' Program '''
name = input("Welcome Player Enter Your Name: ")
for i in range(1, rounds + 1):
    computer_bet = random.choices(tricks)
    user_bet = input("\nEnter Your Bet: ").lower()
    result = wining_rule(computer_bet[0], user_bet)

    if result == -1:
        print("Invalid Input")
        invalid += 1

    elif result == 0:
        print("Tie")
        tie += 1

    elif result == 1:
        print("You Win")
        win += 1

    else:
        print("You Loose")
        loose += 1

print(f'\n\t\t\t\tGame Over \n\nYour Score {win} \nComputer Score {loose}')
if win > loose:
    print(f'Congratulation {name} for Wining')
elif loose > win:
    print(f'Congratulation Computer Ji for Wining')
else:
    print("Draw")
print(f'Total Win: {win}, Loose: {loose}, Draw: {tie}, Invalid Input {invalid}')
