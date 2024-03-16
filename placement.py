import streamlit as st
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score,confusion_matrix
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.naive_bayes import MultinomialNB
import pickle
st.title("Campus Placement Status Prediction using ML")
sample = []
result = None
gender = st.selectbox('Enter your Gender',('M', 'F'))
sample.append(gender)
ssc_p = st.number_input('Percentage of marks in Secondary Education/ 10th')
sample.append(ssc_p)
ssc_b = st.radio("Board of Secondary education - Central/Others",["Others", "Central"])
sample.append(ssc_b)
hsc_p = st.number_input("Percentage of marks in Higher Secondary Education/ 12th")
sample.append(hsc_p)
hsc_b = st.radio("Board of Higher Secondary Education - Central/Others",["Others", "Central"])
sample.append(hsc_b)
hsc_s = st.selectbox('Specialization in Higher Secondary Education/12th',('Commerce', 'Science', 'Arts'))
sample.append(hsc_s)
degree_p = st.number_input("Percentage of marks in Degree")
sample.append(degree_p)
degree_t = st.selectbox('Undergraduation type/ Field of degree education',('Sci&Tech', 'Comm&Mgmt', 'Others'))
sample.append(degree_t)
workex = st.radio("Any previous experience?",['No', 'Yes'])
sample.append(workex)
etest_p = st.number_input("Employability test percentage")
sample.append(etest_p)
specialisation = st.selectbox("Post Graduation(MBA) specialization",('Mkt&HR', 'Mkt&Fin'))
sample.append(specialisation)
mba_p = st.number_input("Percentage of marks in MBA")
sample.append(mba_p)

import os
current_dir = os.path.dirname(__file__)

pickle_file_path = os.path.join(current_dir, r"C:\Users\Acer\Desktop\innomatics\campus.pkl")

with open(pickle_file_path, "rb") as f:
    model = pickle.load(f)

if st.button("Submit") == True:
    result_df = pd.DataFrame([sample],columns=['gender', 'ssc_p', 'ssc_b', 'hsc_p', 'hsc_b', 'hsc_s', 'degree_p','degree_t', 'workex', 'etest_p', 'specialisation', 'mba_p'])
    result = model.predict(result_df)
else:
    pass    
if result == "Placed":
    st.text("Placed!!!")
elif result == "Not Placed":
    st.text("Not Placed :(")
