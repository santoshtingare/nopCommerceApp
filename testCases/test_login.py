import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.customLogger import LogGen


class Test_001_Login:
    baseURL = "https://admin-demo.nopcommerce.com/"
    username = "admin@yourstore.com"
    password = "admin"

    logger = LogGen.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_homepageTitle(self, setup):
        self.logger.info("***************** Test_001_Login *****************")
        self.logger.info("**************** Verifying Home Page Title ***********")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        if act_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("****************  Home Page Title test case is passed ***********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homepageTitle.png")
            self.driver.close()
            self.logger.error("****************  Home Page Title test case is failed ***********")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, setup):
        self.logger.info("****************  Login test case is started ***********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        # Validations
        act_title = self.driver.title
        self.driver.close()
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info("****************  Login test is passed ***********")
            self.driver.close()
        else:
            self.driver.get_screenshot_as_file(".\\Screenshots\\"+"test_login.png")
            self.driver.close()
            self.logger.error("****************  Login test is failed ***********")
            assert False





