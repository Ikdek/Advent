f = open("inputDay2.txt", "r")
list = []
for i in f.read().splitlines():
    if i == "\n":
        pass
    else:
        list.append(i)

dic = {}
dicScore = {
    "X" : 1,
    "Y" : 2,
    "Z" : 3,
    "A" : 1,
    "B" : 2,
    "C" : 3
}
def needTo(a,b):
    if b == "X":
        p = 0
        if a == "A":
            return p + 3
        elif a == "B":
            return p + 1
        elif a == "C":
            return p + 2
    elif b == "Y":
        p = 3
        if a == "A":
            return p + 1
        elif a == "B":
            return p + 2
        elif a == "C":
            return p + 3
    elif b == "Z":
        p = 6
        if a == "A":
            return p + 2
        elif a == "B":
            return p + 3
        elif a == "C":
            return p + 1 
y = 1

for a in list:
    dic[y] = a.split()
    y += 1
score = 0
for i in dic:
    score += needTo(dic[i][0],dic[i][1])


print(score)
