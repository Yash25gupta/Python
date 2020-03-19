import random
items = ('r', 'p', 's')
play = True

while play:
    comp_score = 0
    user_score = 0
    while comp_score<3 and user_score<3:
        print('\nPlease type   "R" for rock,   "P" for paper,   "S" for scissor)')
        user_pick = input('Your Choise : ').lower()
        comp_pick = random.choice(items)
        print('Computer Choose : '+ comp_pick)
        if comp_pick == user_pick:
            print(f'Match Draw ...')
        elif (comp_pick=='p' and user_pick=='s') or (comp_pick=='s' and user_pick=='r') or (comp_pick=='r' and user_pick=='p'):
            user_score += 1
            print('You win !!!')
        else:
            comp_score += 1
            print('Computer win !!!')
        print(f'Your Score : {user_score} and Computer Score : {comp_score}')
    if comp_score == 3:
        print(f'\nComputer wins the game by {comp_score}-{user_score}')
    else:
        print(f'\nYou wins the game by {user_score}-{comp_score}')
    play = False
    again = input('Do you want to Play again? (Y/N)').lower()
    if again == 'y':
        play = True

