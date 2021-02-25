# Dataset yang ditemui di real-world biasanya akan memiliki banyak missing value.
# Kemampuan untuk treatment missing value sangat penting karena jika membiarkan missing value itu
#  dapat memengaruhi analisis dan machine learning model.
# Sehingga jika menemukan nilai yang hilang dalam dataset, harus melakukan treatment sedemikian rupa.

# Cara check kolom yang mempunyai missing value :
# nama_dataframe.isnull().any()

# Cara treatment terhadap missing-value antara lain :
# 1. Leave as it is (dibiarkan)
# 2. Filling the missing value (imputasi)
# 3. Drop them (hapus row yang mengandung missing value)

# Imputasi merupakan suatu metode treatment terhadap missing value dengan mengisinya menggunakan
# teknik tertentu. Bisa menggunakan mean, modus ataupun menggunakan predictive modelling.

# Pada modul ini akan membahas mengenai pemanfaatan function fillna dari Pandas untuk imputasi ini, yaitu :
# nama_dataframe['nama_kolom'].fillna(nama_dataframe.nama_kolom.function())

# .function() yang dimaksud pada syntax di atas adalah penggunaa fungsi .mean() atau .mode().
# Penggunaan fungsi .mean() atau .mode() ini bergantung pada kondisi yang mengharuskan menggunakan
# nilai rata - rata atau modus dari kolom yang akan diimputasi, seperti :
# nama_dataframe['nama_kolom'].fillna(nama_dataframe.nama_kolom.mean())
# atau
# nama_dataframe['nama_kolom'].fillna(nama_dataframe.nama_kolom.modus())

# Drop row yang mengandung missing value. Dapat menggunakan function dropna dari Pandas.
# nama_dataframe['nama_kolom'].dropna()

# Untuk menangani missing data pada retail_raw :
# 1. Ceklah jika terdapat missing value pada variabel dataframe, dan kemudian cetak ke console.
# 2. Imputasi missing value pada kolom quantity dengan menggunaan nilai rataan (mean),
# dan kemudian cetak ke console.
# 3. Drop-lah missing value pada kolom quantity, dan kemudian cetak ke console.

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
