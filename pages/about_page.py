from pages.base_page import BasePage


class AboutPage(BasePage):
    BURGER_MENU_SELECTOR = '#react-burger-menu-btn'
    ABOUT_LINK_SELECTOR = '#about_sidebar_link'

    def __init__(self, page):
        super().__init__(page)
        self._endpoint = '/about.html'

    def get_about_page(self):
        self.assert_element_is_visible(self.BURGER_MENU_SELECTOR)
        self.wait_for_selector_and_click(self.BURGER_MENU_SELECTOR)
        self.wait_for_selector_and_click(self.ABOUT_LINK_SELECTOR)
        self.wait_for_url(self._endpoint)
