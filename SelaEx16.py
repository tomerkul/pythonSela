
d ={}
str = "fdgsdg"
for x in str:
    if x in d : d[x]+=1
    else: d[x] = 1
print(d)