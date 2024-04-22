from pages.base_page import BasePage


class FinishPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self._endpoint = '/checkout-step-two.html'

    BURGER_MENU_SELECTOR = '#react-burger-menu-btn'
    BUTTON_LOGOUT_SELECTOR = '#logout_sidebar_link'

    def logout(self):
        self.assert_element_is_visible(self.BURGER_MENU_SELECTOR)
        self.wait_for_selector_and_click(self.BURGER_MENU_SELECTOR)
        self.wait_for_selector_and_click(self.BUTTON_LOGOUT_SELECTOR)
