def tictactoe(a,b):
    wall = " --- "
    side = "|"
    tab = "    "
    print(wall* int(a))
    for i in range(int(b)):
        print((side+tab)*(int(a)+1))
        print(wall * int(a))
tictactoe(3,3)