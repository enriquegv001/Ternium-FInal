import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import pickle


def load_model():
    with open('model.pkl' , 'rb') as f:
        model = pickle.load(f)
    return model

model = load_model()

global x
  
def load_data():    
    uploaded_file = st.file_uploader("Choose a file")
    #if uploaded_file is not None:
    x = pd.read_csv(uploaded_file)
        
    ID = x.iloc[:, 0]
    ID = np.array(ID)

        #x = x.drop(x.columns[1], axis = 1)
    x = x.drop(x.columns[0], axis = 1)
        
   # else:
    st.write("""No se ha ingresado el archivo""")
    #return x
    #x = pd.read_csv("ejemplo_Ternium.csv")
        # MANEJAMOS CSV
        
    return x, ID





def show_DBpredict_page():
    
    image = Image.open('Ternium.png')
    st.image(image, width = 150)
    
    st.title("Predicción de base de datos de ingresados:")
    
    st.write("""Ingresa la base de datos con todos los registros (el error se quitará después de ello):""")
    
    
    x, ID = load_data()
    # EMPLEAR MODELO
        
    result = model.predict(x)
        
    result_df = pd.DataFrame({'ID':ID, 'Ingresado':result})
       
    result_df = result_df.replace({'Ingresado': 1}, "Si")
    result_df = result_df.replace({'Ingresado': 0}, "No")
        
    result_si = result_df[result_df["Ingresado"] == "Si"]
    result_no = result_df[result_df["Ingresado"] == "No"]

    st.dataframe(result_si)
        
    csv = result_si.to_csv(index=False).encode('utf-8')
    
    st.write("""No se ha ingresado el archivo""")    
    
    
    if csv is not None:
        st.write(csv)
        st.download_button(
            "Press to Download",
            csv,
            "file.csv",
            "text/csv",
            key='download-csv'
            )
    else:
        st.write('')
    