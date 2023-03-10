import utils.database as database

USER_CHOICE = """
Enter:
-- 'a' to add a new book
-- 'l' to list all books
-- 'r' to mark a book as read
-- 'd' to delete a book 
-- 'q' to quit

Your Choice:"""


def menu():
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input == 'a':
            database.add_book(prompt_add_book())
        if user_input == 'l':
            list_books()
        if user_input == 'r':
            prompt_read_book()
        if user_input == 'd':
            prompt_delete_book()

def prompt_add_book():
    book_name = input("Enter the name of the book: ")
    author_name = input("Enter the name of the author: ")
    return {'name': book_name, 'author': author_name, 'read': False}


def list_books():
    database.retrieve_books()


def prompt_read_book():
    book_name = input("Enter the name of the book that needs to be marked as read: ")
    database.mark_as_read(book_name)


def prompt_delete_book():
    book_name = input("Enter the name of the book that needs to be deleted: ")
    database.delete_book(book_name)


menu()
