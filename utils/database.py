books = []

""" 
Next Commit Changes:
Add file integration so that the database won't be a 
python list, but it would be a file on the storage
so that for every execution the file will be changed
and wouldn't be reset to its original form
"""


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
