from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from unittest import TestCase
import time


class GitLogin(TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://github.com/")
        self.driver.set_page_load_timeout(10)

    def test_valid_login(self):
        sign_in_button = self.driver.find_element_by_xpath("//a[@class='HeaderMenu-link no-underline mr-3']")
        sign_in_button.click()
        time.sleep(3)

        username = self.driver.find_element_by_xpath("//input[@id='login_field']")
        password = self.driver.find_element_by_xpath("//input[@id='password']")

        username.send_keys("Vanuhi1992")
        password.send_keys("Hayastan202020")

        submit_button = self.driver.find_element_by_xpath("//input[@name='commit']")
        submit_button.click()

        time.sleep(3)



