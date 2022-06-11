# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 02:20:31 2020

@author: Dipak Argade
"""

# -*- coding: utf-8 -*-
"""
Created on Sat June 11 11:05:04 2022

@author: Dipak Argade
"""

import numpy as np
import pickle
import pandas as pd
import streamlit as st 
from PIL import Image

pickle_in = open("sv.pkl","rb")
sv=pickle.load(pickle_in)  

def predict(Age,Sex,RestingBP,Cholesterol,FastingBS,MaxHR,ExerciseAngina,Oldpeak,ChestPainType_ATA,ChestPainType_NAP,ChestPainType_TA,RestingECG_Normal,RestingECG_ST,ST_Slope_Flat,ST_Slope_Up):
   
    prediction=sv.predict([[Age,Sex,RestingBP,Cholesterol,FastingBS,MaxHR,ExerciseAngina,Oldpeak, ChestPainType_ATA,ChestPainType_NAP,ChestPainType_TA,RestingECG_Normal,RestingECG_ST,ST_Slope_Flat,ST_Slope_Up]])
    print(prediction)
    return prediction



def main():
    html_temp = """
    <div style="background-color:blue;padding:10px">
    <h2 style="color:white;text-align:center;">Heart Disease Prediction </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    Age = st.number_input("Age")
    Sex = st.number_input("Sex")
    Cholesterol	 = st.number_input("Cholesterol")
    RestingBP	 = st.number_input("RestingBP")
    FastingBS	 = st.number_input("FastingBS")
    MaxHR	 = st.number_input("MaxHR")
    ExerciseAngina	 = st.number_input("ExerciseAngina")
    Oldpeak	 = st.number_input("Oldpeak")
    ChestPainType_ATA	 = st.sidebar.selectbox("ChestPainType_ATA_Yes=1_No=0",("0","1"))
    ChestPainType_NAP	 = st.sidebar.selectbox("ChestPainType_NAP_Yes=1_No=0",("0","1"))
    ChestPainType_TA	 = st.sidebar.selectbox("ChestPainType_TA_Yes=1_No=0",("0","1"))
    RestingECG_Normal	 = st.sidebar.selectbox("RestingECG_Normal_Yes=1_No=0",("0","1"))
    RestingECG_ST	 = st.sidebar.selectbox("RestingECG_ST_Yes=1_No=0",("0","1"))
    ST_Slope_Flat	 = st.sidebar.selectbox("ST_Slope_Flat_Yes=1_No=0",("0","1"))
    ST_Slope_Up	 = st.sidebar.selectbox("ST_Slope_Up_Yes=1_No=0",("0","1"))
    result=""
    if st.button("Predict"):
        result=predict(Age,Sex,RestingBP,Cholesterol,FastingBS,MaxHR,ExerciseAngina,Oldpeak,
            ChestPainType_ATA,ChestPainType_NAP,ChestPainType_TA,RestingECG_Normal,RestingECG_ST,ST_Slope_Flat,ST_Slope_Up)
        if result ==1:
            return st.header('Heart Disease predicted')
        else:
            return st.header('No Heart Disease')
if __name__=='__main__':
    main()
    
    
    