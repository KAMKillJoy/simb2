from ManagerForm import ManagerFormMethods
from confest import browser

def sort_clients(browser):
    manager_form = ManagerFormMethods(browser)
    manager_form.go_to_site()
    manager_form.click_customers()
    manager_form.click_firstname_sort()
