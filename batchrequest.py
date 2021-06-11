import requests
import json

Data5 = [{
        "requested": 50000.0,
        "loan_purpose": "baby",
        "credit": "fair",
        "annual_income": 60000,
        "apr": 29
        }, {
        "requested": 30000.0,
        "loan_purpose": "auto",
        "credit": "good",
        "annual_income": 60000,
        "apr": 29
        }, {
        "requested": 500.0,
        "loan_purpose": "business",
        "credit": "excellent" ,
        "annual_income": 100000,
        "apr": 29
         }]

url = 'http://localhost:5000/predict_multiple_api'
r = requests.post(url,json= Data5)

print(r.text)