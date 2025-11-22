import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from page_objects.Admin_Login_Page import Login_Admin_Page
from utilities.read_properties import Read_data
from utilities.custom_logger import Log_Maker
from utilities import XLUtilities

class Test_002_Admin_Login_data_driven:
    admin_page_url = Read_data.get_admin_page()
    logger = Log_Maker.log_gen()
    path=".//test_data//admin_login_data.xlsx"
    satus_list=[]


    def test_valid_Admin_Login_Page_data_driven(self,setup):
        self.logger.info("******* test_valid_Admin_Login_Page_data_driven started ******")
        self.driver = setup
        self.driver.implicitly_wait(10)
        self.driver.get(self.admin_page_url)
        self.admin_lp=Login_Admin_Page(self.driver)

        self.rows = XLUtilities.getRowCount(self.path,"Sheet1")
        print("num of rows: ",self.rows)


        for r in range(2,self.rows+1):
            # reading data from excel file
            self.username=XLUtilities.readData(self.path,"Sheet1",r,1)
            self.password = XLUtilities.readData(self.path, "Sheet1", r, 2)
            self.exp_login = XLUtilities.readData(self.path, "Sheet1", r, 3)
            # passing values to the application
            self.admin_lp.username_login(self.username)
            self.admin_lp.password_login(self.password)
            self.admin_lp.btn_login()
            time.sleep(5)
            act_title=self.driver.title
            exp_title="Dashboard / nopCommerce administration"

            if (act_title == exp_title):
                if self.exp_login=="yes":
                    self.logger.info("******* test_valid_Admin_Login_Page success ******")
                    self.satus_list.append("Pass")
                    self.admin_lp.btn_logout()
                elif self.exp_login=="no":
                    self.logger.info("******* test_valid_Admin_Login_Page failed ******")
                    self.satus_list.append("Fail")
                    self.admin_lp.btn_logout()

            elif (act_title != exp_title):
                if self.exp_login=="yes":
                    self.logger.info("******* test_valid_Admin_Login_Page failed ******")
                    self.satus_list.append("Fail")


                elif self.exp_login=="no":
                    self.logger.info("******* test_valid_Admin_Login_Page success ******")
                    self.satus_list.append("Pass")


        print("Status list is:",self.satus_list)

        if "Fail" in self.satus_list:
            self.logger.info("******* test_valid_Admin_Login_Page failed ******")
            assert False
        else:
            self.logger.info("******* test_valid_Admin_Login_Page success ******")
            assert True











