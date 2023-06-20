import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import utilities.utilities_dang_nhap
def test_login_with_excel_data(path_data_test_login):
    try:
        # Đường dẫn đến file Excel
        data_frame = pd.read_excel(path_data_test_login)

        for index, row in data_frame.iterrows():
            username = row['Username']
            password = row['Password']
            mes = row['Message']

            text_tenDangNhap = browser.find_element(By.ID, utilities.utilities_dang_nhap.txt_dang_nhap())
            text_tenDangNhap.clear()
            text_tenDangNhap.send_keys(username)
            if pd.isna(username):
                print(f"Case {index+1} fail")
                continue
            time.sleep(4)
            text_matKhau = browser.find_element(By.ID, utilities.utilities_dang_nhap.txt_mat_khau())
            text_matKhau.clear()
            text_matKhau.send_keys(password)
            if pd.isna(password):
                print(f"Case {index+1} fail")
                continue
            # text_matKhau.send_keys(password)
            time.sleep(2)
            btn_dangNhap = browser.find_element(By.ID, utilities.utilities_dang_nhap.btn_dang_nhap())
            btn_dangNhap.click()
            time.sleep(2)
            # if browser.current_url == "http://1.hoctestertop.com/control.panel/":
            #     print(f"Case {index+1} pass")
            # else:
            #     print(f"Case {index+1} fail")

            if pd.isna(mes):
                print(f"Case {index+1} pass")
            else:
                if mes in browser.page_source:
                    print(f"Case {index+1} pass")
                else:
                    print(f"Case {index+1} fail")

    except Exception as e:

       print(e)
if __name__ == '__main__':
    browser = webdriver.Chrome()
    browser.get("http://1.hoctestertop.com/admincp/")
    path_data_test_login = r'E:\Test\Automation test\Du_lieu_test\du_lieu_test_man_login.xlx'
    test_login_with_excel_data(path_data_test_login)
