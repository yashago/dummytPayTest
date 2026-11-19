import pytest
from playwright.sync_api import expect

from pages.LoginPage import LoginPage
from utilities.config import DUMMY_PAY_URL


@pytest.mark.smoke
def test_login_flow(login_page: LoginPage) -> None:
    checkPageComponentsAreVisible(login_page)
    login_page.fillCredentialsAndLogIn()
    expect(login_page.page).to_have_url(f"{DUMMY_PAY_URL}/")
    login_page.accountButton.scroll_into_view_if_needed()
    login_page.accountButton.click()
    expect(login_page.signOutButton).to_be_visible()
    login_page.signOutButton.click()
    print(f"Back to: {login_page.page.url}")
    expect(login_page.page).to_have_url(f"{DUMMY_PAY_URL}/login")
    checkPageComponentsAreVisible(login_page)


@pytest.mark.smoke
def test_bad_login_flow(login_page: LoginPage) -> None:
    checkPageComponentsAreVisible(login_page)
    login_page.fillBadCredentialsAndLogIn()
    expect(login_page.alert).to_be_visible()
    expect(login_page.alertMessage).to_be_visible()

def checkPageComponentsAreVisible(login_page: LoginPage) -> None:
    expect(login_page.loginEmailInput).to_be_visible()
    expect(login_page.loginPasswordInput).to_be_visible()
    expect(login_page.loginSignInButton).to_be_visible()