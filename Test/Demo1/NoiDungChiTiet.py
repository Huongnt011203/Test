import time
import Demo1.sp

from selenium.webdriver.common.by import By



tab = Demo1.ThemSP.dr1.find_element(By.XPATH, "/html/body/form/div[4]/div[3]/div/div/div/div[1]/div[2]/ul/li[3]/a")
tab.click()
print("step 1")
time.sleep(4)

#Combobox slTab
cbb_themSLTab = Demo1.ThemSP.dr1.find_element(By.XPATH, "/html/body/form/div[4]/div[3]/div/div/div/div[2]/div[2]/div/div[1]/div[1]/div/select")
cbb_themSLTab.click()
print("step 2")
time.sleep(2)

# Chonj gia tri Combobox slTab = 2
cbb_slTab = Demo1.ThemSP.dr1.find_element(By.XPATH, "/html/body/form/div[4]/div[3]/div/div/div/div[2]/div[2]/div/div[1]/div[1]/div/select/option[2]")
cbb_slTab.click()
print("step 3")
time.sleep(2)

# Sua ten hien thi
txt_tenHienThi = Demo1.ThemSP.dr1.find_element(By.XPATH, "/html/body/form/div[4]/div[3]/div/div/div/div[2]/div[2]/div/div[1]/div[2]/div[2]/div[1]/div[1]/input")
txt_tenHienThi.clear()
txt_tenHienThi.send_keys("Noi dung")
print("step 4")
time.sleep(2)

# Sua thu tu tab
txt_sttTab = Demo1.ThemSP.dr1.find_element(By.XPATH, "/html/body/form/div[4]/div[3]/div/div/div/div[2]/div[2]/div/div[1]/div[2]/div[2]/div[1]/div[1]/input")
txt_sttTab.clear()
txt_sttTab.send_keys("2")
print("step 5")
time.sleep(2)

"""# Sua thu tu tab
txt_noiDung1 = Demo1.ThemSP.dr1.find_element(By.XPATH, "/html/body/form/div[4]/div[3]/div/div/div/div[2]/div[2]/div/div[1]/div[2]/div[2]/div[2]/div/div/div")
txt_noiDung1.clear()
txt_noiDung1.send_keys("2")
print("step 6")
time.sleep(2)"""