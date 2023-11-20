f = open("input.txt", "r")
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
# print(dic)
print(max)
print(maxKey)
del dic[maxKey]
max2 = dic[1]
maxKey2 = 1
for i in dic:
    if dic[i] > max2:
        max2 = dic[i]
        maxKey2 = i

print(max2)
print(maxKey2)

del dic[maxKey2]
max3 = dic[1]
maxKey3 = 1
for i in dic:
    if dic[i] > max3:
        max3 = dic[i]
        maxKey3 = i
        
print(max3)
print(maxKey3)

# test = [6471,1935,1793,3843,6059,6736,6101,3133,6861,1330,1962,5538,6760]
# b = 0
# for i in test:
#     b += i

# print("================")
# print(b)

print(max+max2+max3)