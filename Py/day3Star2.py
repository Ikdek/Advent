import string,itertools
f = open("inputDay3.txt", "r")
list = []
for i in f.read().splitlines():
    list.append(i)
y = 1
sumC = 0

lower = dict.fromkeys(string.ascii_lowercase)
upper = dict.fromkeys(string.ascii_uppercase)
prio = dict(itertools.chain(lower.items(),upper.items()))

badgePoten = {}
for i in prio.keys():
    prio[i] = y
    y +=1
a = 0
id = 0
dicFin = {}

for i in list:
    if id not in dicFin:
        dicFin[id] = []
    if a == 2:
        dicFin[id] += i
        a == 0
        id += 1
    else:
        dicFin[id] += i
        a += 1


print(list)