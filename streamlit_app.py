# -*- coding: utf-8 -*-
"""
Created on Tue Apr 29 01:43:29 2025

@author: Matteo
"""

import numpy as np
import pickle
import streamlit as st
try:
    model = pickle.load(open('diatabes_pred_trained.sav', 'rb'))
except:
    st.error("path non trovato")

def diatabes_pred(input_data):

    data = np.asarray(input_data)
    data = data.reshape(1, -1)
    pred = model.predict(data)
    
    if(pred[0]):
        return 'diabetic'
    else:
        return 'non diabetic'
    
def main():
    st.title("diabetes pred Web App")
    
    # Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age,Outcome
    Pregnancies = st.number_input('number of Pregnancies')
    Glucose = st.number_input('number of Glucose')
    BloodPressure = st.number_input('number of BloodPressure')
    SkinThickness = st.number_input('number of SkinThickness')
    Insulin = st.number_input('number of Insulin')
    BMI = st.number_input('number of BMI')
    DiabetesPedigreeFunction = st.number_input('number of DiabetesPedigreeFunction')
    Age = st.number_input('number of Age')
    
    diagnosis = ''
    datas = [Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]

    if st.button('diabates result'):
        diagnosis = diatabes_pred(datas)
    
    st.success(diagnosis)

if __name__ == "__main__":
    main()