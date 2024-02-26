## Hệ thống quản lý thư viện sử dụng cây tìm kiếm nhị phân
Mô tả: Hệ thống này sử dụng cây tìm kiếm nhị phân để lưu trữ thông tin sách và hỗ trợ các chức năng sau:
- Thêm sách mới
- Tìm kiếm sách theo mã ISBN hoặc tiêu đề
- Mượn sách
- Trả sách
- Liệt kê tất cả sách
- Liệt kê sách đang có sẵn
### Cấu trúc dữ liệu:
  Cây tìm kiếm nhị phân: Lưu trữ thông tin sách theo mã ISBN, giúp tìm kiếm hiệu quả.
  Sách: Bao gồm các thuộc tính như mã ISBN, tiêu đề, tác giả, nhà xuất bản, thể loại và trạng thái (sẵn có/đã mượn).
Chức năng:
1. Thêm sách:
  Nhập thông tin ISBN, tiêu đề, tác giả, nhà xuất bản, thể loại.
  Tạo một đối tượng Sách mới với thông tin được nhập.
  Sử dụng insert để thêm Sách vào cây tìm kiếm nhị phân dựa trên mã ISBN.
2. Tìm kiếm sách:
  Nhập mã ISBN hoặc tiêu đề sách.
  Sử dụng search_by_key hoặc search_by_title để tìm kiếm sách trong cây.
  Hiển thị thông tin chi tiết của sách được tìm thấy.
3. Mượn sách:
  Nhập mã ISBN của sách muốn mượn.
  Sử dụng search_by_key để tìm kiếm sách.
  Nếu sách có trạng thái "sẵn có", hệ thống thay đổi trạng thái thành "đã mượn" và xác nhận việc mượn sách.
  Nếu sách không có sẵn, hệ thống thông báo lỗi.
4. Trả sách:
  Nhập mã ISBN của sách muốn trả.
  Sử dụng search_by_key để tìm kiếm sách.
  Nếu sách có trạng thái "đã mượn", hệ thống thay đổi trạng thái thành "sẵn có" và xác nhận việc trả sách.
  Nếu sách không có trạng thái "đã mượn", hệ thống thông báo lỗi.
5. Liệt kê sách:
  Sử dụng Inorder_Traversal để duyệt qua cây và hiển thị thông tin của tất cả sách.
  Có thể thêm lựa chọn lọc sách theo trạng thái "sẵn có" để chỉ hiển thị sách có thể được mượn.
