s1 = set(map(int, input().split()))
n = int(input())
r = True
for i in range(n):
    s2 = set(map(int, input().split()))
    s2 -= s1
    if(len(s2) > 0):
        r = False
print(r)