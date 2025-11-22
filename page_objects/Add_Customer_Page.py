import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# page object class
class Add_Customer_Page:
    link_customer_menu_xpath="(//a[@class='nav-link'])[23]"
    link_customer_menu_option_xpath="(//a[@class='nav-link'])[24]"
    link_add_new_customer_xpath="//a[normalize-space()='Add new']"

    textbox_email_id="Email"
    textbox_password_id="Password"
    textbox_firstname_id="FirstName"
    textbox_lastname_id="LastName"

    rd_button_male_id="Gender_Male"
    rd_button_female_id="Gender_Female"

    textbox_company_name_id="Company"

    checkbox_tax_attempt_id="IsTaxExempt"

    listbox_customer_roles_xpath="//*[@id='customer-info']//ul[contains(@class,'select2-selection__rendered')]"
    customer_role_Administrators_xpath="(//li[@id='select2-SelectedCustomerRoleIds-result-fidp-1'])[1]"
    customer_role_ForumModerators_xpath="(//li[@id='select2-SelectedCustomerRoleIds-result-u4nq-2'])[1]"
    customer_role_Registered_xpath="//*[@id='select2-SelectedCustomerRoleIds-result-r36h-3']"
    customer_role_Guests_xpath="//li[@class='select2-results__option' and text()='Guests']"
    customer_role_Vendors_xpath="(//li[@id='select2-SelectedCustomerRoleIds-result-cbav-5'])[1]"

    drpdown_manage_vendor_xpath="(//span[@id='select2-VendorId-container'])[1]"

    checkbox_active_xpath="//input[@id='Active']"

    checkbox_password_change_xpath="//input[@id='MustChangePassword']"

    textbox_admin_comments_xpath="//textarea[@id='AdminComment']"

    link_save_button_xpath="//button[@name='save']"


    def __init__(self, driver):
        self.driver = driver

    def click_customer_menu(self):
        self.driver.find_element(By.XPATH, self.link_customer_menu_xpath).click()

    def click_customer_menu_option(self):
        self.driver.find_element(By.XPATH, self.link_customer_menu_option_xpath).click()

    def click_add_new_customer_button(self):
        self.driver.find_element(By.XPATH, self.link_add_new_customer_xpath).click()

    def enter_email(self,email):
        self.driver.find_element(By.ID, self.textbox_email_id).send_keys(email)

    def enter_password(self,password):
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)

    def enter_firstname(self,firstname):
        self.driver.find_element(By.ID, self.textbox_firstname_id).send_keys(firstname)

    def enter_lastname(self,lastname):
        self.driver.find_element(By.ID, self.textbox_lastname_id).send_keys(lastname)

    def select_gender(self,gender):
        if gender == "Male":
            self.driver.find_element(By.ID, self.rd_button_male_id).click()
        elif gender == "Female":
            self.driver.find_element(By.ID, self.rd_button_female_id).click()

    def enter_company(self,companyname):
        self.driver.find_element(By.ID, self.textbox_company_name_id).send_keys(companyname)

    def click_tax_attempt(self):
        self.driver.find_element(By.ID, self.checkbox_tax_attempt_id).click()

    time.sleep(3)

    def select_customer_role(self, role):
        customer_role = self.driver.find_element(By.XPATH, self.listbox_customer_roles_xpath)
        customer_role.click()

        if role == "Guests":
            self.driver.find_element(By.XPATH, self.customer_role_Registered_xpath).click()
            time.sleep(3)
            customer_role.click()
            self.driver.find_element(By.XPATH, self.customer_role_Guests_xpath).click()
        elif role == "Administrators":
            self.driver.find_element(By.XPATH, self.customer_role_Administrators_xpath).click()
        elif role == "ForumModerators":
            self.driver.find_element(By.XPATH, self.customer_role_ForumModerators_xpath).click()
        elif role == "Registered":
            self.driver.find_element(By.XPATH, self.customer_role_Registered_xpath).click()
        elif role == "Vendors":
            self.driver.find_element(By.XPATH, self.customer_role_Vendors_xpath).click()
        else:
            self.driver.find_element(By.XPATH, self.customer_role_Administrators_xpath).click()

    def select_manager_of_vendor(self,value):
        drp_down = Select(self.driver.find_element(By.XPATH, self.drpdown_manage_vendor_xpath))
        drp_down.select_by_visible_text(value)

    def enter_admin_comment(self,admincomments):
        self.driver.find_element(By.XPATH, self.textbox_admin_comments_xpath).send_keys(admincomments)

    def click_save_button(self):
        self.driver.find_element(By.XPATH, self.link_save_button_xpath).click()











