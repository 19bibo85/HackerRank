def count_substring(string, sub_string):
    count = 0
    lenstr = len(string)
    lensub = len(sub_string)
    for i in range(lenstr - lensub + 1):
        if (string[i:i+lensub] == sub_string):
            count += 1
    return count

string = input().strip()
sub_string = input().strip()

count = count_substring(string, sub_string)
print(count)