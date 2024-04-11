from selenium.webdriver.common.by import By


class Homepage:
    shop = (By.XPATH, "//a[text()='Shop']")

    def __init__(self, driver):
        self.driver = driver

    def shopItems(self):
        return self.driver.find_element(*Homepage.shop)
