
import time

from selenium import webdriver
import Demo1.sp
from selenium.webdriver.common.by import By


tab_cauHinhSeo = Demo1.ThemSP.dr1.find_element(By.XPATH, "/html/body/form/div[4]/div[3]/div/div/div/div[1]/div[2]/ul/li[8]/a")
tab_cauHinhSeo.click()
print("step 1")
time.sleep(4)

#Nhập meta title
txt_metaTitle = Demo1.ThemSP.dr1.find_element(By.XPATH, "/html/body/form/div[4]/div[3]/div/div/div/div[2]/div[8]/div/div[1]/div/input")
txt_metaTitle.send_keys("ok1")
print("step 2")
time.sleep(2)

# Nhâp Meta description
txt_metaDescription = Demo1.ThemSP.dr1.find_element(By.XPATH, "/html/body/form/div[4]/div[3]/div/div/div/div[2]/div[8]/div/div[2]/div/textarea")
txt_metaDescription.send_keys("ok2")
print("step 3")
time.sleep(2)

#nhập Meta keyword
txt_metaKeyword = Demo1.ThemSP.dr1.find_element(By.XPATH, "/html/body/form/div[4]/div[3]/div/div/div/div[2]/div[8]/div/div[3]/div/textarea")
txt_metaKeyword.send_keys("ok3")
print("step 4")
time.sleep(5)

#icon Tag
icon_tagSP = Demo1.ThemSP.dr1.find_element(By.XPATH, "/html/body/form/div[4]/div[3]/div/div/div/div[2]/div[8]/div/div[4]/div/a")
icon_tagSP.click()
print("step 5")
time.sleep(2)

#chon doi tuong 1
click_doiTuong = Demo1.ThemSP.dr1.find_element(By.XPATH, "/html/body/form/div[4]/div[3]/div/div/div/div[2]/div[8]/div/div[5]/div/div/div[1]/select/option[1]")
click_doiTuong.click()
print("step 5")
time.sleep(2)

# btn >>
def click_tien():
    btn_tien = Demo1.ThemSP.dr1.find_element(By.XPATH, "/html/body/form/div[4]/div[3]/div/div/div/div[2]/div[8]/div/div[5]/div/div/div[2]/input[1]")
    btn_tien.click()
    print("step 5")
    time.sleep(2)
click_tien()

#chon doi tuong 2
click_doiTuong1 = Demo1.ThemSP.dr1.find_element(By.XPATH, "/html/body/form/div[4]/div[3]/div/div/div/div[2]/div[8]/div/div[5]/div/div/div[1]/select/option[2]")
click_doiTuong1.click()
print("step 5")
time.sleep(2)


click_tien()

#chon doi tuong 1
click_doiTuong2 = Demo1.ThemSP.dr1.find_element(By.XPATH, "/html/body/form/div[4]/div[3]/div/div/div/div[2]/div[8]/div/div[5]/div/div/div[3]/select/option[2]")
click_doiTuong2.click()
print("step 5")
time.sleep(2)

# btn <<
btn_lui = Demo1.ThemSP.dr1.find_element(By.XPATH, "/html/body/form/div[4]/div[3]/div/div/div/div[2]/div[8]/div/div[5]/div/div/div[2]/input[2]")
btn_lui.click()
print("step 5")
time.sleep(2)

