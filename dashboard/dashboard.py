import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

sns.set(style='dark')

# Load cleaned data
all_df = pd.read_csv("main_data.csv")

# Mengubah kolom tahun, bulan, hari, dan jam menjadi kolom datetime untuk analisis waktu
all_df['datetime'] = pd.to_datetime(all_df[['year', 'month', 'day', 'hour']])

# Filter data berdasarkan rentang waktu
min_date = all_df["datetime"].min()
max_date = all_df["datetime"].max()

with st.sidebar:
    # Menambahkan logo (gunakan URL gambar yang tersedia)
    st.image("logoguanyuan.jpeg")
    
    # Mengambil rentang waktu dari date_input
    start_date, end_date = st.date_input(
        label='Rentang Waktu', min_value=min_date, max_value=max_date,
        value=[min_date, max_date]
    )

# Filter dataset berdasarkan rentang waktu yang dipilih
main_df = all_df[(all_df["datetime"] >= str(start_date)) & 
                 (all_df["datetime"] <= str(end_date))]

# Menampilkan header aplikasi
st.header('Dashboard Analisis Kualitas Udara Kota Guanyuan :sparkles:')

# Analisis O3 tertinggi per Jam
st.subheader('Pada jam berapa konsentrasi O3 tertinggi tercatat di Guanyuan?')

# Menggunakan maksimum seperti di Jupyter
o3_hourly_max = main_df.groupby('hour')['O3'].max().reset_index()  # Ubah ke max untuk konsistensi dengan Jupyter
o3_max_hour = o3_hourly_max.loc[o3_hourly_max['O3'].idxmax()]

# Plot data O3 berdasarkan jam
fig, ax = plt.subplots(figsize=(16, 8))
sns.barplot(x="hour", y="O3", data=o3_hourly_max, palette="Oranges", ax=ax)
ax.set_title('Konsentrasi O3 per Jam', fontsize=20)
ax.set_ylabel('Konsentrasi O3 (µg/m³)', fontsize=15)
ax.set_xlabel('Jam', fontsize=15)
ax.tick_params(axis='y', labelsize=12)
ax.tick_params(axis='x', labelsize=12)
st.pyplot(fig)

# Menampilkan jam dengan konsentrasi O3 tertinggi
st.metric(f"Jam dengan Konsentrasi O3 Tertinggi", value=f"{int(o3_max_hour['hour'])}:00", delta=f"{o3_max_hour['O3']:.2f} µg/m³")

# Mengelompokkan dan menjumlahkan data curah hujan per bulan
rain_by_month = main_df.groupby('month')['RAIN'].sum().reset_index()

# Mencari bulan dengan curah hujan tertinggi
max_rainfall_month = rain_by_month.loc[rain_by_month['RAIN'].idxmax()]

# Membuat plot batang untuk curah hujan per bulan
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x="month", y="RAIN", data=rain_by_month, palette="Blues", ax=ax)
ax.set_title('Total Curah Hujan per Bulan', fontsize=20)
ax.set_ylabel('Total Curah Hujan (mm)', fontsize=15)
ax.set_xlabel('Bulan', fontsize=15)
ax.tick_params(axis='y', labelsize=12)
ax.tick_params(axis='x', labelsize=12)

# Menampilkan plot di Streamlit
st.pyplot(fig)

# Menampilkan bulan dengan curah hujan tertinggi
st.metric(
    label="Bulan dengan Curah Hujan Tertinggi", 
    value=f"Bulan {int(max_rainfall_month['month'])}", 
    delta=f"{max_rainfall_month['RAIN']:.2f} mm"
)


