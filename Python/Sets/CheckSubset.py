t = int(input())
r = list()
for i in range(t):
    n1 = int(input())
    l1 = set(map(int, input().split()))
    
    n2 = int(input())
    l2 = set(map(int, input().split()))
    
    v1 = len(l2)
    l2 |= l1
    v2 = len(l2)
    r.append(v1 == v2)
    
for i in r:
    print(i)