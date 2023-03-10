books = []


def add_book(book, author):
    books.append({'name': book, 'author': author, 'read': False})


def retrieve_books():
    return books


# mark something as read will change the read from false to true
def mark_as_read(book_name, author_name):
    for book in books:
        if book['name'] == book_name & book['author'] == author_name:
            book['read'] = True


def delete_book(book_name, author_name):
    global books
    books = [book for book in books if book['name'] != book_name & book['author'] != author_name]
