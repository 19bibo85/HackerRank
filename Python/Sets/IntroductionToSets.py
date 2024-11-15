def average(array):
    s = set()
    for i in array:
        s.add(i)

    sum = 0
    for i in s:
        sum += i
    
    return f"{sum / len(s):.3f}"

n = int(input())
arr = list(map(int, input().split()))
result = average(arr)
print(result)