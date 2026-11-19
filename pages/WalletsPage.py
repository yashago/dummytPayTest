from pages.BasePage import BasePage


class WalletsPage(BasePage):

    def __init__(self, page):
        super().__init__(page)

    @property
    def balance(self):
        return 'abc'