import re
from playwright.sync_api import Locator, expect
from pages.BasePage import BasePage
from utilities.config import DUMMY_PAY_URL
from utilities.functions import CurrencyAmount, parse_amount, parse_currency


class DashboardPage(BasePage):

    PATH = DUMMY_PAY_URL

    def __init__(self, page):
        super().__init__(page)
        self.total_balance = self.page.get_by_test_id("total-balance")

    @property
    def balance(self):
        return 'abc'

    @property
    def total_balance_component(self) -> Locator:
        return self.total_balance

    def get_total_balance(self) -> CurrencyAmount:
        # The balance renders asynchronously; wait until the real content is in place.
        expect(self.total_balance).to_contain_text(re.compile(r"shown in [A-Z]{3}"))
        return parse_currency(self.total_balance.inner_text())

    @property
    def wallets(self) -> Locator:
        return self.page.get_by_test_id(re.compile(r"^wallet-"))

    @property
    def preferred_wallet(self) -> Locator:
        return self.wallets.filter(has=self.page.get_by_text("Preferred", exact=True))

    def get_preferred_curency(self) -> str:
        test_id = self.preferred_wallet.get_attribute("data-testid") or ""
        return test_id.removeprefix("wallet-")

    def get_wallet_balances(self) -> dict[str, float]:
        """Return {currency_code: available_balance} for every wallet card."""
        expect(self.wallets.first).to_contain_text("Available balance")
        balances: dict[str, float] = {}
        for wallet in self.wallets.all():
            currency = (wallet.get_attribute("data-testid") or "").removeprefix("wallet-")
            amount_text = wallet.inner_text().split("Available balance", 1)[1]
            balances[currency] = parse_amount(amount_text)
        return balances

    # Matches "1 EUR → GBP\n0.834065" and captures ("GBP", "0.834065").
    RATE_LINE = re.compile(r"1\s+[A-Z]{3}\W+([A-Z]{3})\s+(\d+(?:\.\d+)?)")

    def get_exchange_rates(self) -> dict[str, float]:
        """Return {target_currency: rate} from the Exchange rates card (1 base -> target)."""
        rates_card = self.page.get_by_test_id("rates-card")
        # Rates render asynchronously; wait until at least one rate line is present.
        expect(rates_card).to_contain_text(self.RATE_LINE, use_inner_text=True)
        text = rates_card.inner_text()
        data_to_return = {currency: float(rate) for currency, rate in self.RATE_LINE.findall(text)}
        return data_to_return

    def get_exchange_rate(self, from_currency: str, to_currency: str) -> float:
        """Rate shown in the Exchange rates card: 1 from_currency -> to_currency."""
        if from_currency == to_currency:
            return 1.0
        return self.get_exchange_rates()[to_currency]
