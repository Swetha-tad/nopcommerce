import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from page_objects.Admin_Login_Page import Login_Admin_Page
from utilities.read_properties import Read_data
from utilities.custom_logger import Log_Maker


class Test_001_Admin_Login:
    admin_page_url = Read_data.get_admin_page()
    username = Read_data.get_username()
    password = Read_data.get_password()
    invalid_username = Read_data.get_invalid_username()
    logger = Log_Maker.log_gen()


    @pytest.mark.sanity
    @pytest.mark.regression
    def test_title_verification(self,setup):
        self.logger.info("******* Test_001_Admin_Login ******")
        self.logger.info("******* test_title_verification started ******")
        self.driver=setup
        self.driver.get(self.admin_page_url)
        time.sleep(5)
        act_title=self.driver.title
        exp_title="nopCommerce demo store. Login"
        if act_title==exp_title:
            self.logger.info("******* test_title_verification passed  ******")
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(r".\\screenshots\\title_verification_fail.png")
            self.logger.info("******* test_title_verification failed ******")
            assert False
            self.driver.close()


    @pytest.mark.regression
    def test_Valid_Admin_Login_Page(self,setup):
        self.logger.info("******* test_Admin_Login_Page started ******")
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.admin_lp=Login_Admin_Page(self.driver)
        self.admin_lp.username_login(self.username)
        self.admin_lp.password_login(self.password)
        self.admin_lp.btn_login()
        time.sleep(5)
        act_dashboard_text=self.driver.find_element(By.XPATH,"//div[@class='content-header']/h1").text
        if act_dashboard_text=="Dashboard":
            self.logger.info("******* test_Admin_Login_Page Passed ******")
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(r".\\screenshots\\valid_login_fail.png")
            self.logger.info("******* test_Admin_Login_Page Failed ******")
            self.driver.close()
            assert False


    @pytest.mark.regression
    def test_Invalid_Admin_Login(self,setup):
        self.logger.info("******* test_Invalid_Admin_Login started ******")
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.admin_lp = Login_Admin_Page(self.driver)
        self.admin_lp.username_login(self.invalid_username)
        self.admin_lp.password_login(self.password)
        self.admin_lp.btn_login()
        error_message=self.driver.find_element(By.XPATH,"//li").text
        if error_message=="No customer account found":
            self.logger.info("******* test_Invalid_Admin_Login Passed ******")
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(r".\\screenshots\\invalid_login_fail.png")
            self.logger.info("******* test_Invalid_Admin_Login Failed ******")
            self.driver.close()
            assert False






