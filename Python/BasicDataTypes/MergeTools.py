def merge_the_tools(string, k):
    for s in range(0, len(string), k):
        for x in dict.fromkeys(string[s:s+k]):
            print(x, end="")
        print()

string, k = input(), int(input())
merge_the_tools(string, k)