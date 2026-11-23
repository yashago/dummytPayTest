import os

import requests
from dotenv import load_dotenv

load_dotenv()

__all__ = ["table", "rpc"]


URL = "https://vtimmqlnyoyxiwczfdwf.supabase.co"
ANON_KEY = os.environ["SUPABASE_ANON_KEY"]  # publishable key only
EMAIL = os.environ["BACKEND_EMAIL"]
PASSWORD = os.environ["BACKEND_PASSWORD"]

def sign_in(email, password):
    r = requests.post(
        f"{URL}/auth/v1/token?grant_type=password",
        headers={"apikey": ANON_KEY},
        json={"email": email, "password": password},
    )
    r.raise_for_status()
    return r.json().get("access_token")  # access_token, refresh_token, expires_in

def rpc(fn, params=None):    
    token = sign_in(EMAIL, PASSWORD)
    # token = session.get("access_token")
    r = requests.post(
        f"{URL}/rest/v1/rpc/{fn}",
        headers={"apikey": ANON_KEY, "Authorization": f"Bearer {token}"},
        json=params or {},
    )
    if not r.ok:
        raise RuntimeError(f"{fn}: {r.status_code} {r.text}")
    return r.json()

def table(table_name, params = None):
    session = sign_in(EMAIL, PASSWORD)
    token = session.get("access_token")
    table_data = requests.get(
        f"{URL}/rest/v1/{table_name}",
        headers={"apikey": ANON_KEY, "Authorization": f"Bearer {token}"},
        params=params,
    )
    table_data.raise_for_status()
    return table_data