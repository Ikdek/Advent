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
def winner(b,a):
    if a == "X":
        if b == "C":
            return 7
        elif b == "B":
            return 1
    elif a == "Y":
        if b == "A":
            return 8
        elif b == "C":
            return 2
    elif a == "Z":
        if b == "B":
            return 9
        elif b == "A":
            return 3
y = 1

for a in list:
    dic[y] = a.split()
    y += 1
score = 0

for i in dic:
    if dicScore[dic[i][0]] == dicScore[dic[i][1]]:
        score += 3
        score += dicScore[dic[i][1]]
    else:
        score += winner(dic[i][0],dic[i][1])
print(score)

print(winner('A',"Y"))
print(winner("B",'X'))
print(winner("C",'Z'))