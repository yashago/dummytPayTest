import pytest
from playwright.sync_api import expect

from pages.DashboardPage import DashboardPage
from utilities.config import DUMMY_PAY_URL


@pytest.mark.smoke
def test_balance(dummy_pay_pages) -> None:
    dashboardPage = dummy_pay_pages
    pass