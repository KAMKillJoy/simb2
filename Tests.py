import AddCustomer
import SortClients
import DeleteClient
from confest import browser

def test_new_client(browser):
    addcustomer.new_client_add_form(browser)

def test_sort_clients(browser):
    SortClients.sort_clients(browser)

def test_delete_client(browser):
    DeleteClient.delete_client(browser)