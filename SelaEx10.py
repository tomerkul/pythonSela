def hangman1():
    from random import randint
    file_path = "C:/Users/Tom/Desktop/Ex30.txt"
    with open(file_path, "r") as i:
        word = i.read()
        WordList = word.split()
        x = randint(0, len(WordList))
        print(WordList[x])

hangman1()