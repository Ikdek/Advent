f = open("C:/Users/srshi/Documents/Efficom 2023/Algo-Python/adventOfCode/Advent/input.txt", "r")
y = 1
list = []
dic = {}
for i in f.read().splitlines():
    if i == "\n":
        pass
    else:
        list.append(i)
for a in list:
    if a == "":
        y += 1
    else:
        if y in dic.keys():
            dic[y] += int(a)
        else:
            dic[y] = int(a)
max = dic[1]
maxKey = 1
for i in dic:
    if dic[i] > max:
        max = dic[i]
        maxKey = i
print(dic)
print(max)
print(maxKey)

# test = [6471,1935,1793,3843,6059,6736,6101,3133,6861,1330,1962,5538,6760]
# b = 0
# for i in test:
#     b += i

# print("================")
# print(b)