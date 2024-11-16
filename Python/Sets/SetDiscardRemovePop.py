n = int(input())
a = set(map(int, input().split()))
m = int(input())
for i in range(m):
    c = input().split()
    if (c[0] == "pop"):
        a.pop()
    elif (c[0] == "remove"):
        e = int(c[1])
        a.remove(e)        
    elif (c[0] == "discard"):
        e = int(c[1])
        a.discard(e)
sum = 0
for i in a:
    sum += i
print(sum)