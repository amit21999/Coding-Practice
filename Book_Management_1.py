import collections
import random

# Define the Book data structure
Book = collections.namedtuple('Book', ['title', 'author', 'genre', 'year'])

class LibraryCatalog:
    def __init__(self, books):
        self._books = books

    def __len__(self):
        return len(self._books)

    def __getitem__(self, position):
        return self._books[position]

    def filter_by_author(self, author_name):
        return [book for book in self._books if book.author == author_name]

    def filter_by_genre(self, genre):
        return [book for book in self._books if book.genre.lower() == genre.lower()]

    def random_book(self):
        return random.choice(self._books)

# Demo usage in main
def main():
    books = [
        Book("1984", "George Orwell", "Dystopian", 1949),
        Book("To Kill a Mockingbird", "Harper Lee", "Classic", 1960),
        Book("The Great Gatsby", "F. Scott Fitzgerald", "Classic", 1925),
        Book("Brave New World", "Aldous Huxley", "Dystopian", 1932),
        Book("The Catcher in the Rye", "J.D. Salinger", "Classic", 1951),
        Book("Fahrenheit 451", "Ray Bradbury", "Dystopian", 1953),
    ]

    catalog = LibraryCatalog(books)

    print("Total books:", len(catalog))

    print("\nFirst book in catalog:")
    print(catalog[0])

    print("\nLast 2 books:")
    print(catalog[-2:])

    print("\nBooks by George Orwell:")
    for book in catalog.filter_by_author("George Orwell"):
        print(book)

    print("\nAll Dystopian books:")
    for book in catalog.filter_by_genre("Dystopian"):
        print(book)

    print("\nRandom book suggestion:")
    print(catalog.random_book())

if __name__ == "__main__":
    main()
