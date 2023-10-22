import pandas as pd
import streamlit as st
import pickle
import numpy as np
import sklearn
from PIL import Image
from sklearn.ensemble import GradientBoostingClassifier
import joblib

def load_model():
    with open('model.pkl', 'rb') as file:
        data = pickle.load(file)
        
    return data
        

data = load_model()

@st.cache_data(experimental_allow_widgets=True)
def show_predict_page():
        
    image = Image.open('Ternium.png')
    st.image(image, width = 150)
    
    st.title("Predicción de Reclutamiento")
    
    st.write("""### Selecciona las características del candidato a evaluar""")
    
    st.write("""##### Operaciones-Calidad, MTTO-DIMA, Comercial-Planeamiento, DIGI-SC, Resto-Soft:\n
            .       Highly Recommend = 2\n
            Recommend = 1\n
            Do Not Recommend = 0\n""")
    OperacionCalidad = (0,1,2)
    OperacionCalidad = st.selectbox("Operaciones-Calidad ", OperacionCalidad)

    MTTO = (0,1,2)
    MTTO = st.selectbox("MTTO-DIMA", MTTO)
    
    Comercial = (0,1,2)
    Comercial = st.selectbox("Comercial-Planeamiento", Comercial)
    
    DIGI = (0,1,2)
    DIGI = st.selectbox("DIGI-SC", DIGI)

    RESTO = (0,1,2)
    RESTO = st.selectbox("Resto-Soft", RESTO)
    
    st.write("""##### Ingles:\n
             .        A1 = 2\n
             A2 = 3\n
             B1 = 4\n
             B2 = 5\n
             C1 = 6\n
             C2 = 7\n""")
    Ingles = (0,1,2,3,4,5,6,7)
    Ingles = st.selectbox("Ingles", Ingles)
    
    ok = st.button("Ingreso")
    if ok:
        X = pd.Series([OperacionCalidad, MTTO, Comercial, DIGI, RESTO, Ingles])      
        
        ingreso = data.predict([X])
        st.subheader(f"""¿El candidato ingresa?:\n
                     (Si = 1; No = 0)\n
                     {ingreso[0]}""")
        