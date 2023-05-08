import numpy as np
import pandas as pd
import pickle
import streamlit as st

#load save model
model = pickle.load(open('heart_failure_model.sav','rb'))

#Judul Web
st.title('Deteksi Kelangsungan Hidup Pasien Gagal Jantung')

col1, col2, col3 = st.columns(3)
with col1:
    age = st.number_input('Umur')

with col2:
    anaemia = st.number_input('Anaemia')

with col3:
    creatinine_phosphokinasee = st.number_input('Enzim CPK')

with col1:
    diabetes = st.number_input('Diabetes')

with col2:
    ejection_fraction = st.number_input('Ejection_Fraction (%)')

with col3:
    high_blood_pressure = st.number_input('Hipertensi')

with col1:
    platelets = st.number_input('Jumlah trombosit')

with col2:
    serum_creatinine = st.number_input('Jumlah Kreatin Serum')

with col3:
    serum_sodium = st.number_input('Jumlah Natrium Serum')

with col1:
    sex = st.number_input('Jenis Kelamin')

with col2:
    smoking = st.number_input('Merokok')

with col3:
    time = st.number_input('Periode Tindak Lanjut (hari)')

#code for prediction
heart_diagnosis = ''

#membuat tombol prediksi
if st.button('Hasil Pasien Gagal Jantung'):
    heart_predicton = model.predict([[age,anaemia,creatinine_phosphokinasee,diabetes,ejection_fraction,high_blood_pressure,
                                     platelets,serum_creatinine,serum_sodium,sex,smoking,time]])
    if (heart_predicton[0] == 0):
        heart_diagnosis = 'PASIEN TERDETEKSI SELAMAT'
    else:
        heart_diagnosis = 'PASIEN TERDETEKSI MENINGGAL'
st.success(heart_diagnosis)