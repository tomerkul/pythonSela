def whoiswinner(a = []):
    for i in a:
        #->
        if i == [2,2,2]:
            return "the winner is 2"
        elif i == [1,1,1]:
            return "the winner is 1"
    #for t in range(len(a)):
    #DOWN
    z = a[0]
    z2 = a[1]
    z3 = a[2]
    for r in range(len(z)):
        if z[r] == 2 and z2[r] == 2 and z3[r] == 2:
                return "the winner is 2"
        if z[r] == 1 and z2[r] == 1 and z3[r] == 1:
                return "the winner is 1"
    #diagonal
    center = z2[1]
    if center == 2:
        if z[0] == 2 and z3[2] == 2:
            return "the winner is 2"
        elif z[2] == 2 and z3[0] == 2:
            return "the winner is 2"
    if center == 1:
        if z[0] == 1 and z3[2] == 1:
            return "the winner is 1"
        elif z[2] == 1 and z3[0] == 1:
            return "the winner is 1"
    return "tie game"
#x = [[1,2,1],[2,0,1],[2,1,1]]
#print(whoiswinner(x))








def tictactoegame():
    game = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    status = whoiswinner(game)
    counter = 1
    while(status=="tie game"):
        if counter ==10:
            return print("tie game")
        if counter%2!=0 :
            x = input("x what is your choice? <row,col= syntax>: ")
            choicex = x.split(',')
            choicex[0] = int(choicex[0]) - 1
            choicex[1] = int(choicex[1]) - 1
            row = game[int(choicex[0])]
            if int(row[int(choicex[1])]) != 0:
                print("the square is not empty try another!")
                continue
            row[int(choicex[1])] = 1
            counter += 1
            [print(*sublist) for sublist in game]
            status = whoiswinner(game)
            if status != "tie game":
                break
        else:
            o = input("o what is your choice? <row,col syntax>: ")
            choiceo = o.split(',')
            choiceo[0] = str(int(choiceo[0]) - 1)
            choiceo[1] = str(int(choiceo[1]) - 1)
            row = game[int(choiceo[0])]
            if int(row[int(choiceo[1])]) != 0:
                print("the square is not empty try another!")
                continue
            row[int(choiceo[1])] = 2
            counter += 1
            status = whoiswinner(game)
            [print(*sublist) for sublist in game]

    return print(status)



tictactoegame()