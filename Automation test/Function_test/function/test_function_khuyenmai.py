import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import Test_thuong.test_function_dangnhap
import Demo1.sp
import utilities.utilities_xpath

def check(duLieu):
    try:
        data_frame = pd.read_excel(duLieu)
        for index, row in data_frame.iterrows():
            giaNiemYet = row['giaNiemYet']
            giaBan = row['giaBan']
            tb = row['thongBao']

            btn_ChonThem = br.find_element(By.XPATH, utilities.utilities_xpath.xpath_btn_chon_them())
            btn_ChonThem.click()
            cbb_nhomSp = br.find_element(By.XPATH,
                                         utilities.utilities_xpath.xpath_cbb_nhomsp())
            cbb_nhomSp.click()

            cbb1 = br.find_element(By.XPATH,utilities.utilities_xpath.xpath_cbb_nhomsp_4())
            cbb1.click()
            time.sleep(5)

            tab_KM = Demo1.ThemSP.find_element(By.XPATH, utilities.utilities_xpath.xpath_tab_tao_km())
            tab_KM.click()
            time.sleep(4)

#Nhâpk giá niêm yết
            txt_giaNiemYet = Demo1.ThemSP.find_element(By.XPATH, utilities.utilities_xpath.xpath_txt_gia_niem_yet())
            txt_giaNiemYet.send_keys(giaNiemYet)
            if pd.isna(giaNiemYet):
                print(f"Case {index + 1} fail")
                continue

            time.sleep(2)

#Nhâpk giá bán
            txt_giaBan = Demo1.ThemSP.find_element(By.XPATH,utilities.utilities_xpath.xpath_txt_gia_ban())
            txt_giaBan.send_keys(giaBan)
            if pd.isna(giaBan):
                print(f"Case {index + 1} fail")
                continue

            time.sleep(2)

# Nhập loa tiền
            txt_loaiTien = Demo1.ThemSP.find_element(By.XPATH, utilities.utilities_xpath.xpath_txt_loai_tien())
            txt_loaiTien.send_keys("VND")

            time.sleep(2)

# click checkbox noi bat
            cb_noiBat = Demo1.ThemSP.find_element(By.XPATH, utilities.utilities_xpath.xpath_check_box_noi_bat())
            cb_noiBat.click()

            time.sleep(2)

# click checkbox moi
            cb_moi = Demo1.ThemSP.find_element(By.XPATH, utilities.utilities_xpath.xpath_check_box_moi())
            cb_moi.click()

            time.sleep(2)

#click btn CapNhat
            btn_capNhat = Demo1.ThemSP.find_element(By.XPATH, utilities.utilities_xpath.xpath_btn_cap_nhat_km())
            btn_capNhat.click()
            time.sleep(2)

            thongBao1 = str(tb)
            if pd.isna(tb):  # Kiểm tra nếu thongBao rỗng
                print(f"Case {index + 1} pass")
            else:
                if thongBao1 in br.page_source:
                    print(f"Case {index + 1} pass")
                else:
                    print(f"Case {index + 1} fail")
            time.sleep(1)
    except Exception as e:
        print(e)

def them(br):
    btn_ThemSP = br.find_element(By.XPATH, "/html/body/form/div[4]/div[2]/div/div[1]/ul/li[4]/a")
    btn_ThemSP.click()
    btn_ChonThem = br.find_element(By.XPATH, utilities.utilities_xpath.xpath_btn_chon_them())
    btn_ChonThem.click()
    time.sleep(5)
    return
if __name__ == '__main__':
    br = webdriver.Chrome()
    br.get("http://1.hoctestertop.com/control.panel/")
    Test_thuong.DangNhap.thanh_cong(br)
    them(br)
    duLieu = r'E:\test\Du_lieu_test\du_lieu_test_man_thongtin'
    check(duLieu)
    # rong(br)