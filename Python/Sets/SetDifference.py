n = int(input())
x = set(map(int, input().split()))
m = int(input())
y = set(map(int, input().split()))
z = x.difference(y)
print(len(z))