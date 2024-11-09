sequences = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    sequence = [name, score]
    sequences.append(sequence)

scores = set()
for sequence in sequences:
    scores.add(sequence[1])

s = list(scores)
s.sort()
secondlowest = s[1]

names = []
for sequence in sequences:
    if (sequence[1] == secondlowest):
        names.append(sequence[0])

names.sort()
for name in names:
    print(name)