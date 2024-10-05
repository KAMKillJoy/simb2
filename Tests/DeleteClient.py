from selenium.webdriver.common.by import By

from ManagerForm import ManagerFormMethods
from confest import browser


def find_loh_client(client_names_list):
    name_len_sum = 0
    for name in client_names_list:
        name_len_sum += len(name)
    av_name_len = name_len_sum/len(client_names_list)
    closest = 999
    for name in client_names_list:
        avdif = abs(len(name) - av_name_len)
        if avdif < closest:
            loh_client = name
            closest = avdif

    return loh_client


def test_delete_client(browser):
    manager_form = ManagerFormMethods(browser)
    manager_form.go_to_site()
    manager_form.click_customers()
    rows = manager_form.get_customers_table()
    client_names = []

    for row in rows:
        client_names.append(row.find_element(By.XPATH, "./td[1]").text)
    loh_client = find_loh_client(client_names)
    #  print (loh_client)
    loh_client_number = client_names.index(loh_client)
    #  print (loh_client_number)
    manager_form.delete_client_by_row_number(loh_client_number)

    rows = manager_form.get_customers_table()
    for row in rows:
        assert loh_client not in row.text

