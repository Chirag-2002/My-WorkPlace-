import streamlit as st
import pickle 
import numpy as np

loaded_model=pickle.load(open('regmodel','rb'))
second_loaded_model=pickle.load(open('Random_Forest.pkl','rb'))

def gold_prediction(input_data):
    # Changing the input array as numpy array 
    input_data_as_numpy_array=np.asarray(input_data)
    input_data_reshaped=input_data_as_numpy_array.reshape(1,-1)
    prediction=loaded_model.predict(input_data_reshaped)
    return prediction

def gold_prediction_using_Regressor(input_data):
    # Changing the input array as numpy array 
    input_data_as_numpy_array=np.asarray(input_data)
    input_data_reshaped=input_data_as_numpy_array.reshape(1,-1)
    prediction=second_loaded_model.predict(input_data_reshaped)
    return prediction


def show_predict_page():
    st.title("GOLD PRICE PREDICTION")
    st.write("""### We need some information to predict the gold price""")
    SPX=st.number_input("Enter the SPX index value",value=0)
    USO=st.number_input("Enter the price of United States Oil Price :",value=0)
    SLV=st.number_input("Enter the closing price of Silver",value=0)
    Dollar =st.number_input("Enter the price of EUR/USD Dollar" ,value=0)
    price = ''
    if st.button("Linear Regression Predict") :
        price=gold_prediction([SPX,USO,SLV,Dollar])
    elif st.button("Random Forest Regressor"):
          price=gold_prediction([SPX,USO,SLV,Dollar])
    
    st.success(st.subheader(f"The estimated gold price is ${price}"))
    
    
    
    