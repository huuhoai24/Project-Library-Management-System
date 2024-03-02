### The problem of Library Management System 
Built using Python and its tkinter graphical user interface (GUI) toolkit. The system manages books in a library, allowing users to perform various operations such as inserting new books, searching for books, borrowing and returning books, and deleting or updating book records. The data structure used to manage books is a binary search tree (BST), which organizes books based on their IDs for efficient retrieval and management.

### Classes and Data Structures:

1. **Node Class**: Represents a node in the binary search tree. Each node contains the data for one book (including its ID, title, author, publisher, genre, and status), as well as references to the left and right child nodes in the tree.

2. **Book Class**: Manages the binary search tree of books. It includes methods for inserting, searching, borrowing, returning, and deleting books, as well as for loading and saving the book collection to a file (using JSON format). It also includes methods to traverse the tree and perform actions such as displaying all books or filtering them based on their availability.


### Functionalities:

- **Inserting Books**: Users can add new books to the library by entering details and clicking the "Insert Book" button. The system checks for duplicate IDs to prevent adding the same book twice.

- **Searching for Books**: Users can search for books by ID or title using the respective search functions.

- **Borrowing and Returning Books**: Users can change the status of a book to "Borrowed" when borrowing and back to "Available" when returning.

- **Updating and Deleting Books**: Books can be updated with new information or removed from the library entirely.

- **Displaying Books**: The system can display lists of all books, only available books, or only borrowed books, based on the user's selection.

- **Data Persistence**: The system saves the library's state to a JSON file, ensuring that data is not lost between sessions.

### GUI Components:

The application uses tkinter to create a user-friendly interface that includes:

- Text entry fields for inputting book information (ID, title, author, publisher, genre, and status).
- Buttons for performing actions like inserting a new book, searching, borrowing, returning, and showing different lists of books (all, available, borrowed).
- A treeview widget to display the list of books, allowing the user to see the details of all books in the library or a filtered list.
- A combobox for selecting the status of a book when inserting or updating it.
