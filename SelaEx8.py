def whoiswinner(a = []):
    for i in a:
        #Side
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
x = [[1,2,1],[2,2,1],[2,1,2]]
print(whoiswinner(x))