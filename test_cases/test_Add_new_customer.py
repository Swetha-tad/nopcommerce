import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from page_objects.Add_Customer_Page import Add_Customer_Page
from page_objects.Admin_Login_Page import Login_Admin_Page
from utilities.read_properties import Read_data
from utilities.custom_logger import Log_Maker


class Test_003_Add_New_Customer:
    admin_page_url = Read_data.get_admin_page()
    username = Read_data.get_username()
    password = Read_data.get_password()
    logger = Log_Maker.log_gen()


    def test_add_new_customer(self,setup):
        self.logger.info("******* Test_003_Add_New_Customer Started ******")
        self.driver=setup
        self.driver.implicitly_wait(5)
        self.driver.get(self.admin_page_url)
        self.admin_lp = Login_Admin_Page(self.driver)
        self.admin_lp.username_login(self.username)
        self.admin_lp.password_login(self.password)
        self.admin_lp.btn_login()
        self.driver.maximize_window()
        self.logger.info("******* Login Successful ******")

        self.logger.info("******* Starting Add New Customer Test ******")
        time.sleep(3)
        self.add_customer = Add_Customer_Page(self.driver)
        self.add_customer.click_customer_menu()
        self.add_customer.click_customer_menu_option()
        self.add_customer.click_add_new_customer_button()
        self.logger.info("******* Providing Customer Info started ******")
        #email = generate_random_email()
        self.add_customer.enter_email("abc123@gmail.com")
        self.add_customer.enter_password("Test@123")
        self.add_customer.enter_firstname("Micheal")
        self.add_customer.enter_lastname("Shah")
        self.add_customer.select_gender("Male")
        self.add_customer.enter_company("XYZ Company")
        self.add_customer.click_tax_attempt()
        self.add_customer.select_customer_role("Guests")
        self.add_customer.select_manager_of_vendor("Vendor 2")
        self.add_customer.enter_admin_comment("Admin Comments Passed")
        self.add_customer.click_save_button()
        time.sleep(5)

        # test case validation as success message in body text
        customer_add_success_text="The new customer has been added successfully."
        success_text=self.driver.find_element(By.XPATH,"//span[normalize-space()='The new customer has been added successfully.']").text

        if customer_add_success_text in success_text:
            assert True
            self.logger.info("******* Test 003_Add_New_Customer Passed ******")
            self.driver.close()
        else:
            self.logger.info("******* Test 003_Add_New_Customer Failed ******")
            self.driver.save_screenshot(".//screenshot/test_003_Add_New_Customer_Failed.png")
            self.driver.close()
            assert False





