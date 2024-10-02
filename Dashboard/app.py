import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'instant': [1, 2, 3],
    'dteday': ['2011-01-01', '2011-01-02', '2011-01-03'],
    'season': [1, 1, 1],
    'yr': [0, 0, 0],
    'mnth': [1, 1, 1],
    'holiday': [0, 0, 0],
    'weekday': [6, 0, 1],
    'workingday': [0, 1, 1],
    'weathersit': [1, 1, 1],
    'temp': [0.24, 0.22, 0.23],
    'atemp': [0.287, 0.276, 0.289],
    'hum': [0.81, 0.80, 0.82],
    'windspeed': [0.0, 0.0, 0.0],
    'casual': [3, 5, 8],
    'registered': [13, 18, 20],
    'cnt': [16, 23, 28]
}


df = pd.DataFrame(data)


df_cleaned = df.drop(columns=['dteday', 'instant'])


df_encoded = pd.get_dummies(df_cleaned, drop_first=True)

correlation_matrix = df_encoded.corr()

st.title("Dashboard Matriks Korelasi Penyewaan Sepeda")

st.subheader("Matriks Korelasi")
fig, ax = plt.subplots(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap="coolwarm", ax=ax)
st.pyplot(fig)


st.subheader("Histogram Data")

columns_to_plot = ['temp', 'atemp', 'hum', 'casual', 'registered', 'cnt']

for column in columns_to_plot:
    fig, ax = plt.subplots(figsize=(10, 5))  
    sns.histplot(df[column], bins=10, kde=True, ax=ax) 
    ax.set_title(f'Histogram of {column}')
    ax.set_xlabel(column)
    ax.set_ylabel('Frequency')
    st.pyplot(fig)