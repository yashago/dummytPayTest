from utilities.backend.backend_base import table, rpc
from utilities.consts import FUNCTIONS, TABLES

__all__ = ["get_wallet_summary", "get_all_wallets"]

def get_wallet_summary():
    wallet_summary = rpc(FUNCTIONS.WALLET_SUMMARY)
    return wallet_summary

def get_all_wallets():
    r = table(TABLES.WALLETS, {"select": "id,currency,balance_minor,created_at,updated_at",
                "order": "created_at.asc"})
    return r.json()

if __name__ == "__main__":
    print(get_wallet_summary())
    print(get_all_wallets())