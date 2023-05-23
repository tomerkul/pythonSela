def hangman1():
    from random import randint
    file_path = "C:/Users/Tom/Desktop/Ex30.txt"
    with open(file_path, "r") as i:
        word = i.read()
        WordList = word.split()
        x = randint(0, len(WordList))
        return WordList[x]








def hangman2():
    print("Welcome to Hangman!")
    word = hangman1()
    print(word)
    index = ""
    wordaslist = list(word)
    secret = len(word)*"_"
    secretlist = list(secret)
    print(secret)
    while("_" in secret):
        guess = input(" Guess your letter: ")
        if guess in wordaslist:
            index = int(wordaslist.index(guess))
            secretlist[index] = guess
            secret = "".join(secretlist)
            print(secret)








hangman2()