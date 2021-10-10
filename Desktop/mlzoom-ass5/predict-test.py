# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 22:09:02 2021

@author: FBI
"""

customer = {"contract": "two_year", "tenure": 1, "monthlycharges": 10}
import requests ## to use the POST method we use a library named requests
url = 'http://localhost:9696/predict' ## this is the route we made for prediction
response = requests.post(url, json=customer).json() ## post the customer information in json format
print(response)