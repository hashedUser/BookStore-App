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
        pass



menu()
