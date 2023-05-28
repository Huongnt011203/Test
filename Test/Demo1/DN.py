import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
def test_login_with_excel_data(path_data_test_login):
    try:
        # Đường dẫn đến file Excel
        data_frame = pd.read_excel(path_data_test_login)

        for index, row in data_frame.iterrows():
            username = row['Username']
            password = row['Password']
            mes = row['Message']

            print(username)
            print(password)


            text_tenDangNhap = browser.find_element(By.ID, "txtUserName")
            text_tenDangNhap.clear()
            text_tenDangNhap.send_keys(username)
            if  not text_tenDangNhap:
                print(f"Case {index+1} fail")
                continue


            text_matKhau = browser.find_element(By.ID, "txtPassWord")
            text_matKhau.clear()
            text_matKhau.send_keys(password)
            if not text_matKhau:
                print(f"Case {index+1} fail")
                continue
            # text_matKhau.send_keys(password)
            time.sleep(2)
            btn_dangNhap = browser.find_element(By.ID, "tbnLogin")
            btn_dangNhap.click()

            if browser.current_url == "http://1.hoctestertop.com/control.panel/":
                print(f"Case {index+1} pass")
            else:
                print(f"Case {index+1} fail")

            if mes in browser.page_source:
                print(f"Case {index+1} pass")
            else:
                print(f"Case {index+1} fail")

    except Exception as e:

       print(e)
if __name__ == '__main__':
    browser = webdriver.Chrome()
    browser.get("http://1.hoctestertop.com/admincp/")
    path_data_test_login = r'E:\test\testok.xlsx'
    test_login_with_excel_data(path_data_test_login)
