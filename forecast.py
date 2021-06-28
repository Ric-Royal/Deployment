import numpy as np
import pickle
import pandas as pd
import streamlit as st 

from PIL import Image



pickle_in = open("model1.pkl","rb")
model=pickle.load(pickle_in)

#@app.route('/')
def welcome():
    return "Welcome All"

#@app.route('/predict',methods=["Get"])
def predict_imr(Year, IMR):
    
    """Let's predict the Infant Mortality Rate 
    This is using docstrings for specifications.
    ---
    parameters:  
      - name: variance
        in: query
        type: number
        required: true
      - name: skewness
        in: query
        type: number
        required: true
      - name: curtosis
        in: query
        type: number
        required: true
      - name: entropy
        in: query
        type: number
        required: true
    responses:
        200:
            description: The output values
        
    """
   
    prediction1=model.predict([[Year, ImR]])
    print(prediction1)
    return prediction1



def main():
    st.title("PMDA")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Bank Authenticator ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    Year = st.text_input("Year","Type Here")
    IMR = st.text_input("Infant Mortality Rate","Type Here")
    result=""
    if st.button("Predict"):
        result=predict_imr(Year, IMR)
    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Lets LEarn")
        st.text("Built with Streamlit")

if __name__=='__main__':
    main()