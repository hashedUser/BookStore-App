books = []


def add_book(book):
    books.append(book)
    return books


def retrieve_books():
    print(books)


# mark something as read will change the read from false to true
def mark_as_read(book_name):
    for index in range(0, len(books)):
        if book_name == books[index]['name']:
            books[index]['read'] = True


def delete_book(book_name):
    for index in range(0, len(books)):
        if book_name == books[index]['name']:
            books.remove(books[index])
