import os, shutil

# NOTE: You can write every single extension inside tuples
dict_extensions = {
    'Audio_extensions' : ('.mp3', '.m4a', '.wav', '.flac'),
    'Video_extensions' : ('.mp4', '.mkv', '.MKV', '.flv', '.mpeg', '.3gp'),
    'Document_extensions' : ('.docx', '.pdf', '.txt', '.xlx'),
    'Image_extensions' : ('.jpg', '.png', '.bmp', '.tiff')
}

folderpath = input('Enter folder path : ')

def file_finder(path, file_extensions):
    files = []
    for file in os.listdir(path):
        for extension in file_extensions:
            if file.endswith(extension):
                files.append(file)
    return files

# # print(file_finder(folderpath, video_extensions))
for extension_type, extension_tuple in dict_extensions.items():
    new_folder_name = extension_type.split('_')[0] + ' Files'
    new_folder_path = os.path.join(folderpath,new_folder_name)  # new folder path
    for item in file_finder(folderpath, extension_tuple):
        if not os.path.exists(new_folder_path):
            os.mkdir(new_folder_path)
        item_path = os.path.join(folderpath, item)
        item_new_path = os.path.join(new_folder_path, item)
        shutil.move(item_path, item_new_path)

