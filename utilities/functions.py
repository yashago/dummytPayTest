import re
from typing import TypedDict


class CurrencyAmount(TypedDict):
    currency: str
    amount: float


def parse_amount(value: str) -> float:
    """Extract the numeric amount from text such as '₪12,900.00' or '−$30.87'."""
    match = re.search(r'([-−]?)\D*?([\d,]+(?:\.\d+)?)', value)
    if not match:
        raise ValueError(f"No amount found in: {value!r}")
    amount = float(match.group(2).replace(",", ""))
    return -amount if match.group(1) else amount


def parse_currency(value: str) -> CurrencyAmount:
    """Parse a total-balance text such as:

        ≈ €3,594.20
        4 wallets · shown in EUR

    into {"currency": "EUR", "amount": 3594.20}.
    """
    amount_match = re.search(r'([\d,]+(?:\.\d+)?)', value)
    currency_match = re.search(r'shown in\s+([A-Z]{3})', value)

    if not amount_match or not currency_match:
        raise ValueError(f"Invalid currency format: {value!r}")

    return {
        "currency": currency_match.group(1),
        "amount": float(amount_match.group(1).replace(",", "")),
    }
