import uuid

from utilities.backend.backend_base import rpc
from utilities.consts import CURENCY, FUNCTIONS


__all__ = ["send_funds"]

def send_funds(user_mail, amount = 10, currency = CURENCY.USD):
    recipient = rpc(FUNCTIONS.LOOKUP_RECEPIENT, {"p_email": user_mail})
    quote = rpc(FUNCTIONS.CREATE_TRANSFER_QUOTE, {
        "p_recipient_id": recipient[0].get("user_id"),   # check the exact return shape
        "p_sending_currency": currency,         # ILS | USD | EUR | GBP
        "p_amount_minor": amount,              # 10.00
        "p_input_side": "send",              # send | receive
    })
    response = rpc("execute_transfer", {
        "p_quote_id": quote.get("quote_id"),
        "p_idempotency_key": str(uuid.uuid4()),
    })
    return response

if __name__ == "__main__":
    print(send_funds("mirka.g@gmail.com"))