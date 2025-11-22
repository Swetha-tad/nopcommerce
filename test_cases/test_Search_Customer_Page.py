import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from page_objects.Add_Customer_Page import Add_Customer_Page
from page_objects.Admin_Login_Page import Login_Admin_Page
from page_objects.Search_Customer_Page import Search_Customer_Page
from utilities.read_properties import Read_data
from utilities.custom_logger import Log_Maker


class Test_004_Search_Customer_Page:
    admin_page_url = Read_data.get_admin_page()
    username = Read_data.get_username()
    password = Read_data.get_password()
    logger = Log_Maker.log_gen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_search_customer_by_email(self,setup):
        self.logger.info("********Test_004_01_Search_Customer_Page Started*********")
        self.driver=setup
        self.driver.implicitly_wait(5)
        self.driver.get(self.admin_page_url)
        self.admin_lp = Login_Admin_Page(self.driver)
        self.admin_lp.username_login(self.username)
        self.admin_lp.password_login(self.password)
        self.admin_lp.btn_login()
        self.driver.maximize_window()
        self.logger.info("******* Login Successful ******")
        time.sleep(3)
        self.logger.info("******* Navigating to customer search page ******")
        self.add_customer = Add_Customer_Page(self.driver)
        self.add_customer.click_customer_menu()
        self.add_customer.click_customer_menu_option()
        self.logger.info("******* Starting search customer by email ******")
        self.search_customer = Search_Customer_Page(self.driver)
        self.search_customer.search_customer_by_email("arthur_holmes@nopCommerce.com")
        self.search_customer.click_search_button()
        time.sleep(3)
        is_email_present=self.search_customer.search_customer_by_email("arthur_holmes@nopCommerce.com")
        if is_email_present:
            assert True
            self.logger.info("******* Email Present Successful ******")
            self.driver.close()
        else:
            self.logger.info("******* Email Present Failed ******")
            self.driver.save_screenshot(".//screenshots//test_search_customer_by_email.png")
            self.driver.close()
            assert False

    @pytest.mark.regression
    def test_search_customer_by_name(self,setup):
        self.logger.info("********Test_004_Search_02_Customer_Page Started*********")
        self.driver=setup
        self.driver.implicitly_wait(5)
        self.driver.get(self.admin_page_url)
        self.admin_lp = Login_Admin_Page(self.driver)
        self.admin_lp.username_login(self.username)
        self.admin_lp.password_login(self.password)
        self.admin_lp.btn_login()
        self.driver.maximize_window()
        self.logger.info("******* Login Successful ******")
        time.sleep(3)
        self.logger.info("******* Navigating to customer search page ******")
        self.add_customer = Add_Customer_Page(self.driver)
        self.add_customer.click_customer_menu()
        self.add_customer.click_customer_menu_option()
        self.logger.info("******* Starting search customer by name ******")
        self.search_customer = Search_Customer_Page(self.driver)
        self.search_customer.enter_customer_firstname("Arthur")
        self.search_customer.enter_customer_lastname("Holmes")
        self.search_customer.click_search_button()
        time.sleep(3)
        is_name_present=self.search_customer.search_customer_by_name("Arthur Holmes")
        if is_name_present:
            assert True
            self.logger.info("******* Name Present Successful ******")
            self.driver.close()
        else:
            self.logger.info("******* Name Present Failed ******")
            self.driver.save_screenshot(".//screenshots//test_search_customer_by_name.png")
            self.driver.close()
            assert False

    @pytest.mark.regression
    def test_search_customer_by_company(self,setup):
        self.logger.info("********Test_004_Search_03_Customer_Page Started*********")
        self.driver=setup
        self.driver.implicitly_wait(5)
        self.driver.get(self.admin_page_url)
        self.admin_lp = Login_Admin_Page(self.driver)
        self.admin_lp.username_login(self.username)
        self.admin_lp.password_login(self.password)
        self.admin_lp.btn_login()
        self.driver.maximize_window()
        self.logger.info("******* Login Successful ******")
        time.sleep(3)
        self.logger.info("******* Navigating to customer search page ******")
        self.add_customer = Add_Customer_Page(self.driver)
        self.add_customer.click_customer_menu()
        self.add_customer.click_customer_menu_option()
        self.logger.info("******* Starting search customer by Company ******")
        self.search_customer = Search_Customer_Page(self.driver)
        self.search_customer.search_customer_by_company("Microsoft")
        self.search_customer.click_search_button()
        time.sleep(3)
        is_company_name_present=self.search_customer.search_customer_by_company("Microsoft")
        if is_company_name_present:
            assert True
            self.logger.info("******* Company name Present Successful ******")
            self.driver.close()
        else:
            self.logger.info("******* Company name Present Failed ******")
            self.driver.save_screenshot(".//screenshots//test_search_customer_by_company.png")
            self.driver.close()
            assert False




