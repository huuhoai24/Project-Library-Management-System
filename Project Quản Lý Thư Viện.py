class Node:
    def __init__(self, isbn, title, author, publisher, genre, status):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.publisher = publisher
        self.genre = genre
        self.status = status
        self.left = None
        self.right = None


class Book:
    def __init__(self):
        self.root = None

    def insert(self, isbn, title, author, publisher, genre, status):
        new_node = Node(isbn, title, author, publisher, genre, status)
        self._insert(new_node, self.root)

    def _insert(self, new_node, current_node):
        """Inserts a new node into the binary search tree."""
        if current_node is None:
            self.root = new_node
            return new_node
        else:
            if new_node.isbn < current_node.isbn:
                current_node.left = self._insert(new_node, current_node.left)
            else:
                current_node.right = self._insert(new_node, current_node.right)
            return current_node

    def search_by_key(self, isbn):
        """Searches for a node by ISBN in the binary search tree."""
        return self._search_by_key(isbn, self.root)

    def _search_by_key(self, isbn, current_node):
        """Searches for a node by ISBN in the binary search tree."""
        if current_node is None:
            return None
        if isbn == current_node.isbn:
            return current_node
        if isbn < current_node.isbn:
            return self._search_by_key(isbn, current_node.left)
        else:
            return self._search_by_key(isbn, current_node.right)

    def search_by_title(self, title):
        """Searches for a node by title in the binary search tree."""
        current_node = self.root
        while current_node is not None:
            if title == current_node.title:
                return current_node
            elif title < current_node.title:
                current_node = current_node.left
            else:
                current_node = current_node.right
        return None

  class Node:
    def __init__(self, isbn, title, author, publisher, genre, status):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.publisher = publisher
        self.genre = genre
        self.status = status
        self.left = None
        self.right = None


class Book:
    def __init__(self):
        self.root = None

    def insert(self, isbn, title, author, publisher, genre, status):
        new_node = Node(isbn, title, author, publisher, genre, status)
        if self.root is None:
            self.root = new_node
        else:
            self._insert(new_node, self.root)

    def _insert(self, new_node, current_node):
        if current_node is None:
            return new_node
        else:
            if new_node.isbn < current_node.isbn:
                current_node.left = self._insert(new_node, current_node.left)
            else:
                current_node.right = self._insert(new_node, current_node.right)
        return current_node


    def search_by_key(self, isbn):
        return self._search_by_key(isbn, self.root)

    def _search_by_key(self, isbn, current_node):
        if current_node is None:
            return None
        if isbn == current_node.isbn:
            return current_node
        elif isbn < current_node.isbn:
            return self._search_by_key(isbn, current_node.left)
        else:
            return self._search_by_key(isbn, current_node.right)

    def search_by_title(self, title):
        return self._search_by_title(title, self.root)

    def _search_by_title(self, title, current_node):
        if current_node is None:
            return None
        if title == current_node.title:
            return current_node
        elif title < current_node.title:
            return self._search_by_title(title, current_node.left)
        else:
            return self._search_by_title(title, current_node.right)

    def borrow_book(self, isbn):
        """Marks a book as borrowed by updating its status."""
        node = self.search_by_key(isbn)
        if node is None:
            print("Book does not exist")
            return
        if node.status == "borrowed":
            print("Book has already been borrowed")
            return
        node.status = "borrowed"  # Cập nhật trạng thái của sách
        print("Book borrowed successfully")

    def return_book(self, isbn):
        """Marks a book as available by updating its status."""
        node = self.search_by_key(isbn)
        if node is None:
            print("Book does not exist")
            return
        if node.status == "available":
            print("Book has not been borrowed")
            return
        node.status = "available"  # Cập nhật trạng thái của sách
        print("Book returned successfully")

    def print_all_books(self):
        """Prints all books in the library."""
        self._inorder_traversal(self.root)

    def _inorder_traversal(self, current_node, available_only=False):
        """Performs an inorder traversal, printing only available books if specified."""
        if current_node:
            self._inorder_traversal(current_node.left, available_only)
            if not available_only or current_node.status == "available":
                print(current_node.isbn, current_node.title, current_node.author,
                      current_node.publisher, current_node.genre, current_node.status)
            self._inorder_traversal(current_node.right, available_only)

    def print_available_books(self):
        """Prints only books that are available for borrowing."""
        print("Available books:")
        self._inorder_traversal(self.root, available_only=True)


def main():
    book_system = Book()

    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. Search by ISBN")
        print("3. Search by Title")
        print("4. Borrow a Book")
        print("5. Return a Book")
        print("6. Print All Books")
        print("7. Print Available Books")
        print("8. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            isbn = input("Enter ISBN: ")
            title = input("Enter Title: ")
            author = input("Enter Author: ")
            publisher = input("Enter Publisher: ")
            genre = input("Enter Genre: ")
            status = input("Enter Status (available/borrowed): ")
            book_system.insert(isbn, title, author, publisher, genre, status)
            print("Book added successfully.")

        elif choice == '2':
            isbn = input("Enter ISBN to search: ")
            node = book_system.search_by_key(isbn)
            if node:
                print(f"Book Found:\nISBN: {node.isbn}\nTitle: {node.title}\nAuthor: {node.author}\nPublisher: {node.publisher}\nGenre: {node.genre}\nStatus: {node.status}")
            else:
                print("Book not found.")

        elif choice == '3':
            title = input("Enter Title to search: ")
            node = book_system.search_by_title(title)
            if node:
                print(f"Book Found:\nISBN: {node.isbn}\nTitle: {node.title}\nAuthor: {node.author}\nPublisher: {node.publisher}\nGenre: {node.genre}\nStatus: {node.status}")
            else:
                print("Book not found.")

        elif choice == '4':
            isbn = input("Enter ISBN of the book to borrow: ")
            book_system.borrow_book(isbn)

        elif choice == '5':
            isbn = input("Enter ISBN of the book to return: ")
            book_system.return_book(isbn)

        elif choice == '6':
            print("Printing all books in the library:")
            book_system.print_all_books()

        elif choice == '7':
            print("Printing all available books in the library:")
            book_system.print_available_books()

        elif choice == '8':
            print("Exiting the system.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


