# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 02:20:31 2020

@author: DA 
"""

# -*- coding: utf-8 -*-
"""
Created on 12/08/2022

@Created by: DA
"""

import numpy as np
import pickle
import pandas as pd
from xgboost import XGBClassifier
import streamlit as st 
from PIL import Image

pickle_in = open("rfc.pkl","rb")
rfc=pickle.load(pickle_in)  

pickle_in2 = open("rfc2.pkl","rb")
rfc2=pickle.load(pickle_in2) 



def main():
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Machine Predictive Maintenance </h2>
    </div>
    """
     
    
    st.markdown(html_temp,unsafe_allow_html=True)

    Type = st.selectbox("Type",("M","L","H"))
    if Type == 'M':
        Type_L = 0
        Type_M = 1
        
    elif Type == 'L':
        Type_L = 1
        Type_M = 0

    else:
        Type_L = 0
        Type_M = 0

    Air_temperature_K = st.number_input("Air temperature(K)")

    Process_temperature_K = st.number_input("Process temperature(K)")

    Rotational_speed_rpm = st.number_input("Rotational speed(rpm)")

    Torque_Nm = st.number_input("Torque(Nm)")

    Tool_wear_min = st.number_input("Tool wear(min)")


    
    result=""
    
    if st.button("Predict the occurance of failure"):
        result=rfc.predict([[Air_temperature_K,Process_temperature_K,Rotational_speed_rpm,Torque_Nm,Tool_wear_min,Type_L,Type_M]])
        if result ==1:
            return st.header('Machine Failure is predicted')
        else:
            return st.header('No Machine Failure')

    result2=""
    
    if st.button("Predict the type of failure"):
        result2=rfc2.predict([[Air_temperature_K,Process_temperature_K,Rotational_speed_rpm,Torque_Nm,Tool_wear_min,Type_L,Type_M]])
        return st.header(result2)

if __name__=='__main__':
    main()
    
    
    