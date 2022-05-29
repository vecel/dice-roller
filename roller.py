from random import randrange


WELCOME_MESSAGE = """\nHey! Welcome to my dice roller.
Enter command in the following format [number of dice]d[dice value] to roll the dice
You can pass more than one roll in one command. Just use SPACE and type next one.\n"""

def fetch_commands(command):
    rolls = command.split()
    return rolls

def roll_value(command):
    dice_number, dice_value = command.split('d')
    sum = 0
    for i in range(int(dice_number)):
        sum += randrange(1, int(dice_value))
    return sum

def roll(command = ''):
    commands = fetch_commands(command)
    results = []
    for i in range(len(commands)):
        results.append(roll_value(commands[i]))
    # print(results)
    return sum(results)

print(WELCOME_MESSAGE)
cmd = input()
print(roll(cmd))



