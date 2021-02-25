# Kita melanjutkan mempelajari ke fungsi berikutnya, yaitu Count.

# Count

# Fungsi count menghitung jumlah pengamatan non-NA / non-null dalam suatu series / column.
# Fungsi len akan hanya menghitung elemen dari kolom yang mempunyai nilai (exclude missing value).

# nama_dataframe["nama_kolom"].count()

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

# Tugas Praktek:
# Setelah yang tadi cukup lancar, kita berniat mengetahui jumlah non-null value dari kolom product_id
# dari dataframe retail_raw agar hasil analisisnya lebih lengkap.

# Tugas praktek:
# count kolom product_id
count_product_id = retail_raw['product_id'].count()
print('Count kolom product_id:', count_product_id)
