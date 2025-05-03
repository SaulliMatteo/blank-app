# -*- coding: utf-8 -*-
"""
Created on Tue Apr 29 01:43:29 2025

@author: Matteo
"""

import pickle
import streamlit as st
import numpy as np
from streamlit_option_menu import option_menu

diabetes_model = pickle.load(open('webApp_heroklu/diatabes_pred_trained.sav', 'rb'))
heart_model = pickle.load(open('webApp_heroklu/heart_deseas_trained.sav', 'rb'))
parkinson_model = pickle.load(open('webApp_heroklu/parkinson_trained.sav', 'rb'))

if __name__ == "__main__":
    with st.sidebar:
        selected = option_menu(
            'Multiple Disease Prediction System',
            [
                'Diabetes Prediction',
                'Heart Disease Prediction',
                'Parkinson Prediction'
            ],
            icons=['activity', 'heart', 'person'],
            default_index=0
        )
        
    if(selected == 'Diabetes Prediction'):
        st.title('Diabetes Predition')
        col1, col2, col3 = st.columns(3)
        with col1:
            pregnancies = st.number_input("Pregnancies")
            
        with col2:
            glucose = st.number_input("Glucose")
            
        with col3:
            bloodPressure = st.number_input("BloodPressure")
            
        with col1:
            skinThickness = st.number_input("SkinThickness")
            
        with col2:
            insulin = st.number_input("Insulin")
            
        with col3:
            bmi = st.number_input("BMI")
                
        with col1:
            diabetesPedigreeFunction = st.number_input("DiabetesPedigreeFunction")
            
        with col2:
            age = st.number_input("Age")

        diagnosis = ''
        
        if st.button('test result'):
            arr = np.asarray([pregnancies,glucose,bloodPressure,skinThickness,insulin,bmi,diabetesPedigreeFunction,age])
            arr = arr.reshape(1, -1)
            pred = diabetes_model.predict(arr)
            if pred[0]:
                diagnosis = 'diabetic'
            else:
                diagnosis = 'non diabetic'
            st.success(diagnosis)
            
    if(selected == 'Heart Disease Prediction'):
        st.title('Heart Disease Prediction')
        col1, col2, col3 = st.columns(3)
        
        with col1:
            age = st.number_input('Age')
            
        with col2:
            sex = st.number_input('Sex')
            
        with col3:
            cp = st.number_input('Chest Pain types')
            
        with col1:
            trestbps = st.number_input('Resting Blood Pressure')
            
        with col2:
            chol = st.number_input('Serum Cholestoral in mg/dl')
            
        with col3:
            fbs = st.number_input('Fasting Blood Sugar > 120 mg/dl')
            
        with col1:
            restecg = st.number_input('Resting Electrocardiographic results')
            
        with col2:
            thalach = st.number_input('Maximum Heart Rate achieved')
            
        with col3:
            exang = st.number_input('Exercise Induced Angina')
            
        with col1:
            oldpeak = st.number_input('ST depression induced by exercise')
            
        with col2:
            slope = st.number_input('Slope of the peak exercise ST segment')
            
        with col3:
            ca = st.number_input('Major vessels colored by flourosopy')
            
        with col1:
            thal = st.number_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')

        diagnosis = ''
        
        if st.button('test result'):
            arr = np.asarray([age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal])
            arr = arr.reshape(1, -1)
            pred = heart_model.predict(arr)
            if pred[0]:
                diagnosis = 'risk of heart disease'
            else:
                diagnosis = 'no risk chill'
            st.success(diagnosis)
            
    if(selected == 'Parkinson Prediction'):
        st.title('Parkinson Prediction')
        col1, col2, col3, col4, col5 = st.columns(5)  
        
        with col1:
            fo = st.number_input('MDVP:Fo(Hz)')
            
        with col2:
            fhi = st.number_input('MDVP:Fhi(Hz)')
            
        with col3:
            flo = st.number_input('MDVP:Flo(Hz)')
            
        with col4:
            Jitter_percent = st.number_input('MDVP:Jitter(%)')
            
        with col5:
            Jitter_Abs = st.number_input('MDVP:Jitter(Abs)')
            
        with col1:
            RAP = st.number_input('MDVP:RAP')
            
        with col2:
            PPQ = st.number_input('MDVP:PPQ')
            
        with col3:
            DDP = st.number_input('Jitter:DDP')
            
        with col4:
            Shimmer = st.number_input('MDVP:Shimmer')

        with col5:
            Shimmer_dB = st.number_input('MDVP:Shimmer(dB)')
            
        with col1:
            APQ3 = st.number_input('Shimmer:APQ3')
            
        with col2:
            APQ5 = st.number_input('Shimmer:APQ5')
            
        with col3:
            APQ = st.number_input('MDVP:APQ')
            
        with col4:
            DDA = st.number_input('Shimmer:DDA')

        with col5:
            NHR = st.number_input('NHR')
            
        with col1:
            HNR = st.number_input('HNR')
            
        with col2:
            RPDE = st.number_input('RPDE')
            
        with col3:
            DFA = st.number_input('DFA')
            
        with col4:
            spread1 = st.number_input('spread1')
            
        with col5:
            spread2 = st.number_input('spread2')
            
        with col1:
            D2 = st.number_input('D2')
            
        with col2:
            PPE = st.number_input('PPE')

        diagnosis = ''
        
        if st.button('test result'):
            arr = np.asarray([fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE])
            arr = arr.reshape(1, -1)
            pred = parkinson_model.predict(arr)
            if pred[0]:
                diagnosis = 'yea parkinson'
            else:
                diagnosis = 'chill no parkinson ur good'
            st.success(diagnosis)