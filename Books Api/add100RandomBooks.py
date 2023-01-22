#!/usr/bin/env python3

#PREPARE

import requests
import json
from faker import Faker

APIHOST = "http://library.demo.local"
LOGIN="cisco"
PASSWORD="Cisco123!"
API_KEY = "cisco|YWOGnz6zXvuJ3gHRRCTLTwzOS-SxNO1K1Gbr2DtFxOU"

def getAuthToken():
 authCreds = (LOGIN, PASSWORD)
 r = requests.post(
    f"{APIHOST}/api/v1/loginViaBasic",
    auth = authCreds
 )
 if r.status_code == 200:
    return r.json()["token"]
 else:
    raise Exception(f"Status code {r.status_code} and text {r.text}, while trying
        to Auth.")

