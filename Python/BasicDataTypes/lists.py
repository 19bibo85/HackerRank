result = []
N = int(input())
for _ in range(N):
    command, *line =  input().split()
    params = list(map(int, line))
    if (command == "insert"):
        result.insert(params[0], params[1])
    elif (command == "print"):
        print(result)
    elif (command == "remove"):
        result.remove(params[0])
    elif (command == "append"):
        result.append(params[0])
    elif (command == "sort"):
        result.sort()
    elif (command == "pop"):
        result.pop()
    elif (command == "reverse"):
        result.reverse()