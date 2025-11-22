from selenium.webdriver.common.by import By

#page object class
class Login_Admin_Page:
    # identifying web elements
    textbox_username_id="Email"
    textbox_password_id="Password"
    btn_login_xpath="//button[normalize-space()='Log in']"
    btn_logout_linktext="Logout"

    # action methods for test cases
    def __init__(self, driver):
        self.driver = driver

    def username_login(self,username):
        self.driver.find_element(By.ID, self.textbox_username_id).clear()
        self.driver.find_element(By.ID, self.textbox_username_id).send_keys(username)

    def password_login(self,password):
        self.driver.find_element(By.ID, self.textbox_password_id).clear()
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)

    def btn_login(self):
        self.driver.find_element(By.XPATH, self.btn_login_xpath).click()

    def btn_logout(self):
        self.driver.find_element(By.LINK_TEXT, self.btn_logout_linktext).click()




