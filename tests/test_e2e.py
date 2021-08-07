from selenium import webdriver
import time
import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from utilities.BaseClass import BaseClass
from pageObjects.HomePage import HomePage
from pageObjects.checkoutPage import CheckOutPage


#@pytest.mark.usefixtures("setup")
class TestOne(BaseClass):

    def test_e2e(self):

        homepage = HomePage(self.driver)
        checkOutPage = homepage.shopItems()
        #self.driver.find_element_by_css_selector("a[href*='shop']").click()

        #products = self.driver.find_elements_by_xpath("//div[@class='card h-100']")
        #checkOutPage = CheckOutPage(self.driver) this is not required since we have created object in homepage
        products = checkOutPage.getProductTitles()

        for product in products:
            productName = product.find_element_by_xpath("div/h4/a").text
            if productName == "Blackberry":
                #Add element to the cart
                #product.find_element_by_xpath("div/button").click()
                checkOutPage.getcardFooter().click()   

        self.driver.find_element_by_css_selector("a[class*='btn-primary']").click()
        #self.driver.find_element_by_xpath("//button[@class='btn btn-success']").click()
        confirmpage = checkOutPage.checkOutItems()
        self.driver.find_element_by_id("country").send_keys("ind")

        # Putting explicit wait for 7 second
        self.verifyLinkPresence("India")
        self.driver.find_element_by_link_text("India").click()
        self.driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()
        self.driver.find_element_by_css_selector("[type='submit']").click()
        successText = self.driver.find_element_by_class_name("alert-success").text

        assert "Success! Thank you!" in successText

        self.driver.get_screenshot_as_file("screen.png")

