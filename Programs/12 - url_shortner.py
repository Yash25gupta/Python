from csv import DictReader, DictWriter
import os
import random

lowers = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
          'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
uppers = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
          'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
nums = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0')
exist = False


def shorten_url(url):
    l = random.sample(lowers, 3)
    l.extend(random.sample(uppers, 3))
    l.extend(random.sample(nums, 1))
    random.shuffle(l)
    return url[:(url.find('//') + 2)] + 'bit.ly/' + ''.join(l)


while True:
    url = input('Enter your URL : ')
    if 0 < url.find('//') < 8:
        break
    print('Not a valid link')

with open('database.csv', 'r') as f:
    csv_reader = DictReader(f)
    for row in csv_reader:
        if url == row['Original']:
            print('Shorten URL : ' + row['Short'])
            exist = True

if not exist:
    with open('database.csv', 'a', newline='') as f:
        csv_writer = DictWriter(f, fieldnames=['Original', 'Short'])
        if os.stat('database.csv').st_size == 0:
            csv_writer.writeheader()
        s_url = shorten_url(url)
        csv_writer.writerow({
            'Original': url,
            'Short': s_url
        })
        print('Shorten URL : ' + s_url)
