# Outliers merupakan data observasi yang muncul dengan nilai-nilai ekstrim.
# Yang dimaksud dengan nilai-nilai ekstrim dalam observasi adalah nilai yang jauh atau beda sama sekali
# dengan sebagian besar nilai lain dalam kelompoknya.

# Cara treatment terhadap outliers antara lain:
# 1. Remove the outliers (dibuang)
# 2. Filling the missing value (imputasi)
# 3. Capping
# 4. Predictio

# Pada umumnya, outliers dapat ditentukan dengan metric IQR (interquartile range).
# Rumus dasar dari IQR: Q3 - Q1, dan data suatu observasi dapat dikatakan outliers,
# jika memenuhi kedua syarat dibawah ini:
# < Q1 - 1.5 * IQR
# > Q3 + 1.5 * IQR

# Syntax di Python :
# Q1 = nama_dataframe.quantile(0.25)
# Q3 = nama_dataframe.quantile(0.75)
# IQR = Q3 - Q1

# Kemudian untuk membuang outliersnya:
# nama_dataframe = nama_dataframe[~(((nama_dataframe < (Q1 - 1.5*IQR)) | (nama_dataframe > (Q2 - 1.5*IQR)))]

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

# Tugas praktek:
# Missing value pada kolom product_id
number_of_missing_values_product_id = length_product_id - count_product_id
float_of_missing_values_product_id = float(
    number_of_missing_values_product_id/length_product_id)
pct_of_missing_values_product_id = '{0:.1f}%'.format(
    float_of_missing_values_product_id * 100)
print('Persentase missing value kolom product_id:',
      pct_of_missing_values_product_id)

# Deskriptif statistics kolom quantity
print('Kolom quantity')
print('Minimum value: ', retail_raw['quantity'].min())
print('Maximum value: ', retail_raw['quantity'].max())
print('Mean value: ', retail_raw['quantity'].mean())
print('Mode value: ', retail_raw['quantity'].mode())
print('Median value: ', retail_raw['quantity'].median())
print('Standard Deviation value: ', retail_raw['quantity'].std())

# Tugas praktek:
# Deskriptif statistics kolom item_price
print('')
print('Kolom item_price')
print('Minimum value: ', retail_raw['item_price'].min())
print('Maximum value: ', retail_raw['item_price'].max())
print('Mean value: ', retail_raw['item_price'].mean())
print('Median value: ', retail_raw['item_price'].median())
print('Standard Deviation value: ', retail_raw['item_price'].std())

# Quantile statistics kolom quantity
print('Kolom quantity:')
print(retail_raw['quantity'].quantile([0.25, 0.5, 0.75]))

# Tugas praktek:
# Quantile statistics kolom item_price
print('')
print('Kolom item_price:')
print(retail_raw['item_price'].quantile([0.25, 0.5, 0.75]))

# Tugas Praktek:
# Korelasi antara quantity dan item_price apa ya? Kita perlu tahu untuk melengkapi syntaks.
print('Korelasi quantity dengan item_price')
print(retail_raw[['quantity', 'item_price']].corr())

# Check kolom yang memiliki missing data
print('Check kolom yang memiliki missing data:')
print(retail_raw.isnull().any())

# Filling the missing value (imputasi)
print('\nFilling the missing value (imputasi):')
print(retail_raw['quantity'].fillna(retail_raw['quantity'].mean()))

# Drop missing value
print('\nDrop missing value:')
print(retail_raw['quantity'].dropna())

# Tugas Praktek
# Lengkapi missing value tersebut dengan mean dari item_price.
print('Filling the missing value (item_price):')
print(retail_raw['item_price'].fillna(retail_raw['item_price'].mean()))

# Q1, Q3, dan IQR
Q1 = retail_raw['quantity'].quantile(0.25)
Q3 = retail_raw['quantity'].quantile(0.75)
IQR = Q3 - Q1

# Check ukuran (baris dan kolom) sebelum data yang outliers dibuang
print('Shape awal: ', retail_raw.shape)

# Removing outliers
retail_raw = retail_raw[~((retail_raw['quantity'] < (
    Q1 - 1.5 * IQR)) | (retail_raw['quantity'] > (Q3 + 1.5 * IQR)))]

# Check ukuran (baris dan kolom) setelah data yang outliers dibuang
print('Shape akhir: ', retail_raw.shape)
