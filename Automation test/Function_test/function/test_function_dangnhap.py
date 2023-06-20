import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import utilities.utilities_dang_nhap
def username_khong_password(browser):
    """
username đúng, rỗng pass
    """
    try:
        text_tenDangNhap = browser.find_element(By.ID, utilities.utilities_dang_nhap.txt_dang_nhap())
        if not text_tenDangNhap:
            print("Case 1 fail")
            return False
        text_tenDangNhap.clear()
        text_tenDangNhap.send_keys("admin")

        text_matKhau = browser.find_element(By.ID, utilities.utilities_dang_nhap.txt_mat_khau())
        if not text_matKhau:
            print("Case 1 fail")
        text_matKhau.clear()

        time.sleep(2)

        btn_dangNhap = browser.find_element(By.ID, utilities.utilities_dang_nhap.btn_dang_nhap())
        btn_dangNhap.click()
        if 'Nhập mật khẩu' in browser.page_source:
            print("Case 1 pass")
            return True
        else:
            print("Case 1 fail")
            return False

    except Exception as e:
        print(e)

def rong_useername_dung_pass(browser):
    """
    trống usename, đúng pass
    """
    try:
        text_tenDangNhap = browser.find_element(By.ID, utilities.utilities_dang_nhap.txt_dang_nhap())
        if not text_tenDangNhap:
            print("Case 2 fail")
            return False
        text_tenDangNhap.clear()

        text_matKhau = browser.find_element(By.ID, utilities.utilities_dang_nhap.txt_mat_khau())
        if not text_matKhau:
            print("Case 2 fail")
            return False
        text_matKhau.clear()
        text_matKhau.send_keys("chithuxinh2021")

        time.sleep(2)  # sleep 1s

        btn_dangNhap = browser.find_element(By.ID, utilities.utilities_dang_nhap.btn_dang_nhap())
        btn_dangNhap.click()
        if 'Nhập tên đăng nhập' in browser.page_source:
            print("Case 2 pass")
            return True
        else:
            print("Case 2 fail")
            return False

    except Exception as e:
        print(e)

def rong_username_va_pass(browser):
    """
    rỗng hai trường
    """
    try:
        text_tenDangNhap = browser.find_element(By.ID, utilities.utilities_dang_nhap.txt_dang_nhap())

        text_tenDangNhap.clear()


        text_matKhau = browser.find_element(By.ID, utilities.utilities_dang_nhap.txt_mat_khau())
        text_matKhau.clear()

        time.sleep(5)  # sleep 1s
        btn_dangNhap = browser.find_element(By.ID, utilities.utilities_dang_nhap.btn_dang_nhap())
        btn_dangNhap.click()
        time.sleep(3)
        if 'Nhập tên đăng nhập' in browser.page_source:
            print("Case 3 pass")
            return True
        else:
            print("Case 3 fail")
            return False
    except:
        pass

def username_dung_sai_pass(browser):
    """
    đúng username sai pass
    """
    try:
        text_tenDangNhap = browser.find_element(By.ID, utilities.utilities_dang_nhap.txt_dang_nhap())
        if not text_tenDangNhap:
            print("Case 4 fail")
            return False
        text_tenDangNhap.clear()
        text_tenDangNhap.send_keys("admin")

        time.sleep(5)
        text_matKhau = browser.find_element(By.ID, utilities.utilities_dang_nhap.txt_mat_khau())
        if not text_matKhau:
            print("Case 4 fail")
            return False
        text_matKhau.clear()
        text_matKhau.send_keys("abcd1234")

        time.sleep(1)

        btn_dangNhap = browser.find_element(By.ID, utilities.utilities_dang_nhap.btn_dang_nhap())
        btn_dangNhap.click()
        time.sleep(2)
        if 'Tên đăng nhập hoặc mật khẩu không tồn tại' in browser.page_source:
            print("Case 4 pass")
            return True
        else:
            print("Case 4 fail")
            return False

    except Exception as e:
        print(e)



def username_sai_pass_dung(browser):
    """
    username sai, pass đúng
    """
    try:
        text_tenDangNhap = browser.find_element(By.ID, utilities.utilities_dang_nhap.txt_dang_nhap())

        if not text_tenDangNhap:
            print("Case 5 fail")
            return False
        text_tenDangNhap.clear()
        text_tenDangNhap.send_keys("ad")

        text_matKhau = browser.find_element(By.ID, utilities.utilities_dang_nhap.txt_mat_khau())
        if not text_matKhau:
            print("Case 5 fail")
            return False
        text_matKhau.clear()
        text_matKhau.send_keys("chithuxinh2021")

        time.sleep(1)

        btn_dangNhap = browser.find_element(By.ID, utilities.utilities_dang_nhap.btn_dang_nhap())
        btn_dangNhap.click()
        time.sleep(2)
        if 'Tên đăng nhập hoặc mật khẩu không tồn tại' in browser.page_source:
            print("Case 5 pass")
            return True
        else:
            print("Case 5 fail")
            return False

    except Exception as e:
        print(e)

def username_qua_maxlength_pass_dung(browser):
    """
    nhập usrname quas maxlength, pass đúng
    """
    try:
        text_tenDangNhap = browser.find_element(By.ID, utilities.utilities_dang_nhap.txt_dang_nhap())
        if not text_tenDangNhap:
            print("Case 6 fail")
            return False
        text_tenDangNhap.clear()
        long_text = 500 * "admin"
        text_tenDangNhap.send_keys(long_text)

        text_matKhau = browser.find_element(By.ID, utilities.utilities_dang_nhap.txt_mat_khau())
        if not text_matKhau:
            print("Case 6 fail")
            return False
        text_matKhau.clear()
        text_matKhau.send_keys("chithuxinh2021")

        time.sleep(2)

        btn_dangNhap = browser.find_element(By.ID, utilities.utilities_dang_nhap.btn_dang_nhap())
        btn_dangNhap.click()
        time.sleep(2)
        if 'Tên đăng nhập quá maxlength' in browser.page_source:
            print("Case 6 pass")
            return True
        else:
            print("Case 6 fail")
            return False

    except Exception as e:
        print(e)

def username_sai_pass_sai(browser):
    """
    sai usenaem, sai passs
    """
    try:
        text_tenDangNhap = browser.find_element(By.ID, utilities.utilities_dang_nhap.txt_dang_nhap())
        if not text_tenDangNhap:
            print("Case 7 fail")
            return False
        text_tenDangNhap.clear()
        text_tenDangNhap.send_keys("m")

        text_matKhau = browser.find_element(By.ID, utilities.utilities_dang_nhap.txt_mat_khau())
        if not text_matKhau:
            print("Case 7 fail")
            return False
        text_matKhau.clear()
        text_matKhau.send_keys("abcd1234")

        time.sleep(1)  # sleep 1s

        btn_dangNhap = browser.find_element(By.ID, utilities.utilities_dang_nhap.btn_dang_nhap())
        btn_dangNhap.click()
        time.sleep(2)
        if 'Tên đăng nhập hoặc mật khẩu không tồn tại' in browser.page_source:
            print("Case 7 pass")
            return True
        else:
            print("Case 7 fail")
            return False

    except Exception as e:
        print(e)

def thanh_cong(browser):
    """
    thành công
    """
    try:
        text_tenDangNhap = browser.find_element(By.ID, utilities.utilities_dang_nhap.txt_dang_nhap())

        if not text_tenDangNhap:
            print("Case 8 fail")
            return False

        text_tenDangNhap.clear()
        text_tenDangNhap.send_keys("admin")

        text_matKhau = browser.find_element(By.ID, utilities.utilities_dang_nhap.txt_mat_khau())
        if not text_matKhau:
            print("Case 8 fail")
            return False

        text_matKhau.clear()
        text_matKhau.send_keys("chithuxinh2021")

        time.sleep(1)

        btn_dangNhap = browser.find_element(By.ID, utilities.utilities_dang_nhap.btn_dang_nhap())
        btn_dangNhap.click()

        if browser.current_url == "http://1.hoctestertop.com/control.panel/":
            print("Case 8 pass")
            return True
        else:
            print("Case 8 fail")
            return False

        time.sleep(5)



    except Exception as e:
        print(e)

if __name__ == '__main__':
    browser = webdriver.Chrome()
    browser.get("http://1.hoctestertop.com/admincp/")
    username_khong_password(browser)
    rong_useername_dung_pass(browser)
    rong_username_va_pass(browser)
    username_dung_sai_pass(browser)
    username_sai_pass_dung(browser)
    username_qua_maxlength_pass_dung(browser)
    username_sai_pass_sai(browser)
    thanh_cong(browser)
    time.sleep(3)




