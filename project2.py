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

    def _insert(self, new_node, curr_node):
        if curr_node is None:
            self.root = new_node
            return
        if new_node.isbn < curr_node.isbn:
            self._insert(new_node, curr_node.left)
        else:
            self._insert(new_node, curr_node.right)

    def search_by_key(self, isbn):
        return self._search_by_key(isbn, self.root)

    def _search_by_key(self, isbn, curr_node):
        if curr_node is None:
            return None
        if isbn == curr_node.isbn:
            return curr_node
        if isbn < curr_node.isbn:
            return self._search_by_key(isbn, curr_node.left)
        else:
            return self._search_by_key(isbn, curr_node.right)

    def search_by_title(self, title):
        return self._search_by_title(title, self.root)

    def _search_by_title(self, title, curr_node):
        if curr_node is None:
            return None
        if title == curr_node.title:
            return curr_node
        if title < curr_node.title:
            return self._search_by_title(title, curr_node.left)
        else:
            return self._search_by_title(title, curr_node.right)

    def inorder_traversal(self):
        self._inorder_traversal(self.root)

    def _inorder_traversal(self, curr_node):
        if curr_node is not None:
            self._inorder_traversal(curr_node.left)
            print(curr_node.isbn, curr_node.title, curr_node.author, curr_node.publisher, curr_node.genre, curr_node.status)
            self._inorder_traversal(curr_node.right)

    def borrow_book(self, isbn):
        node = self.search_by_key(isbn)
        if node is None:
            print("Sách không tồn tại")
            return
        if node.status == "đã mượn":
            print("Sách đã được mượn")
            return
        node.status = "đã mượn"
        print("Mượn sách thành công")

    def return_book(self, isbn):
        node = self.search_by_key(isbn)
        if node is None:
            print("Sách không tồn tại")
            return
        if node.status == "sẵn có":
            print("Sách chưa được mượn")
            return
        node.status = "sẵn có"
        print("Trả sách thành công")

    def list_all_books(self):
        self._inorder_traversal(self.root)

    def list_available_books(self):
        self._inorder_traversal(self.root, True)

    def _inorder_traversal(self, curr_node, only_available=False):
        if curr_node is not None:
            self._inorder_traversal(curr_node.left, only_available)
            if not only_available or curr_node.status == "sẵn có":
                print(curr_node.isbn, curr_node.title, curr_node.author, curr_node.publisher, curr_node.genre, curr_node.status)
            self._inorder_traversal(curr_node.right, only_available)
def main():
    book_system = Book()

    while True:
        print("\n--- Thư viện sách ---")
        print("1. Thêm sách")
        print("2. Tìm kiếm sách theo mã ISBN")
        print("3. Tìm kiếm sách theo tiêu đề")
        print("4. Mượn sách")
        print("5. Trả sách")
        print("6. Liệt kê tất cả sách")
        print("7. Liệt kê sách đang có sẵn")
        print("8. Thoát")

        choice = input("Nhập lựa chọn của bạn (1-8): ")

        if choice == '1':
            isbn = input("Nhập mã ISBN: ")
            title = input("Nhập tiêu đề: ")
            author = input("Nhập tác giả: ")
            publisher = input("Nhập nhà xuất bản: ")
            genre = input("Nhập thể loại: ")
            status = input("Nhập trạng thái (sẵn có/đã mượn): ")
            book_system.insert(isbn, title, author, publisher, genre, status)
            print("Thêm sách thành công")

        elif choice == '2':
            isbn = input("Nhập mã ISBN: ")
            search_result = book_system.search_by_key(isbn)
            if search_result:
                print("Thông tin sách:")
                print("Mã ISBN:", search_result.isbn)
                print("Tiêu đề:", search_result.title)
                print("Tác giả:", search_result.author)
                print("Nhà xuất bản:", search_result.publisher)
                print("Thể loại:", search_result.genre)
                print("Trạng thái:", search_result.status)
            else:
                print("Sách không tìm thấy")

        elif choice == '3':
            title = input("Nhập tiêu đề: ")
            search_result = book_system.search_by_title(title)
            if search_result:
                print("Thông tin sách:")
                print("Mã ISBN:", search_result.isbn)
                print("Tiêu đề:", search_result.title)
                print("Tác giả:", search_result.author)
                print("Nhà xuất bản:", search_result.publisher)
                print("Thể loại:", search_result.genre)
                print("Trạng thái:", search_result.status)
            else:
                print("Sách không tìm thấy")

        elif choice == '4':
            isbn = input("Nhập mã ISBN: ")
            book_system.borrow_book(isbn)

        elif choice == '5':
            isbn = input("Nhập mã ISBN: ")
            book_system.return_book(isbn)

        elif choice == '6':
            book_system.list_all_books()

        elif choice == '7':
            book_system.list_available_books()

        elif choice == '8':
            break

        else:
            print("Lựa chọn không hợp lệ. Vui lòng nhập lại.")

if __name__ == "__main__":
    main()
