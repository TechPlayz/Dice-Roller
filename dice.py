import pyfiglet as pf
import random
import time

#Header
header = 'Dice Roller'
print(pf.figlet_format(header))
print('An open source project by TechPlayz')
time.sleep(1)

while True:
    print()
    print('1. Single Dice(1-6)')
    print('2. Double Dice(1-12)')
    dtype = int(input('What type of dice do you want: '))

    print()
    cheat = input('Allow Cheats? (Y/N): ')

    def roll(dtype,startval,stepval):
        if dtype == 1:
            print()
            print('Your dice number is: ',random.randrange(startval,7,stepval))
        elif dtype == 2:
            print()
            print('Your dice number is: ',random.randrange(startval,13,stepval))  

    if cheat.upper() == 'N':
        startval = 1
        stepval = 1 
    elif cheat.upper() == 'Y':
        print()
        print('1. Only odd numbers')
        print('2. Only even numbers')
        ch = int(input('Cheat type: '))
        if ch == 1:
            startval = 1
            stepval = 2
        elif ch == 2:
            startval = 2
            stepval = 2


    roll(dtype,startval,stepval)
    time.sleep(1)
    print()
    cont = input('Do you want to continue? (Y/N): ')
    if cont.upper() == 'N':
        print()
        print(pf.figlet_format('Thank You!'))
        time.sleep(2)
        break




