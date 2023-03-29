import logging
import softest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium import  webdriver
from selenium.webdriver.common.action_chains import ActionChains
from utilities.utils import Utils
from testCases import conftest


# anything what takes the reference of the driver object directly
class BaseDriver(softest.TestCase):
    log = Utils.loggen()

    def __init__(self, driver):
        # super function initialize the base driver class
        super().__init__()
        self.driver = driver

    # locator_type #By.XPATH. locator #"[@...]"
    def wait_for_presence_of_all_elements(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 10)
        my_list = wait.until(EC.presence_of_all_elements_located((locator_type, locator)))
        return my_list

    # def wait_for_presence_of_element(self, locator_type, locator):
    #     wait = WebDriverWait(self.driver, 10)
    #     my_element = wait.until(EC.presence_of_element_located(locator_type, locator))
    #     return my_element

    def wait_until_element_is_clickable(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((locator_type, locator)))
        return element

    def getCurrentTitle(self):
        current_title = self.driver.title
        return current_title

    # def getScreenshot(self, test_name):
    #     self.driver.save_screenshot(".\\screenshots\\" + test_name + ".png")

    def verify_title(self, expected_title, test_name):
        # if failure happen, with soft_assert cript will continue to verify
        self.soft_assert(self.assertEqual, self.getCurrentTitle(), expected_title)
        if self.getCurrentTitle() == expected_title:
            print("Test is passed")
            self.log.info(test_name + " is passed")
        else:
            self.log.error(test_name, " is failed")
            print("test failed")
        # self.assert_all()


