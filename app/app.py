import streamlit as stl
from predict import show_predict
from explore import show_explore

ok = stl.sidebar.selectbox("Eplore And Predict Mark" , ("Predict" , "Explore"))
if ok == "Predict":
    show_predict()
else: 
    show_explore()