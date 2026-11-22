from enum import StrEnum

CONSTS: dict[str, str] = {
    "alertMessage": "Incorrect email or password."
}

class CURENCY(StrEnum):
    USD = 'USD'
    ILS = 'ILS'
    GBP = 'GBP'
    EUR = 'EUR'

class TABLES(StrEnum):
    WALLETS = 'wallets'

class FUNCTIONS(StrEnum):
    LOOKUP_RECEPIENT = "lookup_recipient"
    CREATE_TRANSFER_QUOTE = "create_transfer_quote"
    WALLET_SUMMARY = "get_wallet_summary"