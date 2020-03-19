# Tutorial 228 - OS Module Part 1
import os

# print(os.getcwd())                    # get current working path
# os.mkdir('movies')                    # make a folder
# print(os.path.exists('movies'))       # check folder exist or not

# if os.path.exists('movies'):
#     print('Already Exist')
# else:
#     os.mkdir('movies')

# open('makefile.txt', 'a').close()     # create a file

# os.mkdir(r'F:\Games\folder')

# os.chdir(r'F:\Games')                 # change current working directory
# os.mkdir('movies')

# print(os.listdir())                   # list all files
# print(os.listdir(r'F:\Games'))

# for item in os.listdir():             # print full path of files
#     # print(os.getcwd() + '\\' + item)
#     path = os.path.join(os.getcwd(),item)
#     print(path)

for item in os.listdir(r'F:\Games'):
    path = os.path.join(r'F:\Games',item)
    print(path)


# *****************************************************************************************
# Tutorial 229 - OS module Part 2 and shutil module
import shutil
os.chdir(r'F:\test')
# print(os.listdir())

# fileiter = os.walk(r'F:\test')
# for current_path, folders_names, file_names in fileiter:
#     print(f'current path : {current_path}')
#     print(f'folders name : {folders_names}')
#     print(f'files name : {file_names}')

# os.rmdir('nn')                    # delete folder if empty
# shutil.rmtree('Songs')            # Delete folder with files permanently

# os.makedirs('new/movies')         # make folder inside folder

# shutil.copytree('new', 'movies/new')    # copy a folder to another location with files
# shutil.move('new', 'movies/new_move')     # move a folder and rename it

# shutil.copy('file.txt', 'new/file.txt')   # copy a file
# shutil.move('file.txt', 'new/file2.txt')  # move a file

