n = int(input())
a = set(map(int, input().split()))
m = int(input())
b = set(map(int, input().split()))

l = list(a.symmetric_difference(b))
l.sort()
for i in l:
    print(i)
