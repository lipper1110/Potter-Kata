def compute_total(books):
    discount = [1, 0.95, 0.9, 0.8, 0.75]
    books_dict = {0:0, 1:0, 2:0, 3:0, 4:0}
    result = 0;
    types = []
    books_len = len(books)
    for i in books:
        books_dict[i] += 1
    while books_len:
        types = set([i for i in books_dict if books_dict[i]])
        if books_len == 8 and len(types) == 5:
            result += 6.4
            books_len = 0
            break
        for i in range(5):
            if books_dict[i]:
                books_dict[i] -= 1
                books_len -= 1
        result += len(types) * discount[len(types) - 1 ]
        types = []
    return result * 8

def price(books):
    if len(books) == 0:
        return 0
    return compute_total(books)
