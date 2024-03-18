from typing import List


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.page = 0

    def turn_page(self, page):
        self.page = page


class Library:

    def __init__(self, books):
        self.books: List[Book] = books

    def add_book(self, book: Book):
        self.books.append(book)

    def remove_book(self, title):
        to_remove = [b for b in self.books if b.title == title]
        if not to_remove:
            raise ValueError('No such title')
        if len(to_remove) > 1:
            raise ValueError('Too many titles were found')

        self.books.remove(to_remove[0])

    def get_books_by_author(self, author):
        return [b for b in self.books if b.author == author]

    def get_book_by_title(self, title):
        books = [b for b in self.books if b.title == title]

        if not books:
            raise ValueError('No such title')



