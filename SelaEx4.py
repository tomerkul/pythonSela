def mydivisor():
    mylist =[]
    mynum = int(input("enter a number:"))
    x = range(1,int(mynum))
    for i in x:
        if mynum%i== 0:
            print(i)
            mylist.append(i)
    print(mylist)
mydivisor()