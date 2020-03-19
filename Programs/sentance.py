import os
sourcePath = os.listdir('old/')
for eachFile in sourcePath:
    inputFile = 'old/' + eachFile
    destinationPath = 'new/' + eachFile
    print("Conversionis ongoing for: " + inputFile)
    with open(inputFile,'r') as rf:
        with open(destinationPath, 'a') as wf:

            line = rf.readline()
            wf.write(line)
            line = rf.readline()
            c=1
            while not '</sami>' in line:
                data = ''
                while line != '\n':
                    if c == 1:
                        data += line[:-1]
                    else:
                        data += line[line.find("'>")+2:-1]
                    line = rf.readline()
                    c+= 1
                wf.write(data + '\n')
                c = 1
                line = rf.readline()

