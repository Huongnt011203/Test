
import Demo1.sp
import time

from selenium.webdriver.common.by import By


tab_hinhAnh = Demo1.ThemSP.dr1.find_element(By.XPATH, "/html/body/form/div[4]/div[3]/div/div/div/div[1]/div[2]/ul/li[4]/a")
tab_hinhAnh.click()
print("step 1")
time.sleep(4)

#Combobox slAnh
cbb_themSLAnh = Demo1.ThemSP.dr1.find_element(By.XPATH, "/html/body/form/div[4]/div[3]/div/div/div/div[2]/div[3]/div/div[1]/div/select")
cbb_themSLAnh.click()
print("step 2")
time.sleep(2)

# Chonj gia tri Combobox slAnh = 2
cbb_slAnh = Demo1.ThemSP.dr1.find_element(By.XPATH, "/html/body/form/div[4]/div[3]/div/div/div/div[2]/div[3]/div/div[1]/div/select/option[2]")
cbb_slAnh.click()
print("step 3")
time.sleep(2)

# btn chon anh thu 1
btn_chonAnh = Demo1.ThemSP.dr1.find_element(By.XPATH, "/html/body/form/div[4]/div[3]/div/div/div/div[2]/div[3]/div/div[2]/div[1]/div/div/div/button")
btn_chonAnh.click()
print("step 4")
time.sleep(5)



