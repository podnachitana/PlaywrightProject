# from playwright.sync_api import sync_playwright
# import time
#
# playwright = sync_playwright().start()
# browser = playwright.chromium.launch(headless=False, slow_mo=500)
# page = browser.new_page()
# page.goto("https://www.saucedemo.com/")
# page.type(selector='[id="user-name"]', text="standard_user", delay=100)
# page.fill(selector='#password', value='secret_sauce')
# page.click(selector='.submit-button')
# page.wait_for_url('https://www.saucedemo.com/inventory.html', timeout=10000)
# page.wait_for_selector('#inventory_container')
#
# button_add_to_cart = '[data-test="add-to-cart-sauce-labs-backpack"]'
# alt_locator_for_card = '.inventory_item a:has-text("Sauce Labs Backpack")'
# card_button = '.inventory_item_description:has-text("Sauce Labs Backpack") button:has-text("Add to cart")'
#
# page.is_visible(selector=button_add_to_cart)
# page.is_enabled(selector=button_add_to_cart)
# # page.click(selector=button_add_to_cart)
# # page.click(selector=alt_locator_for_card)
# page.click(card_button)
# page.is_visible('[data-test="shopping-cart-link"]')
# page.click('[data-test="shopping-cart-link"]')
# page.wait_for_url('https://www.saucedemo.com/cart.html', timeout=10000)
# button_checkout = '#checkout'
# page.wait_for_selector(button_checkout)
# page.is_visible(button_checkout)
# page.is_enabled(button_checkout)
# page.click(button_checkout)
# page.wait_for_url('https://www.saucedemo.com/checkout-step-one.html')
#
# page.fill(selector='#first-name', value='Name')
# page.fill(selector='#last-name', value='Surname')
# page.fill(selector='#postal-code', value='12345')
#
# page.click('[id="continue"][type="submit"]')
# page.wait_for_url('https://www.saucedemo.com/checkout-step-two.html')
# page.wait_for_selector('button:has-text("Finish")')
# page.click(selector='#finish')
# page.wait_for_url('https://www.saucedemo.com/checkout-complete.html')
#
# page.click('#react-burger-menu-btn')
# button_logout = '#logout_sidebar_link'
# page.wait_for_selector(button_logout)
# page.is_visible(button_logout)
# page.is_enabled(button_logout)
# page.click(button_logout)
#
#
#
# time.sleep(5)
#
# browser.close()
# playwright.stop()