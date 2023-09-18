import random
lowers = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
          'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
uppers = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
          'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
nums = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0')
symbols = ("@", "#", "$", "%", "+", "\"", "/", "'", "!", "^", "?",
           ":", ".", "(", ")", "{", "}", "[", "]", "~", "-", "_", "=")
generate = True

# Length
while True:
    try:
        l = int(input('How many character you want in your Password? : '))
        if l >= 6:
            break
        print('Minimum length should be 6.')
    except ValueError:
        print('Please type digits only.')

# Number, Case, Symbol
msg = ('Numbers', 'Mix Case', 'Symbols')
msg_choice = {'want_numbers': None, 'want_mixcase': None, 'want_symbol': None}
for i in range(3):
    while True:
        s = input(
            'Do you want {} in your Password? (Y/N) : '.format(msg[i])).upper()
        if s == 'Y' or s == 'N':
            msg_choice[i] = False
            if s == 'Y':
                msg_choice[i] = True
            break
        print('Please type "Y/y/N/n" only')

# generate Password
while generate:
    password = ''
    count = 0
    while count < l:
        password = password + random.choice(lowers)
        count += 1
        if msg_choice[0] and count < l:     # Numbers
            password = password + random.choice(nums)
            count += 1
        if msg_choice[1] and count < l:     # Mixed Case
            password = password + random.choice(uppers)
            count += 1
        if msg_choice[2]and count < l:      # Symbols
            password = password + random.choice(symbols)
            count += 1
        if count == l:
            password = ''.join(random.sample(password, l))
            print('Generated Password : ' + password)
            again = input('\nGenerate Again? (Y/N) : ').upper()
            generate = False
            if again == 'Y':
                generate = True
            break
