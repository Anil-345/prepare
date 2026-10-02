from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://example-ecommerce.com")

driver.find_element(By.ID, "username").send_keys("testuser")
driver.find_element(By.ID, "password").send_keys("password123")
driver.find_element(By.ID, "login").click()

driver.find_element(By.ID, "search").send_keys("Laptop")
driver.find_element(By.ID, "searchButton").click()

driver.quit()