import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
chromeOptions = Options()
desired_dirctory = os.path.join(r"C:\orange\orders", )
prefs = {
    "download.default_directory" : desired_dirctory,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True,
    'profile.default_content_setting_values.automatic_downloads': 2,
}
chromeOptions.add_experimental_option("prefs",prefs)

class OrangeOrder():
    def setup_method(self, options):
        self.driver = webdriver.Chrome(chrome_options=options)

    def teardown_method(self):
      self.driver.quit()

    def DownloadOrangeOrder(self):
        self.driver.get("https://admin-xxxxxxx-xxxx.xxxx.xx/webmaster/login")
        self.driver.find_element(By.ID, "manager_login_id").send_keys("xxxxxxxxx")
        self.driver.find_element(By.ID, "password").send_keys("xxxxxxxx")
        self.driver.find_element(By.ID, "login_btn").click()
        self.driver.find_element(By.CSS_SELECTOR, "b").click()
        self.driver.find_element(By.CSS_SELECTOR, ".active-result").click()
        self.driver.find_element(By.CSS_SELECTOR, "#left-navigation-block-order > .clearfix").click()
        self.driver.find_element(By.CSS_SELECTOR, "#left-navigation-block-order li:nth-child(1) > a").click()
        self.driver.find_element(By.CSS_SELECTOR, ".bt-submit:nth-child(13)").click()

download = OrangeOrder()
download.setup_method(chromeOptions)
download.DownloadOrangeOrder()

time.sleep(5)
download.teardown_method()
time.sleep(5)
