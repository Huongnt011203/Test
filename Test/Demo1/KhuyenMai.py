import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pandas as pd
import Demo1.DangNhap
import Demo1.sp

def check(duLieu):
    try:
        data_frame = pd.read_excel(duLieu)
        for index, row in data_frame.iterrows():
            giaNiemYet = row['giaNiemYet']
            giaBan = row['giaBan']
            tb = row['thongBao']

            btn_ChonThem = br.find_element(By.XPATH, "/html/body/form/div[4]/div[2]/div/div[1]/ul/li[4]/ul/li[1]/a")
            btn_ChonThem.click()
            cbb_nhomSp = br.find_element(By.XPATH,
                                         "/html/body/form/div[4]/div[3]/div/div/div/div[2]/div[1]/div/div[1]/div/select")
            cbb_nhomSp.click()

            cbb1 = br.find_element(By.XPATH,"/html/body/form/div[4]/div[3]/div/div/div/div[2]/div[1]/div/div[1]/div/select/option[2]")
            cbb1.click()
            time.sleep(5)

            tab_KM = Demo1.ThemSP.find_element(By.XPATH, "/html/body/form/div[4]/div[3]/div/div/div/div[1]/div[2]/ul/li[7]/a")
            tab_KM.click()
            time.sleep(4)

#Nhâpk giá niêm yết
            txt_giaNiemYet = Demo1.ThemSP.find_element(By.XPATH, "/html/body/form/div[4]/div[3]/div/div/div/div[2]/div[7]/div/div[1]/div/input")
            txt_giaNiemYet.send_keys(giaNiemYet)
            if pd.isna(giaNiemYet):
                print(f"Case {index + 1} fail")
                continue

            time.sleep(2)

#Nhâpk giá bán
            txt_giaBan = Demo1.ThemSP.find_element(By.XPATH, "/html/body/form/div[4]/div[3]/div/div/div/div[2]/div[7]/div/div[2]/div/input")
            txt_giaBan.send_keys(giaBan)
            if pd.isna(giaBan):
                print(f"Case {index + 1} fail")
                continue

            time.sleep(2)

# Nhập loa tiền
            txt_loaiTien = Demo1.ThemSP.find_element(By.XPATH, "/html/body/form/div[4]/div[3]/div/div/div/div[2]/div[7]/div/div[3]/div/input")
            txt_loaiTien.send_keys("VND")

            time.sleep(2)

# click checkbox noi bat
            cb_noiBat = Demo1.ThemSP.find_element(By.XPATH, "/html/body/form/div[4]/div[3]/div/div/div/div[2]/div[7]/div/div[4]/div/input[1]")
            cb_noiBat.click()

            time.sleep(2)

# click checkbox moi
            cb_moi = Demo1.ThemSP.find_element(By.XPATH, "/html/body/form/div[4]/div[3]/div/div/div/div[2]/div[7]/div/div[4]/div/input[2]")
            cb_moi.click()

            time.sleep(2)

#click btn CapNhat
            btn_capNhat = Demo1.ThemSP.find_element(By.XPATH, "/html/body/form/div[4]/div[3]/div/div/div/div[2]/div[9]/div/div/a[1]")
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
    btn_ChonThem = br.find_element(By.XPATH, "/html/body/form/div[4]/div[2]/div/div[1]/ul/li[4]/ul/li[1]/a")
    btn_ChonThem.click()
    time.sleep(5)
    return
if __name__ == '__main__':
    br = webdriver.Chrome()
    br.get("http://1.hoctestertop.com/control.panel/")
    Demo1.DangNhap.thanh_cong(br)
    them(br)
    duLieu = r'E:\tensp_check.xlsx'
    check(duLieu)
    # rong(br)