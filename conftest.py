from collections.abc import Generator
from typing import Any

import pytest
from playwright.sync_api import Browser, Page

from pages.DashboardPage import DashboardPage
from pages.LoginPage import LoginPage
from pages.PaymentCardsPage import PaymentCardsPage


# @pytest.fixture(scope='module')
# def module_page(browser: Browser, browser_context_args: dict[str, Any]) -> Generator[Page, None, None]:
#     # pytest-playwright's `page` is function-scoped, so build a page that
#     # lives for the whole module from the session-scoped `browser`.
#     context = browser.new_context(**browser_context_args)
#     page = context.new_page()
#     yield page
#     context.close()


@pytest.fixture(scope='function')
def login_page(page: Page) -> LoginPage:
    login = LoginPage(page)
    login.open()
    return login

@pytest.fixture(scope='function')
def dummy_pay_pages(page: Page):
    login = LoginPage(page)
    login.open()
    login.fillCredentialsAndLogIn()
    return login

@pytest.fixture(scope='function')
def payment_cards(dummy_pay_pages):
    payment_cards_page = PaymentCardsPage(dummy_pay_pages.page)
    payment_cards_page.navigateToPage()
    return payment_cards_page