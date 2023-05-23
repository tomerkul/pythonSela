import json
import re
def months(jsonfile):
    monthsofyear = {}
    with open(jsonfile, 'r+') as f:
        data = json.loads(f.read())
        listofdic =[]
        for i in data.values():
            pattern = r"(?<=\/)\d+(?=\/)"
            matches = re.findall(pattern, i)
            listofdic.append(matches[0])
        for c in listofdic:
            if str(int(c)) in monthsofyear:
                monthsofyear[str(int(c))] += 1
            else:
                monthsofyear[str(int(c))] = 1
    return monthsofyear
print(months("dictionar.json"))