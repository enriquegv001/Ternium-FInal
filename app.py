import streamlit as st
from predict_page import predict_user #show_predict_page
from DBpredict_page import DBpredict #show_DBpredict_page
from explore_page import DataAnalysis #show_explore_page
import pickle
import pandas as pd
import numpy as np
from PIL import Image

#main class for grouping all classes into one and using same attributes
class main(predict_user, DBpredict, DataAnalysis):
    def __init__(self, model, test_data, image, all_data):
        #super().__init__(model, data, image) # this can't work because each class using different number of attributes
        predict_user.__init__(self, model, image)  # Call constructor of PredictUser
        DBpredict.__init__(self, model, test_data, image)     # Call constructor of DBPredict
        DataAnalysis.__init__(self, all_data, image)

    def display_app(self):
        option = st.sidebar.selectbox("Explore Or Predict", ("Predecir por candidato", "Predecir por base de datos", "Análisis descriptivo"))
        return option

# Functins for loading model and file
def load_model():
    with open('model.pkl' , 'rb') as f:
        model = pickle.load(f)
    return model

def load_data(path = None):  
    if path == None:  
        pass
    
    elif path == 'load_file':
        uploaded_file = st.file_uploader("Choose a file")
        if uploaded_file is not None:
            x = pd.read_csv(uploaded_file)
            
            ID = np.array(x.iloc[:, 0])

            #x = x.drop(x.columns[1], axis = 1)
            x = x.drop(x.columns[0], axis = 1)
            return x, ID
    
    else:
        dataset = pd.read_csv(path)
        #df.dataset = df.dataset[['Especialidad', 'Operaciones-Calidad', 'MTTO-DIMA', 'Comercial-Planeamiento', 'DIGI-SC','Resto-Soft', 'Apto/No Apto',	'Destacado Pym.1',	'Ingles']]
        return dataset
    
def load_image():
    image = Image.open('Ternium.png')
    return image
#model = load_model()

if __name__ == "__main__": 
    MainObj = main(load_model(), load_data, load_image(), load_data("dfexplore (1).csv"))   
    page = MainObj.display_app()
    
    print(page) 
    if page == "Predecir por candidato":
        MainObj.show_predict_page()
    elif page == 'Predecir por base de datos':
        MainObj.show_DBpredict_page()
    else:
        MainObj.show_explore_page()
      