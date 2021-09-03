import requests
from datetime import date
import time

URL = 'http://wsify:4040'

while True:
    today = date.today()
    resp = requests.post(URL + '/publish' , json={
        "payload": "Test by " + str(today),
        "channel": "testchan"
    })
    time.sleep(3)

