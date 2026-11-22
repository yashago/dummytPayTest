import os
from dotenv import load_dotenv

DUMMY_PAY_URL = 'https://dummypay.vercel.app'

load_dotenv(override=True)

SITE_CREDENTIALS: dict[str, str] = {
    "username": os.environ["BACKEND_EMAIL"],
    "password": os.environ["DUMMY_PAY_PASSWORD"],
    "bad_password": os.environ["DUMMY_PAY_BAD_PASSWORD"],
}