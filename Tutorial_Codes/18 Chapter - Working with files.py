# Tutorial 213 - Read Text Files
# read file             
# open function         # open file
# read method           # read file
# seek method           # to change position of curser
# tell method           # tell position of curser
# readline method       # read 1 line
# close method          # close file

# f = open('file_read.txt', 'r')
f = open(r'E:\Computer Learning\Programs\Python\file_read.txt', 'r')

# print(f'curser position - {f.tell()}')
# print(f.read())
# print(f'curser position - {f.tell()}')
# f.seek(0)
# print(f'curser position after seek - {f.tell()}')
# print(f.read())
# print(f.readline(), end="")
# print(f.readline(), end="")
# print(f.readline(), end="")

# lines = f.readlines()[:2]   # return list of lines
# print(lines)
# print(len(lines))
# for line in lines:
#     print(line, end='')
# for line in f:
    # print(line, end='')

# print(f.name)
# print(f.closed)

f.close()


# *****************************************************************************************
# Tutorial 214 - With Block - Read File

# f = open('file_read.txt', 'r')
# f.read()
# f.close()

# with block
# context maneger
with open('file_read.txt') as f:     # no need to close file
    data = f.read()
    print(data)


# *****************************************************************************************
# Tutorial 215 - File IO Write to File
# w     # overwrite file          # use when file is empty  # can create file
# a     # append data to file     # add data                # can create file
# r+    # overwrite data(insert mode)  # begin from top     # can't create file

# with open('file_write.txt', 'w') as f:
#     f.write('Hello World.')

# with open('file_write.txt', 'a') as f:
#     f.write('My name is yash.\n')

# with open('write.txt', 'r+') as f:
#     f.seek(len(f.read()))       # used to move curser to last position
#     f.write('My age is 20.\n')


# *****************************************************************************************
# Tutorial 216 - File IO Read and Write
# read text from 'file_read.txt' and write it to 'file_write.txt'
with open('file_read.txt','r') as rf:
    with open('file_write.txt','w') as wf:
        wf.write(rf.read())


# *****************************************************************************************
# Tutorial 217 & 218 - Exercise 1 & solution
'''
read file --->  r.txt
    Yash,100
    Harsh,80
    Krish,50
    Gupta,20
write file -->  w.txt
    Yash's salary is 100
    Harsh's salary is 80
    Krish's salary is 50
    Gupta's salary is 20
'''

with open('r.txt','r') as rf:
    with open('w.txt','a') as wf:
        wf.write(rf.read().replace(',', "'s salary is "))
        # data = rf.read()
        # data = data.replace(',', "'s salary is ")
        # wf.write(data)

# with open('r.txt','r') as rf:
#     with open('w.txt','a') as wf:
#         for line in rf.readlines():
#             name,salary = line.split(',')
#             wf.write(f"{name}'s salary is {salary}")


# *****************************************************************************************
# Tutorial 219 & 220 & 221 - Exercise 2 & solution & Better solution

# with open('index.html','r') as rf:
#     with open('index_link.txt','w') as wf:
#         for line in rf.readlines():
#             if '<a href=' in line:
#                 a = line.find('"') + 1
#                 b = line.find('"', a)
#                 wf.write(line[a:b] + '\n')

with open('index.html','r') as rf:
    with open('index_link.txt','w') as wf:
        text = rf.read()
        link_exist = True
        while link_exist:
            pos = text.find('<a href=')
            if pos == -1:
                link_exist = False
            else:
                a = text.find('"',pos) + 1
                b = text.find('"', a)
                wf.write(text[a:b] + '\n')
                text = text[b:]


# *****************************************************************************************
# Tutorial 222 - Read LOVE STORY with python
with open('long.txt', 'r', encoding='utf-8') as f:
    print(f.encoding)
    data = f.read()
    print(data)

with open('long.txt', 'r') as f:
    data = f.read(100)
    while len(data) > 0:
        print(data)
        data = f.read(100)
    
