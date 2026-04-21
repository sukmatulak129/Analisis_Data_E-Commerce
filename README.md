# E-Commerce Public Data Analysis Dashboard ✨

## Deskripsi
 Proyek ini bertujuan untuk melakukan proses analisis data mulai dari Data Wrangling, Exploratory Data Analysis (EDA), hingga Data Visualization pada E-Commerce Public Dataset. Hasil analisis kemudian disajikan dalam bentuk dashboard interaktif menggunakan Streamlit.

## Pertanyaan Bisnis
1. Bagaimana perbandingan rata-rata review score antar kategori produk pada periode 2017–2018 untuk mengidentifikasi kategori dengan tingkat kepuasan pelanggan tertinggi dan terendah?
2. Bagaimana tren jumlah pesanan bulanan serta kontribusi pendapatan tiap kategori produk pada semester kedua 2017 untuk menentukan strategi penjualan yang lebih efektif?

## Struktur Direktori
- `/data`: Direktori yang berisi dataset mentah (E-Commerce Public Dataset).
- `/dashboard`: Direktori yang berisi file `dashboard.py` dan data yang telah dibersihkan (`main_data.csv`).
- `notebook.ipynb`: File Jupyter Notebook yang berisi proses analisis data secara lengkap.
- `README.md`: Dokumentasi proyek.
- `requirements.txt`: Daftar pustaka (library) Python yang dibutuhkan.
- `url.txt`: Berisi link Github dan dashboard Streamlit.

## Instalasi
### 1. Setup Environment - Anaconda
`conda create --name main-ds python= Versi 3.12.3 (Versi yang saya gunakan dalam pengembangan)

conda activate main-ds

pip install -r requirements.txt`

### 2. Setup Environment - Shell/Terminal
mkdir proyek_analisis_data

cd proyek_analisis_data

pipenv install

pipenv shell

pip install -r requirements.txt

### 3. Menjalankan Dashboard Streamlit
streamlit run dashboard/dashboard.py

## Catatan Dataset
**File geolocation_dataset.csv tidak diunggah ke GitHub karena ukurannya melebihi batas maksimal. Namun, file tersebut telah disertakan dalam versi ZIP sehingga proyek tetap dapat dijalankan secara lokal.**

**Pada file dashboard.py:**
- Versi GitHub menggunakan data dari link (raw GitHub)
- Versi ZIP menggunakan file lokal (main_data.csv)

**Hal ini bertujuan agar dashboard dapat berjalan baik secara online maupun offline.**

## Disclaimer penggunaan AI : 
Pada penyelesaian proyek ini saya menggunakan AI Gemini untuk membantu saya jika terdapat eror di codingan, dan membantu saya dalam memilih kalimat agar proyek ini mudah di pahami.
