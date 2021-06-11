import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template
import pickle
import os
import json

app = Flask(__name__)
predictions_path = os.getenv("PREDICTIONS_PATH", "app/predictions.pkl")
model = pickle.load(open(predictions_path, 'rb'))

loan_purpose_dict = {'auto': 0, 'auto_purchase': 1, 'auto_refinance': 2, 'baby': 3, 'boat': 4, 'business': 5, 'car_repair': 6, 'cosmetic': 7, 'credit_card_refi': 8, 'debt_consolidation': 9, 'emergency': 10, 'green': 11, 'home_improvement': 12, 'home_purchase': 13, 'household_expenses': 14, 'large_purchases': 15, 'life_event': 16, 'medical_dental': 17, 'motorcycle': 18, 'moving_relocation': 19, 'other': 20, 'special_occasion': 21, 'student_loan': 22, 'student_loan_refi': 23, 'taxes': 24, 'unknown': 25, 'vacation': 26, 'wedding': 27}

credit_dict = {'excellent': 0, 'fair': 1, 'good': 2, 'limited': 3, 'poor': 4, 'unknown': 5}

@app.route('/')
def index():
    return "clicks inference system"



@app.route('/predict_api',methods=['POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''
    data = request.get_json(force=True)
    requested = float(data['requested'])
    loan_purpose = str(data['loan_purpose'])
    credit = str(data['credit'])
    annual_income = float(data['annual_income'])
    apr = float(data['apr'])

    if loan_purpose in loan_purpose_dict:
        loan_purpose = loan_purpose_dict[loan_purpose]
    else:
        loan_purpose = loan_purpose_dict['other']
    
    if credit in credit_dict:
        credit = credit_dict[credit]
    else:
        credit = credit_dict['unknown']


    prediction = model.predict_proba([[requested, loan_purpose,credit, annual_income, apr]])

    output = prediction[0][1]

    return 'Probability_of_click:'+ str(output)

@app.route('/predict_multiple_api',methods=['POST'])
def predict_multiple_api():
    '''
        For batch API calls
    '''

    json_ = request.get_json()
    

    #test =  json.loads(json_)

    for i in json_ :
        if i['loan_purpose'] in loan_purpose_dict:
            i['loan_purpose'] = loan_purpose_dict[i['loan_purpose']]
        else:
            i['loan_purpose'] = loan_purpose_dict['other']
    
    for i in json_:
        if i['credit'] in credit_dict:
            i['credit'] = credit_dict[i['credit']]
        else:
            i['credit'] = credit_dict['unknown']
    

    
    query = pd.DataFrame(json_)

    prediction = model.predict_proba(query)

    output = list(prediction[:,1])
    
    return 'Probability_of_click:'+ str(output)




if __name__ == "__main__":
    app.run(host ='0.0.0.0',debug=True)