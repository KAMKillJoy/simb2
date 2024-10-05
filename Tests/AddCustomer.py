from NewClient import Client
from ManagerForm import ManagerFormMethods
from confest import browser
from selenium.webdriver.common.by import By

def test_new_client_add_form(browser):
    client = Client()
    manager_form = ManagerFormMethods(browser)
    manager_form.go_to_site()
    manager_form.click_add_customer_button()
    manager_form.enter_firstname(client.first_name)
    manager_form.enter_lastname(client.second_name)
    manager_form.enter_postcode(client.postcode)
    manager_form.click_submit_customer_button()

    manager_form.dismiss_alert()
    manager_form.click_customers()
    manager_form.click_customers()
    rows = manager_form.get_customers_table()
    for row in rows:
        if client.first_name in row.text:
            cells = row.find_elements(By.TAG_NAME, "td")
            assert cells[0].text == str(client.first_name)
            assert cells[1].text == str(client.second_name)
            assert cells[2].text == str(client.postcode)