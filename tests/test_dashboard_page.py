import pytest

from pages.DashboardPage import DashboardPage


@pytest.mark.smoke
def test_balance(dashboard) -> None:
    dashboardPage = DashboardPage(dashboard.page)

    total = dashboardPage.get_total_balance()
    preferred_currency = dashboardPage.get_preferred_curency()
    wallets = dashboardPage.get_wallet_balances()
    # Rates on the card are 1 preferred currency -> X target currency.
    rates = dashboardPage.get_exchange_rates()
    rates[preferred_currency] = 1.0

    print(f"total: {total}")
    print(f"preferred_currency: {preferred_currency}")
    print(f"wallets: {wallets}")
    print(f"rates: {rates}")

    total_balance_in_preferred_currency = 0
    for key in wallets:
        total_balance_in_preferred_currency += wallets[key] / rates[key]
    total_balance_in_preferred_currency = round(total_balance_in_preferred_currency, 2)
    print(f"total_balance_in_preferred_currency: {total_balance_in_preferred_currency}")
    assert total["amount"] == total_balance_in_preferred_currency