def getMoneySpent(keyboards, drives, b):
    current = -1
    for k in keyboards:
        for d in drives:
            sum = k + d
            if (sum <= b and sum > current):
                current = sum
    return current

budget = int(input("Give me the budget: "))
keyboards = list(map(int, input("Give me the keyboards : ").split()))
drives = list(map(int, input("Give me the drives : ").split()))

print(getMoneySpent(keyboards, drives, budget))