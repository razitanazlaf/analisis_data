# Analisis Data - Dashboard Kualitas Udara Guanyuan
Proyek ini berfokus pada analisis data kualitas udara dari kota Guanyuan, khususnya terkait konsentrasi O3 dan pola curah hujan. Dashboard ini memvisualisasikan data tersebut dari waktu ke waktu, memberikan wawasan mengenai tingkat polusi dan tren cuaca.

## Setup Environment

## Menggunakan Anaconda
```
conda create --name main-ds python=3.9
conda activate main-ds
pip install -r requirements.txt
```

## Menggunakan Shell/Terminal
```
mkdir analisis_data
cd analisis_data
pipenv install
pipenv shell
pip install -r requirements.txt
```

## Menjalankan Aplikasi Streamlit
```
streamlit run dashboard.py
```
