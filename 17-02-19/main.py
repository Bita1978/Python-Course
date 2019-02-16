import mysql.connector
from books_model.dbdao import BooksDBAO
from books_model.book import Book

try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="root",
        database="db",
        pool_name="cp",
        pool_size=10
    )

    dbdao = BooksDBAO(db=mydb)
    book = dbdao.create_book(name="Easy Python", author="Enosh")
    print(book)
    dbdao.create_book(8, 'k')

    book = dbdao.find_by_id('jo')
    book = dbdao.find_by_id(89)
    book = dbdao.find_by_id(4)
    print(book)

    dbdao.find_by_name("joh")
    book = dbdao.find_by_name('Easy Python')
    print(book)

    book = Book(name='Easy JavaScript', author='Enosh', id=4)
    dbdao.update_book(7)
    updated_book = dbdao.update_book(book)
    print(updated_book)

    all_books = dbdao.find_all()
    print(all_books)

    dbdao.remove_book('k')
    deleted_book = dbdao.remove_book(4)
    print(deleted_book)

    print(dbdao.find_all())

except mysql.connector.Error as err:
    print(f"Something went wrong: {err}")