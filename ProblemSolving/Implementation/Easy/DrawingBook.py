def pageCount(n, p):
    lastPage = 1
    book = {}
    for page in range(1, n + 1):
        if (page % 2 == 0):
            lastPage += 1
        book[page] = lastPage

    return min(book[p] - 1, lastPage - book[p])


n = int(input("Give me the number of pages in the book: "))
p = int(input("Give me the page number to turn: "))
if (p > n):
    print(f"Page to turn {p} cannot be greater than {n}")
else:
    print(pageCount(n,p))
