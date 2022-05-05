from collections import defaultdict
def compute_total(book_count):
    discount = [1, 0.95, 0.9, 0.8, 0.75]
    total = 0
    for val in book_count.values():
        total += 8 * val
    total *= discount[len(book_count) - 1]
    return total


def price(books):
    if len(books) == 0:
        return 0
    book_count = defaultdict(int)
    for i in books:
        book_count[i] += 1
    return compute_total(book_count)

