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
        #  print(ManagerFormLocators.LOCATOR_DELETE_CUSTOMER)
        self.find_element(ManagerFormLocators.LOCATOR_DELETE_CUSTOMER).click()

    def get_client_names(self, rows):
        client_names = []
        for row in rows:
            client_names.append(row.find_element(By.XPATH, "./td[1]").text)
        return client_names