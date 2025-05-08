class Book:
    def __init__(self, title, author, price):
        self._title = title
        self._author = author
        self._price = price

    # Developer-focused representation
    def __repr__(self):
        return f"Book('{self._title}', '{self._author}', {self._price})"

    # User-facing string for print() or str()
    def __str__(self):
        return f"📘 {self.title} by {self.author} - ${self.price:.2f}"

    # --------- Properties with Getters ---------
    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @property
    def price(self):
        return self._price

    # --------- Setters with Validation ---------
    @title.setter
    def title(self, value):
        if not value.strip():
            raise ValueError("❌ Title cannot be empty!")
        self._title = value

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("❌ Price cannot be negative!")
        self._price = value


# -------------------- Testing It --------------------

def main():
    # Create a book object
    book = Book("1984", "George Orwell", 15.99)

    # Print the book
    print("✅ Initial book:")
    print(book)                  # uses __str__
    print("Developer view:", repr(book))  # uses __repr__

    # Update title and price correctly
    print("\n✅ Updating book title and price...")
    book.title = "Animal Farm"
    book.price = 12.49
    print(book)

    # Try setting an invalid title
    print("\n❌ Attempting to set empty title:")
    try:
        book.title = "   "
    except ValueError as e:
        print("Caught error:", e)

    # Try setting a negative price
    print("\n❌ Attempting to set negative price:")
    try:
        book.price = -10.00
    except ValueError as e:
        print("Caught error:", e)

    # Final object state
    print("\n✅ Final book object:")
    print(book)

if __name__ == '__main__':
    main()
