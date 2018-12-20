import os.path
import json
import random
from colorama import init
init()
from colorama import Fore



# File path
file_path = 'player.txt'

print(Fore.BLUE + "Hi there!")
print(Fore.LIGHTCYAN_EX + "Next text")

# Checking existence
if not os.path.isfile(file_path):

    with open(file_path, mode='w') as my_file:
        player = {'name': input('Enter youer name').title() , 'score': 0}
        my_file.write(json.dumps(player))
else:

    with open(file_path, mode='r') as my_file:
        player = json.loads(my_file.read())


# Say hello to player
print(f"Hello and wlcome back {player['name']}")

# Ask player to continue
continue_question = input("Do you want to start the game? (Y/N)")

quit_answer = True

while quit_answer:
    # Validate answer
    if continue_question.lower().strip() == 'n' or continue_question.lower().strip() == 'no':
        print(f"bye bye {player['name']}")
        quit()

    elif continue_question.lower().strip() == 'y' or continue_question.lower().strip() == 'yes':
        print(f"Nice! {player['name']}")
        break
    else:
        print(f"i dont know what is {continue_question}")

    continue_question = input('')


computer_number = random.randint(1, 3)
print(f"Computer number {computer_number}")

print(f"Your Last Score is {player['score']}")


print('Do you think you can guess the number?! ')

for index in range(1, 4):

    guess = int(input(f"Guess number {index}: What is my number?\n"))
    if guess == computer_number:
        print(f"Nice!!! {player['name']} You did it!")
        print(f"I was thinking about {computer_number}")
        if index == 1:
            player['score'] = player['score'] + 15
            break
        elif index == 2:
            player['score'] = player['score'] + 10
            break
        else:
            player['score'] = player['score'] + 5
            break
    else:
        if index < 3:
            print(f"{player['name']} you should try again :)")
        else:
            print(f"Not so lucky {player['name']} :(")


with open(file_path, mode='w') as my_file:
    my_file.write(json.dumps(player))

input('')









