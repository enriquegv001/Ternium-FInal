import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
"""
def load_data():
    dataset = pd.read_csv("dfexplore (1).csv")
    #df.dataset = df.dataset[['Especialidad', 'Operaciones-Calidad', 'MTTO-DIMA', 'Comercial-Planeamiento', 'DIGI-SC','Resto-Soft', 'Apto/No Apto',	'Destacado Pym.1',	'Ingles']]
    return dataset

dataset = load_data()
"""

class DataAnalysis:
    def __init__(self, dataset, image):
        self.dataset = dataset
        self.image = image

    #@st.cache_data(experimental_allow_widgets=True)
    def show_explore_page(self):
        # page visualization
        #image = Image.open('Ternium.png')
        st.image(self.image, width = 150)
        st.title("Análisis descrptivo Candidatos Ingresados")
         
        # Speciality pie chart
        st.write(""" #### Gráfico especialidades """)
        data = self.dataset["Especialidad"].value_counts()
        fig1, ax1 = plt.subplots()
        ax1.pie(data, labels=data.index, autopct="%1.1f%%", shadow=True, startangle=90)
        ax1.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.
        st.pyplot(fig1)

        # Candidate's semester bar plot
        st.write("""#### Gráfica número de semestres de los candidatos""")
        data = self.dataset['Avance'].value_counts().sort_values(ascending=True)
        st.bar_chart(data)

        # Bar plot for recommendation per area 
        st.write("""#### Gráfica de recomendacion en cada area""")
        recom = ['Not Recommended', 'Recommended', 'Highly Recommended']
        d_op = [self.dataset['Operaciones-Calidad'][self.dataset['Operaciones-Calidad']=='Do Not Recommend'].count(), self.dataset['Operaciones-Calidad'][self.dataset['Operaciones-Calidad']=='Recommend'].count(), self.dataset['Operaciones-Calidad'][self.dataset['Operaciones-Calidad']=='Highly Recommend'].count()]
        d_mtto = [self.dataset['MTTO-DIMA'][self.dataset['MTTO-DIMA']=='Do Not Recommend'].count(), self.dataset['MTTO-DIMA'][self.dataset['MTTO-DIMA']=='Recommend'].count(), self.dataset['MTTO-DIMA'][self.dataset['MTTO-DIMA']=='Highly Recommend'].count()]
        d_com = [self.dataset['Comercial-Planeamiento'][self.dataset['Comercial-Planeamiento']=='Do Not Recommend'].count(), self.dataset['Comercial-Planeamiento'][self.dataset['Comercial-Planeamiento']=='Recommend'].count(), self.dataset['Comercial-Planeamiento'][self.dataset['Comercial-Planeamiento']=='Highly Recommend'].count()]
        d_digi = [self.dataset['DIGI-SC'][self.dataset['DIGI-SC']=='Do Not Recommend'].count(), self.dataset['DIGI-SC'][self.dataset['DIGI-SC']=='Recommend'].count(), self.dataset['DIGI-SC'][self.dataset['DIGI-SC']=='Highly Recommend'].count()]
        d_resto = [self.dataset['Resto-Soft'][self.dataset['Resto-Soft']=='Do Not Recommend'].count(), self.dataset['Resto-Soft'][self.dataset['Resto-Soft']=='Recommend'].count(), self.dataset['Resto-Soft'][self.dataset['Resto-Soft']=='Highly Recommend'].count()]
        x_axis = np.arange(len(recom))
        # visualization
        fig = plt.figure(figsize = (15, 8))
        plt.bar(x_axis -0.3, d_op, width=0.15, label = 'Operaciones-calidad')
        plt.bar(x_axis -0.15, d_mtto, width=0.15, label = 'MTTO-DIMA')
        plt.bar(x_axis +0, d_com, width=0.15, label = 'Comercial-Planeamiento')
        plt.bar(x_axis +0.15, d_digi, width=0.15, label = 'DIGI-SC')
        plt.bar(x_axis +0.3, d_resto, width=0.15, label = 'Resto-Soft')
        plt.xticks(x_axis, recom)
        plt.legend()
        st.pyplot(fig)

        # Pie chart for groupal activiy fot the Destacados trugh Pym1 test 
        st.write(""" #### Actividad grupal """)
        data = self.dataset["Destacado Pym.1"].value_counts()
        fig1, ax1 = plt.subplots()
        ax1.pie(data, labels=data.index, autopct="%1.1f%%", shadow=True, startangle=90)
        ax1.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.
        st.pyplot(fig1)