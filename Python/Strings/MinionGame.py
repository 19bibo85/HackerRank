def minion_game(string):
    vowels = "AEIOU"
    vIndexes = [i for i in range(len(string)) if (string[i] in vowels)]
    cIndexes = [i for i in range(len(string)) if (string[i] not in vowels)]

    vc = 0
    cc = 0        
    for v in vIndexes:
        vc += len(string) - v
    for c in cIndexes:
        cc += len(string) - c
        
    if(vc > cc):
        print(f"Kevin {vc}")
    elif(vc == cc):
        print(f"Draw")
    else:
        print(f"Stuart {cc}")
    
minion_game(input())