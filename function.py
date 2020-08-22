def countWordsFromFile():
    fileName = input("enter the file name: ")
    numberOfWords = 0
    file = open(fileName, "r")
    for line in file :
        words = line.split()
        numberOfWords = numberOfWords + len(words)
    print("Number of Words")
    print(numberOfWords)

countWordsFromFile()
