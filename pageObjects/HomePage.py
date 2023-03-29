import time

from selenium.webdriver.common.by import By

from base.base_driver import BaseDriver
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

# now scroll is available for every page with inherit (BaseDriver)
class HomePage(BaseDriver):
    def __init__(self, driver):
        # super().__init__(driver)
        self.driver = driver

    button_alert_xpath = "/html/body/div[8]/div[1]/div/div[3]/a[1]"

    def accept_alert(self):
        self.driver.switch_to.frame("trustarc_cm")
        self.wait_until_element_is_clickable(By.XPATH, self.button_alert_xpath).click()
        self.driver.switch_to.frame(0)
        # alert = self.driver.swich_to.alert
        # time.sleep(1)
        # alert.accept()
