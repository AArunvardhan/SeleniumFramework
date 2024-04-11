from selenium.webdriver.common.by import By


class Submission:
    def __init__(self,driver):
        self.driver = driver

    name = (By.NAME, 'name')
    email = (By.NAME, 'email')
    password = (By.ID, 'exampleInputPassword1')
    check = (By.CLASS_NAME, 'form-check-input')
    Gender = (By.CSS_SELECTOR, "#exampleFormControlSelect1")
    button = (By.XPATH, "//input[@type='submit']")
    message = (By.CLASS_NAME, 'alert-success')
    def entername(self):
        return self.driver.find_element(*Submission.name)

    def enteremail(self):
        return self.driver.find_element(*Submission.email)

    def enterpassword(self):
        return self.driver.find_element(*Submission.password)

    def checkoption(self):
        return self.driver.find_element(*Submission.check)

    def getgender(self):
        return self.driver.find_element(*Submission.Gender)
    def submitbutton(self):
        return self.driver.find_element(*Submission.button)

    def successmsg(self):
        return self.driver.find_element(*Submission.message)


