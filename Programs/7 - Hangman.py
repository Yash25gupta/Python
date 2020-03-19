import random


def showlist(lst):
    for i in lst:
        print(i, end=' ')
    print()


with open('words.txt', 'r') as f:
    word = f.readlines()[random.randint(3, 279495)].upper()

# print(word)
word_list = ['_' for i in range(1, len(word))]
showlist(word_list)

game_over = False
lives = 6
while not game_over:
    while True:
        char = input('Guess a letter. : ').upper()
        if len(char) == 1:
            break
        print('Enter single letter only !!!')
    if char not in word:
        lives -= 1
    print('Lives remaining : {}\n'.format(lives))
    for i in range(len(word)):
        if char == word[i]:
            word_list[i] = char
    showlist(word_list)
    if '_' not in word_list or lives == 0:
        if lives == 0:
            print('Game Over. You lose!!!')
        else:
            print('You Win !!!')
        print('The word was : {}'.format(word))
        game_over = True
