from playwright.sync_api import sync_playwright
import time

from pages.about_page import AboutPage
from pages.checkout_page import CheckoutPage
from pages.finish_page import FinishPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


def test_create_order(browser):
    page = browser.new_page()
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    checkout_page = CheckoutPage(page)
    finish_page = FinishPage(page)

    login_page.login('standard_user', 'secret_sauce')
    inventory_page.add_first_item_to_cart()
    checkout_page.start_checkout()
    checkout_page.fill_checkout_form('John', 'Doe', '12345')
    checkout_page.finish_checkout()
    finish_page.logout()


def test_create_order_without_items(browser):
    page = browser.new_page()
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    checkout_page = CheckoutPage(page)
    finish_page = FinishPage(page)

    login_page.login('standard_user', 'secret_sauce')
    inventory_page.do_not_add_items_to_cart()
    checkout_page.start_checkout()
    checkout_page.fill_checkout_form('John', 'Doe', '12345')
    checkout_page.finish_checkout()
    finish_page.logout()


def test_create_order_inside_the_page_order(browser):
    page = browser.new_page()
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    checkout_page = CheckoutPage(page)
    finish_page = FinishPage(page)

    login_page.login('standard_user', 'secret_sauce')
    inventory_page.add_item_to_cart()
    checkout_page.start_checkout()
    checkout_page.fill_checkout_form('John', 'Doe', '12345')
    checkout_page.finish_checkout()
    finish_page.logout()


def test_about_page(browser):
    page = browser.new_page()
    login_page = LoginPage(page)
    about_page = AboutPage(page)

    login_page.login('standard_user', 'secret_sauce')
    about_page.get_about_page()
