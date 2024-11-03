def countingValleys(steps, path):
    valleys = 0
    seaLevel = 0
    currentStep = 0
    for step in range(0, steps):
        if (path[step] == 'U'):
            currentStep += 1
        elif (path[step] == 'D'):
            currentStep -= 1    

        if (seaLevel >= 0 and currentStep < 0):
            valleys += 1

        seaLevel = currentStep        
        
    return valleys

steps = input("Give me a sequence of steps: ")
print(countingValleys(len(steps), steps))