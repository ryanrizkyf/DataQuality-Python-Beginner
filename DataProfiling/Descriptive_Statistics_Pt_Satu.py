# Di bagian ini, kita akan mempelajari berbagai statistik deskriptif yang dapat digunakan untuk
# lebih memahami struktur data.

# Length

# Fungsi len menghitung jumlah pengamatan dalam suatu series / column.
# Fungsi len akan menghitung semua pengamatan,
# terlepas dari apakah ada null-value atau tidak (include missing value).

# len(nama_dataframe["nama_kolom"])

# Dataset : 'https://storage.googleapis.com/dqlab-dataset/retail_raw_reduced_data_quality.csv'.

import pandas as pd
import numpy as np
import io
import pandas_profiling
retail_raw = pd.read_csv(
    'retail_raw_reduced_data_quality.csv')

# Cetak tipe data di setiap kolom retail_raw
print(retail_raw.dtypes)

# Kolom city
length_city = len(retail_raw['city'])
print('Length kolom city:', length_city)

# Tugas Praktek:
# Setelah membaca modul referensi, kita coba memulai analisis dengan menginspeksi length
# dari kolom product_id dari dataframe retail_raw! Kita akan membuat syntaks Python untuk mencapai
# hal tersebut di code editor.

# Tugas Praktek:
# Kolom product_id
length_product_id = len(retail_raw['product_id'])
print('Length kolom product_id:', length_product_id)
