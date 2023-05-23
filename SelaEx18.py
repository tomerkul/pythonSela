import json

def printBirthday(jsonfile):
    with open(jsonfile,'r+') as f:
        data = json.loads(f.read())
    print("Welcome to the birthday dictionary. We know the birthdays of:")
    for key in data.keys():
        print(key)
    userchoice = input("Who's birthday do you want to look up? ")
    print(userchoice + "'s birthday is :" + data[userchoice])
    with open(jsonfile, 'r+') as f:
        newdata = list(str(input("would you like to add new data to your file? <syntax:key,value>: ")).split(","))
        data[str(newdata[0])] = str(newdata[1])
        json.dump(data, f, indent=4)




printBirthday("dictionar.json")
