import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Edge()
driver.get("https://rahulshettyacademy.com/angularpractice")
driver.maximize_window()
driver.implicitly_wait(5)

# driver.find_element(By.NAME,'name').send_keys('Arun vardhan')
# driver.find_element(By.NAME,"email").send_keys("vardhan@arun.com")
# driver.find_element(By.XPATH,"//input[@type='password']").send_keys('12334566')
# driver.find_element(By.CSS_SELECTOR,"input[type='checkbox']").click()
# driver.find_element(By.XPATH,"//select/option[1]").click()
# driver.find_element(By.CSS_SELECTOR,"#inlineRadio2").click()
# driver.find_element(By.XPATH,"//input[@name='bday']").send_keys('01/01/2010')
# driver.find_element(By.XPATH,"//input[@type='submit']").click()
# message = driver.find_element(By.CSS_SELECTOR,".alert-success").text
# assert 'Success' in message
driver.find_element(By.XPATH,"//ul/li[2]").click()
options = driver.find_elements(By.CSS_SELECTOR,".col-lg-3.col-md-6.mb-3")
for option in options:
    if option.find_element(By.CSS_SELECTOR,".card-title").text == 'Samsung Note 8':
        option.find_element(By.CSS_SELECTOR,".btn.btn-info").click()

driver.find_element(By.CSS_SELECTOR,".btn-primary").click()
driver.find_element(By.CSS_SELECTOR,".btn.btn-success").click()
driver.find_element(By.CSS_SELECTOR,"#country").send_keys('In')
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,"India")))
driver.find_element(By.LINK_TEXT,"India").click()
driver.find_element(By.CSS_SELECTOR,"label[for='checkbox2']").click()
driver.find_element(By.XPATH,"//input[@value='Purchase']").click()
print(driver.find_element(By.CSS_SELECTOR,".alert-success").text)
