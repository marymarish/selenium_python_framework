from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver


class LoginPage(BaseDriver):
    # log = Utils.loggen(loglevel=logging.INFO)
    def __init__(self, driver):
    # super().__init__(driver)
        self.driver = driver

    # locators
    textbox_email_css = "input[name='identity']"
    button_next_email_css = "button[type='submit']"
    textbox_password_xpath = "//input[@name='credential']"
    button_submit_xpath = "//button[@type='submit']"
    link_logout_linktext = "Sign Out"
    button_home_linktext = "Dashboard"

    def set_user_name(self, username):
        self.driver.find_element(By.CSS_SELECTOR, self.textbox_email_css).clear()
        self.driver.find_element(By.CSS_SELECTOR, self.textbox_email_css).send_keys(username)

    def click_next_after_email(self):
        self.wait_until_element_is_clickable(By.CSS_SELECTOR, self.button_next_email_css).click()

    def set_password(self, password):
        self.driver.find_element(By.XPATH, self.textbox_password_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_password_xpath).send_keys(password)

    def click_submit(self):
        self.driver.find_element(By.XPATH, self.button_submit_xpath).click()

    def click_button_home(self):
        self.driver.find_element(By.LINK_TEXT, self.button_home_linktext).click()

    def click_log_out(self):
        self.driver.find_element(By.LINK_TEXT, self.link_logout_linktext).click()