import streamlit as st 
import pandas as pd 
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle
import numpy as np

loaded_model=pickle.load(open('regmodel','rb'))
second_loaded_model=pickle.load(open('Random_Forest.pkl','rb'))


def load_data():
    gold_data = pd.read_csv('gld_price_data.csv')
    return gold_data

gold_data=load_data()

def split(df):
    X=df[['SPX' ,'USO','SLV','EUR/USD']]
    Y=df['GLD']
    X_train , X_test , Y_train ,Y_test=train_test_split(X,Y,test_size=0.2,random_state=20)
    return X_train , X_test , Y_train , Y_test

X_train , X_test , Y_train , Y_test=split(gold_data)

def gold_prediction(input_data1 , input_data2):
    # Changing the input array as numpy array 
    prediction=loaded_model.predict(X_test)
    return prediction

prediction=gold_prediction(X_train , Y_train)

def gold_prediction_using_Regressor(input_data1 , input_data2):
  
    prediction1=second_loaded_model.predict(X_test)
    return prediction1

prediction1 = gold_prediction_using_Regressor(X_train , Y_train)

def show_explore_page():
    st.title("EXPLORE THE CHARTS")
    fig,ax=plt.subplots(nrows=2 , ncols=2 ,figsize=(15,10))
    
    ax[0,0].scatter(gold_data.SPX , gold_data.GLD)
    ax[0,0].set_xlabel("SPX INDEX")
    ax[0,0].set_ylabel("GLD PRICE")
    ax[0,0].set_title("SPX INDEX VS GLD PRICE ") 
    
    ax[0,1].scatter(gold_data.USO , gold_data.GLD)
    ax[0,1].set_xlabel("United State Oil Price")
    ax[0,1].set_ylabel("GLD PRICE")
    ax[0,1].set_title("United State Oil Price Vs GLD Price")
    

    ax[1,0].scatter(Y_test , prediction)
    ax[1,0].set_xlabel("Actual Data")
    ax[1,0].set_ylabel("Prediction")
    ax[1,0].set_title("Actual Data Vs Prediction (Linear Reg)")

    ax[1,1].scatter(Y_test , prediction1)
    ax[1,1].set_xlabel("Actual Data")
    ax[1,1].set_ylabel("Prediction")
    ax[1,1].set_title("Actual Data Vs Prediction (Randoom Forest Regressor)")
    
    plt.subplots_adjust(hspace=0.5)
    st.pyplot(fig)
    
    