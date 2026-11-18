import os
from dotenv import load_dotenv

DUMMY_PAY_URL = 'https://dummypay.vercel.app/'

load_dotenv()

SITE_CREDENTIALS: dict[str, str] = {
    "username": os.environ["DUMMY_PAY_USERNAME"],
    "password": os.environ["DUMMY_PAY_PASSWORD"],
    "bad_password": os.environ["DUMMY_PAY_BAD_PASSWORD"],
}