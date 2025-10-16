import nasdaqdatalink
import os
import pandas as pd

try:
    # For Python 3.0 and later
    from urllib.request import urlopen
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen

import certifi
import json

def get_jsonparsed_data(url):
    response = urlopen(url, cafile=certifi.where())
    data = response.read().decode("utf-8")
    return json.loads(data)

url = ("https://financialmodelingprep.com/stable/quote?symbol=HGUSD&apikey=6ka7JK8HfuFq3v8UAh7POM6xqhBumObx")
print(get_jsonparsed_data(url))

