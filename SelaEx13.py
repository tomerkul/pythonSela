import json


def library(a):
    dic = {}
    b = list(str(a))
    while(len(b)>0):
        count = 1
        pop = b.pop(0)
        while (True):
            if pop in b:
                count += 1
                b.remove(pop)
            else:
                dic[str(pop)] = count
                break
    return dic





x = "11112222eedfgsodgodnsfgjnvgnjsssf333"
js = json.dumps(library(x))
print(js)
with open("dictionar.json", "w") as outfile:
    outfile.write(js)











