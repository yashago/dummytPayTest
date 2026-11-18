from playwright.sync_api import Locator, Page

from pages.BasePage import BasePage
from utilities.config import DUMMY_PAY_URL, SITE_CREDENTIALS


class LoginPage(BasePage):

    PATH = DUMMY_PAY_URL

    def __init__(self, page: Page) -> None:
        super().__init__(page)

    def fillBadCredentialsAndLogIn(self) -> None:
        self.loginEmailInput.fill(SITE_CREDENTIALS["username"])
        self.loginPasswordInput.fill(SITE_CREDENTIALS["bad_password"])
        self.loginSignInButton.click()

    @property
    def alert(self) -> Locator:
        return self.page.get_by_role("alert")

    @property
    def alertMessage(self) -> Locator:
        return self.page.get_by_text("Incorrect email or password.")
    