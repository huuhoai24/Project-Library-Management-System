import tkinter as tk
from tkinter import ttk, messagebox
import json

# Define the Node and Book classes for your code
class Node:
    def __init__(self, id, title, author, publisher, genre, status="Available"):
        self.id = id
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
        self.load_from_file()

    def load_from_file(self, filename="library_data.json"):
        try:
            with open(filename, 'r') as file:
                book_list = json.load(file)
            for book in book_list:
                if not self.search_by_id(book['id']):  # Prevent duplication
                    self.insert(book['id'], book['title'], book['author'], book['publisher'], book['genre'], book['status'])
        except FileNotFoundError:
            self.add_default_books()  # Only add default books if file not found

    def add_default_books(self):
        default_books = [
            ("978-0-316-19699-8", "Sapiens: A Brief History of Humankind", "Yuval Noah Harari", "HarperCollins", "Non-fiction, History", "Available"),
            ("978-1-4391-7103-7", "The Alchemist", "Paulo Coelho", "HarperCollins", "Fiction, Fantasy", "Available"),
            # Add more default books here
        ]
        for id, title, author, publisher, genre, status in default_books:
            if not self.search_by_id(id):  # Check if the book already exists
                self.insert(id, title, author, publisher, genre, status)

    def save_to_file(self, filename="library_data.json"):
        book_list = []
        def add_to_list(node):
            if node:
                book_list.append({
                    'id': node.id,
                    'title': node.title,
                    'author': node.author,
                    'publisher': node.publisher,
                    'genre': node.genre,
                    'status': node.status
                })
        self._inorder_traversal(self.root, add_to_list)
        with open(filename, 'w') as file:
            json.dump(book_list, file, indent=4)



    def insert(self, id, title, author, publisher, genre, status):
        new_node = Node(id, title, author, publisher, genre, status)
        if self.root is None:
            self.root = new_node
        else:
            self._insert(new_node, self.root)
        self.save_to_file()

    def _insert(self, new_node, current_node):
        if new_node.id < current_node.id:
            if current_node.left is None:
                current_node.left = new_node
            else:
                self._insert(new_node, current_node.left)
        else:
            if current_node.right is None:
                current_node.right = new_node
            else:
                self._insert(new_node, current_node.right)

    def search_by_id(self, id):
        return self._search_by_id(id, self.root)

    def _search_by_id(self, id, current_node):
        if current_node is None:
            return None
        if id == current_node.id:
            return current_node
        elif id < current_node.id:
            return self._search_by_id(id, current_node.left)
        else:
            return self._search_by_id(id, current_node.right)
        
    def search_by_title(self, title):
        return self._search_by_title(title, self.root)

    def _search_by_title(self, title, current_node):
        if current_node is None:
            return None
        if title.lower() in current_node.title.lower():
            return current_node
        left_search = self._search_by_title(title, current_node.left)
        if left_search is not None:
            return left_search
        return self._search_by_title(title, current_node.right)

    def borrow_book(self, id):
        node = self.search_by_id(id)
        if node is None:
            return "Book does not exist"
        if node.status == "Borrowed":
            return "Book has already been borrowed"
        node.status = "Borrowed"
        return "Book borrowed successfully"

    def return_book(self, id):
        node = self.search_by_id(id)
        if node is None:
            return "Book does not exist"
        if node.status == "Available":
            return "Book has not been borrowed"
        node.status = "Available"
        return "Book returned successfully"

    def _inorder_traversal(self, current_node, callback, available_only=False):
        if current_node:
            self._inorder_traversal(current_node.left, callback, available_only)
            if not available_only or current_node.status == "Available":
                callback(current_node)
            self._inorder_traversal(current_node.right, callback, available_only)


    def show_all_books(self, callback, available_only=False):
        self._inorder_traversal(self.root, callback, available_only)

    def show_available_books(self, callback):
        self._inorder_traversal(self.root, callback, available_only=True)

    def show_borrowed_books(self, callback):
        def filter_borrowed_books(node):
            if node.status == 'Borrowed':
                callback(node)
        self._inorder_traversal(self.root, filter_borrowed_books)

    def delete_book(self, id):
        self.root, deleted = self._delete_book(self.root, id)
        if deleted:
            self.save_to_file()  # Save changes after deleting
        return "Book deleted successfully" if deleted else "Book does not exist"

    def _delete_book(self, current_node, id):
        if current_node is None:
            return None, False
        if id < current_node.id:
            current_node.left, deleted = self._delete_book(current_node.left, id)
        elif id > current_node.id:
            current_node.right, deleted = self._delete_book(current_node.right, id)
        else:
            if current_node.left is None:
                return current_node.right, True
            elif current_node.right is None:
                return current_node.left, True
            min_larger_node = self._min_value_node(current_node.right)
            current_node.id, current_node.title, current_node.author, current_node.publisher, current_node.genre, current_node.status = \
                min_larger_node.id, min_larger_node.title, min_larger_node.author, min_larger_node.publisher, min_larger_node.genre, min_larger_node.status
            current_node.right, _ = self._delete_book(current_node.right, current_node.id)
            deleted = True
        return current_node, deleted

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def update_book(self, id, new_title, new_author, new_publisher, new_genre, new_status):
        node = self.search_by_id(id)
        if node:
            node.title = new_title
            node.author = new_author
            node.publisher = new_publisher
            node.genre = new_genre
            node.status = new_status
            self.save_to_file()
            return "Book updated successfully"
        return "Book does not exist"

# GUI Class Definition
class BookApp:
    def __init__(self, root):
        self.root = root
        self.book = Book()
        self.setup_ui()

    def setup_ui(self):
        self.root.title("Library Management System")
        self.root.geometry("800x600")

        main_frame = tk.Frame(self.root)
        main_frame.pack(expand=True, fill='both', padx=20, pady=20)

        left_frame = tk.Frame(main_frame)
        left_frame.pack(side='left', fill='y', expand=False)

        labels = ['ID:', 'Title:', 'Author:', 'Publisher:', 'Genre:', 'Status:']
        entries = [tk.Entry(left_frame) for _ in labels]
        self.id_entry, self.title_entry, self.author_entry, self.publisher_entry, self.genre_entry, self.status_entry = entries

        for i, label in enumerate(labels):
            tk.Label(left_frame, text=label).grid(row=i, column=0, sticky='e', pady=5)
            entries[i].grid(row=i, column=1, pady=5)

        self.status_var = tk.StringVar()
        self.status_combo = ttk.Combobox(left_frame, textvariable=self.status_var, state="readonly", values=['Available', 'Borrowed'])
        self.status_combo.grid(row=5, column=1, pady=5)
        self.status_combo.current(0)

        buttons = ['Insert Book', 'Search by ID', 'Search by Title', 'Borrow Book', 'Return Book', 'Show All Books', 'Show Available Books', 'Show Borrowed Books', 'Delete Book', 'Update Book', 'Exit']
        commands = [self.insert_book, self.search_by_id, self.search_by_title, self.borrow_book, self.return_book, self.show_all_books, self.show_available_books, self.show_borrowed_books, self.delete_book, self.update_book, self.exit_app]
        for i, (button_text, command) in enumerate(zip(buttons, commands)):
            tk.Button(left_frame, text=button_text, command=command).grid(row=6 + i, column=0, columnspan=2, sticky='ew', pady=5)

        right_frame = tk.Frame(main_frame)
        right_frame.pack(side='right', fill='both', expand=True)

        tk.Label(right_frame, text="Library Management System", font=('Arial', 20, 'bold')).pack(side='top', fill='x')

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
        id = self.id_entry.get().strip()  
        title = self.title_entry.get().strip()
        author = self.author_entry.get().strip()
        publisher = self.publisher_entry.get().strip()
        genre = self.genre_entry.get().strip()
        status = self.status_var.get().strip()

        if not all([id, title, author, publisher, genre, status]):
            messagebox.showerror("Insert Error", "All fields must be filled out")
            return

        existing_book = self.book.search_by_id(id)
        if existing_book:
            messagebox.showerror("Insert Error", "A book with this ID already exists")
            return

        self.book.insert(id, title, author, publisher, genre, status)
        messagebox.showinfo("Insert Result", "Book added successfully")
        self.clear_entries()
        self.show_all_books()  


    def search_by_id(self):
        id = self.id_entry.get()
        book_node = self.book.search_by_id(id)
        self.clear_tree_view()
        if book_node:
            self.tree_view.insert('', 'end', values=(book_node.id, book_node.title, book_node.author, book_node.publisher, book_node.genre, book_node.status))
        else:
            messagebox.showinfo("Search Result", "No book found with that ID")

    def search_by_title(self):
        title = self.title_entry.get()
        self.clear_tree_view()
        book_node = self.book.search_by_title(title)
        if book_node:
            self.tree_view.insert('', 'end', values=(book_node.id, book_node.title, book_node.author, book_node.publisher, book_node.genre, book_node.status))
        else:
            messagebox.showinfo("Search Result", "No book found with that title")

    def borrow_book(self):
        id = self.id_entry.get()
        result = self.book.borrow_book(id)
        messagebox.showinfo("Borrow Result", result)
        self.clear_entries()
        self.show_all_books()

    def return_book(self):
        id = self.id_entry.get()
        result = self.book.return_book(id)
        messagebox.showinfo("Return Result", result)
        self.clear_entries()
        self.show_all_books()

    def show_all_books(self):
        self.clear_tree_view()
        self.book.show_all_books(self.display_book)

    def show_available_books(self):
        self.clear_tree_view()
        self.book.show_available_books(self.display_book)

    def show_borrowed_books(self):
        self.clear_tree_view()
        self.book.show_borrowed_books(self.display_book)

    def delete_book(self):
        id = self.id_entry.get()
        result = self.book.delete_book(id)
        messagebox.showinfo("Delete Result", result)
        self.clear_entries()
        self.show_all_books()

    def update_book(self):
        id = self.id_entry.get()
        title = self.title_entry.get()
        author = self.author_entry.get()
        publisher = self.publisher_entry.get()
        genre = self.genre_entry.get()
        status = self.status_var.get()
        result = self.book.update_book(id, title, author, publisher, genre, status)
        messagebox.showinfo("Update Result", result)
        self.clear_entries()
        self.show_all_books()

    def clear_entries(self):
        for entry in [self.id_entry, self.title_entry, self.author_entry, self.publisher_entry, self.genre_entry]:
            entry.delete(0, tk.END)
        self.status_combo.set('Available')  

    def clear_tree_view(self):
        for item in self.tree_view.get_children():
            self.tree_view.delete(item)

    def display_book(self, book):
        self.tree_view.insert('', 'end', values=(book.id, book.title, book.author, book.publisher, book.genre, book.status))

    def on_book_select(self, event):
        selection = self.tree_view.selection()
        if selection:
            item = self.tree_view.item(selection[0])
            values = item['values']
            self.id_entry.delete(0, tk.END)
            self.id_entry.insert(0, values[0])
            self.title_entry.delete(0, tk.END)
            self.title_entry.insert(0, values[1])
            self.author_entry.delete(0, tk.END)
            self.author_entry.insert(0, values[2])
            self.publisher_entry.delete(0, tk.END)
            self.publisher_entry.insert(0, values[3])
            self.genre_entry.delete(0, tk.END)
            self.genre_entry.insert(0, values[4])
            self.status_combo.set(values[5])

    def exit_app(self):
        if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
            self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = BookApp(root)
    root.mainloop()
