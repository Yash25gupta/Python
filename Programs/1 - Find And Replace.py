import os
txtToFnd = '&#39;'
txtToReplace = "'"
sourcePath = os.listdir('old/')
for eachFile in sourcePath:
    inputFile = 'old/' + eachFile
    print("Conversionis ongoing for: " + inputFile)
    with open(inputFile,'r') as inputFile:
        fileData = inputFile.read()
        freq = 0
        freq = fileData.count(txtToFnd)
    destinationPath = 'new/' + eachFile
    fileData = fileData.replace(txtToFnd,txtToReplace)
    with open(destinationPath,'w') as eachFile:
        eachFile.write(fileData)
    print('Total %d Record Replaced' %freq)

