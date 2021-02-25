# Lanjut ke bagian berikutnya.

# Missing Value

# Dengan Length dan Count, sekarang dapat menghitung jumlah missing-value.
# Jumlah nilai yang hilang adalah perbedaan antara Length dan Count.

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
# Kolom product_id
length_product_id = len(retail_raw['product_id'])
print('Length kolom product_id:', length_product_id)

# Count kolom city
count_city = retail_raw['city'].count()
print('Count kolom count_city:', count_city)

# Tugas praktek:
# count kolom product_id
count_product_id = retail_raw['product_id'].count()
print('Count kolom product_id:', count_product_id)

# Missing value pada kolom city
number_of_missing_values_city = length_city - count_city
float_of_missing_values_city = float(number_of_missing_values_city/length_city)
pct_of_missing_values_city = '{0:.1f}%'.format(
    float_of_missing_values_city * 100)
print('Persentase missing value kolom city:', pct_of_missing_values_city)

# Tugas Praktek:
# Kita berhasil mendapatkan length dan count dari product_id,
# sekarang kita perlu mengetahui jumlah missing-value dari kolom tersebut.
# Ini artiya kita perlu membuat syntaks untuk menghitung persentase missing-value dari product_id.

# Tugas praktek:
# Missing value pada kolom product_id
number_of_missing_values_product_id = length_product_id - count_product_id
float_of_missing_values_product_id = float(
    number_of_missing_values_product_id/length_product_id)
pct_of_missing_values_product_id = '{0:.1f}%'.format(
    float_of_missing_values_product_id * 100)
print('Persentase missing value kolom product_id:',
      pct_of_missing_values_product_id)
