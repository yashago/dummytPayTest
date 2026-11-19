from playwright.sync_api import Page, Locator

from utilities.config import SITE_CREDENTIALS



class BasePage:
    PATH = "/"

    def __init__(self, page: Page) -> None:
        self.page = page

    def open(self) -> None:
        print(f'Opening: {self.PATH}')
        self.page.goto(self.PATH, wait_until="domcontentloaded")

    @property
    def loginEmailInput(self) -> Locator:
        return self.page.get_by_role("textbox", name="Email")

    @property
    def loginPasswordInput(self) -> Locator:
        return self.page.get_by_role("textbox", name="Password")

    @property
    def loginSignInButton(self) -> Locator:
        return self.page.get_by_role("button", name="Sign in")

    @property
    def accountButton(self) -> Locator:
        return self.page.get_by_role("button", name="Account menu:")

    @property
    def signOutButton(self) -> Locator:
        return self.page.get_by_role("menuitem", name="Sign out")

    def fillCredentialsAndLogIn(self) -> None:
        self.loginEmailInput.fill(SITE_CREDENTIALS["username"])
        self.loginPasswordInput.fill(SITE_CREDENTIALS["password"])
        self.loginSignInButton.click()
        self.page.wait_for_url(self.PATH)

    def clickOnAccountAndLogOut(self):
        self.accountButton.scroll_into_view_if_needed()
        self.accountButton.click()
        self.signOutButton.click()

    def navigateToPage(self) -> None:
        self.page.goto(self.PATH)