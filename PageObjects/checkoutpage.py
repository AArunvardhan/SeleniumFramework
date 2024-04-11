from selenium.webdriver.common.by import By


class CheckOutPage:

    def __init__(self, driver):
        self.driver = driver

    cardTitle = (By.CSS_SELECTOR, ".col-lg-3.col-md-6.mb-3")
    cardFooter = (By.CSS_SELECTOR, ".card-title")
    addbutton = (By.CSS_SELECTOR, ".btn.btn-info")
    checkoutbutton= (By.CSS_SELECTOR, ".btn-primary")
    successbutton = (By.CSS_SELECTOR, ".btn-success")

    def getCardTitles(self):
        return self.driver.find_elements(*CheckOutPage.cardTitle)

    def getProductName(self):
        return self.driver.find_element(*CheckOutPage.cardFooter)

    def clickbutton(self):
        return self.driver.find_element(*CheckOutPage.addbutton)

    def checkout(self):
        return self.driver.find_element(*CheckOutPage.checkoutbutton)

    def successButton(self):
        return self.driver.find_element(*CheckOutPage.successbutton)