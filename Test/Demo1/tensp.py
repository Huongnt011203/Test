import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import random
import pandas as pd
import Demo1.DangNhap
def thanh_cong(br):
    # btn_ChonThem = br.find_element(By.XPATH, "//*[@id='sidebar']/div/div[1]/ul/li[4]/ul/li[1]/a")
    # btn_ChonThem.click()

    cbb_nhomSp = br.find_element(By.XPATH, "//*[@id='ctl00_ContentPlaceHolder1_ucLoadControl_ctl00_ddlForder']")
    cbb_nhomSp.click()

    cbb1 = br.find_element(By.XPATH, "//*[@id='ctl00_ContentPlaceHolder1_ucLoadControl_ctl00_ddlForder']/option[2]")
    cbb1.click()
    time.sleep(1)

    cbb_hangsx = br.find_element(By.XPATH,
                                 "//*[@id='ctl00_ContentPlaceHolder1_ucLoadControl_ctl00_ddlMan']")

    cbb_hangsx.click()
    time.sleep(1)
    nsx = br.find_element(By.XPATH, "//*[@id='ctl00_ContentPlaceHolder1_ucLoadControl_ctl00_ddlMan']/option[3]")
    nsx.click()
    time.sleep(1)

    cbb_model = br.find_element(By.XPATH,
                                "//*[@id='ctl00_ContentPlaceHolder1_ucLoadControl_ctl00_ddlModel']")
    cbb_model.click()
    time.sleep(1)
    c = br.find_element(By.XPATH, "//*[@id='ctl00_ContentPlaceHolder1_ucLoadControl_ctl00_ddlModel']/option[3]")
    c.click()
    time.sleep(1)

    txt_maSp = br.find_element(By.XPATH,
                               "/html/body/form/div[4]/div[3]/div/div/div/div[2]/div[1]/div/div[5]/div/input")

    txt_maSp.send_keys("HT0101")
    time.sleep(1)
    txt_tenSp = br.find_element(By.XPATH,
                               "/html/body/form/div[4]/div[3]/div/div/div/div[2]/div[1]/div/div[4]/div/input")
    txt_tenSp.send_keys("Nhãn")
    time.sleep(1)

    txt_bh = br.find_element(By.XPATH,
                             "/html/body/form/div[4]/div[3]/div/div/div/div[2]/div[1]/div/div[6]/div/input")
    txt_bh.send_keys("10")
    time.sleep(1)

    txt_sl = br.find_element(By.XPATH,
                             "/html/body/form/div[4]/div[3]/div/div/div/div[2]/div[1]/div/div[9]/div/input")
    txt_sl.send_keys("100")
    time.sleep(1)

    # Nhap thu tu
    txt_stt = br.find_element(By.XPATH,
                              "/html/body/form/div[4]/div[3]/div/div/div/div[2]/div[1]/div/div[10]/div/input")
    txt_stt.send_keys("2")
    time.sleep(1)

    # Chọn còn hàng
    rd_conHang = br.find_element(By.XPATH,
                                 "/html/body/form/div[4]/div[3]/div/div/div/div[2]/div[1]/div/div[11]/div/table/tbody/tr/td[1]/input")
    rd_conHang.click()
    time.sleep(1)

    # Click calendar
    click_calendar = br.find_element(By.XPATH,
                                     "/html/body/form/div[4]/div[3]/div/div/div/div[2]/div[1]/div/div[12]/div/div/input")
    click_calendar.click()
    time.sleep(1)

    # Click checkbox
    click_checkBox = br.find_element(By.XPATH,
                                     "/html/body/form/div[4]/div[3]/div/div/div/div[2]/div[1]/div/div[13]/div/input")
    click_checkBox.click()
    time.sleep(1)

    btn_capNhat = br.find_element(By.XPATH, "/html/body/form/div[4]/div[3]/div/div/div/div[2]/div[9]/div/div/a[1]")
    btn_capNhat.click()
    time.sleep(1)

    if br.current_url == "http://1.hoctestertop.com/admin-product/list.aspx":
        print("Case 7 pass")
        return True
    else:
        print("Case 7 fail")
        return False
def thanh_cong_check(du_lieu):

    try:
        data_frame = pd.read_excel(du_lieu)
        for index, row in data_frame.iterrows():
            ten_sp = row['Tensp']
            thongBao = row['ThongBao']

            btn_ChonThem = br.find_element(By.XPATH, "/html/body/form/div[4]/div[2]/div/div[1]/ul/li[4]/ul/li[1]/a")
            btn_ChonThem.click()
            cbb_nhomSp = br.find_element(By.XPATH,
                                         "/html/body/form/div[4]/div[3]/div/div/div/div[2]/div[1]/div/div[1]/div/select")
            cbb_nhomSp.click()

            cbb1 = br.find_element(By.XPATH,
                                   "/html/body/form/div[4]/div[3]/div/div/div/div[2]/div[1]/div/div[1]/div/select/option[2]")
            cbb1.click()
            time.sleep(1)

            cbb_hangsx = br.find_element(By.XPATH,
                                         "/html/body/form/div[4]/div[3]/div/div/div/div[2]/div[1]/div/div[2]/div/select")

            cbb_hangsx.click()
            time.sleep(1)
            nsx = br.find_element(By.XPATH,
                                  "/html/body/form/div[4]/div[3]/div/div/div/div[2]/div[1]/div/div[2]/div/select/option[5]")
            nsx.click()
            time.sleep(1)

            cbb_model = br.find_element(By.XPATH,
                                        "/html/body/form/div[4]/div[3]/div/div/div/div[2]/div[1]/div/div[3]/div/select")
            cbb_model.click()
            time.sleep(1)
            c = br.find_element(By.XPATH,
                                "/html/body/form/div[4]/div[3]/div/div/div/div[2]/div[1]/div/div[3]/div/select/option[3]")
            c.click()
            time.sleep(1)

            txt_tenSp = br.find_element(By.XPATH,
                                        "/html/body/form/div[4]/div[3]/div/div/div/div[2]/div[1]/div/div[4]/div/input")
            txt_tenSp.clear()
            txt_tenSp.send_keys(ten_sp)

            if not txt_tenSp:
                print(f"Case {index + 1} fail")
                continue

            txt_maSp = br.find_element(By.XPATH,
                                       "/html/body/form/div[4]/div[3]/div/div/div/div[2]/div[1]/div/div[5]/div/input")

            txt_maSp.send_keys("HT0101")
            time.sleep(1)
            txt_bh = br.find_element(By.XPATH,
                                     "/html/body/form/div[4]/div[3]/div/div/div/div[2]/div[1]/div/div[6]/div/input")
            txt_bh.send_keys("10")
            time.sleep(1)

            txt_sl = br.find_element(By.XPATH,
                                     "/html/body/form/div[4]/div[3]/div/div/div/div[2]/div[1]/div/div[9]/div/input")
            txt_sl.send_keys("100")
            time.sleep(1)

            # Nhap thu tu
            txt_stt = br.find_element(By.XPATH,
                                      "/html/body/form/div[4]/div[3]/div/div/div/div[2]/div[1]/div/div[10]/div/input")
            txt_stt.send_keys("2")
            time.sleep(1)

            # Chọn còn hàng
            rd_conHang = br.find_element(By.XPATH,
                                         "/html/body/form/div[4]/div[3]/div/div/div/div[2]/div[1]/div/div[11]/div/table/tbody/tr/td[1]/input")
            rd_conHang.click()
            time.sleep(1)

            # Click calendar
            click_calendar = br.find_element(By.XPATH,
                                             "/html/body/form/div[4]/div[3]/div/div/div/div[2]/div[1]/div/div[12]/div/div/input")
            click_calendar.click()
            time.sleep(1)
            # Click checkbox
            click_checkBox = br.find_element(By.XPATH,
                                             "/html/body/form/div[4]/div[3]/div/div/div/div[2]/div[1]/div/div[13]/div/input")
            click_checkBox.click()
            time.sleep(1)



            btn_capNhat = br.find_element(By.XPATH, "/html/body/form/div[4]/div[3]/div/div/div/div[2]/div[9]/div/div/a[1]")
            btn_capNhat.click()
            time.sleep(1)

            thongBao1 = str(thongBao)
            if thongBao1 in br.page_source:
                print(f"Case {index + 1} pass")
            else:
                print(f"Case {index + 1} fail")
            # if br.current_url == "http://1.hoctestertop.com/admin-product/list.aspx":
            #     print(f"Case {index + 1} pass")
            #     # return True
            # else:
            #     print(f"Case {index + 1} fail")
                # return False
    except Exception as e:
        print(e)

def rong(br):
    btn_ChonThem = br.find_element(By.XPATH, "//*[@id='sidebar']/div/div[1]/ul/li[4]/ul/li[1]/a")
    btn_ChonThem.click()

    cbb_nhomSp = br.find_element(By.XPATH, "/html/body/form/div[4]/div[3]/div/div/div/div[2]/div[1]/div/div[1]/div/select")
    cbb_nhomSp.click()

    cbb1 = br.find_element(By.XPATH, "/html/body/form/div[4]/div[3]/div/div/div/div[2]/div[1]/div/div[1]/div/select/option[2]")
    cbb1.click()
    time.sleep(1)

    cbb_hangsx = br.find_element(By.XPATH,
                                 "/html/body/form/div[4]/div[3]/div/div/div/div[2]/div[1]/div/div[2]/div/select")

    cbb_hangsx.click()
    time.sleep(1)
    nsx = br.find_element(By.XPATH, "/html/body/form/div[4]/div[3]/div/div/div/div[2]/div[1]/div/div[2]/div/select/option[5]")
    nsx.click()
    time.sleep(1)

    cbb_model = br.find_element(By.XPATH,
                                "/html/body/form/div[4]/div[3]/div/div/div/div[2]/div[1]/div/div[3]/div/select")
    cbb_model.click()
    time.sleep(1)
    c = br.find_element(By.XPATH, "/html/body/form/div[4]/div[3]/div/div/div/div[2]/div[1]/div/div[3]/div/select/option[3]")
    c.click()
    time.sleep(1)

    txt_tenSp = br.find_element(By.XPATH,
                                "/html/body/form/div[4]/div[3]/div/div/div/div[2]/div[1]/div/div[4]/div/input")
    if not txt_tenSp:
        print("Case  fail ten sp rong")
        return False
    # txt_tenSp.send_keys("HT0101")
    time.sleep(1)
    txt_maSp = br.find_element(By.XPATH,
                               "/html/body/form/div[4]/div[3]/div/div/div/div[2]/div[1]/div/div[5]/div/input")
    txt_maSp.send_keys("Ht1")
    time.sleep(1)

    txt_bh = br.find_element(By.XPATH,
                             "/html/body/form/div[4]/div[3]/div/div/div/div[2]/div[1]/div/div[6]/div/input")
    txt_bh.send_keys("10")
    time.sleep(1)

    txt_sl = br.find_element(By.XPATH,
                             "/html/body/form/div[4]/div[3]/div/div/div/div[2]/div[1]/div/div[9]/div/input")
    txt_sl.send_keys("100")
    time.sleep(1)

    # Nhap thu tu
    txt_stt = br.find_element(By.XPATH,
                              "/html/body/form/div[4]/div[3]/div/div/div/div[2]/div[1]/div/div[10]/div/input")
    txt_stt.send_keys("2")
    time.sleep(1)

    # Chọn còn hàng
    rd_conHang = br.find_element(By.XPATH,
                                 "/html/body/form/div[4]/div[3]/div/div/div/div[2]/div[1]/div/div[11]/div/table/tbody/tr/td[1]/input")
    rd_conHang.click()
    time.sleep(1)

    # Click calendar
    click_calendar = br.find_element(By.XPATH,
                                     "/html/body/form/div[4]/div[3]/div/div/div/div[2]/div[1]/div/div[12]/div/div/input")
    click_calendar.click()
    time.sleep(1)

    # Click checkbox
    click_checkBox = br.find_element(By.XPATH,
                                     "/html/body/form/div[4]/div[3]/div/div/div/div[2]/div[1]/div/div[13]/div/input")
    click_checkBox.click()
    time.sleep(1)

    btn_capNhat = br.find_element(By.XPATH, "/html/body/form/div[4]/div[3]/div/div/div/div[2]/div[9]/div/div/a[1]")
    btn_capNhat.click()
    time.sleep(1)

    if 'Chưa nhập tên sản phẩm' in br.page_source:
        print("Case 7 pass")
        return True
    else:
        print("Case 7 fail")
        return False
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
    thanh_cong(br)
    du_lieu = r'E:\tensp_check.xlsx'
    thanh_cong_check(du_lieu)
    rong(br)