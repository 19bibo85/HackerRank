def swap_case(s):
    r = ""
    for i in s:
        if (i.islower()):
            r += i.upper()
        else:                   
            r += i.lower()
    return r

print(swap_case("Alberto"))