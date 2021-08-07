from selenium.webdriver.common.by import By
from pageObjects.ConfirmPage import ConfirmPage


class CheckOutPage:

    def __init__(self, driver):
        self.driver = driver


    #driver.find_elements_by_xpath("//div[@class='card h-100']")
    productTitle = (By.XPATH, "//div[@class='card h-100']")
    cardFooter = (By.CSS_SELECTOR, ".card-footer button")
    checkOut = (By.XPATH, "//button[@class='btn btn-success']")

    def getProductTitles(self):
        return self.driver.find_elements(*CheckOutPage.productTitle)

    def getcardFooter(self):
        return self.driver.find_element(*CheckOutPage.cardFooter)

    def checkOutItems(self):
        self.driver.find_element(*CheckOutPage.checkOut).click()
        confirmPage = ConfirmPage(self.driver)
        return confirmPage








