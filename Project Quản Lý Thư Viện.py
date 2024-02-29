import tkinter as tk
from tkinter import ttk, messagebox

# Định nghĩa lớp Node và Book từ mã của bạn
class Node:
    def __init__(self, isbn, title, author, publisher, genre, status="Available"):
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
        self.add_default_books()
    
    def add_default_books(self):
        default_books = [
            ("8", "Sapiens: Lược sử loài người", "Yuval Noah Harari", "HarperCollins", "Khoa học phổ thông, Lịch sử", "available"),
            ("7", "Nhà giả kim", "Paulo Coelho", "HarperCollins", "Tiểu thuyết, Giả tưởng", "available"),
            ("2", "Kiêu hãnh và định kiến", "Jane Austen", "Penguin Books", "Tiểu thuyết, Lãng mạn", "available"),
            ("1", "Bố già", "Mario Puzo", "G. P. Putnam's Sons", "Tiểu thuyết, Tội phạm", "borrowed"),
            ("5", "Chúa tể của những chiếc nhẫn", "J. R. R. Tolkien", "Houghton Mifflin Harcourt", "Tiểu thuyết, Giả tưởng", "available"),
            ("6", "Harry Potter và Hòn đá Phù thủy", "J. K. Rowling", "Bloomsbury Publishing", "Tiểu thuyết, Giả tưởng", "available"),
            ("4", "Hoàng tử bé", "Antoine de Saint-Exupéry", "Gallimard", "Tiểu thuyết, Giả tưởng", "available"),
            ("10", "1984", "George Orwell", "Penguin Books", "Tiểu thuyết, Chính trị", "borrowed")
        ]
        for isbn, title, author, publisher, genre, status in default_books:
            self.insert(isbn, title, author, publisher, genre, status)

    def insert(self, isbn, title, author, publisher, genre, status):
        new_node = Node(isbn, title, author, publisher, genre, status)
        if self.root is None:
            self.root = new_node
        else:
            self._insert(new_node, self.root)

    def _insert(self, new_node, current_node):
        if new_node.isbn < current_node.isbn:
            if current_node.left is None:
                current_node.left = new_node
            else:
                self._insert(new_node, current_node.left)
        else:
            if current_node.right is None:
                current_node.right = new_node
            else:
                self._insert(new_node, current_node.right)

    def search_by_isbn(self, isbn):
        return self._search_by_isbn(isbn, self.root)

    def _search_by_isbn(self, isbn, current_node):
        if current_node is None:
            return None
        if isbn == current_node.isbn:
            return current_node
        elif isbn < current_node.isbn:
            return self._search_by_isbn(isbn, current_node.left)
        else:
            return self._search_by_isbn(isbn, current_node.right)
        
    def search_by_title(self, title):
        return self._search_by_title(title, self.root)

    def _search_by_title(self, title, current_node):
        if current_node is None:
            return None
        if title.lower() == current_node.title.lower():
            return current_node
        left_search = self._search_by_title(title, current_node.left)
        if left_search is not None:
            return left_search
        return self._search_by_title(title, current_node.right)


    def borrow_book(self, isbn):
        node = self.search_by_isbn(isbn)
        if node is None:
            return "Book does not exist"
        if node.status == "borrowed":
            return "Book has already been borrowed"
        node.status = "borrowed"
        return "Book borrowed successfully"

    def return_book(self, isbn):
        node = self.search_by_isbn(isbn)
        if node is None:
            return "Book does not exist"
        if node.status == "available":
            return "Book has not been borrowed"
        node.status = "available"
        return "Book returned successfully"

    # In Book class
    def show_all_books(self, callback, available_only=False):
        self._inorder_traversal(self.root, callback, available_only)


    def _inorder_traversal(self, current_node, callback, available_only=False):
        if current_node:
            self._inorder_traversal(current_node.left, callback, available_only)
            if not available_only or current_node.status == "available":
                callback(current_node)
            self._inorder_traversal(current_node.right, callback, available_only)

    def show_available_books(self, callback):
        self._inorder_traversal(self.root, callback, available_only=True)

    def show_borrowed_books(self, callback):
    # Sử dụng inorder traversal để hiển thị sách đang được mượn
        def filter_borrowed_books(node):
            if node.status == 'borrowed':  # Chỉ lọc ra những sách đang được mượn
                callback(node)
        self._inorder_traversal(self.root, filter_borrowed_books)


    def delete_book(self, isbn):
        self.root, deleted = self._delete_book(self.root, isbn)
        return deleted

    def _delete_book(self, current_node, isbn):
        if current_node is None:
            return current_node, False  # Book does not exist

        if isbn < current_node.isbn:
            current_node.left, deleted = self._delete_book(current_node.left, isbn)
        elif isbn > current_node.isbn:
            current_node.right, deleted = self._delete_book(current_node.right, isbn)
        else:
            # This is the node to be deleted
            if current_node.left is None:
                return current_node.right, True
            elif current_node.right is None:
                return current_node.left, True
            temp = self._min_value_node(current_node.right)
            current_node.isbn = temp.isbn
            current_node.title = temp.title
            current_node.author = temp.author
            current_node.publisher = temp.publisher
            current_node.genre = temp.genre
            current_node.status = temp.status
            current_node.right, _ = self._delete_book(current_node.right, current_node.isbn)
            deleted = True
        return current_node, deleted

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current
    
    def update_book(self, isbn, new_title, new_author, new_publisher, new_genre, new_status):
        node = self.search_by_isbn(isbn)
        if node:
            node.title = new_title
            node.author = new_author
            node.publisher = new_publisher
            node.genre = new_genre
            node.status = new_status
            return True  # Thành công khi cập nhật sách
        return False  # Trả về False nếu không tìm thấy sách

# Định nghĩa lớp GUI
class BookApp:
    def __init__(self, root):
        self.root = root
        self.book = Book()  # Sử dụng lớp Book đã được
        self.setup_ui()

    def setup_ui(self):
        self.root.title("Library Management System")
        self.root.geometry("800x600")

        # Create main frame for padding and alignment
        main_frame = tk.Frame(self.root)
        main_frame.pack(expand=True, fill='both', padx=20, pady=20)

        # Create left frame for the form entries and buttons
        left_frame = tk.Frame(main_frame)
        left_frame.pack(side='left', fill='y', expand=False)

        # Form entries
        labels = ['ID:', 'Title:', 'Author:', 'Publisher:', 'Genre:', 'Status:']
        entries = [tk.Entry(left_frame) for _ in labels]
        self.isbn_entry, self.title_entry, self.author_entry, self.publisher_entry, self.genre_entry, self.status_entry = entries

        for i, label in enumerate(labels):
            tk.Label(left_frame, text=label).grid(row=i, column=0, sticky='e', pady=5)
            entries[i].grid(row=i, column=1, pady=5)

        # Status dropdown setup
        self.status_var = tk.StringVar()
        self.status_combo = ttk.Combobox(left_frame, textvariable=self.status_var, state="readonly", values=['available', 'borrowed'])
        self.status_combo.grid(row=5, column=1, pady=5)
        self.status_combo.current(0)

        # Buttons
        buttons = ['ID', 'Search by ID', 'Search by Title', 'Borrow Book', 'Return Book', 'Show All Books', 'Show Available Books', "Show Borrowed Books", 'Delete Book', 'Update Book', 'Exit']
        commands = [self.insert_book, self.search_by_isbn,self.search_by_title, self.borrow_book, self.return_book, self.show_all_books, self.show_available_books, self.show_borrowed_books, self.delete_book, self.update_book, self.exit_app]
        for i, (button_text, command) in enumerate(zip(buttons, commands)):
            tk.Button(left_frame, text=button_text, command=command).grid(row=6+i, column=0, columnspan=2, sticky='ew', pady=5)   



        # Right frame for the book list and scrollbar
        right_frame = tk.Frame(main_frame)
        right_frame.pack(side='right', fill='both', expand=True)

        # Label for headings
        headings = "Library Management System"
        tk.Label(right_frame, text=headings, font=('Arial', 20, 'bold')).pack(side='top', fill='x')


        self.tree_view = ttk.Treeview(right_frame, columns=("ID", "Title", "Author", "Publisher", "Genre", "Status"), show="headings")
        self.tree_view.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        for col in ("ID", "Title", "Author", "Publisher", "Genre", "Status"):
            self.tree_view.heading(col, text=col)
            self.tree_view.column(col, anchor=tk.W)

        scrollbar = ttk.Scrollbar(right_frame, orient=tk.VERTICAL, command=self.tree_view.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.tree_view.configure(yscrollcommand=scrollbar.set)

        self.tree_view.bind("<<TreeviewSelect>>", self.on_book_select)



    def insert_book(self):
        isbn = self.isbn_entry.get()
        title = self.title_entry.get()
        author = self.author_entry.get()
        publisher = self.publisher_entry.get()
        genre = self.genre_entry.get()
        status = self.status_var.get()
        self.book.insert(isbn, title, author, publisher, genre, status)
        messagebox.showinfo("Success", "Book added successfully")
        self.clear_entries()

    def search_by_isbn(self):
        isbn = self.isbn_entry.get()
        book_node = self.book.search_by_isbn(isbn)
        if book_node:
            # Nếu sách được tìm thấy, hiển thị thông tin trong TreeView
            # Đầu tiên, xóa tất cả các hàng hiện có trong TreeView
            for item in self.tree_view.get_children():
                self.tree_view.delete(item)
            # Tiếp theo, thêm sách tìm được vào TreeView
            self.tree_view.insert('', 'end', values=(book_node.isbn, book_node.title, book_node.author, book_node.publisher, book_node.genre, book_node.status))
            # Hiển thị thông báo sách đã được tìm thấy
           
        else:
            # Nếu không tìm thấy sách, hiển thị thông báo và đảm bảo TreeView rỗng
            for item in self.tree_view.get_children():
                self.tree_view.delete(item)
            messagebox.showinfo("Not Found", "No book found with that ISBN")
 
    def search_by_title(self):
        title = self.title_entry.get()
        book_node = self.book.search_by_title(title)
        # Xóa tất cả các hàng hiện có trong TreeView trước khi hiển thị kết quả
        for item in self.tree_view.get_children():
            self.tree_view.delete(item)
        if book_node:
            # Thêm sách tìm được vào TreeView
            self.tree_view.insert('', 'end', values=(book_node.isbn, book_node.title, book_node.author, book_node.publisher, book_node.genre, book_node.status))
        else:
            messagebox.showinfo("Not Found", "No book found with that title")




    def borrow_book(self):
        isbn = self.isbn_entry.get()
        result = self.book.borrow_book(isbn)
        messagebox.showinfo("Result", result)

    def return_book(self):
        isbn = self.isbn_entry.get()
        result = self.book.return_book(isbn)
        messagebox.showinfo("Result", result)

    def show_all_books(self):
    # Xóa tất cả các hàng trong Treeview trước khi thêm mới
        for item in self.tree_view.get_children():
            self.tree_view.delete(item)
        self.book.show_all_books(self.display_book)


    def show_available_books(self):
        # Xóa tất cả các hàng trong Treeview trước khi thêm mới
        for item in self.tree_view.get_children():
            self.tree_view.delete(item)
        # Chỉ hiển thị sách có sẵn
        self.book.show_all_books(self.display_book, available_only=True)

    def show_borrowed_books(self):
        # Xóa tất cả các hàng hiện tại trong Treeview
        for item in self.tree_view.get_children():
            self.tree_view.delete(item)
        # Hiển thị các sách đang được mượn
        self.book.show_borrowed_books(self.display_book)



    def delete_book(self):
        isbn = self.isbn_entry.get()
        deleted = self.book.delete_book(isbn)
        if deleted:
            messagebox.showinfo("Success", "Book deleted successfully")
        else:
            messagebox.showinfo("Error", "No book found with that ISBN")
        self.clear_entries()

    def clear_entries(self):
        # Clears all the entry widgets
        self.isbn_entry.delete(0, tk.END)
        self.title_entry.delete(0, tk.END)
        self.author_entry.delete(0, tk.END)
        self.publisher_entry.delete(0, tk.END)
        self.genre_entry.delete(0, tk.END)
        # Refresh the book list
        self.show_all_books()

    def display_book(self, book):
    # Thêm sách vào Treeview thay vì Listbox
        self.tree_view.insert('', 'end', values=(book.isbn, book.title, book.author, book.publisher, book.genre, book.status))
    
    def on_book_select(self, event):
        for selection in self.tree_view.selection():
            item = self.tree_view.item(selection)
            values = item['values']
            if values:
                self.isbn_entry.delete(0, tk.END)
                self.isbn_entry.insert(0, values[0])
                self.title_entry.delete(0, tk.END)
                self.title_entry.insert(0, values[1])
                self.author_entry.delete(0, tk.END)
                self.author_entry.insert(0, values[2])
                self.publisher_entry.delete(0, tk.END)
                self.publisher_entry.insert(0, values[3])
                self.genre_entry.delete(0, tk.END)
                self.genre_entry.insert(0, values[4])
                self.status_combo.set(values[5])

    def update_book(self):
        isbn = self.isbn_entry.get()
        title = self.title_entry.get()
        author = self.author_entry.get()
        publisher = self.publisher_entry.get()
        genre = self.genre_entry.get()
        status = self.status_var.get()
        updated = self.book.update_book(isbn, title, author, publisher, genre, status)
        if updated:
            # Cập nhật thông tin trên TreeView
            for selection in self.tree_view.selection():
                self.tree_view.item(selection, values=(isbn, title, author, publisher, genre, status))
            messagebox.showinfo("Success", "Book updated successfully")
        else:
            messagebox.showinfo("Error", "Failed to update the book")
    
    def exit_app(self):
        response = messagebox.askyesno("Exit", "Are you sure you want to exit?")
        if response:
            self.root.destroy()  # Đóng cửa sổ ứng dụng


if __name__ == "__main__":
    root = tk.Tk()
    app = BookApp(root)
    root.mainloop()

