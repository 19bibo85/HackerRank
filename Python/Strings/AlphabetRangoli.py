def print_rangoli(size):
    alphabet = "abc"
    for i in range(size * 2 - 1):
        for j in range((size - 1) * 2 + 1):
            if (j % 2 == 0 and i == size - 1):
                print("a", end = "")
            else:
                print("-", end = "")                
        print()

n = int(input())
print_rangoli(n)