from pages.base_page import BasePage


class InventoryPage(BasePage):
    ADD_TO_CART_SELECTOR = ".inventory_item >> text='Add to cart'"
    TITLE_OF_ITEM_SELECTOR = '#item_4_title_link'
    ADD_TO_CART_ITEM_SELECTOR = '#add-to-cart'
    SHOPPING_CART_LINK_SELECTOR = '[data-test="shopping-cart-link"]'

    def __init__(self, page):
        super().__init__(page)
        self._endpoint = 'inventory.html'

    def add_first_item_to_cart(self):
        self.wait_for_selector_and_click(self.ADD_TO_CART_SELECTOR)
        self.wait_for_selector_and_click(self.ADD_TO_CART_SELECTOR)
        self.assert_element_is_visible(self.SHOPPING_CART_LINK_SELECTOR)
        self.wait_for_selector_and_click(self.SHOPPING_CART_LINK_SELECTOR)

    def do_not_add_items_to_cart(self):
        self.assert_element_is_visible(self.SHOPPING_CART_LINK_SELECTOR)
        self.wait_for_selector_and_click(self.SHOPPING_CART_LINK_SELECTOR)

    def add_item_to_cart(self):
        self.assert_element_is_visible(self.TITLE_OF_ITEM_SELECTOR)
        self.wait_for_selector_and_click(self.TITLE_OF_ITEM_SELECTOR)
        self.assert_element_is_visible(self.ADD_TO_CART_ITEM_SELECTOR)
        self.wait_for_selector_and_click(self.ADD_TO_CART_ITEM_SELECTOR)
        self.assert_element_is_visible(self.SHOPPING_CART_LINK_SELECTOR)
        self.wait_for_selector_and_click(self.SHOPPING_CART_LINK_SELECTOR)
