import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Setup Konfigurasi Halaman
st.set_page_config(page_title="E-Commerce Analysis Dashboard", layout="wide")

# --- LOAD DATA ---
@st.cache_data
def load_data():
    df = pd.read_csv("main_data.csv")
    df['order_purchase_timestamp'] = pd.to_datetime(df['order_purchase_timestamp'])
    df['month'] = df['order_purchase_timestamp'].dt.month
    df['year'] = df['order_purchase_timestamp'].dt.year
    return df

all_df = load_data() 

# --- SIDEBAR ---
with st.sidebar:
    st.title("Analisis Data E-Commerce")
    st.image("https://github.com/dicodingacademy/assets/raw/main/logo.png")
    
    # Menentukan rentang waktu minimum dan maksimum dari data
    min_date = all_df["order_purchase_timestamp"].min()
    max_date = all_df["order_purchase_timestamp"].max()
    
    try:
        start_date, end_date = st.date_input(
            label='Rentang Waktu',
            min_value=min_date,
            max_value=max_date,
            value=[min_date, max_date]
        )
    except Exception:
        start_date, end_date = min_date, max_date

# Filter Data Berdasarkan Input Sidebar
main_df = all_df[(all_df["order_purchase_timestamp"] >= str(start_date)) & 
                 (all_df["order_purchase_timestamp"] <= str(end_date))]

# --- HEADER ---
st.title('E-Commerce Performance Dashboard:sparkles:')
st.markdown("---")

# PERTANYAAN 1: KEPUASAN (REVIEW SCORE)
st.header("Analisis Kepuasan Pelanggan")

col1, col2 = st.columns(2)

# Agregasi Review menggunakan main_df agar interaktif
review_stats = main_df.groupby('product_category_name_english')['review_score'].mean()

with col1:
    st.subheader("Top 5 Kategori (Kepuasan Tertinggi)")
    top_5_rev = review_stats.sort_values(ascending=False).head(5).sort_values(ascending=True)
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x=top_5_rev.values, y=top_5_rev.index, color="#72BCD4", ax=ax)
    ax.set_xlabel("Rata-rata Skor Review")
    ax.set_ylabel(None)
    ax.set_title("Top 5 Kategori", loc="center", fontsize=15)
    st.pyplot(fig)

with col2:
    st.subheader("Bottom 5 Kategori (Kepuasan Terendah)")
    bottom_5_rev = review_stats.sort_values(ascending=True).head(5).sort_values(ascending=False)
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x=bottom_5_rev.values, y=bottom_5_rev.index, color="#72BCD4", ax=ax)
    ax.set_xlabel("Rata-rata Skor Review")
    ax.set_ylabel(None)
    ax.set_title("Bottom 5 Kategori", loc="center", fontsize=15)
    st.pyplot(fig)

st.markdown("---")

# PERTANYAAN 2: TREN & REVENUE
st.header("Analisis Penjualan")
order_2017 = all_df[(all_df['year'] == 2017) & (all_df['month'] >= 7)]

# 1. Visualisasi Tren Pesanan (Line Chart)
st.subheader("Tren Jumlah Pesanan Bulanan")
monthly_orders = order_2017.groupby('month')['order_id'].nunique()

fig, ax = plt.subplots(figsize=(12, 5))
sns.lineplot(x=monthly_orders.index, y=monthly_orders.values, marker='o', color="#72BCD4", linewidth=2, ax=ax)

ax.set_xlabel("Bulan (7=Juli, 12=Desember)")
ax.set_ylabel("Jumlah Pesanan")
ax.set_xticks(monthly_orders.index)
ax.grid(True, linestyle='--', alpha=0.6)
st.pyplot(fig)

# 2. Visualisasi Top 10 Revenue (Bar Chart)
st.subheader("Top 10 Kategori Produk Penyumbang Revenue Terbesar")
top_revenue = main_df.groupby('product_category_name_english')['price'].sum().sort_values(ascending=False).head(10).sort_values(ascending=True)

fig, ax = plt.subplots(figsize=(12, 7))
sns.barplot(x=top_revenue.values, y=top_revenue.index, color="#72BCD4", ax=ax)
ax.set_xlabel("Total Revenue (BRL)")
ax.set_ylabel(None)
st.pyplot(fig)

st.caption('Copyright (c) Sukma Novianti Tulak 2026')