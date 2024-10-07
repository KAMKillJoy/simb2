import allure
from NewClient import Client
from Pages.ManagerForm import ManagerFormMethods
from confest import browser
from selenium.webdriver.common.by import By


def test_new_client_add_form(browser):
    allure.dynamic.title("Тест добавления нового клиента")
    allure.dynamic.description("Тест генерирует Имя клиента по алгоритму из документации (пункт 61141414141),"
                               "заполняет поля Firstname, Lastname, Postcode и нажимает кнопку добавления клиента."
                               "Затем проверяет наличие добавленного клиента в таблице клиентов")
    allure.dynamic.tag("GUI_test", "Simbirsoft", "ManagerForm")
    allure.dynamic.severity(allure.severity_level.CRITICAL)
    allure.dynamic.label("owner", "John Doe")
    allure.dynamic.link("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager",
                        name="Website")

    client = Client()
    manager_form = ManagerFormMethods(browser)

    with allure.step("Открытие сайта"):manager_form.go_to_site()
    with allure.step("Нажатие кнопки добавления клиента"):manager_form.click_add_customer_button()
    with allure.step("Введение имени клиента (Firstname)"):manager_form.enter_firstname(client.first_name)
    with allure.step("Введение фамилии клиента (Lastname)"):manager_form.enter_lastname(client.second_name)
    with allure.step("Введение почтового кода (postcode"):manager_form.enter_postcode(client.postcode)
    with allure.step("Нажатие кнопки отправки данных"):manager_form.click_submit_customer_button()

    with allure.step("Закрытие алерта браузера с подтверждением добавления клиента"):manager_form.dismiss_alert()
    with allure.step("Открытие таблицы со всеми клиентами"):manager_form.click_customers()
    rows = manager_form.get_customers_table()
    for row in rows:
        if client.first_name in row.text:
            if client.second_name in row.text:
                with allure.step("Поиск в таблице строки, содержащей Firstname и Lastname добавленного клиента"): True
                cells = row.find_elements(By.TAG_NAME, "td")
                with allure.step("Проверка соответствия Firstname ожидаемому"):assert cells[0].text == str(client.first_name)
                with allure.step("Проверка соответствия Lastname ожидаемому"):assert cells[1].text == str(client.second_name)
                with allure.step("Проверка соответствия Postcode ожидаемому"):assert cells[2].text == str(client.postcode)