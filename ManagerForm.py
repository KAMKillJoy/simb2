import os

from selenium.webdriver import Keys
from selenium.webdriver.support.select import Select

from BaseApp import BasePage
from selenium.webdriver.common.by import By


class ManagerFormLocators(BasePage):
    LOCATOR_ADD_CUSTOMER_BUTTON = (By.XPATH, "(//button[contains(text(), 'Add Customer')])[1]")
    LOCATOR_OPEN_ACCOUNT_BUTTON = (By.XPATH, "//button[contains(text(), 'Open Account')]")
    LOCATOR_CUSTOMERS_BUTTON = (By.XPATH, "//button[contains(text(), 'Customers')]")

    LOCATOR_FIRSTNAME_FIELD = (By.XPATH, "//input[@ng-model='fName']")
    LOCATOR_LASTNAME_FIELD = (By.XPATH, "//input[@ng-model='lName']")
    LOCATOR_POSTCODE_FIELD = (By.XPATH, "//input[@ng-model='postCd']")
    LOCATOR_SUBMIT_CUSTOMER_BUTTON = (By.XPATH, "(//button[contains(text(), 'Add Customer')])[2]")

    LOCATOR_FIRSTNAME_SORT = (By.XPATH, "//a[contains(text(), 'First Name')]")

    LOCATOR_CUSTOMERS_TABLE = (By.XPATH, "/html/body/div[1]/div/div[2]/div/div[2]/div/div/table/tbody/tr")

    LOCATOR_DELETE_CUSTOMER = (By.XPATH, "//tr[@class='ng-scope'][{row}]//button[@ng-click='deleteCust(cust)']")




class ManagerFormMethods(BasePage):
    def enter_firstname(self, firstname):
        self.find_element(ManagerFormLocators.LOCATOR_FIRSTNAME_FIELD).send_keys(firstname)

    def enter_lastname(self, lastname):
        self.find_element(ManagerFormLocators.LOCATOR_LASTNAME_FIELD).send_keys(lastname)

    def enter_postcode(self, postcode):
        self.find_element(ManagerFormLocators.LOCATOR_POSTCODE_FIELD).send_keys(postcode)

    def click_add_customer_button(self):
        self.find_element(ManagerFormLocators.LOCATOR_ADD_CUSTOMER_BUTTON).click()

    def click_submit_customer_button(self):
        self.find_element(ManagerFormLocators.LOCATOR_SUBMIT_CUSTOMER_BUTTON).click()

    def click_firstname_sort(self):
        self.find_element(ManagerFormLocators.LOCATOR_FIRSTNAME_SORT).click()

    def click_customers(self):
        self.find_element(ManagerFormLocators.LOCATOR_CUSTOMERS_BUTTON).click()

    def get_customers_table(self):
        return self.find_elements(ManagerFormLocators.LOCATOR_CUSTOMERS_TABLE)

    def delete_client_by_row_number(self, row):
        ManagerFormLocators.LOCATOR_DELETE_CUSTOMER = \
            (ManagerFormLocators.LOCATOR_DELETE_CUSTOMER[0],
             ManagerFormLocators.LOCATOR_DELETE_CUSTOMER[1].replace("{row}", str(row+1)))
        print(ManagerFormLocators.LOCATOR_DELETE_CUSTOMER)
        self.find_element(ManagerFormLocators.LOCATOR_DELETE_CUSTOMER).click()
'''
    def read_result_modal_title(self):
        self.read_element(self.find_element(ManagerFormLocators.LOCATOR_RESULT_MODAL_TITLE))

    def read_result_modal_student_name(self):
        self.read_element(self.find_element(ManagerFormLocators.LOCATOR_RESULT_MODAL_STUDENT_NAME))

    def read_result_modal_student_email(self):
        self.read_element(ManagerFormLocators.LOCATOR_RESULT_MODAL_STUDENT_EMAIL)

    def read_result_modal_student_gender(self):
        self.read_element(ManagerFormLocators.LOCATOR_RESULT_MODAL_STUDENT_GENDER)

    def read_result_modal_student_mobile(self):
        self.read_element(ManagerFormLocators.LOCATOR_RESULT_MODAL_STUDENT_MOBILE)

    def read_result_modal_student_date_of_birth(self):
        self.read_element(ManagerFormLocators.LOCATOR_RESULT_MODAL_STUDENT_DATE_OF_BIRTH)

    def read_result_modal_student_subjects(self):
        self.read_element(ManagerFormLocators.LOCATOR_RESULT_MODAL_STUDENT_SUBJECTS)

    def read_result_modal_student_hobbies(self):
        self.read_element(ManagerFormLocators.LOCATOR_RESULT_MODAL_STUDENT_HOBBIES)

    def read_result_modal_student_picture(self):
        self.read_element(ManagerFormLocators.LOCATOR_RESULT_MODAL_STUDENT_PICTURE)

    def read_result_modal_student_address(self):
        self.read_element(ManagerFormLocators.LOCATOR_RESULT_MODAL_STUDENT_ADDRESS)

    def read_result_modal_state_and_city(self):
        self.read_element(ManagerFormLocators.LOCATOR_RESULT_MODAL_STUDENT_STATE_AND_CITY)
        
'''
