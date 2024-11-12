import re
def solve(s):
    r = ""
    for w in re.split(r'( +)', s):
        r += f"{w[0].upper()}{w[1:]}"
    return r

print(solve(input()))