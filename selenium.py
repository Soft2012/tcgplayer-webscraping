
from selenium.webdriver.common.by import By
import time
from seleniumbase import Driver

driver = Driver(uc=True, headless2=True)
driver.maximize_window()
url = 'https://www.tcgplayer.com/product/248251/'
driver.get(url)

time.sleep(5)

# email input
rarity = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/section[2]/section/div/div[2]/section[2]/section[3]/div/div[1]/div/ul/li[1]/div/span')
print("rarity: ", rarity.text)
cardNumber = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/section[2]/section/div/div[2]/section[2]/section[3]/div/div[1]/div/ul/li[2]/div/span')
print("cardNumber: ", cardNumber.text)

# while True:
#     pass
driver.close()
