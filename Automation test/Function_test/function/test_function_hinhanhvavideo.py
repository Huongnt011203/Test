
import Demo1.sp
import time

from selenium.webdriver.common.by import By
import utilities.utilities_xpath

tab_hinhAnh = Demo1.ThemSP.dr1.find_element(By.XPATH, utilities.utilities_xpath.xpath_tab_hinh_anh())
tab_hinhAnh.click()
print("step 1")
time.sleep(4)

#Combobox slAnh
cbb_themSLAnh = Demo1.ThemSP.dr1.find_element(By.XPATH, utilities.utilities_xpath.xpath_them_sl_anh())
cbb_themSLAnh.click()
print("step 2")
time.sleep(2)

# Chonj gia tri Combobox slAnh = 2
cbb_slAnh = Demo1.ThemSP.dr1.find_element(By.XPATH, utilities.utilities_xpath.xpath_sl_anh())
cbb_slAnh.click()
print("step 3")
time.sleep(2)

# btn chon anh thu 1
btn_chonAnh = Demo1.ThemSP.dr1.find_element(By.XPATH, utilities.utilities_xpath.xpath_btn_chon_anh())
btn_chonAnh.click()
print("step 4")
time.sleep(5)



