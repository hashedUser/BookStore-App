import utils.database as database

USER_CHOICE = """
Enter:
-- 'a' to add a new book
-- 'l' to list all books
-- 'r' to mark a book as read
-- 'd' to delete a book 
-- 'q' to quit

Your Choice: """


def menu():
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input == 'a':
            prompt_add_book()
        elif user_input == 'l':
            list_books()
        elif user_input == 'r':
            prompt_read_book()
        elif user_input == 'd':
            prompt_delete_book()
        else:
            print("Unknown command please try again")

        user_input = input(USER_CHOICE)


def prompt_add_book():
    book_name = input("Enter the new book name: ")
    author_name = input("Enter the new book author: ")
    database.add_book(book_name, author_name)


def list_books():
    books = database.retrieve_books()
    for book in books:
        read = "YES" if book['read'] == "1" else "NO"
        print(f"{book['name']} by {book['author']}, read: {read}")


def prompt_read_book():
    book_name = input("Enter the name of the book that you just finished reading: ")
    database.mark_as_read(book_name)


def prompt_delete_book():
    book_name = input("Enter the name of the book that needs to be removed: ")
    database.delete_book(book_name)


menu()