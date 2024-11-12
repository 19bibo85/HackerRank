def print_formatted(number):
    max = len(format(number, "b"))
    for i in range(1, number + 1):        
        d = format(i, "d").rjust(max)
        o = format(i, "o").rjust(max)
        x = format(i, "x").rjust(max)        
        b = format(i, "b").rjust(max)
        print(str.upper(f"{d} {o} {x} {b}"))

n = int(input())
print_formatted(n)