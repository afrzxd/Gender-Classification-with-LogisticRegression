# Import Semua Modul / Library yang dibutuhkan
import streamlit as st
import pandas as pd
import joblib
from sklearn.preprocessing import LabelEncoder

# Muhamad Afriza 202143501681 R6T

# Load model yang sudah di joblib
model = joblib.load("tugas.joblib")

# Load mapped dataset
mapped_data = pd.read_csv("Transformed Data Set - Sheet1.csv")

# URL gambar
url_gambar = 'https://storage.nu.or.id/storage/post/16_9/big/ilustrasi-gender-fotofreepikcom_1702114947.webp'

# agar gambar berada ditengah tengah
col1, col2, col3 = st.columns(3)
with col1:
    st.write(' ')

with col2:
    # Menampilkan gambar dari URL
    st.image(url_gambar)

with col3:
    st.write(' ')

# Menampilkan judul dan pembuat
st.title("Gender Classification with Logistic Regression ")
# Muhamad Afriza 202143501681 R6T
st.write("created : muhamad afriza 202143501681")

# Inisialisasi untuk menyimpan objek LabelEncoder
label_encoders = {}
# meloop setiap kolom pada mapped_Data
for column in mapped_data.columns:
    # Membuat objek LabelEncoder baru untuk setiap kolom
    le = LabelEncoder()
    # Mengubah nilai dalam kolom menjadi nilai numerik yang sesuai
    mapped_data[column] = le.fit_transform(mapped_data[column])
    # Menyimpan objek LabelEncoder ke dalam kamus dengan nama kolom sebagai kuncinya
    label_encoders[column] = le


# Pilihan untuk fitur-fitur yang akan diinput
color_op = ['Cool', 'Neutral', 'Warm']
music_genre_op = ['Rock', 'Hip hop', 'Folk/Traditional', 'Jazz/Blues', 'Pop', 'Electronic','R&B and soul']
beverage_op = ['Vodka', 'Wine', 'Whiskey',"Doesn't drink",'Beer', 'Other']
soft_drink_op = ['7UP/Sprite', 'Coca Cola/Pepsi','Fanta','Other']

# Layout form dengan 2 kolom
left_column, right_column = st.columns(2)
with left_column:
    
    # Dropdown menu untuk memilih warna favorit opsi terdapat pada color_op
    favorite_color = st.selectbox('Favorite Color', ['Select Value']+color_op)
    # Dropdown menu untuk memilih genre musik favorit opsi terdapat pada music_genre_op
    favorite_music_genre = st.selectbox('Favorite Music Genre', ['Select Value']+music_genre_op)


    # Mapping kategori ke nilai numerik
    color_map = {'Cool': 0, 'Neutral': 1, 'Warm': 2}
    music_genre_map = {
        'Rock': 6, 
        'Hip hop': 2, 
        'Folk/Traditional': 1, 
        'Jazz/Blues': 3,
        'Pop': 4,
        'Electronic': 0,
        'R&B and soul': 5,
    } 
with right_column:
    # Dropdown menu untuk memilih beverage favorit opsi terdapat pada beverage_op
    favorite_beverage = st.selectbox('Favorite Beverage', ['Select Value']+beverage_op)
    # Dropdown menu untuk memilih soft drink favorit opsi terdapat pada soft_drink_op
    favorite_soft_drink = st.selectbox('Favorite Soft Drink', ['Select Value']+soft_drink_op)

    # Mapping kategori ke nilai numerik
    beverage_map = {
        'Vodka' : 3, 
        'Wine' : 2, 
        'Whiskey' : 4,
        "Doesn't drink" : 1,
        'Beer': 5, 
        'Other' : 6
    }
    soft_drink_map = {
        '7UP/Sprite': 0, 
        'Coca Cola/Pepsi': 1,
        'Fanta': 2,
        'Other' : 3
    }

progress_bar = st.progress(0)
# Tambahkan tombol untuk memicu prediksi
if st.button('Get Predict!'):
    # jika salah 1 selectbox masih berisi 'Select Value' maka akan error
    if favorite_color != 'Select Value' and favorite_music_genre != 'Select Value' and favorite_beverage != 'Select Value' and favorite_soft_drink != 'Select Value':
        with progress_bar:    
            # mengambil nilai numerik dari selectbox yg dipilih
            favorite_color_numeric = color_map[favorite_color]
            favorite_music_genre_numeric = music_genre_map[favorite_music_genre]
            favorite_beverage_numeric = beverage_map[favorite_beverage]
            favorite_soft_drink_numeric = soft_drink_map[favorite_soft_drink]

            # Prediksi gender berdasarkan nilai numerik
            prediction = model.predict([[favorite_color_numeric, favorite_music_genre_numeric, favorite_beverage_numeric, favorite_soft_drink_numeric]])[0]

        #kalo data terisi semua maka progress bar jadi 100%
        progress_bar.progress(100)
        # Menampilkan hasil prediksi
        st.success(f"Predicted Gender: {prediction}")
    else:
        # jika salah satu data blm diisi / 'Select Value'
        st.error("Please select values for all features.")

# Muhamad Afriza 202143501681 R6T