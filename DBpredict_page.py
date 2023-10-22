import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import pickle

class DBpredict:
    def __init__(self, model, load_data, image):
        self.model = model
        self.load_data = load_data
        self.image = image

    #@st.cache_data(experimental_allow_widgets=True)
    def show_DBpredict_page(self):
        # page visualization 
        #image = Image.open('Ternium.png')
        st.image(self.image, width = 150)
        st.title("Predicción de base de datos de ingresados:")
        st.write("""Ingresa la base de datos con todos los registros:""")
        
        # load data
        data = self.load_data('load_file')
        if data is not None:
            # predictions
            x, ID = data[0], data[1]
            result = self.model.predict(x)
            
            # post processing
            result_df = pd.DataFrame({'ID':ID, 'Ingresado':result})
            result_df = result_df.replace({'Ingresado': 1}, "Si")
            result_df = result_df.replace({'Ingresado': 0}, "No")
            result_si = result_df[result_df["Ingresado"] == "Si"]
            result_no = result_df[result_df["Ingresado"] == "No"]  # this is not being used
            st.dataframe(result_si)
            
            # results saving
            csv = result_si.to_csv(index=False).encode('utf-8')
            st.download_button(
                "Press to Download",
                csv,
                "file.csv",
                "text/csv",
                key='download-csv'
            )
        
        else:
            st.write("""No se ha ingresado el archivo""")