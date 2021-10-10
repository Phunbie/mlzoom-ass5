# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 21:19:51 2021

@author: FBI
"""
import pickle
from flask import Flask, request, jsonify

model = pickle.load(open('model1.bin','rb'))
dictv = pickle.load(open('dv.bin','rb'))




def predict_single(customer, dv, model):
  X = dv.transform([customer])  ## apply the one-hot encoding feature to the customer data 
  y_pred = model.predict_proba(X)[:, 1]
  return y_pred[0]


app = Flask('predict')


@app.route('/predict', methods=['POST'])  ## in order to send the customer information we need to post its data.
def predict():
    customer = request.get_json()  ## web services work best with json frame, So after the user post its data in json format we need to access the body of json.
    
    prediction = predict_single(customer, dictv, model)
    
    result = {
        'churn_probability': float(prediction), ## we need to conver numpy data into python data in flask framework
    }
    
    return jsonify(result)  ## send back the data in json format to the user

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9696)

