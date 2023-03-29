from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver


class SearchFlight(BaseDriver):
    # log = Utils.loggen(loglevel=logging.INFO)
    def __init__(self, driver):
        # super().__init__(driver)
        self.driver = driver

    # locators
    textbox_departure_city_xpath = '//*[@id="jb-autocomplete-3-search"]'
    submit_departure_city_xpath = "//div[@class='avenir body royal-blue']"
    textbox_arriving_city_xpath = '//*[@id="jb-autocomplete-4-search"]'
    submit_arriving_city_xpath = "//div[@class='avenir body royal-blue']"
    input_depart_xpath = '//*[@id="jb-date-picker-input-id-4"]'
    button_depart_data_xpath = "//button[@aria-label='depart Saturday, April 1, 2023']"
    input_return_xpath = '//*[@id="jb-date-picker-input-id-5"]'
    button_return_data_css = "button[aria-label='return Thursday, May 25, 2023'] span[class='flex flex-column'] span"
    button_done_xpath = "//div[@class='avenir body royal-blue']"
    button_search_xpath = "//button[@class='pointer avenir b no-underline t-med-bg t-out-hover w-100 w-auto-ns tc border-box inline-flex align-items-center justify-center jb-booker-air-submit mt3-m mt3 jb-button-primary jb-button-large b--none bg-royal-blue br-rounded-2 body hover-white white w-max-ns ng-star-inserted relative']"

    def set_depart_city(self, departure):
        self.wait_until_element_is_clickable(By.XPATH, self.textbox_departure_city_xpath).click()
        self.driver.find_element(By.XPATH, self.textbox_departure_city_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_departure_city_xpath).send_keys(departure)

    def confirm_austin_city(self):
        self.driver.find_element(By.XPATH, self.submit_departure_city_xpath).click()

    def set_arriving_city(self, arriving):
        self.driver.find_element(By.XPATH, self.textbox_arriving_city_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_arriving_city_xpath).send_keys(arriving)

    def confirm_new_york_city(self):
        self.driver.find_element(By.XPATH, self.submit_arriving_city_xpath).click()

    def select_depart_data(self):
        self.driver.find_element(By.XPATH, self.input_depart_xpath).click()
        self.driver.find_element(By.XPATH, self.button_depart_data_xpath).click()

    def select_return_data(self):
        self.driver.find_element(By.XPATH, self.input_return_xpath).click()
        self.driver.find_element(By.CSS_SELECTOR, self.button_return_data_css).click()

    def click_search(self):
        self.driver.find_element(By.XPATH, self.button_done_xpath).click()
        self.driver.find_element(By.XPATH, self.button_search_xpath).click()