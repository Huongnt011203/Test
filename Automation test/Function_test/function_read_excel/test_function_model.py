import time

from selenium import webdriver
from selenium.webdriver.common.by import By

import Test_thuong.test_function_dangnhap

import utilities.utilities_xpath
def nhom_model_thanhcong(br):
        btn_ChonThem = br.find_element(By.XPATH, utilities.utilities_xpath.xpath_btn_chon_them())
        btn_ChonThem.click()

        cbb_nhomSp = br.find_element(By.XPATH, utilities.utilities_xpath.xpath_cbb_nhomsp())
        cbb_nhomSp.click()

        cbb1 = br.find_element(By.XPATH, utilities.utilities_xpath.xpath_cbb_nhomsp_4())
        cbb1.click()
        time.sleep(1)

        cbb_hangsx = br.find_element(By.XPATH,
                                     utilities.utilities_xpath.xpath_cbb_hangnsx())

        cbb_hangsx.click()
        time.sleep(1)
        nsx = br.find_element(By.XPATH, utilities.utilities_xpath.xpath_cbb_hangnsx_3())
        nsx.click()
        time.sleep(1)

        cbb_model = br.find_element(By.XPATH,
                                    utilities.utilities_xpath.xpath_cbb_model())
        cbb_model.click()
        time.sleep(1)
        c = br.find_element(By.XPATH, utilities.utilities_xpath.xpath_cbb_model_1())
        c.click()
        time.sleep(1)

        txt_tenSp = br.find_element(By.XPATH,
                                    utilities.utilities_xpath.xpath_txt_tensp())
        txt_tenSp.send_keys("HT0101")
        time.sleep(1)
        txt_maSp = br.find_element(By.XPATH,
                                   utilities.utilities_xpath.xpath_txt_masp())
        txt_maSp.send_keys("Nhãn")
        time.sleep(1)

        txt_bh = br.find_element(By.XPATH,
                                 utilities.utilities_xpath.xpath_txt_bh())
        txt_bh.send_keys("10")
        time.sleep(1)

        txt_sl = br.find_element(By.XPATH,
                                 utilities.utilities_xpath.xpath_txt_sl())
        txt_sl.send_keys("100")
        time.sleep(1)

        # Nhap thu tu
        txt_stt = br.find_element(By.XPATH,
                                  utilities.utilities_xpath.xpath_txt_stt())
        txt_stt.send_keys("2")
        time.sleep(1)

        # Chọn còn hàng
        rd_conHang = br.find_element(By.XPATH,
                                     utilities.utilities_xpath.xpath_rd_con_hang())
        rd_conHang.click()
        time.sleep(1)

        # Click calendar
        click_calendar = br.find_element(By.XPATH,
                                         utilities.utilities_xpath.xpath_lich_calendar())
        click_calendar.click()
        time.sleep(1)

        # Click checkbox
        click_checkBox = br.find_element(By.XPATH,
                                         utilities.utilities_xpath.xpath_checkbox())
        click_checkBox.click()
        time.sleep(1)

        btn_capNhat = br.find_element(By.XPATH, utilities.utilities_xpath.xpath_btn_capNhat())
        btn_capNhat.click()
        time.sleep(1)

        if br.current_url == "http://1.hoctestertop.com/admin-product/list.aspx":
            print("Case 5 pass")
            return True
        else:
            print("Case 5 fail")
            return False
def nhom_model_derong(br):
        btn_ChonThem = br.find_element(By.XPATH, utilities.utilities_xpath.xpath_btn_chon_them())
        btn_ChonThem.click()

        cbb_nhomSp = br.find_element(By.XPATH, utilities.utilities_xpath.xpath_cbb_nhomsp())
        cbb_nhomSp.click()

        cbb1 = br.find_element(By.XPATH, utilities.utilities_xpath.xpath_cbb_nhomsp_4())
        cbb1.click()
        time.sleep(1)

        cbb_hangsx = br.find_element(By.XPATH,
                                     utilities.utilities_xpath.xpath_cbb_hangnsx())

        cbb_hangsx.click()
        time.sleep(1)
        nsx = br.find_element(By.XPATH, utilities.utilities_xpath.xpath_cbb_hangnsx_3())
        nsx.click()
        time.sleep(1)

        txt_tenSp = br.find_element(By.XPATH,
                                    utilities.utilities_xpath.xpath_txt_tensp())
        txt_tenSp.send_keys("HT0101")
        time.sleep(1)
        txt_maSp = br.find_element(By.XPATH,
                                   utilities.utilities_xpath.xpath_txt_masp())
        txt_maSp.send_keys("Nhãn")
        time.sleep(1)

        txt_bh = br.find_element(By.XPATH, utilities.utilities_xpath.xpath_txt_bh())
        txt_bh.send_keys("10")
        time.sleep(1)

        txt_sl = br.find_element(By.XPATH, utilities.utilities_xpath.xpath_txt_sl())
        txt_sl.send_keys("100")
        time.sleep(1)

    # Nhap thu tu
        txt_stt = br.find_element(By.XPATH,
                                  utilities.utilities_xpath.xpath_txt_stt())
        txt_stt.send_keys("2")
        time.sleep(1)

    # Chọn còn hàng
        rd_conHang = br.find_element(By.XPATH,
                                     utilities.utilities_xpath.xpath_rd_con_hang())
        rd_conHang.click()
        time.sleep(1)

    # Click calendar
        click_calendar = br.find_element(By.XPATH,
                                         utilities.utilities_xpath.xpath_lich_calendar())
        click_calendar.click()
        time.sleep(1)

    # Click checkbox
        click_checkBox = br.find_element(By.XPATH,
                                         utilities.utilities_xpath.xpath_checkbox())
        click_checkBox.click()
        time.sleep(1)

        btn_capNhat = br.find_element(By.XPATH, utilities.utilities_xpath.xpath_btn_capNhat())
        btn_capNhat.click()
        time.sleep(1)

        if br.current_url == "http://1.hoctestertop.com/admin-product/list.aspx":
            print("Case 6 pass")
            return True
        else:
            print("Case 6 fail")
            return False
        time.sleep(1)
def them(br):
    btn_ThemSP = br.find_element(By.XPATH, "//*[@id='sidebar']/div/div[1]/ul/li[4]/a")
    btn_ThemSP.click()
    btn_ChonThem = br.find_element(By.XPATH, "//*[@id='sidebar']/div/div[1]/ul/li[4]/ul/li[1]/a")
    btn_ChonThem.click()
    time.sleep(2)
    return

if __name__ == '__main__':
    br = webdriver.Chrome()
    br.get("http://1.hoctestertop.com/control.panel/")
    Test_thuong.DangNhap.thanh_cong(br)
    them(br)
    nhom_model_thanhcong(br)
    nhom_model_derong(br)
    time.sleep(2)
