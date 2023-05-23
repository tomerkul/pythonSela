def grep(word,path):
    i = open(path, "r")
    lines = i.readlines()
    for line in lines:
        if word in line:
                print(line)
    i.close()

file_path = "C:/Users/Tom/Desktop/Ex1.txt"
w = "Shalom"
grep(w,file_path)
