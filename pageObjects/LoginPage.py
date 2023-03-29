from selenium import webdriver
from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver


class LoginPage(BaseDriver):
    # log = Utils.loggen(loglevel=logging.INFO)
    def __init__(self, driver):
#        super().__init__(driver)
        self.driver = driver

    # locators
    textbox_username_id = "Email"
    textbox_password_id = "Password"
    button_login_xpath = "//button[@type='submit']"
    link_logout_linktext = "Logout"

    # login_page_expected_title = "Your store. Login"

    # self.driver - class element
    # super function initialize the base driver class

    # implement action method for the elements above:
    def setUserName(self, username):
        self.driver.find_element(By.ID, self.textbox_username_id).clear()
        self.driver.find_element(By.ID, self.textbox_username_id).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.ID, self.textbox_password_id).clear()
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)

    def clickLogin(self):
        # self.driver.find_element(By.XPATH, self.button_login_xpath).click()
        self.wait_until_element_is_clickable(By.XPATH, self.button_login_xpath).click()
        # self.wait_until_element_is_clickable(By.XPATH, self.button_login_xpath).click()

    def clickLogOUt(self):
        self.driver.find_element(By.LINK_TEXT, self.link_logout_linktext).click()
