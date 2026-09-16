import streamlit as st
import pandas as pd
st.title('Mechine Learning App')
st.info('This app builds a mechining learning model!')
with st.expander('Data'):
  st.write('**Raw Data**')
  df=pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv?utm_source=chatgpt.com')

  

