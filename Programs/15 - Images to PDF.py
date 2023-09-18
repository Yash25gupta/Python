from PIL import Image
from os import path, listdir

FOLDER = 'images'
imgPageList = []
if path.exists(FOLDER):
    for item in listdir(FOLDER):
        if item.endswith('.jpg'):
            filePath = path.join(FOLDER, item)
            imgPage = Image.open(filePath).convert('RGB')
            imgPageList.append(imgPage)

if len(imgPageList) > 1:
    imgPageList[0].save(r'Catalogue.pdf', save_all=True, append_images=imgPageList[1:])
elif len(imgPageList) == 1:
    imgPageList[0].save(r'Catalogue.pdf')
