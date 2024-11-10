def mutate_string(string, position, character):
    chars = list(string)
    chars[position] = character
    return "".join(chars)
    # r = ""
    # for i in range(len(string)):
    #     if (i != position):
    #         r += s[i]
    #     else:
    #         r += character
    # return r

s = input()
i, c = input().split()
s_new = mutate_string(s, int(i), c)
print(s_new)