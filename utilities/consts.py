from enum import Enum


CONSTS: dict[str, str] = {
    "alertMessage": "Incorrect email or password."
}

class CURENCY(Enum):
    USD = '$'
    ILS = '₪'
    GBP = '£'
    EUR = '€'