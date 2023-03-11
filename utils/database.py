"""
Concerned with storing and retrieving books from a csv file
Format of the csv file:

name,author,read
"""

books_file = "books.txt"


def add_book(book, author):
    with open(books_file, 'a') as file:
        file.write(f'{book},{author},0\n')
        ...


def retrieve_books():
    with open(books_file, "r") as file:
        lines = [line.strip().split(",") for line in file.readlines()]

    return [
        {'name': line[0], 'author': line[1], 'read': line[2]} for line in lines
    ]


# mark something as read will change the read from false to true
def mark_as_read(book_name, author_name):
    books = retrieve_books()
    for book in books:
        if book['name'] == book_name & book['author'] == author_name:
            book['read'] = "1"
    _save_all_books(books)


def _save_all_books(books):
    with open(books_file, 'w') as file:
        for book in books:
            file.write(f"{book['name']},{book['author']},{book['read']}\n")


def delete_book(book_name, author_name):
    books = retrieve_books()
    books_new = [book for book in books if book['name'] != book_name & book['author'] != author_name]
    _save_all_books(books_new)
