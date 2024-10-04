from NewClient import Client
from ManagerForm import ManagerFormMethods
from confest import browser

def new_client_add_form(browser):
    client = Client()
    manager_form = ManagerFormMethods(browser)
    manager_form.go_to_site()
    manager_form.click_add_customer_button()
    manager_form.enter_firstname(client.first_name)
    manager_form.enter_lastname(client.second_name)
    manager_form.enter_postcode(client.postcode)
    manager_form.click_submit_customer_button()