# Giới thiệu về file automation test
## Trong file sẽ chia làm hai phần:
### - Là các function đọc dữ liệu từ file excel.
### - Là các function sẽ dùng dữ liệu fix cứng. 
## 1. Function đọc dữ liệu từ file excel:
#### - Sau khi khởi chạy thì sẽ tự động đọc dữ liệu từ file excel có sẵn trong file data_test.
#### - Sau khi chạy hết thì sẽ có trả về kết quả từng testcase là pass hay là fail.
#### - Các function đều sẽ phải chạy function_dangnhap trước.
## 2. Function dùng dữ liệu fix cứng:
#### - Sau khi khởi chạy thì sẽ dùng dữ liệu fix cứng sẵn cho từng hàm.
#### - Sau khi chạy hết thì sẽ có trả về kết quả từng testcase là pass hay là fail.
#### - Các function đều sẽ phải chạy function_dangnhap trước.
## Ngoài ra còn một file dùng để lưu xpath cho từng trường.
