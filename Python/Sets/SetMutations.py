a = int(input())
l = set(map(int, input().split()))
n = int(input())
for i in range(n):
    command = input().split()  
    value = set(map(int, input().split()))
    if(command[0] == 'update'):
        #l.update(value)
        l |= value
    elif(command[0] == 'intersection_update'):
        #l.intersection_update(value)
        l &= value
    elif(command[0] == 'difference_update'):
        #l.difference_update(value)
        l -= value
    elif(command[0] == 'symmetric_difference_update'):
        #l.symmetric_difference_update(value)
        l ^= value

print(sum(l))