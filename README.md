## Hệ thống quản lý thư viện sử dụng cây tìm kiếm nhị phân 
### Node:
- IBSN (book id)
- Title
- Author
- Pusblisher
- Genre 
- Status (available / borrowed)
### Functions:
- Insert Book
- Search by key and title
- Borrow / Return book
- Show book:
    - Show all books
    - Show available book
- Delete book

  



### Cấu trúc dữ liệu:
1. **Binary Search Tree (BST):** Lớp `Node` và các phương thức trong lớp `Book` như `insert`, `_insert`, `search_by_isbn`, `_search_by_isbn`, `delete_book`, và `_delete_book` đều chỉ ra việc sử dụng cây tìm kiếm nhị phân để lưu trữ và quản lý các sách. Trong BST này, mỗi nút chứa thông tin về một cuốn sách bao gồm ISBN, tiêu đề, tác giả, nhà xuất bản, thể loại, và trạng thái. ISBN được sử dụng làm khóa để sắp xếp các nút trong cây.

2. **List:** `default_books` là một danh sách các bộ gồm thông tin sách được sử dụng để khởi tạo cây với các sách mặc định.

3. **Variables and Objects:** Các biến như `isbn`, `title`, `author`, `publisher`, `genre`, `status` được sử dụng để lưu trữ thông tin tạm thời và truyền dữ liệu giữa các phương thức và lớp.

### Thuật toán:
1. **Insertion in BST:** Phương thức `insert` và `_insert` mô tả cách thêm một nút mới vào cây tìm kiếm nhị phân dựa trên ISBN.

2. **Search in BST:** Phương thức `search_by_isbn` và `_search_by_isbn` cùng với `search_by_title` và `_search_by_title` biểu diễn thuật toán tìm kiếm trong BST, tìm kiếm dựa trên ISBN hoặc tiêu đề.

3. **In-order Traversal:** Phương thức `_inorder_traversal` được sử dụng để duyệt cây theo thứ tự inorder. Điều này giúp liệt kê các sách trong thứ tự ISBN tăng dần và cũng được sử dụng để hiển thị sách theo trạng thái cụ thể (có sẵn hoặc đã mượn).

4. **Delete in BST:** Phương thức `delete_book` và `_delete_book` mô tả thuật toán xóa một nút khỏi BST, điều chỉnh cây để giữ cấu trúc sau khi xóa.

5. **Update Information:** Phương thức `update_book` cho phép cập nhật thông tin của một cuốn sách nếu nó tồn tại trong cây.

### Ứng dụng GUI:
Ứng dụng cũng sử dụng thư viện Tkinter để tạo giao diện người dùng đồ họa (GUI), cho phép tương tác với hệ thống quản lý thư viện bằng cách sử dụng các biểu mẫu và nút nhấn thay vì thông qua dòng lệnh. Các cấu trúc dữ liệu như danh sách và chuỗi được sử dụng để quản lý các yếu tố giao diện như entries, labels, và buttons.
