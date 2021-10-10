# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 13:03:07 2021

@author: FBI
"""

import pickle

model = pickle.load(open('model1.bin','rb'))
dictv = pickle.load(open('dv.bin','rb'))



def predict_single(customer, dv, model):
  X = dv.transform([customer])  ## apply the one-hot encoding feature to the customer data 
  y_pred = model.predict_proba(X)[:, 1]
  return y_pred[0]

customer = {"contract": "two_year", "tenure": 12, "monthlycharges": 19.7}

X = predict_single(customer,dictv,model)

print('ans',X)

