file = open("C:/Users/srshi/Documents/Efficom 2023/Algo-Python/adventOfCode/Advent/inputDay2.txt", "r")
list = []
def cleanUp(file):
    for i in file.read().splitlines():
        if i == "\n":
            pass
        else:
            list.append(i)
cleanUp(file)

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

def splitToDic(list):
    inc = 1
    for a in list:
        dic[inc] = a.split()
        inc += 1
splitToDic(list)
score = 0

for i in dic:
    if dicScore[dic[i][0]] == dicScore[dic[i][1]]:
        score += 3
        score += dicScore[dic[i][1]]
    else:
        score += winner(dic[i][0],dic[i][1])
        

print(f"La somme des victoire donne un score de {score}")
