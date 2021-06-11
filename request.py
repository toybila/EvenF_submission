import requests
import json

data = {
        "requested": 50000.0,
        "loan_purpose": "baby",
        "credit": "fair",
        "annual_income": 60000,
        "apr": 29
        }


url = 'http://localhost:5000/predict_api'
#r = requests.post(url,json={'requested':500.0, 'loan_purpose': 'auto', 'credit': 'excellent','annual_income':60000, 'apr':29})
r=requests.post(url,json= data)
print(r.text)