n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()

scores = student_marks[query_name]
sum = sum(scores)
count = len(scores)
avg = f"{round(sum / count, 2):.2f}"
print(avg)