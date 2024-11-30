k = int(input())
rooms = list(map(int, input().split()))
dic = {}
for room in rooms:
    if (not(dic.get(room))):
        dic[room] = 1
    else:
        dic[room] += 1

for d in dic:
    if (dic[d] != k):
        print(d)
        break