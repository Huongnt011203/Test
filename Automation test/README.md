# Giới thiệu về file automation test
## Trong file sẽ chia làm hai phần:
### - Các function_test.
### - Data_test. 
# 1. Các function test:
#### - Function đọc dữ liệu từ file excel
#### - Function dùng dữ liệu fix cứng
## a. Function đọc dữ liệu từ file excel:
#### - Sau khi khởi chạy thì sẽ tự động đọc dữ liệu từ file excel có sẵn trong file data_test.
#### - Sau khi chạy hết thì sẽ có trả về kết quả từng testcase là pass hay là fail.
#### - Các function đều sẽ phải chạy function_dangnhap trước.
## b. Function dùng dữ liệu fix cứng:
#### - Sau khi khởi chạy thì sẽ dùng dữ liệu fix cứng sẵn cho từng hàm.
#### - Sau khi chạy hết thì sẽ có trả về kết quả từng testcase là pass hay là fail.
#### - Các function đều sẽ phải chạy function_dangnhap trước.
## ** Ngoài ra còn một file dùng để lưu xpath cho từng trường.**
# 2. Data test: 
#### - Dữ liệu trong file data test được thiết kế dựa trên input của file testcase và lưu trữ dưới file excel
