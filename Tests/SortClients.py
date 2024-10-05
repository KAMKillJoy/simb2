from selenium.webdriver.common.by import By

from ManagerForm import ManagerFormMethods
from confest import browser

def test_sort_clients(browser):
    manager_form = ManagerFormMethods(browser)
    manager_form.go_to_site()
    manager_form.click_customers()
    manager_form.click_firstname_sort()
    manager_form.click_firstname_sort()

    rows = manager_form.get_customers_table()
    names = list()
    for row in rows:
        name = row.find_elements(By.TAG_NAME, "td")[0].text
        names.append(name)
    sorted_names = names
    sorted_names.sort()
    # print (sorted_names)
    assert sorted_names == names