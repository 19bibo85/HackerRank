n = int(input())
x = set(map(int, input().split()))
m = int(input())
y = set(map(int, input().split()))
z = x.intersection(y)
print(len(z))