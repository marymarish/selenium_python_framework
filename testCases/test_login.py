import logging
import time

import pytest
from base.base_driver import BaseDriver
from pageObjects.HomePage import HomePage
from pageObjects.searchFlight import SearchFlight
from utilities.readProperties import ReadConfig
from utilities.utils import Utils
# file_data to read external file
from ddt import ddt, data, file_data, unpack

@pytest.mark.usefixtures("setup")
class TestSearchFlight():
    # create variables:
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()
    baseURL = ReadConfig.getApplicationURL()
    # searchURL = ReadConfig.getSearchURL()
    expected_title_home_page = ReadConfig.getExpectedTitleHome()
    expected_title_search_page = ReadConfig.getExpectedTitleSearch()
    # create new object from class
    log = Utils.loggen(loglevel=logging.INFO)

    def testHomePageTitle(self, setup):
        self.log.info("Test_001_Home_Page")
        self.log.info("Verifying Home Page Title")
        # open home_page
        self.driver = setup
        self.driver.get(self.baseURL)
        time.sleep(2)
        hp = HomePage(self.driver)
        hp.accept_alert()

        # verify current title with expected:
        bd = BaseDriver(self.driver)
        bd.verify_title(self.expected_title_home_page, "test_homePageTitle")

    #@ddt
    # get data from xml
    # utils returns list
    #@data(*Utils.read_from_excel("C:/Users/Iuliia/Desktop/search_flight_book.xlsx", "Sheet1"))

    # @data(("Austin", "New York"))
    # @unpack

    # data from json:
    #@file_data("../testData/testdata.json")

    #get data from csv
    # @data(*Utils.read_data_from_csv("C:\\Users\\Iuliia\\Desktop\\Framework\\package\\testData\\csv_search_flight.csv"))
    # @unpack
    # def test_search_flight(self, departure, arriving):
    #     sp = SearchFlight(self.driver)
    #     sp.set_depart_city(departure)
    #     sp.confirm_austin_city()
    #     sp.set_arriving_city(arriving)
    #     sp.confirm_new_york_city()
    #     sp.select_depart_data()
    #     sp.select_return_data()
    #     sp.click_search()
    #     #
    #     # verify:
    #     bd = BaseDriver(self.driver)
    #     bd.verify_title(self.expected_title_search_page, "test_search_page")


    # get data from ()
    # @data(("Austin", "New York"))
    # @unpack
    # get data from file:
    # @file_data("../testData/testdata.json")
    # def test_search_flight(self, departure, arriving):
    #     sp = SearchFlight(self.driver)
    #     sp.set_depart_city(departure)
    #     sp.confirm_austin_city()
    #     sp.set_arriving_city(arriving)
    #     sp.confirm_new_york_city()
    #     sp.select_depart_data()
    #     sp.select_return_data()
    #     sp.click_search()
    #
    #     # verify:
    #     bd = BaseDriver()
    #     bd.verify_title(self.expected_title_search_page, "test_search_page")
    #     self.driver.close()

    # data driven testing, second() for second set of data
    # @data(("t.ly/c8-q", "tulubuy@gmail.com", "1235566z"), ("tesla.com", "tulubuy@gmail.com", "1235566z"))
    # @data(("t.ly/c8-q", "tulubuy@gmail.com", "1235566z"))
    # @unpack
    # def test_login(self, setup, username, password):
    #     self.log.info("Verifying Login test")
    #     self.driver = setup
    #     self.driver.get(self.loginURL)
    #
    #     lp = LoginPage(self.driver)
    #     lp.set_user_name(username)
    #     lp.click_next_after_email()
    #     lp.set_password(password)
    #     lp.click_submit()
    #
    #     # verify:
    #     bd = BaseDriver()
    #     bd.verify_title(self.expected_title_login_page, "test login page")
    #     self.driver.close()

    # def test_login(self, setup):
    #     self.log.info("Verifying Login test")
    #     self.driver = setup
    #     self.driver.get(self.loginURL)
    #
    #     lp = LoginPage(self.driver)
    #     lp.set_user_name(self.username)
    #     lp.click_next_after_email()
    #     lp.set_password(self.password)
    #     lp.click_submit()
    #
    #     # verify:
    #     bd = BaseDriver()
    #     bd.verify_title(self.expected_title_login_page, "test login page")
    #     self.driver.close()

    # def test_login(self, setup):
    #     self.log.info("Verifying Login test")
    #     # open home_page
    #     self.driver = setup
    #     # self.driver.get(self.baseURL)
    #     # create object to use methods from class LoginPage:
    #     lp = LoginPage(self.driver)
    #     # input username
    #     lp.setUserName(self.username)
    #     # input password
    #     lp.setPassword(self.password)
    #     # click submit
    #     lp.clickLogin()
    #
    #     # apply validation. Success or not:
    #     bd = BaseDriver()
    #     bd.verify_title(self.expected_title_login_page, "test_login")
