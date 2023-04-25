import streamlit as st 
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

def load_data():
    gold_data = pd.read_csv('gld_price_data.csv')
    return gold_data

gold_data=load_data()

def show_data():
    st.title("Gold Price Dataset")
    st.dataframe(data=gold_data)