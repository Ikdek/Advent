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
for i in prio.keys():
    prio[i] = y
    y +=1
for z in range(len(list)):
    banlist = []
    firstHalf = list[z][:len(list[z])//2]
    lastHalf = list[z][len(list[z])//2:]
    for i in firstHalf:
        if i in lastHalf:
            if i not in banlist:
                sumC += prio[i]
                banlist.append(i)

print(sumC)