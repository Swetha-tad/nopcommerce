from selenium.webdriver.common.by import By

#page object class
class Search_Customer_Page:
    # locating web elements
    text_email_id="SearchEmail"
    text_firstname_id="SearchFirstName"
    text_lastname_id="SearchLastName"
    text_company_id="SearchCompany"
    click_search_button_id="search-customers"

    row_table_xpath="//table[@id='customers-grid']/tbody//tr"
    col_table_xpath="//table[@id='customers-grid']/tbody//tr/td"

    def __init__(self, driver):
        self.driver = driver

    def enter_customer_email(self,email):
        self.driver.find_element(By.ID, self.text_email_id).clear()
        self.driver.find_element(By.ID, self.text_email_id).send_keys(email)

    def enter_customer_firstname(self,firstname):
        self.driver.find_element(By.ID, self.text_firstname_id).clear()
        self.driver.find_element(By.ID, self.text_firstname_id).send_keys(firstname)

    def enter_customer_lastname(self,lastname):
        self.driver.find_element(By.ID, self.text_lastname_id).clear()
        self.driver.find_element(By.ID, self.text_lastname_id).send_keys(lastname)

    def enter_customer_company(self,company_name):
        self.driver.find_element(By.ID, self.text_company_id).clear()
        self.driver.find_element(By.ID, self.text_company_id).send_keys(company_name)

    def click_search_button(self):
        self.driver.find_element(By.ID, self.click_search_button_id).click()

    def get_results_row_table(self):
        return len(self.driver.find_elements(By.XPATH, self.row_table_xpath))

    def get_results_col_table(self):
        return len(self.driver.find_elements(By.XPATH, self.col_table_xpath))

    def search_customer_by_email(self,email):
        email_present_flag=False
        for r in range(1,self.get_results_row_table()+1):
            cus_email=self.driver.find_element(By.XPATH, "//table[@id='customers-grid']/tbody//tr["+str(r)+"]/td[2]").text

            if cus_email==email:
                email_present_flag=True
                break
            return email_present_flag

    def search_customer_by_name(self,name):
        name_present_flag = False
        for r in range(1, self.get_results_row_table() + 1):
            cus_name = self.driver.find_element(By.XPATH, "//table[@id='customers-grid']/tbody//tr["+str(r)+"]/td[3]").text

            if cus_name == name:
                name_present_flag = True
                break
            return name_present_flag

    def search_customer_by_company(self,company_name):
        company_name_present_flag = False
        for r in range(1, self.get_results_row_table() + 1):
            cus_company_name = self.driver.find_element(By.XPATH, "//table[@id='customers-grid']/tbody//tr["+str(r)+"]/td[5]").text

            if cus_company_name == company_name:
                company_name_present_flag = True
                break
            return company_name_present_flag








