import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Contoh DataFrame dengan kolom sesuai dengan yang ada di gambar korelasi
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

# Ubah menjadi DataFrame
df = pd.DataFrame(data)

# Menghapus kolom yang tidak perlu (dteday dan instant)
df_cleaned = df.drop(columns=['dteday', 'instant'])

# Mengonversi kolom kategorikal menjadi numerik jika ada
df_encoded = pd.get_dummies(df_cleaned, drop_first=True)

# Menghitung matriks korelasi
correlation_matrix = df_encoded.corr()

# Judul Dashboard
st.title("Dashboard Matriks Korelasi Penyewaan Sepeda")

# Menampilkan Matriks Korelasi
st.subheader("Matriks Korelasi")
fig, ax = plt.subplots(figsize=(12, 8))  # Ukuran heatmap
sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap="coolwarm", ax=ax)
st.pyplot(fig)

# Menampilkan Histogram untuk beberapa kolom
st.subheader("Histogram Data")

# Daftar kolom untuk histogram
columns_to_plot = ['temp', 'atemp', 'hum', 'casual', 'registered', 'cnt']

# Loop untuk menampilkan histogram untuk setiap kolom
for column in columns_to_plot:
    fig, ax = plt.subplots(figsize=(10, 5))  # Ukuran histogram
    sns.histplot(df[column], bins=10, kde=True, ax=ax)  # Histogram dengan KDE
    ax.set_title(f'Histogram of {column}')
    ax.set_xlabel(column)
    ax.set_ylabel('Frequency')
    st.pyplot(fig)

# Tambahkan lebih banyak visualisasi atau analisis sesuai kebutuhan
