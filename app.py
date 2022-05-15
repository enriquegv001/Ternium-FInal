import streamlit as st
from predict_page import show_predict_page
from DBpredict_page import show_DBpredict_page
from explore_page import show_explore_page


page = st.sidebar.selectbox("Explore Or Predict", ("Predecir por candidato", "Predecir por base de datos", "Análisis descriptivo"))

if page == "Predecir por candidato":
    show_predict_page()
    
elif page == 'Predecir por base de datos':
    show_DBpredict_page()
    
else:
    show_explore_page()    