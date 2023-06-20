import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import Demo1.utilities_xpath
import Test_thuong.test_function_dangnhap


def nhom_sp_thanhcong(br):
    cbb_nhomSp = br.find_element(By.XPATH,Demo1.utilities_xpath.xpath_cbb_nhomsp())
    if not cbb_nhomSp:
        print("Case 1 fail - comb")
        return False
    cbb_nhomSp.click()
    time.sleep(1)
    a = br.find_element(By.XPATH, Demo1.utilities_xpath.xpath_cbb_nhomsp_4())
    a.click()
    time.sleep(1)
    cbb_hangsx = br.find_element(By.XPATH,
                                     Demo1.utilities_xpath.xpath_cbb_hangnsx())
    cbb_hangsx.click()
    time.sleep(1)

    nsx = br.find_element(By.XPATH, Demo1.utilities_xpath.xpath_cbb_hangnsx_3())
    nsx.click()
    time.sleep(1)

    cbb_model = br.find_element(By.XPATH,
                                    Demo1.utilities_xpath.xpath_cbb_model())
    cbb_model.click()
    time.sleep(1)
    c = br.find_element(By.XPATH, Demo1.utilities_xpath.xpath_cbb_model_1())
    c.click()
    time.sleep(1)
    txt_tenSp = br.find_element(By.XPATH,
                                 Demo1.utilities_xpath.xpath_txt_tensp())
    txt_tenSp.send_keys("HT0101")
    time.sleep(1)
    txt_maSp = br.find_element(By.XPATH,
                                Demo1.utilities_xpath.xpath_txt_masp())
    txt_maSp.send_keys("Nhãn")
    time.sleep(1)

    txt_bh = br.find_element(By.XPATH, Demo1.utilities_xpath.xpath_txt_bh())
    txt_bh.send_keys("10")
    time.sleep(1)

    txt_sl = br.find_element(By.XPATH, Demo1.utilities_xpath.xpath_txt_sl())
    txt_sl.send_keys("100")
    time.sleep(1)

    # Nhap thu tu
    txt_stt = br.find_element(By.XPATH,
                               Demo1.utilities_xpath.xpath_txt_stt())
    txt_stt.send_keys("2")
    time.sleep(1)

    # Chọn còn hàng
    rd_conHang = br.find_element(By.XPATH,
                                  Demo1.utilities_xpath.xpath_rd_con_hang())
    rd_conHang.click()
    time.sleep(1)

    # Click calendar
    click_calendar = br.find_element(By.XPATH,
                                      Demo1.utilities_xpath.xpath_lich_calendar())
    click_calendar.click()
    time.sleep(1)

    # Click checkbox
    click_checkBox = br.find_element(By.XPATH,
                                      Demo1.utilities_xpath.xpath_checkbox())
    click_checkBox.click()
    time.sleep(1)


    btn_capNhat = br.find_element(By.XPATH, Demo1.utilities_xpath.xpath_btn_capNhat())
    btn_capNhat.click()
    time.sleep(1)



    if br.current_url == "http://1.hoctestertop.com/admin-product/list.aspx":
        print("Case 1 pass")
        return True
    else:
        print("Case 1 fail")
        return False

    time.sleep(1)


def nhom_sp_derong(br):
    btn_ChonThem = br.find_element(By.XPATH, Demo1.utilities_xpath.xpath_btn_chon_them())
    btn_ChonThem.click()
    cbb_hangsx = br.find_element(By.XPATH,
                                 Demo1.utilities_xpath.xpath_cbb_hangnsx())
    cbb_hangsx.click()
    time.sleep(1)

    nsx = br.find_element(By.XPATH, Demo1.utilities_xpath.xpath_cbb_hangnsx_3())
    nsx.click()
    time.sleep(1)

    cbb_model = br.find_element(By.XPATH,
                                Demo1.utilities_xpath.xpath_cbb_model())
    cbb_model.click()
    time.sleep(1)
    c = br.find_element(By.XPATH, Demo1.utilities_xpath.xpath_cbb_model_1())
    c.click()
    time.sleep(1)
    txt_tenSp = br.find_element(By.XPATH,
                                Demo1.utilities_xpath.xpath_txt_tensp())
    txt_tenSp.send_keys("HT0101")
    time.sleep(1)
    txt_maSp = br.find_element(By.XPATH,
                               Demo1.utilities_xpath.xpath_txt_masp())
    txt_maSp.send_keys("Nhãn")
    time.sleep(1)

    txt_bh = br.find_element(By.XPATH, Demo1.utilities_xpath.xpath_txt_bh())
    txt_bh.send_keys("10")
    time.sleep(1)

    txt_sl = br.find_element(By.XPATH, Demo1.utilities_xpath.xpath_txt_sl())
    txt_sl.send_keys("100")
    time.sleep(1)

    # Nhap thu tu
    txt_stt = br.find_element(By.XPATH,
                              Demo1.utilities_xpath.xpath_txt_stt())
    txt_stt.send_keys("2")
    time.sleep(1)

    # Chọn còn hàng
    rd_conHang = br.find_element(By.XPATH,
                                 Demo1.utilities_xpath.xpath_rd_con_hang())
    rd_conHang.click()
    time.sleep(1)

    # Click calendar
    click_calendar = br.find_element(By.XPATH,
                                     Demo1.utilities_xpath.xpath_rd_con_hang())
    click_calendar.click()
    time.sleep(1)

    # Click checkbox
    click_checkBox = br.find_element(By.XPATH,
                                     Demo1.utilities_xpath.xpath_checkbox())
    click_checkBox.click()
    time.sleep(1)

    btn_capNhat = br.find_element(By.XPATH, Demo1.utilities_xpath.xpath_btn_capNhat())
    btn_capNhat.click()
    time.sleep(1)

    if 'Chưa chọn nhóm sản phẩm' in br.page_source:
        print("Case 2 pass")
        return True
    else:
        print("Case 2 fail")
        return False


def nhom_nsx_thanhcong(br):
        btn_ChonThem = br.find_element(By.XPATH, Demo1.utilities_xpath.xpath_btn_chon_them())
        btn_ChonThem.click()

        cbb_nhomSp = br.find_element(By.XPATH, Demo1.utilities_xpath.xpath_cbb_nhomsp())
        cbb_nhomSp.click()

        cbb1 = br.find_element(By.XPATH, Demo1.utilities_xpath.xpath_cbb_nhomsp_4())
        cbb1.click()
        time.sleep(1)

        cbb_hangsx = br.find_element(By.XPATH,
                                     Demo1.utilities_xpath.xpath_cbb_hangnsx())
        if not cbb_hangsx:
            print("Case 3 fail - combo nsx rong")
            return False

        cbb_hangsx.click()
        time.sleep(1)

        nsx = br.find_element(By.XPATH, Demo1.utilities_xpath.xpath_cbb_hangnsx_3())
        nsx.click()
        time.sleep(1)

        cbb_model = br.find_element(By.XPATH,
                                    Demo1.utilities_xpath.xpath_cbb_model())
        cbb_model.click()
        time.sleep(1)
        c = br.find_element(By.XPATH, Demo1.utilities_xpath.xpath_cbb_model_1())
        c.click()
        time.sleep(1)
        txt_tenSp = br.find_element(By.XPATH,
                                    Demo1.utilities_xpath.xpath_txt_tensp())
        txt_tenSp.send_keys("Nhãn")
        time.sleep(1)
        txt_maSp = br.find_element(By.XPATH,
                                   Demo1.utilities_xpath.xpath_txt_masp())
        txt_maSp.send_keys("HT000002")
        time.sleep(1)

        txt_bh = br.find_element(By.XPATH,
                                 Demo1.utilities_xpath.xpath_txt_bh())
        txt_bh.send_keys("10")
        time.sleep(1)

        txt_sl = br.find_element(By.XPATH,
                                 Demo1.utilities_xpath.xpath_txt_sl())
        txt_sl.send_keys("100")
        time.sleep(1)

        # Nhap thu tu
        txt_stt = br.find_element(By.XPATH,
                                  Demo1.utilities_xpath.xpath_txt_stt())
        txt_stt.send_keys("2")
        time.sleep(1)

        # Chọn còn hàng
        rd_conHang = br.find_element(By.XPATH,
                                     Demo1.utilities_xpath.xpath_rd_con_hang())
        rd_conHang.click()
        time.sleep(1)

        # Click calendar
        click_calendar = br.find_element(By.XPATH,
                                         Demo1.utilities_xpath.xpath_lich_calendar())
        click_calendar.click()
        time.sleep(1)

        # Click checkbox
        click_checkBox = br.find_element(By.XPATH,
                                         Demo1.utilities_xpath.xpath_checkbox())
        click_checkBox.click()
        time.sleep(1)

        btn_capNhat = br.find_element(By.XPATH, Demo1.utilities_xpath.xpath_btn_capNhat())
        btn_capNhat.click()
        time.sleep(1)

        if br.current_url == "http://1.hoctestertop.com/admin-product/list.aspx":
            print("Case 1 pass")
            return True
        else:
            print("Case 1 fail")
            return False
def nhom_nsx_derong(br):
        btn_ChonThem = br.find_element(By.XPATH, Demo1.utilities_xpath.xpath_btn_chon_them())
        btn_ChonThem.click()

        cbb_nhomSp = br.find_element(By.XPATH, Demo1.utilities_xpath.xpath_cbb_nhomsp())
        cbb_nhomSp.click()

        cbb1 = br.find_element(By.XPATH, Demo1.utilities_xpath.xpath_cbb_nhomsp_4())
        cbb1.click()
        time.sleep(1)


        cbb_model = br.find_element(By.XPATH,
                                Demo1.utilities_xpath.xpath_cbb_model())
        cbb_model.click()
        time.sleep(1)
        c = br.find_element(By.XPATH, Demo1.utilities_xpath.xpath_cbb_nhomsp_4())
        c.click()
        time.sleep(1)
        txt_tenSp = br.find_element(By.XPATH,
                                Demo1.utilities_xpath.xpath_txt_tensp())
        txt_tenSp.send_keys("HT0101")
        time.sleep(1)
        txt_maSp = br.find_element(By.XPATH,
                               Demo1.utilities_xpath.xpath_txt_masp())
        txt_maSp.send_keys("Nhãn")
        time.sleep(1)

        txt_bh = br.find_element(By.XPATH, Demo1.utilities_xpath.xpath_txt_bh())
        txt_bh.send_keys("10")
        time.sleep(1)

        txt_sl = br.find_element(By.XPATH, Demo1.utilities_xpath.xpath_txt_sl())
        txt_sl.send_keys("100")
        time.sleep(1)

    # Nhap thu tu
        txt_stt = br.find_element(By.XPATH,
                              Demo1.utilities_xpath.xpath_txt_stt())
        txt_stt.send_keys("2")
        time.sleep(1)

    # Chọn còn hàng
        rd_conHang = br.find_element(By.XPATH,
                                 Demo1.utilities_xpath.xpath_rd_con_hang())
        rd_conHang.click()
        time.sleep(1)

    # Click calendar
        click_calendar = br.find_element(By.XPATH,
                                     Demo1.utilities_xpath.xpath_lich_calendar())
        click_calendar.click()
        time.sleep(1)

    # Click checkbox
        click_checkBox = br.find_element(By.XPATH,
                                     Demo1.utilities_xpath.xpath_checkbox())
        click_checkBox.click()
        time.sleep(1)

        btn_capNhat = br.find_element(By.XPATH, Demo1.utilities_xpath.xpath_btn_capNhat())
        btn_capNhat.click()
        time.sleep(1)

        if br.current_url == "http://1.hoctestertop.com/admin-product/list.aspx":
            print("Case 4 pass")
            return True
        else:
            print("Case 4 fail")
            return False
        time.sleep(1)
def them(br):
    btn_ThemSP = br.find_element(By.XPATH, "//*[@id='sidebar']/div/div[1]/ul/li[4]/a")
    btn_ThemSP.click()
    btn_ChonThem = br.find_element(By.XPATH, Demo1.utilities_xpath.xpath_btn_chon_them())
    btn_ChonThem.click()
    time.sleep(2)
    return
if __name__ == '__main__':
    br = webdriver.Chrome()
    br.get("http://1.hoctestertop.com/control.panel/")
    Test_thuong.DangNhap.thanh_cong(br)
    them(br)
    nhom_sp_thanhcong(br)
    nhom_sp_derong(br)
    nhom_nsx_thanhcong(br)
    nhom_nsx_thanhcong(br)
    time.sleep(2)



