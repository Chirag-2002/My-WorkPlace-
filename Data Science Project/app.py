import streamlit as st 
from predict import show_predict_page
from explore_page import show_explore_page
from Reveal_Data import show_data

page=st.sidebar.selectbox("Explore or Predict or Reveal Data",("predict","explore_page","Reveal_Data"))

if page== "predict":
    show_predict_page()
elif page=="Reveal_Data":
    show_data()
else:
    show_explore_page()
    