import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
chromeOptions = Options()
desired_dirctory = os.path.join(r"C:\orange\customers", )
prefs = {
    "download.default_directory" : desired_dirctory,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True,
    'profile.default_content_setting_values.automatic_downloads': 2,
}
chromeOptions.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(chrome_options=chromeOptions)
driver.get("https://admin-xxxxxxx-xxxx.xxxx.xx/webmaster/login")
driver.find_element(By.ID, "manager_login_id").send_keys("")
driver.find_element(By.ID, "password").send_keys("")
driver.find_element(By.ID, "login_btn").click()
driver.find_element(By.CSS_SELECTOR, "b").click()
driver.find_element(By.CSS_SELECTOR, ".active-result").click()
driver.find_element(By.LINK_TEXT, "顧客管理").click()
driver.find_element(By.CSS_SELECTOR, "#left-navigation-block-customer li:nth-child(1) > a").click()
driver.find_element(By.CSS_SELECTOR, ".bt-submit:nth-child(33)").click()
time.sleep(5)
driver.close()
time.sleep(5)
