from selenium.webdriver.common.by import By

from ManagerForm import ManagerFormMethods
from confest import browser

def test_sort_clients(browser):
    manager_form = ManagerFormMethods(browser)
    manager_form.go_to_site()
    manager_form.click_customers()
    rows =  manager_form.get_customers_table()

    for row in rows:
        # Получите все ячейки в строке
        cells = row.find_elements(By.TAG_NAME, "td")
        for cell in cells:
            print(cell.text)  # Вывод текста каждой ячейки
