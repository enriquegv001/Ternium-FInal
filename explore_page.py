import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image



def load_data():
    df = pd.read_csv("dfexplore (1).csv")
    #df = df[['Especialidad', 'Operaciones-Calidad', 'MTTO-DIMA', 'Comercial-Planeamiento', 'DIGI-SC','Resto-Soft', 'Apto/No Apto',	'Destacado Pym.1',	'Ingles']]
    return df

df = load_data()


@st.cache_data(experimental_allow_widgets=True)
def show_explore_page():
    
    image = Image.open('Ternium.png')
    st.image(image, width = 150)
    
    st.title("Análisis descrptivo Candidatos Ingresados")
    
    st.write(
        """ #### Gráfico especialidades """
    )
    
    data = df["Especialidad"].value_counts()
    
    fig1, ax1 = plt.subplots()
    ax1.pie(data, labels=data.index, autopct="%1.1f%%", shadow=True, startangle=90)
    ax1.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.
    st.pyplot(fig1)

    st.write("""#### Gráfica número de semestres de los candidatos""")
    
    data = df['Avance'].value_counts().sort_values(ascending=True)
    st.bar_chart(data)

    st.write("""#### Gráfica de recomendacion en cada area""")
    
    recom = ['Not Recommended', 'Recommended', 'Highly Recommended']
    d_op = [df['Operaciones-Calidad'][df['Operaciones-Calidad']=='Do Not Recommend'].count(), df['Operaciones-Calidad'][df['Operaciones-Calidad']=='Recommend'].count(), df['Operaciones-Calidad'][df['Operaciones-Calidad']=='Highly Recommend'].count()]
    d_mtto = [df['MTTO-DIMA'][df['MTTO-DIMA']=='Do Not Recommend'].count(), df['MTTO-DIMA'][df['MTTO-DIMA']=='Recommend'].count(), df['MTTO-DIMA'][df['MTTO-DIMA']=='Highly Recommend'].count()]
    d_com = [df['Comercial-Planeamiento'][df['Comercial-Planeamiento']=='Do Not Recommend'].count(), df['Comercial-Planeamiento'][df['Comercial-Planeamiento']=='Recommend'].count(), df['Comercial-Planeamiento'][df['Comercial-Planeamiento']=='Highly Recommend'].count()]
    d_digi = [df['DIGI-SC'][df['DIGI-SC']=='Do Not Recommend'].count(), df['DIGI-SC'][df['DIGI-SC']=='Recommend'].count(), df['DIGI-SC'][df['DIGI-SC']=='Highly Recommend'].count()]
    d_resto = [df['Resto-Soft'][df['Resto-Soft']=='Do Not Recommend'].count(), df['Resto-Soft'][df['Resto-Soft']=='Recommend'].count(), df['Resto-Soft'][df['Resto-Soft']=='Highly Recommend'].count()]

    x_axis = np.arange(len(recom))

    # Multi bar Chart
    
    fig = plt.figure(figsize = (15, 8))


    plt.bar(x_axis -0.3, d_op, width=0.15, label = 'Operaciones-calidad')
    plt.bar(x_axis -0.15, d_mtto, width=0.15, label = 'MTTO-DIMA')
    plt.bar(x_axis +0, d_com, width=0.15, label = 'Comercial-Planeamiento')
    plt.bar(x_axis +0.15, d_digi, width=0.15, label = 'DIGI-SC')
    plt.bar(x_axis +0.3, d_resto, width=0.15, label = 'Resto-Soft')

    # Xticks

    plt.xticks(x_axis, recom)

    # Add legend

    plt.legend()

    # Display
    st.pyplot(fig)
    
    
    st.write(
        """ #### Actividad grupal """
    )
    
    data = df["Destacado Pym.1"].value_counts()
    
    fig1, ax1 = plt.subplots()
    ax1.pie(data, labels=data.index, autopct="%1.1f%%", shadow=True, startangle=90)
    ax1.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.
    st.pyplot(fig1)