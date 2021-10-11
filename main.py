from random import randint, choice
import pyautogui  # hotkeys

###################################################


def asci():
    ttt = f"""
          _______________________________________
         |            |            |            |
         |     {availab[0]}     |     {availab[1]}     |     {availab[2]}     |
         |            |            |            |
         |____________|____________|____________|
         |            |            |            |
         |     {availab[3]}     |     {availab[4]}     |     {availab[5]}     |
         |            |            |            |
         |____________|____________|____________|
         |            |            |            |
         |     {availab[6]}     |     {availab[7]}     |     {availab[8]}     |
         |            |            |            |
         |____________|____________|____________|

        """
    return ttt


print('\nWelcome to Tic Tac Toe game!')

username = input("What's your name?:  ")
sign = input(f"Which one do you choose {username}? (X or O):  ").upper()

if sign == 'X':
    sign = 'X '
    computer = '🟡'
else:
    sign = '🟡'
    computer = 'X '

availab = ["1 ", "2 ", "3 ", "4 ", "5 ", "6 ", "7 ", "8 ", "9 "]
chosen_list = []
user_list = []
comp_list = []
for _ in range(5):

    print(asci())
    try:
        user = int(input(f'Where do you put < {sign}>, select numbers: '))
    except ValueError:
        user = int(input("Enter a number, not a string!: "))

    while True:
        if user in chosen_list:
            user = int(input(f'Number {user} has been chosen, please select another number!'))
        else:
            break
    try:
        chosen_list.append(user)
        availab[user-1] = sign
    except IndexError:
        user = int(input('Please select available numbers: '))
        chosen_list.append(user)
        availab[user - 1] = sign
    while True:
        bot = randint(1, 9)
        if bot not in chosen_list:
            break
        if len(chosen_list) == 9:
            break
    chosen_list.append(bot)
    availab[bot-1] = computer

    user_list.append(user)
    comp_list.append(bot)

    pyautogui.hotkey('ctrl', '9')

    print(f'\n               Computer has just chosen {bot}')  # wait add needed
    
    if 1 in user_list and 2 in user_list and 3 in user_list:
        print(asci(), f'{username} won the game! 😃')
        break
    elif 4 in user_list and 5 in user_list and 6 in user_list:
        print(asci(), f'{username} won the game! 😃')
        break
    elif 7 in user_list and 8 in user_list and 9 in user_list:
        print(asci(), f'{username} won the game! 😃')
        break
    elif 1 in user_list and 5 in user_list and 9 in user_list:
        print(asci(), f'{username} won the game! 😃')
        break
    elif 7 in user_list and 5 in user_list and 3 in user_list:
        print(asci(), f'{username} won the game! 😃')
        break
    elif 1 in user_list and 4 in user_list and 7 in user_list:
        print(asci(), f'{username} won the game! 😃')
        break
    elif 2 in user_list and 5 in user_list and 8 in user_list:
        print(asci(), f'{username} won the game! 😃')
        break
    elif 3 in user_list and 6 in user_list and 9 in user_list:
        print(asci(), f'{username} won the game! 😃')
        break

    elif 1 in comp_list and 2 in comp_list and 3 in comp_list:
        print(asci(), f'You lose 😔 Computer won the game!')
        break
    elif 4 in comp_list and 5 in comp_list and 6 in comp_list:
        print(asci(), f'You lose 😔 Computer won the game!')
        break
    elif 7 in comp_list and 8 in comp_list and 9 in comp_list:
        print(asci(), f'You lose 😔 Computer won the game!')
        break
    elif 1 in comp_list and 5 in comp_list and 9 in comp_list:
        print(asci(), f'You lose 😔 Computer won the game!')
        break
    elif 7 in comp_list and 5 in comp_list and 3 in comp_list:
        print(asci(), f'You lose 😔 Computer won the game!')
        break
    elif 1 in comp_list and 4 in comp_list and 7 in comp_list:
        print(asci(), f'You lose 😔 Computer won the game!')
        break
    elif 2 in comp_list and 5 in comp_list and 8 in comp_list:
        print(asci(), f'You lose 😔 Computer won the game!')
        break
    elif 3 in comp_list and 6 in comp_list and 9 in comp_list:
        print(asci(), f'You lose 😔 Computer won the game!')
        break

    if _ == 4:
        print("It's a draw. No one wins! 🤨")





