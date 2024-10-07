import allure
from selenium.webdriver.common.by import By

from Pages.ManagerForm import ManagerFormMethods
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
    allure.dynamic.title("Тест удаления клиента")
    allure.dynamic.description(
        "Удаляет клиента, чьё имя ближе всего по длине к среднему значению длин всех имён клиентов")
    allure.dynamic.tag("GUI_test", "Simbirsoft", "ManagerForm")
    allure.dynamic.severity(allure.severity_level.CRITICAL)
    allure.dynamic.label("owner", "John Doe")
    allure.dynamic.link("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager",
                        name="Website")
    manager_form = ManagerFormMethods(browser)
    with allure.step("Открытие сайта"):manager_form.go_to_site()
    with allure.step("Открытие таблицы со всеми клиентами"):manager_form.click_customers()

    with allure.step("Получение строк таблицы с клиентами"):rows = manager_form.get_customers_table()

    with allure.step("Составление списка со всеми именами клиентов"):client_names = manager_form.get_client_names(rows)

    with allure.step("Вычисление клиента, чьё имя ближе всего по длине к среднему значению длин всех имён клиентов"):loh_client = find_loh_client(client_names)
    #  print (loh_client)
    loh_client_number = client_names.index(loh_client)
    #  print (loh_client_number)
    with allure.step("Удаление найденного клиента"):manager_form.delete_client_by_row_number(loh_client_number)

    rows = manager_form.get_customers_table()
    for row in rows:
        assert loh_client not in row.text
    else:
        with allure.step("Проверка отсутствия удалённого клиента в таблице"):True

    client_names.remove(loh_client)
    expected_client_names = client_names
    client_names = manager_form.get_client_names(rows)

    with allure.step("Проверка наличия остальных клиентов в таблице"):assert client_names == expected_client_names

